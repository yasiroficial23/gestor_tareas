import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ListaTareas = () => {
    const [tareas, setTareas] = useState([]);

    useEffect(() => {
        const fetchTareas = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:5000/tareas');
                setTareas(response.data);
            } catch (error) {
                console.error('Error al listar tareas:', error);
            }
        };
        fetchTareas();
    }, []);

    return (
        <div>
            <h2>Lista de Tareas</h2>
            <ul>
                {tareas.map((tarea) => (
                    <li key={tarea.id}>
                        <strong>{tarea.titulo}</strong>: {tarea.descripcion} ({tarea.completada ? 'Completada' : 'Pendiente'})
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ListaTareas;