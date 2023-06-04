import React from 'react';
import { Layout } from 'antd';
const { Footer } = Layout;

export default class Foot extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <Footer style={{ textAlign: 'center', }}>
                    Motion115 ©2023
                </Footer>
            </div>
        )
    }
}