import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {
  const [linea1, setlinea1] = useState('');
  const [linea2, setlinea2] = useState('');
  const onChangelinea1 = function(evento){
    setlinea1(evento.target.value)
  }

  const onChangelinea2 = function(evento){
    setlinea2(evento.target.value)
  }
  
  return (
    <div className="App">

      <select>
        <option value= "Fire">Casa en llamas</option>
        <option value="Futurama">Futurama</option>
        <option value="Alien">Aliens</option>
        <option value ="Matrix">Matrix</option>
        <option value = "Smart">Smart Guy</option>
      </select> <br/>

      <input onChange={onChangelinea1} type = "text" placeholder = "Line 1" />
      <br/>
      <input onChange={onChangelinea2} type = "text" placeholder = "Line 2" />
      <br />
      <button>Export</button>

      <div>
          <span>{linea1}</span> <br /><br/>
          <span>{linea2}</span>
          <img src = ""/>
      </div>
      {/* //seelct picker meme
      //input text - first line
      //input text - second line
      // export button */}
    </div>
  );
}

export default App;
