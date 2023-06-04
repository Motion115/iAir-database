import './default_style.css';
import Plot from './module/plot.js'
import Head from './default_header.js'
import Foot from './default_footer.js'
import StationDist from './module/station_dist.js'
import React from 'react';
import axios from 'axios';
import { Breadcrumb, Layout, Menu, theme } from 'antd';
import { Card } from 'antd';
const { Header, Content, Footer } = Layout;

export default class App extends React.Component {
    constructor(props) {
        super(props);
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
                            <Card title="Trend">
                                {/*<Plot></Plot>*/}
                            </Card>
                            <Card title="AQI">
                                <StationDist></StationDist>
                            </Card>

                        </div>
                    </Content>
                    
                    <Foot></Foot>
                </Layout>

            </div>
        )
    }
}