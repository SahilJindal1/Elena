import React from 'react';
import { Form, Button } from 'semantic-ui-react';
import { useForm } from "react-hook-form";
import { useState } from 'react';
import "./InputView.css";
import findRoute from "../controller/APIs"
import {src, dest, ResetMap} from './MapboxView';

export default function InputView({setMyData}) {
    const loader = document.querySelector('.loader');

    // if you want to show the loader when React loads data again
    const showLoader = () => loader.classList.remove('loader--hide');

    const hideLoader = () => loader.classList.add('loader--hide');

    const { register, handleSubmit, formState: { errors }, clearErrors } = useForm();

    const [inputs, setInputs] = useState({});
    const setThisData = (path) => {
        setMyData(path)
    }
    const validateLocation = (check) =>{
        console.log("inside input valid");
        const msgdisplay = document.getElementById("locationError");
        const formMsg = document.getElementsByClassName("validationText");
        if(check === true){
            msgdisplay.innerHTML= "Enter a start and end location";
        }
        else{
            msgdisplay.innerHTML= "";
            formMsg.innerHTML = "";          
        }

    }
    const onSubmit = async(data)=> {
        showLoader();
        console.log(data);
        console.log("src");
        console.log(src, dest);
        if(src==null || dest==null){
            console.log("In the errorr ")
            hideLoader();
            validateLocation(true);
        }
        else
        {
            try {
                validateLocation(false);
                let send_data = {
                    "start_latitude": src[1],
                    "end_latitude": dest[1],
                    "start_longitude": src[0],
                    "end_longitude": dest[0],
                    "elevation_type": data.elevationType,
                    "distance_limit": data.distanceLimit         
                }
                console.log(send_data);
                const path = await findRoute(JSON.stringify(send_data)).catch(err => {
                    console.log("An error occurent in finding route");
                }).finally(() => {
                    hideLoader();
                    console.log("finally");
                }) //Sends the data to the controller 
                console.log(path)
                setThisData(path)
            } catch(e) {
                console.log(e);
                hideLoader();
                console.log('Missing values');
            } 
        }

    }
    const handleChange = (event) => {
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({...values, [name]: value}))
    }

    const onReset = () => {
        validateLocation(false);
        clearErrors();
        setInputs({})
        setMyData(undefined)
        ResetMap();
        console.log("Here's the inputs",inputs)

    }

    return (
        <div className="inputView">
            <div className='loader loader--hide'></div>
            <Form onSubmit={handleSubmit(onSubmit)} className="inputTable">
                <Form.Field className="formFields">
                <p className="label">Elevation Gain:</p>
                <div className='field'>
                    <label htmlFor="field-Minimum">
                        
                        <input
                            {...register("elevationType", { required: true})}
                            type="radio"
                            value="Minimum"
                            id="field-Minimum"
                            className="input-values"
                            onChange={handleChange}
                        />
                        Minimize
                    </label>
                    <label htmlFor="field-Maximum">
                        <input
                            {...register("elevationType", { required: true})}
                            type="radio"
                            value="Maximum"
                            id="field-Maximum"
                            className="input-values"
                            onChange={handleChange}
                        />
                        Maximize
                    </label>
                </div>
                </Form.Field >
                {errors.elevationType && <p className='validationText'>Select Elevation Type</p>}
                <Form.Field className="formFields">
                    <label className='label'>Max. Limit (x%):</label>
                    <input
                        placeholder='%'
                        type="number"
                        className = "field text-input input-values"
                        onChange={handleChange}
                        {...register("distanceLimit", { required: true, maxLength: 10, min:100, max:200 })}
                    />
                </Form.Field>
                {errors.distanceLimit && <p className='validationText'>Enter Valid Max. Distance Limit</p>}
                <Button type='submit' className='routeButton'>Find Route</Button>
                <Button type='reset' className='resetButton' onClick={onReset}>Reset</Button>
                <p className='validationText' id="locationError"></p>
            </Form>
        </div>
    )
}
