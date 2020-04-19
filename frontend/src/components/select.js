import React, { Component } from "react";
import { render } from "react-dom";

class SelectFilter extends React.Component {
  constructor(props){
    super(props);
    this.state = {
    selected: 0,
    data: [],
    loaded: false,
                }
    }

  componentDidMount() {
    fetch("api/comuni")
    .then(response => {
      if (response.status > 400) {
        return this.setState(() => {
          return { placeholder: "C'e stato un problema nel caricamento!" };
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
      $('#locali-consegna').formSelect();
    });
  }


  render() {
      return(
        <div className="input-field col s12">
          <select id='locali-consegna' value={this.state.selected} onChange={e => {
            this.setState({
              selected: e.target.value,
              validationError:
                e.target.value === ""
                  ? "Nessun locale selezionato"
                  : ""
            });}
            }>
              <option key="0" value="0" >Ovunque</option>
            {this.state.data.map(comune => {
              return(
                <option key={comune.id} value={comune.comune}>{comune.comune_verbose}</option>
              )
              })}
          </select>
          <label className='label-select'>Consegna a...</label>
        </div>
      )
  }
}

export default SelectFilter;
