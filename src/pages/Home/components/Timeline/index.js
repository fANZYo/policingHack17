import React from 'react';

// Styles
import './index.css';

const TimeItem = (props, index) => {
  return (
    <li key={index} className="line__item">
      <div className="line__item__card">
        <h2 className="line__item__title">{props.title}</h2>
        <p className="line__item__date">{props.date}</p>
        { props.description && <p className="line__item__description">{props.description}</p> }
      </div>
    </li>
  );
}

const Timeline = (props) => {
  return (
    <ul className="line">
      {props.data.map(TimeItem)}
    </ul>
  );
};

export default Timeline;
