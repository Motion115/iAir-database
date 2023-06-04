import React, { useState, useEffect } from 'react';
import { Scatter } from '@ant-design/plots';
import axios from 'axios';

const DemoScatter = () => {
	const [data, setData] = useState([]);

	useEffect(() => {
		asyncFetch();
	}, []);

	const asyncFetch = () => {
		axios.get("http://127.0.0.1:5000/getStationDistribution")
			.then(res => {
				setData(res.data)
				//console.log(res.data)
			})
	}

	const config = {
		appendPadding: 10,
		data,
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
};

export default DemoScatter;
