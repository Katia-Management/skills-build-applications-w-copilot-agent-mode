import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { studentRegister } from '../api';

const StudentRegister = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    first_name: '',
    last_name: '',
    grade: '',
    age: '',
    height_cm: '',
    weight_kg: '',
    fitness_level: 'beginner'
  });
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      await studentRegister(formData);
      setSuccess(true);
      setTimeout(() => {
        navigate('/');
      }, 2000);
    } catch (err) {
      const errors = err.response?.data;
      if (errors) {
        const errorMessages = Object.entries(errors)
          .map(([key, value]) => `${key}: ${value}`)
          .join(', ');
        setError(errorMessages);
      } else {
        setError('Registration failed. Please try again.');
      }
    } finally {
      setLoading(false);
    }
  };

  if (success) {
    return (
      <div className="container mt-5">
        <div className="alert alert-success text-center" role="alert">
          <h4>Registration Successful!</h4>
          <p>Your account has been created. Redirecting...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-5 mb-5">
      <div className="row justify-content-center">
        <div className="col-md-8 col-lg-6">
          <div className="card shadow">
            <div className="card-body">
              <h2 className="card-title text-center mb-4">Student Registration</h2>
              
              {error && (
                <div className="alert alert-danger" role="alert">
                  {error}
                </div>
              )}

              <form onSubmit={handleSubmit}>
                <div className="row">
                  <div className="col-md-6 mb-3">
                    <label htmlFor="first_name" className="form-label">First Name *</label>
                    <input
                      type="text"
                      className="form-control"
                      id="first_name"
                      name="first_name"
                      value={formData.first_name}
                      onChange={handleChange}
                      required
                    />
                  </div>

                  <div className="col-md-6 mb-3">
                    <label htmlFor="last_name" className="form-label">Last Name *</label>
                    <input
                      type="text"
                      className="form-control"
                      id="last_name"
                      name="last_name"
                      value={formData.last_name}
                      onChange={handleChange}
                      required
                    />
                  </div>
                </div>

                <div className="mb-3">
                  <label htmlFor="username" className="form-label">Username *</label>
                  <input
                    type="text"
                    className="form-control"
                    id="username"
                    name="username"
                    value={formData.username}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="mb-3">
                  <label htmlFor="email" className="form-label">Email *</label>
                  <input
                    type="email"
                    className="form-control"
                    id="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="mb-3">
                  <label htmlFor="password" className="form-label">Password * (min 8 characters)</label>
                  <input
                    type="password"
                    className="form-control"
                    id="password"
                    name="password"
                    value={formData.password}
                    onChange={handleChange}
                    minLength="8"
                    required
                  />
                </div>

                <div className="row">
                  <div className="col-md-6 mb-3">
                    <label htmlFor="grade" className="form-label">Grade (9-12) *</label>
                    <input
                      type="number"
                      className="form-control"
                      id="grade"
                      name="grade"
                      value={formData.grade}
                      onChange={handleChange}
                      min="9"
                      max="12"
                      required
                    />
                  </div>

                  <div className="col-md-6 mb-3">
                    <label htmlFor="age" className="form-label">Age (13-19) *</label>
                    <input
                      type="number"
                      className="form-control"
                      id="age"
                      name="age"
                      value={formData.age}
                      onChange={handleChange}
                      min="13"
                      max="19"
                      required
                    />
                  </div>
                </div>

                <div className="row">
                  <div className="col-md-6 mb-3">
                    <label htmlFor="height_cm" className="form-label">Height (cm)</label>
                    <input
                      type="number"
                      step="0.01"
                      className="form-control"
                      id="height_cm"
                      name="height_cm"
                      value={formData.height_cm}
                      onChange={handleChange}
                    />
                  </div>

                  <div className="col-md-6 mb-3">
                    <label htmlFor="weight_kg" className="form-label">Weight (kg)</label>
                    <input
                      type="number"
                      step="0.01"
                      className="form-control"
                      id="weight_kg"
                      name="weight_kg"
                      value={formData.weight_kg}
                      onChange={handleChange}
                    />
                  </div>
                </div>

                <div className="mb-3">
                  <label htmlFor="fitness_level" className="form-label">Fitness Level *</label>
                  <select
                    className="form-select"
                    id="fitness_level"
                    name="fitness_level"
                    value={formData.fitness_level}
                    onChange={handleChange}
                    required
                  >
                    <option value="beginner">Beginner</option>
                    <option value="intermediate">Intermediate</option>
                    <option value="advanced">Advanced</option>
                  </select>
                </div>

                <button 
                  type="submit" 
                  className="btn btn-success w-100"
                  disabled={loading}
                >
                  {loading ? 'Registering...' : 'Register'}
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default StudentRegister;
