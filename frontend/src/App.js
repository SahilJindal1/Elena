import React, { useState, useEffect } from 'react';
import InputView from './view/InputView.js';
import {MapboxView, DisplayRoute} from './view/MapboxView.js';
import AlgorithmTableView from './view/AlgorithmTableView.js';
import "./App.css";
//import  from './view/MapboxView.js';

export default function App() {
  
  
  const [tableValues, setTableValues] = useState()

  //const showRoute = (pathValue) => {
    
  //}

  const setAlgorithmValues = (pathValue) => {
    setTableValues(pathValue);
    DisplayRoute(pathValue);
  }

    return (
        
        <div class="main">
            <MapboxView/>
            <div className='sideView'>
              <InputView setMyData={setAlgorithmValues} />
              <AlgorithmTableView data={tableValues} />
            </div>
        </div>
        );
}
