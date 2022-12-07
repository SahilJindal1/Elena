import React, { useState } from 'react';
import InputView from './view/InputView.js';
import MapboxView from './view/MapboxView.js';
import AlgorithmTableView from './view/AlgorithmTableView.js';
import "./App.css";

export default function App() {
  
  
  const [tableValues, setTableValues] = useState()

  const setAlgorithmValues = (pathValue) => {
    setTableValues(pathValue)
  }

    return (
        
        <div className="main">
            <MapboxView/>
            <div className='sideView'>
              <InputView setMyData={setAlgorithmValues} />
              <AlgorithmTableView data={tableValues} />
            </div>
        </div>
        );
}
