import React from 'react';
import ReactDOM from 'react-dom/client';
import Routing from "./Router.js"
import {BrowserRouter as Router } from 'react-router-dom';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <Router>
      <Routing />
    </Router>
);