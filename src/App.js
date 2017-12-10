import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
} from 'react-router-dom';

// Styles
import './reset.css';
import './index.css';

// Components
import Nav from './components/Nav';
import Home from './pages/Home';
import Faq from './pages/Faq';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      collapsed: true,
    };
  }

  navHandler(event) {
    event.stopPropagation();
    this.setState({ collapsed: !this.state.collapsed })
  }

  navUp(event) {
    this.setState({ collapsed: true })
  }

  render() {
    return (
      <Router>
        <div className="wrapper" onClick={this.navUp.bind(this)}>
          <header className="header">
            <h1 className="header__title"><img className="header__title__img" src="logo.png" alt="Policing hackathon logo" /></h1>
            <Nav collapsed={this.state.collapsed} handler={this.navHandler.bind(this)} />
          </header>
          <section>
            <Route exact path="/" component={Home} />
            <Route path="/faq" component={Faq} />
          </section>
        </div>
      </Router>
    );
  }
}

export default App;
