import InputView from './view/InputView.js';
import MapboxView from './view/MapboxView.js';
import "./App.css";

export default function App() {

    return (
        
        <div class="main">
            <MapboxView/>
            <InputView/>
        </div>
        );
}
