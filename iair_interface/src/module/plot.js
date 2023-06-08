import React, { Component } from 'react';
import axios from 'axios';
import { Line } from '@ant-design/plots';

class DemoLine extends Component {
    constructor(props) {
        super(props);
        this.state = {
            cur_city: props.city,
            metric: "",
            data: []
        };
    }

    componentDidMount() {
        this.asyncFetch();
    }

    componentDidUpdate(prevProps) {
        if (prevProps.city !== this.props.city) {
            this.setState({ cur_city: this.props.city });
            this.setState({ metric: this.props.metric})
            this.asyncFetch();
        }
    }

    asyncFetch() {
        axios.get("http://127.0.0.1:5000/getCityStatistics/" + this.props.city)
            .then(res => {
                this.setState({ data: res.data });
                //console.log(res.data)
            })
    }

    render() {
        const config = {
            data: this.state.data,
            padding: 'auto',
            xField: 'tod',
            yField: this.state.metric,
            xAxis: {
                // type: 'timeCat',
                tickCount: 5,
            },
            slider: {
                start: 0.2,
                end: 0.6,
            },
            annotations: [
                {
                    type: 'line',
                    start: ['min', 'mean'],
                    end: ['max', 'mean'],
                    style: {
                        stroke: '#327039',
                    },
                },
                {
                    type: 'text',
                    position: ['min', 'mean'],
                    content: 'mean',
                    offsetY: -4,
                    style: { textBaseline: 'bottom' },
                }
            ],
        };

        return <Line {...config} />;
    }
}

export default DemoLine;