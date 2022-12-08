import React from 'react';
import { Form, Button } from 'semantic-ui-react';
import { useForm } from "react-hook-form";
import { useState } from 'react';
import "./InputView.css";
import findRoute from "../controller/APIs"
import {src, dest} from './MapboxView';

export default function InputView({setMyData}) {
    const { register, handleSubmit, formState: { errors } } = useForm();

    const [inputs, setInputs] = useState({});
    const setThisData = (path) => {
        setMyData(path)
    }
    const validateLocation = () =>{
        const msgdisplay = document.getElementById("locationError");
        msgdisplay.innerHTML= "Enter a start and end location";
    }
    const onSubmit = async(data)=> {
        console.log(data);
        console.log("src");
        console.log(src, dest);
        if(src==null || dest==null){
            console.log("In the errorr ")
            validateLocation();
        }
        try {
            let send_data = {
                "start_latitude": src[1],
                "end_latitude": dest[1],
                "start_longitude": src[0],
                "end_longitude": dest[0],
                "elevation_type": data.elevationType,
                "distance_limit": data.distanceLimit         
            }
            console.log(send_data);
            const path = await findRoute(JSON.stringify(send_data)) //Sends the data to the controller 
            console.log(path)
            setThisData(path)
        } catch(e) {
            console.log(e);
            console.log('Missing values');
        } 
    }
    const handleChange = (event) => {
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({...values, [name]: value}))
    }

    return (
        <div>
            <Form onSubmit={handleSubmit(onSubmit)} className="inputView">
                <Form.Field className="formFields">
                <p className="label">Elevation Gain:</p>
                <div className='field'>
                    <label htmlFor="field-Minimum">
                        
                        <input
                            {...register("elevationType", { required: true})}
                            type="radio"
                            value="Minimum"
                            id="field-Minimum"
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
                        className = "field text-input"
                        onChange={handleChange}
                        {...register("distanceLimit", { required: true, maxLength: 10 })}
                    />
                </Form.Field>
                {errors.distanceLimit && <p className='validationText'>Enter the Max. Distance Limit</p>}
                <Button type='submit' className='routeButton'>Find Route</Button>
                <p className='validationText' id="locationError"></p>
            </Form>
        </div>
    )
}
