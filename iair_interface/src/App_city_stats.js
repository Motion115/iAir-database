import './default_style.css';
import Plot from './module/plot.js'
import DoublePlot from './module/double_plot.js'
import InputBracket from './module/input_bracket.js'
import Tagging from './module/tag.js'
import Head from './default_header.js'
import Foot from './default_footer.js'
import StationDist from './module/station_dist.js'
import React from 'react';
import axios from 'axios';
import { Breadcrumb, Button, Layout, Menu, theme, Row, Col } from 'antd';
import { Card } from 'antd';
const { Header, Content, Footer } = Layout;

const levenshtein = require('fast-levenshtein');


export default class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            city_names: [],
            target_city: ''
        }
    }

    componentDidMount() {
        this.getViableCity()
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

    get_similar_cities = (city_name, dictionary) => {
        let similarities = [];
        for (let i = 0; i < dictionary.length; i++) {
            let similarity = this.jaccard(city_name, dictionary[i]);
            similarities.push({city: dictionary[i], similarity: similarity});
        }
        similarities.sort((a, b) => b.similarity - a.similarity);
        return similarities.slice(0, 5).map(s => s.city);
    }

    jaccard = (str1, str2) => {
        const set1 = new Set(str1.split(''));
        const set2 = new Set(str2.split(''));
        const intersection = new Set([...set1].filter(x => set2.has(x)));
        const union = new Set([...set1, ...set2]);
        return intersection.size / union.size;
    }

    getSerachKey = (key) => {
        // console.log(this.state.city_names)
        // check if the key is in the city_names list
        if (this.state.city_names.indexOf(key) !== -1) {
            this.setState({
                target_city: key
            })
        }
        else {
            console.log('key is not in the list')
            // get the most similar city name
            let similar_city = this.get_similar_cities(key, this.state.city_names)
            // extend similar_city to a string
            let similar_city_str = ''
            for (let i = 0; i < similar_city.length; i++) {
                similar_city_str += similar_city[i] + ' or '
            }
            alert('Did you mean: ' + similar_city_str + "else?")
        }
    }


    render() {
        return (
            <div>
                <Layout className="layout">
                    <Head menu_id="2"></Head>

                    <Content style={{ padding: '0 50px', }}>
                        <br />
                        <div className="site-layout-content">
                            <br />
                            <Card title="City">
                                {/*<InputBracket onValueChange={this.getSerachKey}></InputBracket>*/}
                                <Tagging data={this.state.city_names} onValueChange={this.getSerachKey}></Tagging>
                            </Card>
                            <br />
                            <Card title="City Station Distribution">
                                <StationDist city={this.state.target_city}></StationDist>
                            </Card>
                            <br />
                            <Card title="AQI Trend">
                                <DoublePlot city={this.state.target_city} metric="AQI"></DoublePlot>
                            </Card>
                            <br />
                            <Row gutter={16}>
                                <Col span={12}>
                                    <Card title="PM2.5 Trend">
                                        <Plot city={this.state.target_city} metric="pm2.5"></Plot>
                                    </Card>
                                </Col>
                                <Col span={12}>
                                    <Card title="PM10 Trend">
                                        <Plot city={this.state.target_city} metric="pm10"></Plot>
                                    </Card>
                                </Col>
                            </Row>
                            <br />
                            <Row gutter={16}>
                                <Col span={12}>
                                    <Card title="SO2 Trend">
                                        <Plot city={this.state.target_city} metric="so2"></Plot>
                                    </Card>
                                </Col>
                                <Col span={12}>
                                    <Card title="CO Trend">
                                        <Plot city={this.state.target_city} metric="co"></Plot>
                                    </Card>
                                </Col>
                            </Row>
                            <br />
                            <Row gutter={16}>
                                <Col span={12}>
                                    <Card title="O3 Trend">
                                        <Plot city={this.state.target_city} metric="o3"></Plot>
                                    </Card>
                                </Col>
                                <Col span={12}>
                                    <Card title="NO2 Trend">
                                        <Plot city={this.state.target_city} metric="no2"></Plot>
                                    </Card>
                                </Col>
                            </Row>
                            <br />
                        </div>
                    </Content>
                    
                    <Foot></Foot>
                </Layout>

            </div>
        )
    }
}