import React from 'react';

// Styles
import './index.css';

const Report = (props) => {
  return (
    <form className="report" onSubmit={props.reportSend.bind(this)}>
      <button className="report__close" onClick={props.close.bind(this)}>x</button>
      <label className="report__label">Title: <input className="report__input" type="text" name="title" /></label>
      <label className="report__label">Description: <textarea className="report__input" rows="10" cols="35" name="description"></textarea></label>
      <button className="report__submit" type="submit">Send</button>
      <label style={{float: "right", marginTop: ".25em"}}>Victim? <input onChange={props.isVic.bind(this)} type="checkbox" name="check" /></label>
    </form>
  )
}

export default Report;
