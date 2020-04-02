import React, { Component } from "react";
import { render } from "react-dom";
import Emoji from "./emoji.js";
import emoji from "./emoji_dict.js"

class NavBarComponent extends Component {
  constructor(props) {
    super(props);
  }

  render()
    return {

    }
}

export default NavBarComponent;

render(<NavBarComponent />, document.getElementById("navbar"));
