import React from 'react';

// Styles
import './index.css';

const Report = (props) => {
  return (
    <form className="file" onSubmit={props.fileUpload.bind(this)}>
      <button className="file__close" onClick={props.close.bind(this)}>x</button>
      <label className="file__label">Title: <input className="file__input" type="text" name="title" /></label>
      <label className="file__label">Description: <textarea className="file__input" rows="10" cols="35" name="description"></textarea></label>
      <label className="file__label">File: <input className="file__input" type="file" name="file"></input></label>
      <button className="file__submit" type="submit">Send</button>
      <label style={{float: "right", marginTop: ".25em"}}>Victim? <input onChange={props.isVic.bind(this)} type="checkbox" name="check" /></label>
    </form>
  )
}

export default Report;
