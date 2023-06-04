import React from 'react';
import axios from 'axios';
import { Scatter } from '@ant-design/charts';

class DemoScatter extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			cur_city: props.city,
			data: []
		};
	}

	componentDidMount() {
		this.asyncFetch();
	}

	componentDidUpdate(prevProps) {
		if (prevProps.city !== this.props.city) {
			this.setState({ cur_city: this.props.city });
			this.asyncFetch();
		}
	}

	asyncFetch() {
		axios.get("http://127.0.0.1:5000/getStationDistribution/" + this.props.city)
			.then(res => {
				this.setState({ data: res.data });
			});
	}

	render() {
		const config = {
			appendPadding: 10,
			data: this.state.data,
			xField: 'latitude',
			yField: 'longitude',
			shape: 'circle',
			colorField: 'district_id',
			size: 4,
			tooltip: {
				fields: ['station_name'],
			},
			yAxis: {
				title: {
					text: "longitude",
				},
				nice: true,
				line: {
					style: {
						stroke: '#aaa',
					},
				},
			},
			xAxis: {
				title: {
					text: "latitude",
				},
				nice: true,
				grid: {
					line: {
						style: {
							stroke: '#eee',
						},
					},
				},
				line: {
					style: {
						stroke: '#aaa',
					},
				},
			},
		};

		return <Scatter {...config} />;
	}
}

export default DemoScatter;