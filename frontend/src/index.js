import React from 'react';
import ReactDOM from 'react-dom';
import 'mapbox-gl/dist/mapbox-gl.css';
import './index.css';
import App from './App';
import '@mapbox/mapbox-gl-geocoder/lib/mapbox-gl-geocoder.css';

ReactDOM.render(
  //<React.StrictMode>
    <App />,
  //</React.StrictMode>
  document.getElementById('root')
);
