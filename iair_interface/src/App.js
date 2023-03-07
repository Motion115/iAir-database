import './App.css';
import React from 'react';
import axios from 'axios';

export default class App extends React.Component {
  state = {
    city_table: []
  }

  click() {
    axios.get("http://127.0.0.1:5000/data")
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
        // button for activating the call function
        <button onClick={() => this.click()}>Click</button>
        <p>
          {this.call()}
        </p>
      </div>
    )
  }
}