import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

const user = {
    "firstName": "Pramodh",
    "lastName": "Bettadapura"
}

ReactDOM.render(<App user={user}/>, document.getElementById('root'));
