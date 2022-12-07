import React, { useState } from 'react';
import InputView from './view/InputView.js';
import MapboxView from './view/MapboxView.js';
import AlgorithmTableView from './view/AlgorithmTableView.js';
import "./App.css";
import {DisplayRoute} from './view/MapboxView.js';

export default function App() {
  
  
  const [tableValues, setTableValues] = useState()

  //const showRoute = (pathValue) => {
    
  //}

  const setAlgorithmValues = (pathValue) => {
    setTableValues(pathValue);
    DisplayRoute(pathValue);
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
