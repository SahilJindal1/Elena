import { useState } from 'react';
import React from "react";
import "./InputView.css";
import findRoute from "../controller/APIs"


const InputView = ({setMyData}) => {
    const [inputs, setInputs] = useState({});
    const [backend_data, setDataStats] = useState();
    console.log("backend Data", backend_data);

    const setThisData = (path) => {
        setMyData(path)
    }

    const onClickButton = async () => {
        let data = {
            "start_latitude": 0.009,
            "end_latitude":0.02,
            "start_longitude":0.087,
            "end_longitude":0.236,
            "elevation_type":"maximum",
            "distance_limit": 1.50          
        }
        console.log(data);
        let path = await findRoute(JSON.stringify(data)) //Sends the data to the controller 
        setDataStats(path)
        setThisData(path)
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
                <input type="radio" value="Minimize" id="minimize" name="elevationType" className='elevationType'
                    onChange={handleChange} checked={inputs.elevationType === 'Minimize'}/>
                <label>MINIMIZE</label>
                <br></br>
                <input type="radio" value="Maximize" id="maximize" name="elevationType" className='elevationType'
                    onChange={handleChange} checked={inputs.elevationType === 'Maximize'}/>
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
            <div>OUTPUT:{backend_data}</div>
        </div>
    );
}

export default InputView