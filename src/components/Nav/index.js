import React from 'react';
import { Link } from 'react-router-dom';
import { Icon } from 'react-fa';

// Styles
import './index.css';

const Nav = (props) => {
  return (
    <nav className="header__nav nav">
      <ul className={"nav__list" + (props.collapsed ? " nav__list--collapse" : "")}>
        <li className="nav__list__item nav__list__item--hamburger" onClick={props.handler.bind(this)}><Icon name="bars" size="lg" /></li>
        <li className="nav__list__item"><Link to="/">Home</Link></li>
        <li className="nav__list__item"><Link to="/faq">Common officer decisions</Link></li>
      </ul>
    </nav>
  );
};

export default Nav;
