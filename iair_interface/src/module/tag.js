import { Space, Tag } from 'antd';
import { Component } from 'react';

const { CheckableTag } = Tag;

class Tagging extends Component {
    constructor(props) {
        super(props);
        this.state = {
            tagsData: this.props.data,
            selectedTags: ['BeiJing']
        };
        this.handleChange = this.handleChange.bind(this);
    }

    componentDidUpdate(prevProps) {
        if (prevProps.data !== this.props.data) {
            this.setState({ tagsData: this.props.data });
        }
    }

    handleChange(tag, checked) {
        let nextSelectedTags = checked ? [tag] : [];
        // console.log('You are interested in: ', nextSelectedTags);
        this.setState({ selectedTags: nextSelectedTags });
        this.props.onValueChange(nextSelectedTags[0])
    }
    


    render() {
        const { selectedTags } = this.state;
        return (
            <div>
                <Space size={[0, 8]} wrap>
                    {this.state.tagsData.map((tag) => (
                        <CheckableTag
                            key={tag}
                            checked={selectedTags.includes(tag)}
                            onChange={(checked) => this.handleChange(tag, checked)}
                            style={{ fontSize: 14 }}
                        >
                            {tag}
                        </CheckableTag>
                    ))}
                </Space>
            </div>
        );
    }
}

export default Tagging;