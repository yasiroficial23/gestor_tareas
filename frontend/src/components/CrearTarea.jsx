import React, { useState } from 'react';
import axios from 'axios';

const CrearTarea = () => {
    const [titulo, setTitulo] = useState('');
    const [descripcion, setDescripcion] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://127.0.0.1:5000/tareas', {
                titulo,
                descripcion,
            });
            alert('Tarea creada!');
            setTitulo('');
            setDescripcion('');
        } catch (error) {
            console.error('Error al crear tarea:', error);
            alert('Error al crear la tarea');
        }
    };

    return (
        <div>
            <h2>Crear Nueva Tarea</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Título:</label>
                    <input
                        type="text"
                        value={titulo}
                        onChange={(e) => setTitulo(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Descripción:</label>
                    <textarea
                        value={descripcion}
                        onChange={(e) => setDescripcion(e.target.value)}
                    />
                </div>
                <button type="submit">Agregar Tarea</button>
            </form>
        </div>
    );
};

export default CrearTarea;