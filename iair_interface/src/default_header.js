import './default_style.css';
import React from 'react';
import { Breadcrumb, Layout, Menu, theme, Typography } from 'antd';
import { Row, Col } from 'antd';
const { Header, Content, Footer } = Layout;
const { Text } = Typography;

export default class Head extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            current_key : props.menu_id,
        }
    }

    render() {
        return (
            <div>
                <Header>
                    <Row>
                        <Col span={2}>
                            <Text className='title'>iAirDB</Text>
                        </Col>
                        <Col span={1}></Col>
                        <Col span={20}>
                            <Menu
                                theme="dark"
                                mode="horizontal"
                                selectedKeys={[this.state.current_key]}
                                items={[
                                    {
                                        key: 1, label: (<a rel="noopener noreferrer" href="./">
                                            General Stat
                                        </a>)
                                    },
                                    {
                                        key: 2, label: (
                                            <a rel="noopener noreferrer" href="./citystats">
                                                City Stat
                                            </a>)
                                    },
                                    { 
                                        key: 3, label: (
                                            <a rel="noopener noreferrer" href="./professional">
                                                Professional
                                            </a>)
                                    },
                                ]}
                            >
                            </Menu>
                        </Col>
                    </Row>
                </Header>
            </div>
        )
    }
}