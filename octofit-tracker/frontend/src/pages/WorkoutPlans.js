import React, { useState, useEffect } from 'react';
import { getWorkoutPlans } from '../api';

const WorkoutPlans = () => {
  const [plans, setPlans] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchPlans = async () => {
      try {
        const response = await getWorkoutPlans();
        setPlans(response.data);
      } catch (err) {
        setError('Failed to load workout plans');
        console.error('Error:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchPlans();
  }, []);

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
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h1>Workout Plans</h1>
      </div>
      
      {error && (
        <div className="alert alert-danger" role="alert">
          {error}
        </div>
      )}

      <div className="row">
        {plans.map((plan) => (
          <div key={plan.id} className="col-md-6 col-lg-4 mb-4">
            <div className="card shadow-sm h-100">
              <div className="card-body">
                <h5 className="card-title">{plan.title}</h5>
                <p className="card-text">{plan.description}</p>
                <div className="mb-2">
                  <span className={`badge bg-${
                    plan.difficulty_level === 'beginner' ? 'info' :
                    plan.difficulty_level === 'intermediate' ? 'warning' : 'danger'
                  }`}>
                    {plan.difficulty_level}
                  </span>
                </div>
                <div className="text-muted small">
                  <div>Duration: {plan.duration_weeks} weeks</div>
                  <div>Exercises: {plan.exercise_count}</div>
                  <div>Status: {plan.is_active ? 'Active' : 'Inactive'}</div>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {plans.length === 0 && !error && (
        <div className="text-center text-muted py-5">
          No workout plans created yet
        </div>
      )}
    </div>
  );
};

export default WorkoutPlans;
