import React from 'react';
import CrearTarea from './components/CrearTarea';
import ListaTareas from './components/ListaTareas';
import './App.css';

function App() {
    return (
        <div>
            <h1>Gestor de Tareas</h1>
            <CrearTarea />
            <ListaTareas />
        </div>
    );
}

export default App;
