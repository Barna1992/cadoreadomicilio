import React, { Component } from "react";
import { render } from "react-dom";
import Emoji from "./emoji.js";
import Collapsible from "./collapsible.js";


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("api/locali")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }


  render() {
    return (
      <ul class="collapsible">
        {this.state.data.map(locale => {
          return (
            <li key={locale.id}>
              <Collapsible locale={locale}/>
            </li>
          );
        })}
      </ul>
    );
  }

}

export default App;

render(<App />, document.getElementById("app"));
