import React, { useState } from 'react';
import InputView from './view/InputView.js';
import MapboxView from './view/MapboxView.js';
import AlgorithmTableView from './view/AlgorithmTableView.js';
import "./App.css";
import {DisplayRoute} from './view/MapboxView.js';

export default function App() {
  
  
  const [tableValues, setTableValues] = useState()

  const setAlgorithmValues = (pathValue) => {
    setTableValues(pathValue);
  }

    return (
        
        <div className="main">
            <MapboxView response={tableValues} className='mapView'/>
            <div className='sideView'>
              <img src="https://drive.google.com/uc?export=view&id=16clIzknlokS-moS1RTtkL5MjEv0hkXIX" width="150" height="60"/> 
              <InputView setMyData={setAlgorithmValues} />
              <AlgorithmTableView data={tableValues} />
            </div>
        </div>
        );
}
