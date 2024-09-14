import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import PatientList from './components/PatientList';
import PatientForm from './components/PatientForm';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/patients" component={PatientList} />
          <Route path="/add-patient" component={PatientForm} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
