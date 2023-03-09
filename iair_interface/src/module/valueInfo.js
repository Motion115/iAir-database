import { ArrowDownOutlined, ArrowUpOutlined } from '@ant-design/icons';
import { Card, Col, Row, Statistic } from 'antd';
import axios from 'axios';
import React from 'react';

export default class SingleStat extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            num_cities: props.city_length,
            num_city_group: 0,
            num_districts: 0,
            num_stations: 0,
        };
    }

    getTableLength(table_name, parameter_name) {
        axios.get("http://127.0.0.1:5000/getTableLength/" + table_name)
            .then(res => {
                this.setState({ [parameter_name]: res.data })
            })
    }

    getCityGroups() {
        axios.get("http://127.0.0.1:5000/getCityGroups")
            .then(res => {
                this.setState({ num_city_group: res.data })
            })
    }

    componentDidMount() {
        this.getTableLength("city", "num_cities")
        this.getCityGroups()
        this.getTableLength("district", "num_districts")
        this.getTableLength("station", "num_stations")
    }


    render() {
        return (
            <div>
                <Row gutter={16}>
                    <Col span={6}>
                        <Card bordered={true} hoverable={true}>
                            <Statistic
                                title="Cities"
                                value={this.state.num_cities}
                                precision={0}
                                valueStyle={{
                                    color: '#3f8600',
                                }}
                                prefix={<ArrowUpOutlined />}
                                suffix=""
                            />
                        </Card>
                    </Col>
                    <Col span={6}>
                        <Card bordered={true} hoverable={true}>
                            <Statistic
                                title="City Groups"
                                value={this.state.num_city_group}
                                precision={0}
                                valueStyle={{
                                    color: '#cf1322',
                                }}
                                prefix={<ArrowDownOutlined />}
                                suffix=""
                            />
                        </Card>
                    </Col>
                    <Col span={6}>
                        <Card bordered={true} hoverable={true}>
                            <Statistic
                                title="Districts"
                                value={this.state.num_districts}
                                precision={0}
                                valueStyle={{
                                    color: '#cf1322',
                                }}
                                prefix={<ArrowDownOutlined />}
                                suffix=""
                            />
                        </Card>
                    </Col>
                    <Col span={6}>
                        <Card bordered={true} hoverable={true}>
                            <Statistic
                                title="Stations"
                                value={this.state.num_stations}
                                precision={0}
                                valueStyle={{
                                    color: '#cf1322',
                                }}
                                prefix={<ArrowDownOutlined />}
                                suffix=""
                            />
                        </Card>
                    </Col>
                </Row>
            </div>
        )
    }
}