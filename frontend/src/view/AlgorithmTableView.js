import React, {useRef, useState} from "react";
import './AlgorithmTableView.css'

const AlgorithmTableView = ({data}) => {
    let shortestDistance = null;
    let shortestElevation = null;
    let dijkstraDistance = null;
    let dijkstrElevation = null;
    let astarDistance = null;
    let astarElevation = null;

    console.log("final data", data)
    if(data !== undefined) {
        shortestDistance = data['shortest_path']['distance']
        shortestElevation = data['shortest_path']['elevation_gain']
        dijkstraDistance = data['dijkstra']['distance']
        dijkstrElevation = data['dijkstra']['elevation_gain']
        astarDistance = data['a_star']['distance']
        astarElevation = data['a_star']['elevation_gain']
    }

    return (
        <div>
            <table class="styled-table">
                <thead>
                    <tr>
                        <th>Algorithm</th>
                        <th>Distance</th>
                        <th>Elevation Gain</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Shortest Path</td>
                        <td>{shortestDistance}</td>
                        <td>{shortestElevation}</td>
                    </tr>
                    <tr class="active-row">
                        <td>Elena-Dijkstra</td>
                        <td>{dijkstraDistance}</td>
                        <td>{dijkstrElevation}</td>
                    </tr>
                    <tr>
                        <td>Elena-A*</td>
                        <td>{astarDistance}</td>
                        <td>{astarElevation}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    );
}

export default AlgorithmTableView