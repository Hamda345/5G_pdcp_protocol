import logo from './logo.svg';
import PDCPHandler from "./PDCPHandler.js";
import PDCPLogList from "./PDCPLogList.js";
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <PDCPHandler />
        <PDCPLogList />
      </header>
    </div>
  );
}

export default App;
