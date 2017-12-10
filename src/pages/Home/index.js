import React from 'react';

// Components
import Timeline from './components/Timeline';

// Dummy data
import data from './dummy.json';

// Style
import './index.css';

const Home = (props) => {
  console.log(data);
  return (
    <section className="case">
      <h1 className="case__title">{data.name}</h1>
      <p className="case__description">{data.description}</p>
      <Timeline data={data.timeline} />
    </section>
  );
};

export default Home;
