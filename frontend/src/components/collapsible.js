import React, { Component } from "react";
import { render } from "react-dom";
import Emoji from "./emoji.js";
import emoji from "./emoji_dict.js"

const CollapsibleBody = props => (
  <div className='content'>
    <div className='row'>
      <h5 className="center-align">{ props.locale.name } <Emoji label='Luogo' symbol={emoji['Luogo']}/> { props.locale.comune } </h5>
      <h5 className="center-align">Categoria: { props.locale.categoria } <Emoji label={props.locale.categoria} symbol={emoji[props.locale.categoria]}/></h5>
      <div className='row'>
        <div className='col'>
          <h5>Come funziona:</h5>
        </div>
      </div>
      <div className='row'>
        <div className='col'>
      { props.locale.come_funziona ? (
        <p><i className="fas fa-pen" aria-hidden="true"></i>{props.locale.come_funziona}</p>
      ) : '' }
      </div></div>
      <div className='row'>
        <div className='col'>
          <h5>Contatti:</h5>
        </div>
      </div>
      <div className="row">
      <div className="col m3"><p>telefono <i className="fa fa-phone grey-text darken-4" aria-hidden="true"></i></p></div>
      <div className="col m3">
      { props.locale.telefono ? (
        <p>{props.locale.telefono}</p>
      ) : '' }
      </div>
      </div><div className="row">
      <div className="col m3"><p>facebook <i className="fab fa-facebook blue-text darken-4" aria-hidden="true"></i></p></div>
      <div className="col m3">
      { props.locale.facebook ? (
        <p><a href={props.locale.facebook}>{props.locale.facebook}</a></p>
      ) :'' }
      </div>
      </div><div className="row">
      <div className="col m3"><p>email <i className="fa fa-envelope red-text accent-4" aria-hidden="true"></i></p></div>
      <div className="col m3">
      { props.locale.email ? (
        <p><a href="mailto: {props.locale.email}">{props.locale.email}</a></p>
      ) :'' }
      </div>
      </div><div className="row">
      <div className="col m3"><p>sito <i className="fa fa-laptop grey-text darken-4" aria-hidden="true"></i></p></div>
      <div className="col m3">
      { props.locale.sito ?   (
        <p><a href={props.locale.sito}>{props.locale.sito}</a></p>
      ) :'' }
      </div>
      </div>
      <div className='row'>
        <div className='col'>
          <h5>Orari giornalieri:</h5>
        </div>
      </div>
      <div className="row">
        <div className="col m3">
        <p>mattina</p>
        </div>
        <div className="col m3">
        { props.locale.orario_mattina ? (
          <p>{props.locale.orario_mattina}</p>
        ) :'' } </div>
      </div>
      <div className="row">
        <div className="col m3">
        <p>pomeriggio</p>
        </div>
        <div className="col m3">
        { props.locale.orario_pomeriggio ? (
          <p>{props.locale.orario_pomeriggio}</p>
        ) :'' }</div>
      </div>
      <div className="row">
        <div className="col m3">
        <p>chiude di:</p>
        </div>
        <div className="col m3">
        { props.locale.chiusura ? (
          <p>{props.locale.chiusura}</p>
        ) :'' }</div>
      </div>
      <div className='row'>
        <div className='col'>
          <h5>Altre informazioni:</h5>
        </div>
      </div>
      <div className='row'>
        <div className='col'>
        <p> Consegna a pranzo {
            props.locale.pranzo ? (
              <i className="fas fa-check"></i>
            ) : <i className="fas fa-times"></i>
        } </p>
        </div>
      </div>
        <div className='row'>
          <div className='col'>
        <p> Consegna a cena {
            props.locale.cena ? (
              <i className="fas fa-check"></i>
            ) : <i className="fas fa-times"></i>
        } </p>
          </div>
        </div>
        <div className='row'>
          <div className='col'>
          <p><strong> Consegna ai seguenti paesi </strong></p> {
              props.locale.consegno_a.map(
                (nome) => <p>{nome}</p>
              )
          }
          </div>
        </div>
        <div className='row'>
          <div className='col'>
        { props.locale.note ? (
          <p><i className="fas fa-pen" aria-hidden="true"></i>{props.locale.note}</p>
        ) : '' }
        </div>
      </div>
    </div>
  </div>
)

class Collapsible extends React.Component {
    constructor(props){
      super(props);
      this.state = {
      open: false
      }
      this.togglePanel = this.togglePanel.bind(this);
      }

    togglePanel(e){
      this.setState({
        open: !this.state.open
      })
    }

    render() {
      return (<div>
        <div onClick={(e)=>this.togglePanel(e)} className='header'>
         <div className = "row hoverable">
           <div className='col s10 m10 valign-wrapper'><h6 className='center-align'><Emoji label={this.props.locale.categoria} symbol={emoji[this.props.locale.categoria]}/>   {this.props.locale.name}</h6></div>
          <div className='col s2 m2 valign-wrapper'><h6 className='center-align'>
          {this.state.open ? ( <i className="fas fa-angle-up right"></i> ) : ( <i className="fas fa-angle-down right"></i> ) }
          </h6></div>
        </div>
        </div>
        {this.state.open ? (
          <CollapsibleBody locale={this.props.locale} />
        ) : null}
      </div>);
      }
    }

export default Collapsible;
