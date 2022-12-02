import './App.css';

import AlgorithmTableView from './view/AlgorithmTableView.js';
import InputView from './view/InputView.js';
import MapView from './view/MapView.js';

function App() {
  return (
    <div className="App">
      <div className="App-header">
      ELENA
      </div>
      <div class="main-content">
        <div class="content">
          <InputView />
          <AlgorithmTableView />
        </div>
        <MapView />
      </div>
    </div>
  );
}

export default App;

