import React from 'react';
import './AlgorithmTableView.css'

/**
 * This method contains the algorithm table view related front-end functions and the UI.
 * @param {*} data The algorithm data we get from backend
 * @returns A table view
 */
const AlgorithmTableView = ({data}) => {
    let shortestDistance = null;
    let shortestElevation = null;
    let dijkstraDistance = null;
    let dijkstrElevation = null;
    let astarDistance = null;
    let astarElevation = null;
    if(data !== undefined) {
            shortestDistance = data['shortest_path']['distance'].toFixed(3)
            shortestElevation = data['shortest_path']['elevation_gain'].toFixed(3)
            dijkstraDistance = data['dijkstra']['distance'].toFixed(3)
            dijkstrElevation = data['dijkstra']['elevation_gain'].toFixed(3)
            astarDistance = data['a_star']['distance'].toFixed(3)
            astarElevation = data['a_star']['elevation_gain'].toFixed(3)   
    }

    return (
        <div className="algorithm-table-view">
            <table className="styled-table">
                <thead>
                    <tr>
                        <th>Algorithm</th>
                        <th>Distance (in m)</th>
                        <th>Elevation Gain (in m)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Shortest Path</td>
                        <td>{shortestDistance}</td>
                        <td>{shortestElevation}</td>
                    </tr>
                    <tr className="active-row">
                        <td>EleNA - Dijkstra</td>
                        <td>{dijkstraDistance}</td>
                        <td>{dijkstrElevation}</td>
                    </tr>
                    <tr>
                        <td>EleNA - A*</td>
                        <td>{astarDistance}</td>
                        <td>{astarElevation}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    );
}

/**
 * This function resets the table view.
 */
export const ResetTableView = () => {
    let data = {'shortest_path':{'distance':'', 'elevation_gain':''},
            'dijkstra':{'distance':'', 'elevation_gain':''},
            'a_star':{'distance':'', 'elevation_gain':''}};
}

export default AlgorithmTableView