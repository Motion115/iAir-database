import React from 'react';
import { AudioOutlined } from '@ant-design/icons';
import { Input, Space } from 'antd';
const { Search } = Input;


export default class InputBracket extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            input_content : ''
        }
    }

    recordChange = (e) => {
        this.setState({
            input_content : e
        })
        this.props.onValueChange(e)
    }

    render() {
        return (
            <div>
                <Search
                    allowClear
                    defaultValue='BeiJing'
                    onSearch={this.recordChange}
                    style={{
                        width: 300,
                    }}
                />
            </div>
        )
    }
}