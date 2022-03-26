import Nav from './component/Nav'
import './App.css';
import Search from './component/Search'
import {BrowserRouter as Router,Routes, Route} from "react-router-dom"
function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <Nav />
          <Routes>
            <Route path="/" exact component = {Search} />

          </Routes>
        </header>
      </div>
    </Router>
  );
}

export default App;
