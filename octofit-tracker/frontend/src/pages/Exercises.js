import React, { useState, useEffect } from 'react';
import { getExercises } from '../api';

const Exercises = () => {
  const [exercises, setExercises] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [filter, setFilter] = useState('all');

  useEffect(() => {
    const fetchExercises = async () => {
      try {
        const response = await getExercises();
        setExercises(response.data);
      } catch (err) {
        setError('Failed to load exercises');
        console.error('Error:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchExercises();
  }, []);

  const filteredExercises = filter === 'all' 
    ? exercises 
    : exercises.filter(ex => ex.category === filter);

  const categories = ['all', 'cardio', 'strength', 'flexibility', 'sports', 'other'];

  if (loading) {
    return (
      <div className="container mt-5 text-center">
        <div className="spinner-border" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <h1 className="mb-4">Exercises</h1>
      
      {error && (
        <div className="alert alert-danger" role="alert">
          {error}
        </div>
      )}

      <div className="mb-4">
        <div className="btn-group" role="group">
          {categories.map(cat => (
            <button
              key={cat}
              type="button"
              className={`btn ${filter === cat ? 'btn-primary' : 'btn-outline-primary'}`}
              onClick={() => setFilter(cat)}
            >
              {cat.charAt(0).toUpperCase() + cat.slice(1)}
            </button>
          ))}
        </div>
      </div>

      <div className="row">
        {filteredExercises.map((exercise) => (
          <div key={exercise.id} className="col-md-6 col-lg-4 mb-4">
            <div className="card shadow-sm h-100">
              <div className="card-body">
                <h5 className="card-title">{exercise.name}</h5>
                <p className="card-text">{exercise.description}</p>
                <div className="d-flex justify-content-between align-items-center">
                  <span className="badge bg-primary">{exercise.category}</span>
                  <small className="text-muted">
                    {exercise.calories_per_minute} cal/min
                  </small>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {filteredExercises.length === 0 && !error && (
        <div className="text-center text-muted py-5">
          No exercises found
        </div>
      )}
    </div>
  );
};

export default Exercises;
