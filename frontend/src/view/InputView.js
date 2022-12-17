import React from 'react';
import { Form, Button } from 'semantic-ui-react';
import { useForm } from "react-hook-form";
import { useState } from 'react';
import "./InputView.css";
import findRoute from "../controller/APIs"
import {src, dest, ResetMap} from './MapboxView';

/**
 * This method contains the input field view and its related handling functions.
 * @param {*} setMyData A method defined in App.js which sets the user-given input data to tableValues.
 * @returns A view displaying the input fields and buttons.
 */
export default function InputView({setMyData}) {
    const loader = document.querySelector('.loader');

    // if you want to show the loader when React loads data again
    const showLoader = () => loader.classList.remove('loader--hide');

    const hideLoader = () => loader.classList.add('loader--hide');

    const { register, handleSubmit, formState: { errors }, clearErrors } = useForm();

    const [inputs, setInputs] = useState({});

    /**
     * This functions calls the setMyData method which sets the tableValues field in App.js.
     * @param {*} path Input values
     */
    const setThisData = (path) => {
        setMyData(path)
    }

    /**
     * This function displays a message if the start and end location are not specified.
     * @param {*} check This value is true if the locations are specified, otherwise false
     */
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

    /**
     * This function is called on submitting the find route button.
     * @param {*} data The input values given by user
     */
    const onSubmit = async(data)=> {
        showLoader();
        if(src==null || dest==null){
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
                const path = await findRoute(JSON.stringify(send_data)).catch(err => {
                    console.log("An error occurent in finding route");
                }).finally(() => {
                    hideLoader();
                }) //Sends the data to the controller 
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

    /**
     * This function is called when we click on reset button.
     */
    const onReset = () => {
        validateLocation(false);
        clearErrors();
        setInputs({})
        setMyData(undefined)
        ResetMap();
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
