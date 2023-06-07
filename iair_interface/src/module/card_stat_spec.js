import { InfoCircleOutlined, ArrowUpOutlined, CloudDownloadOutlined } from '@ant-design/icons';
import { Card, Col, Row, Statistic } from 'antd';
import axios from 'axios';
import FileSaver from 'file-saver';
import React from 'react';

export default class SingleStat extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            verification: this.props.verification,
            title: this.props.title,
            mode: this.props.mode,
            value: this.props.value,
            city_name: this.props.city_name
        };
    }


    download = () => {
        console.log(this.state.verification)
        if (this.state.verification === false) {
            alert("You have to get an access token to access the data.")
            return
        }
        if (this.state.mode === 'city' || this.state.mode === 'district' || this.state.mode === 'station') {
            axios({
                url: 'http://127.0.0.1:5000/downloader/' + this.state.mode,
                method: 'GET',
                responseType: 'blob',
            }).then((response) => {
                const filename = 'data.csv';
                FileSaver.saveAs(response.data, filename);
            });
        }
        else {
            axios({
                url: 'http://127.0.0.1:5000/downloader2/' + this.state.mode + '/' + this.state.city_name,
                method: 'GET',
                responseType: 'blob',
            }).then((response) => {
                const filename = 'data.csv';
                FileSaver.saveAs(response.data, filename);
            });
        }
    }



    componentDidUpdate(prevProps) {
        if (prevProps !== this.props) {
            this.setState({
                title: this.props.title,
                mode: this.props.mode,
                value: this.props.value,
                city_name: this.props.city_name,
                verification: this.props.verification
            })
        }
    }

    render() {
        return (
            <div>
                <Card bordered={true} hoverable={true} onClick={this.download}>
                    <div style={{ display: 'flex', alignItems: 'center' }}>
                        <Statistic
                            title={this.state.title}
                            value={this.state.value}
                            precision={0}
                            valueStyle={{
                                color: '#3f8600',
                            }}
                        />
                        <CloudDownloadOutlined style={{ fontSize: '24px', color: '#08c', marginLeft: '10px' }} />
                    </div>
                </Card>
            </div>
        )
    }
}