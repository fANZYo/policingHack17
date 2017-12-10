import React from 'react';
import { Icon } from 'react-fa';

// Styles
import './index.css';

const TimeItem = (props, index) => {
  return (
    <li key={index} className="line__item">
      <div className="line__item__card" style={props.isVictim ? { background: "#FFE2ED" } : { background: "#c5effd" }}>
        <h2 className="line__item__title">{props.title}</h2>
        <p className="line__item__date">{props.date}</p>
        { props.description && <p className="line__item__description">{props.description}</p> }
        { props.media && <a href={props.media[0].url} target="_blank"><Icon className="line__item__file" name="file" />test</a> }
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
