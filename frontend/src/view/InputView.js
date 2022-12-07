import { useRef, useState } from 'react';
import React from "react";
import "./InputView.css";
import findRoute from "../controller/APIs"

import {src, dest} from './MapboxView';

const InputView = ({setMyData}) => {
    const [inputs, setInputs] = useState({});
    const setThisData = (path) => {
        setMyData(path)
    }

    const onClickButton = async () => {
        console.log(src, dest);
        try {
            let data = {
                "start_latitude": src[1],
                "end_latitude": dest[1],
                "start_longitude": src[0],
                "end_longitude": dest[0],
                "elevation_type": inputs.elevationType,
                "distance_limit": inputs.distanceLimit         
            }
            console.log(data);
            const path = await findRoute(JSON.stringify(data)) //Sends the data to the controller 
            console.log(path)
            setThisData(path)
        } catch(e) {
            console.log('Missing values');
        }
        
        
    }

    const handleChange = (event) => {
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({...values, [name]: value}))
    }

    const handleSubmit = (event) => {
        console.log(inputs);
        setInputs({})
    }

    const selectVal = (event) => {
        console.log(event);
    }


    return (
        <div className="inputView">
            {/* <div className='formFields'>
                <div className='label startLabel'>
                    Start Destination
                </div>
                <input 
                    type="text" 
                    name="startDestination" 
                    className='field text-input'
                    value={inputs.startDestination || ""} 
                    onChange={handleChange}
                />
            </div>
            <div className='formFields'>
                <div className='label endLabel'>
                    End Destination
                </div>
                <input 
                    type="text" 
                    name="endDestination" 
                    className='field text-input'
                    value={inputs.endDestination || ""} 
                    onChange={handleChange}
                />
            </div> */}
            <div className='formFields'>
                <div className='label elevationTypeLabel'>
                    Elevation Gain
                </div>

                <div className='field'>
                <input type="radio" value="minimum" id="minimize" name="elevationType" className='elevationType'
                    onChange={handleChange} checked={inputs.elevationType === 'minimum'}/>
                <label>MINIMIZE</label>
                <br></br>
                <input type="radio" value="maximum" id="maximize" name="elevationType" className='elevationType'
                    onChange={handleChange} checked={inputs.elevationType === 'maximum'}/>
                <label>MAXIMIZE</label>
                </div>
            </div>
            <div className='formFields'>
                <div className='label distanceLimitLabel'>
                    Max. Distance Limit (x%)
                </div>
                <input 
                    type="number" 
                    name="distanceLimit" 
                    className='field text-input'
                    min="100"
                    value={inputs.distanceLimit || ""} 
                    onChange={handleChange}
                />
            </div>
            <input type="button" value="Find Route" className='routeButton' onClick={onClickButton}/><br></br>
        </div>
    );
}

export default InputView