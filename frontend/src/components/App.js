import React, { Component } from "react";
import { render } from "react-dom";
import Emoji from "./emoji.js";
import WholeCollapsible from "./collapsible.js";
import SelectFilter from "./select.js";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      selected: '0'
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    this.setState({
      selected: event.target.value
    });
  };

  render() {
    return (
      <div onChange={this.handleChange}>
        <SelectFilter />
        <WholeCollapsible filter={this.state.selected}/>
      </div>
    );
  }

}

export default App;

render(<App />, document.getElementById("app"));
