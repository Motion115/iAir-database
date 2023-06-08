import './default_style.css';
import Head from './default_header.js'
import Foot from './default_footer.js'
import React from 'react';
import CardStat from './module/card_stat_spec.js'
import Tagging from './module/tag.js'
import axios from 'axios';
import { CheckCircleTwoTone, CloseCircleTwoTone, EnterOutlined} from '@ant-design/icons';
import { Layout, Typography, Input} from 'antd';
import { Card } from 'antd';
import { Row, Col } from 'antd';
const { Content } = Layout;
const { Text } = Typography;
const { Search } = Input;

export default class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            city_table: [],
            statistics: {
                num_cities: 0,
                num_districts: 0,
                num_stations: 0,
            },
            city_names: [],
            target_city: '',
            verification: false
        };
    }

    getTableLength(table_name, parameter_name) {
        axios.get("http://127.0.0.1:5000/getTableLength/" + table_name)
            .then(res => {
                let statistics = this.state.statistics
                statistics[parameter_name] = res.data
                this.setState({
                    statistics: statistics
                })
            })
    }

    componentDidMount() {
        this.getViableCity()
        this.getTableLength("city", "num_cities")
        this.getTableLength("district", "num_districts")
        this.getTableLength("station", "num_stations")
    }

    getViableCity = () => {
        axios.get('http://127.0.0.1:5000/getDistinctCity')
            .then(res => {
                let city_names = []
                for (let i = 0; i < res.data.length; i++) {
                    city_names.push(res.data[i]["city_name"])
                }
                this.setState({
                    city_names: city_names,
                    target_city: city_names[0]
                })
            })
    }

    getSerachKey = (key) => {
        this.setState({
            target_city: key
        })
    }

    recordChange = (value) => {
        axios.get("http://127.0.0.1:5000/validification/" + value)
            .then(res => {
                if (res.data === "granted"){
                    this.setState({
                        verification: true
                    })
                }
                else {
                    this.setState({
                        verification: false
                    })
                }
            })
    }

    render() {
        return (
            <div>
                <Layout className="layout">
                    <Head menu_id="3"></Head>
                    <Content style={{ padding: '0 50px', }}>
                        <br />
                        <div className="site-layout-content">
                            <Card title="Verification">
                                <Row>
                                    <Col span={12}>
                                        <Search
                                            allowClear
                                            defaultValue='Access token'
                                            onSearch={this.recordChange}
                                            style={{
                                                width: 300,
                                            }}
                                            enterButton={<EnterOutlined />}
                                        />
                                        <p>File Access Status:  {this.state.verification ? <CheckCircleTwoTone style={{ fontSize: '25px' }} twoToneColor="#52c41a" /> : <CloseCircleTwoTone style={{ fontSize: '25px' }} twoToneColor="#FF0000" />}</p>
                                    </Col>
                                </Row>
                            </Card>
                            <br />
                            <Card title="Data Panel">
                                <Row gutter={16}>
                                    <Col span={6}>
                                        <CardStat title="Cities" mode="city" value={this.state.statistics.num_cities} verification={this.state.verification}/>
                                    </Col>
                                    <Col span={6}>
                                        <CardStat title="Districts" mode="district" value={this.state.statistics.num_districts} verification={this.state.verification} />
                                    </Col>
                                    <Col span={6}>
                                        <CardStat title="Stations" mode="station" value={this.state.statistics.num_stations} verification={this.state.verification} />
                                    </Col>
                                </Row>
                                <br />
                                <Row gutter={16}>
                                    <Col span={6}>
                                        <CardStat title="Cities Air Quality" mode="AQI" value={this.state.statistics.num_cities} city_name={this.state.target_city} verification={this.state.verification} />
                                    </Col>
                                    <Col span={18}>
                                        <Tagging data={this.state.city_names} onValueChange={this.getSerachKey}></Tagging>
                                    </Col>
                                </Row>
                                <br />
                                <Row gutter={16}>
                                    <Col span={6}>
                                        <CardStat title="Cities Meteo" mode="meteo" value={this.state.statistics.num_cities} city_name={this.state.target_city} verification={this.state.verification} />
                                    </Col>
                                    <Col span={18}>
                                        <Tagging data={this.state.city_names} onValueChange={this.getSerachKey}></Tagging>
                                    </Col>
                                </Row>
                                <br />
                                <Row gutter={16}>
                                    <Col span={6}>
                                        <CardStat title="Cities Forecast" mode="forecast" value={this.state.statistics.num_cities} city_name={this.state.target_city} verification={this.state.verification} />
                                    </Col>
                                    <Col span={18}>
                                        <Tagging data={this.state.city_names} onValueChange={this.getSerachKey}></Tagging>
                                    </Col>
                                </Row>
                            </Card>
                            <br />
                        </div>
                        <div>
                            <Text>*The data of iAirDB is from <a href='https://www.microsoft.com/en-us/research/project/urban-air/' target='_blank'>Microsoft Urban Air</a> Research's open dataset. 
                                Latest entry is 2015.4. If you are interested in updating new data (in time or locale), you can contact <a href='http://github.com/Motion115' target='_blank'>the author</a>  of iAirDB.</Text>
                        </div>
                    </Content>
                    <Foot></Foot>
                </Layout>
            </div>
        )
    }
}