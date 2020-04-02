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
      <div className="nav-wrapper">
        <a href="/" className="brand-logo"><Emoji label='Casa' symbol={emoji['Casa']}/> Cadore a domicilio <Emoji label='Montagna' symbol={emoji['Montagna']}/></a>
        <ul id="nav-mobile" className="right">
          <li><a href="about.html">About</a></li>
        </ul>
      </div>
    }
}

export default NavBarComponent;

render(<NavBarComponent />, document.getElementById("navbar"));
