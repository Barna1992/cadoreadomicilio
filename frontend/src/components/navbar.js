import React, { Component } from "react";
import { render } from "react-dom";
import Emoji from "./emoji.js";
import emoji from "./emoji_dict.js"

const NavBar = props => (
  <div className="nav-wrapper">
    <a href="#" className="brand-logo"><Emoji label='Casa' symbol={emoji['Casa']}/> Cadore a domicilio <Emoji label='Montagna' symbol={emoji['Montagna']}/></a>
    <ul id="nav-mobile" className="right hide-on-med-and-down">
      <li><a href="about.html">About</a></li>
    </ul>
  </div>
)

export default NavBar;

render(<NavBar />, document.getElementById("navbar"));
