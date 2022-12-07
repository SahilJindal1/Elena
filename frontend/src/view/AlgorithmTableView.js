import React, {useRef, useState} from "react";

const AlgorithmTableView = ({data}) => {
    let values = null;
    console.log("final data", data)
    if(data === undefined) {
        values = 'No values yet'
    } else {
        values = JSON.stringify(data)
    }

    return (
        <div>
             {values}
        </div>
    );
}

export default AlgorithmTableView