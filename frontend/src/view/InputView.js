import React from 'react';
import { Form, Button } from 'semantic-ui-react';
import { useForm } from "react-hook-form";
import { useRef, useState } from 'react';
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
            console.log('Missing values');
        } 
    }
    const handleChange = (event) => {
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({...values, [name]: value}))
    }

    const selectVal = (event) => {
        console.log(event);
    }

    return (
        <div>
            <Form onSubmit={handleSubmit(onSubmit)} className="inputView">
                <Form.Field className="formFields">
                <p ClassName="label">Elevation Gain</p>
                <div className='field'>
                    <label htmlFor="field-Minimum">
                        
                        <input
                            {...register("elevationType", { required: true})}
                            type="radio"
                            value="Minimum"
                            id="field-Minimum"
                            onChange={handleChange}
                        />
                        Minimum
                    </label>
                    <label htmlFor="field-Maximum">
                        <input
                            {...register("elevationType", { required: true})}
                            type="radio"
                            value="Maximum"
                            id="field-Maximum"
                            onChange={handleChange}
                        />
                        Maximum
                    </label>
                    
                </div>
                </Form.Field >
                {errors.elevationType && <p className='validationText'>Select Elevation Type</p>}
                <Form.Field className="formFields">
                    <label className='label'>Max. Distance Limit (x%)</label>
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


// import { useRef, useState } from 'react';
// import React from "react";
// import "./InputView.css";
// import findRoute from "../controller/APIs"
// import ReactFormInputValidation from "react-form-input-validation";
// import {src, dest} from './MapboxView';

// const InputView = ({setMyData}) => {
//     const [inputs, setInputs] = useState({});
//     const setThisData = (path) => {
//         setMyData(path)
//     }
//     this.form = new ReactFormInputValidation(this);
//     const onClickButton = async () => {
//         console.log(src, dest);
//         try {
//             let data = {
//                 "start_latitude": src[1],
//                 "end_latitude": dest[1],
//                 "start_longitude": src[0],
//                 "end_longitude": dest[0],
//                 "elevation_type": inputs.elevationType,
//                 "distance_limit": inputs.distanceLimit         
//             }
//             console.log(data);
//             const path = await findRoute(JSON.stringify(data)) //Sends the data to the controller 
//             console.log(path)
//             setThisData(path)
//         } catch(e) {
//             console.log('Missing values');
//         }
        
        
//     }

//     const handleChange = (event) => {
//         const name = event.target.name;
//         const value = event.target.value;
//         setInputs(values => ({...values, [name]: value}))
//     }

//     const handleSubmit = (event) => {
//         console.log(inputs);
//         setInputs({})
//     }

//     const selectVal = (event) => {
//         console.log(event);
//     }

//     const required = (value) => (value ? undefined : "Required");

//     return (
//         <div className="inputView">
//             <form>
//                 <div className='formFields'>
//                     <div className='label elevationTypeLabel'>
//                         Elevation Gain
//                     </div>

//                     <div className='field'>
//                     <input type="radio" value="minimum" id="minimize" name="elevationType" className='elevationType' required = "True"
//                         onChange={handleChange} checked={inputs.elevationType === 'minimum'}/>
//                     <label>MINIMIZE</label>
//                     <br></br>
//                     <input type="radio"  value="maximum" id="maximize" name="elevationType" className='elevationType'
//                         onChange={handleChange} checked={inputs.elevationType === 'maximum'}/>
//                     <label>MAXIMIZE</label>
//                     </div>
//                 </div>
//                 <div className='formFields'>
//                     <div className='label distanceLimitLabel'>
//                         Max. Distance Limit (x%)
//                     </div>
//                     <input 
//                         type="number" 
//                         name="distanceLimit" 
//                         className='field text-input'
//                         min="100"
//                         value={inputs.distanceLimit || ""} 
//                         onChange={handleChange}/>
//                 </div>
//             <input type="button" value="Find Route" className='routeButton' onClick={onClickButton}/><br></br>
//             </form>
//         </div>
//     );
// }

// export default InputView