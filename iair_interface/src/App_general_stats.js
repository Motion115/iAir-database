import './default_style.css';
import ValueInfo from './module/valueInfo.js'
import Distmap from './module/distmap.js'
import Head from './default_header.js'
import Foot from './default_footer.js'
import React from 'react';
import { Layout } from 'antd';
import { Card } from 'antd';
const { Content } = Layout;


export default class App extends React.Component {
	constructor(props) {
		super(props);
	}

	render() {
		return (
			<div>
				<Layout className="layout">
					<Head menu_id="1"></Head>
					<Content style={{ padding: '0 50px', }}>
						<br />
						<div className="site-layout-content">
							<Card title="General Statistics">
								<ValueInfo></ValueInfo>
							</Card>
							<br />
							<Card title="Distribution Map">
								<Distmap></Distmap>
							</Card>
						</div>
					</Content>
					<Foot></Foot>
				</Layout>
			</div>
		)
	}
}