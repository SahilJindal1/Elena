import React, { useState, useEffect } from 'react';
import InputView from './view/InputView.js';
import MapboxView from './view/MapboxView.js';
import "./App.css";

export default function App() {
  const [p, setP] = useState({})

  const setPath = (my_path) => {
    setP(my_path)
  }

    return (
        
        <div class="main">
            <MapboxView/>
            <InputView setMyPath={setPath} />
        </div>
        );
}
