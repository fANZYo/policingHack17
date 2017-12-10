import React from 'react';

// Styles
import './index.css';

const Add = (props) => {
  return (
    <ul className={"add" + (props.collapsed ? " add--collapse" : "")} >
      <li onClick={props.file.bind(this)} className="add__item">File</li>
      <li onClick={props.report.bind(this)} className="add__item">Report</li>
      <li><button className="add__button" onClick={props.handler.bind(this)}>+</button></li>
    </ul>
  );
};

export default Add;
