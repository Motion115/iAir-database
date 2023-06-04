import './default_style.css';
import ValueInfo from './module/valueInfo.js'
import Distmap from './module/distmap.js'
import Head from './default_header.js'
import Foot from './default_footer.js'
import React from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import { Breadcrumb, Layout, Menu, theme, Typography } from 'antd';
import { Card } from 'antd';
import { Row, Col } from 'antd';
const { Header, Content, Footer } = Layout;
const { Text } = Typography;

export default class App extends React.Component {
	constructor(props) {
		super(props);

		this.state = {
			city_table: [],
			statistics: {
				num_cities: 0,
				num_city_group: 0,
				num_districts: 0,
				num_stations: 0,
			}
		};

		//this.handleClick = this.handleClick.bind(this);
	}

	click() {
		axios.get("http://127.0.0.1:5000/getTableLength/city")
			.then(res => {
				const city_data = res.data
				this.setState({ city_table: city_data })
			})
	}

	call() {
		console.log(this.state.city_table)
		// iterate through this array and print the values
		let paragraph = ""
		for (let i = 0; i < this.state.city_table.length; i++) {
			paragraph += this.state.city_table[i].city_name + ", "
		}
		return paragraph
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