import { useState } from 'react';
import React from "react";
import "./InputView.css";

const InputView = () => {
    const [inputs, setInputs] = useState({});

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
            <input type="button" value="Find Route" className='routeButton' onClick={handleSubmit}/>
        </div>
    );
}

export default InputView