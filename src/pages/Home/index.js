import React from 'react';

// Components
import Timeline from './components/Timeline';
import Add from '../../components/Add';
import Report from '../../components/ReportForm';
import File from '../../components/FileForm';

// Dummy data
import data from './dummy.json';

// Style
import './index.css';

import openSocket from 'socket.io-client';
const socket = openSocket('http://192.168.1.34:5000');

const sub = (cb) => {
  socket.on('000001', (event) => cb(null, event));
};

class Home extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      collapsed: true,
      state: false,
      data: {
        "timeline": []
      },
      timeline: [],
      report: false,
      file: false,
    };

    sub((err, val) => {
      console.log(val);
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
      "crimeID": "000001",
      "title": event.target.title.value,
      "description": event.target.description.value,
      "status": "on going"
    };

    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", () => {
        this.componentWillMount();
    });

    xhr.open("POST", "http://192.168.1.34:5000/updateCrime");
    xhr.setRequestHeader("content-type", "application/json");

    xhr.send(JSON.stringify(data));
  }

  close(event) {
    event.preventDefault();
    this.setState({ report: false, file: false });
  }

  addHandler(event) {
    event.stopPropagation();
    setTimeout(() => {
      this.setState({collapsed: true});
    }, 3333);

    this.setState({ collapsed: !this.state.collapsed })
  }

  fileUpload(event) {
    event.preventDefault();
    const data = new FormData();
    data.append("crimeID", "000001");
    data.append("file", event.target.file.files[0]);
    data.append("title", event.target.title.value);
    data.append("description", event.target.description.value);

    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", () => {
        this.componentWillMount();
    });

    xhr.open("POST", "http://192.168.1.34:5000/uploadMedia");

    xhr.send(data);
  }

  componentWillMount() {
    let data = null;

    const xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", () => {
      if (xhr.readyState === 4) {
        const d = JSON.parse(xhr.responseText);
        this.setState({report: false, file: false, data: d, timeline: d.timeline});
        window.scrollTo(0, 1000000000);
      }
    });

    xhr.open("GET", "http://192.168.1.34:5000/report/000001");
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
        {this.state.report && <Report reportSend={this.addReport.bind(this)} close={this.close.bind(this)} />}
        {this.state.file && <File fileUpload={this.fileUpload.bind(this)} close={this.close.bind(this)} />}
      </section>
    );
  }
};

export default Home;
