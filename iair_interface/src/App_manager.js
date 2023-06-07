import './default_style.css';
import Head from './default_header.js'
import Foot from './default_footer.js'
import React from 'react';
import CardStat from './module/card_stat_spec.js'
import Tagging from './module/tag.js'
import axios from 'axios';
import { CheckCircleTwoTone, CloseCircleTwoTone, EnterOutlined } from '@ant-design/icons';
import { Breadcrumb, Layout, Menu, theme, Typography, Input } from 'antd';
import { Card } from 'antd';
import { Row, Col } from 'antd';
const { Header, Content, Footer } = Layout;
const { Text } = Typography;
const { Search } = Input;

export default class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            verification: false
        };
    }

    recordChange = (value) => {
        axios.get("http://127.0.0.1:5000/isManager/" + value)
            .then(res => {
                console.log(res.data)
                if (res.data === "manager") {
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

    addUser = (value) => {
        if (this.state.verification === false) {
            alert("You are not a manager!")
            return
        }
        axios.get("http://127.0.0.1:5000/addUser/" + value)
            .then(res => {
                console.log(res.data)
            })
        alert("Token " + value + " added!")
    }

    deleteUser = (value) => {
        if (this.state.verification === false) {
            alert("You are not a manager!")
            return
        }
        axios.get("http://127.0.0.1:5000/deleteUser/" + value)
            .then(res => {
                console.log(res.data)
        })
        alert("Token " + value + " deleted!")
    }

    render() {
        return (
            <div>
                <Layout className="layout">
                    <Head menu_id="4"></Head>
                    <Content style={{ padding: '0 50px', }}>
                        <br />
                        <div className="site-layout-content">
                            <Card title="Verification">
                                <Row>
                                    <Col span={12}>
                                        <Search
                                            allowClear
                                            defaultValue='secret key'
                                            onSearch={this.recordChange}
                                            style={{
                                                width: 300,
                                            }}
                                            enterButton={<EnterOutlined />}
                                        />
                                        <p>Manager Status:  {this.state.verification ? <CheckCircleTwoTone style={{ fontSize: '25px' }} twoToneColor="#52c41a" /> : <CloseCircleTwoTone style={{ fontSize: '25px' }} twoToneColor="#FF0000" />}</p>
                                    </Col>
                                </Row>
                            </Card>
                            <br />
                            <Card title="Manager User">
                                <Row>
                                    <Col span={12}>
                                        <Text>Token to add:  </Text>
                                        <Search
                                            allowClear
                                            onSearch={this.addUser}
                                            style={{
                                                width: 300,
                                            }}
                                            enterButton={<EnterOutlined />}
                                        />
                                    </Col>
                                </Row>
                                <br />
                                <Row>
                                    <Col span={12}>
                                        <Text>Token to delete:  </Text>
                                        <Search
                                            allowClear
                                            onSearch={this.deleteUser}
                                            style={{
                                                width: 300,
                                            }}
                                            enterButton={<EnterOutlined />}
                                        />
                                    </Col>
                                </Row>
                                
                            </Card>
                        </div>
                    </Content>
                    <Foot></Foot>
                </Layout>

            </div>
        )
    }
}