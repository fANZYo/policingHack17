import React from 'react';

// Components
import Timeline from './components/Timeline';
import Add from '../../components/Add';
import Report from '../../components/ReportForm';
import File from '../../components/FileForm';

// Style
import './index.css';

import openSocket from 'socket.io-client';
const socket = openSocket('http://localhost:5000');

const sub = (cb) => {
  socket.on('4daae28f26021bb18ccd611342459110c872fb9ef4cb06663c47ee97434a2390', (event) => cb(null, event));
};

class Home extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      crimeID: '4daae28f26021bb18ccd611342459110c872fb9ef4cb06663c47ee97434a2390',
      collapsed: true,
      state: false,
      data: {
        "timeline": []
      },
      timeline: [],
      report: false,
      file: false,
      isVictim: false,
    };

    sub((err, val) => {
      let arr = this.state.timeline.slice();
      arr.push(val.updated);
      this.setState({timeline: arr});
      window.scrollTo(0, 1000000000);
    });

  }

  reportHandler(event) {
    this.setState({report: true})
  }

  fileHandler(event) {
    this.setState({file: true})
  }

  addReport(event) {
    event.preventDefault();
    const data = {
      "crimeID": this.state.crimeID,
      "title": event.target.title.value,
      "description": event.target.description.value,
      "status": "on going",
      "isVictim": this.state.isVictim,
    };

    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", () => {
        this.componentWillMount();
    });

    xhr.open("POST", "http://localhost:5000/updateCrime");
    xhr.setRequestHeader("content-type", "application/json");

    xhr.send(JSON.stringify(data));
  }

  close(event) {
    event.preventDefault();
    this.setState({ report: false, file: false, isVictim: false });
  }

  addHandler(event) {
    event.stopPropagation();
    setTimeout(() => {
      this.setState({collapsed: true});
    }, 3333);

    this.setState({ collapsed: !this.state.collapsed })
  }

  isVicHandler(event) {
    this.setState({isVictim: !this.state.isVictim});
  }

  fileUpload(event) {
    event.preventDefault();
    const data = new FormData();
    data.append("crimeID", this.state.crimeID);
    data.append("file", event.target.file.files[0]);
    data.append("title", event.target.title.value);
    data.append("description", event.target.description.value);
    data.append("isVictim", this.state.isVictim);

    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", () => {
        this.componentWillMount();
    });

    xhr.open("POST", "http://localhost:5000/uploadMedia");

    xhr.send(data);
  }

  componentWillMount() {
    let data = null;

    const xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", () => {
      if (xhr.readyState === 4) {
        const d = JSON.parse(xhr.responseText);
        this.setState({report: false, file: false, isVictim: false, data: d, timeline: d.timeline});
        window.scrollTo(0, 1000000000);
      }
    });

    xhr.open("GET", `http://localhost:5000/report/${this.state.crimeID}`);
    xhr.setRequestHeader("content-type", "application/json");

    xhr.send(data);
  }

  render() {
    return (
      <section className="case">
        <h1 className="case__title">{this.state.data.name}</h1>
        <p className="case__description">{this.state.data.description}</p>
        <Timeline data={this.state.timeline} />
        <Add
          handler={this.addHandler.bind(this)}
          report={this.reportHandler.bind(this)}
          file={this.fileHandler.bind(this)}
          collapsed={this.state.collapsed}
        />
        {this.state.report && <Report isVic={this.isVicHandler.bind(this)} reportSend={this.addReport.bind(this)} close={this.close.bind(this)} />}
        {this.state.file && <File isVic={this.isVicHandler.bind(this)} fileUpload={this.fileUpload.bind(this)} close={this.close.bind(this)} />}
      </section>
    );
  }
};

export default Home;
