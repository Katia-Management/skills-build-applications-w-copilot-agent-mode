import React, { useState, useEffect } from 'react';
import { getStudents } from '../api';

const Students = () => {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchStudents = async () => {
      try {
        const response = await getStudents();
        setStudents(response.data);
      } catch (err) {
        setError('Failed to load students');
        console.error('Error:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchStudents();
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
      <h1 className="mb-4">Students</h1>
      
      {error && (
        <div className="alert alert-danger" role="alert">
          {error}
        </div>
      )}

      <div className="card shadow-sm">
        <div className="card-body">
          <div className="table-responsive">
            <table className="table table-hover">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Email</th>
                  <th>Grade</th>
                  <th>Age</th>
                  <th>Fitness Level</th>
                </tr>
              </thead>
              <tbody>
                {students.map((student) => (
                  <tr key={student.id}>
                    <td>{student.full_name}</td>
                    <td>{student.user.email}</td>
                    <td>{student.grade}</td>
                    <td>{student.age}</td>
                    <td>
                      <span className={`badge bg-${
                        student.fitness_level === 'beginner' ? 'info' :
                        student.fitness_level === 'intermediate' ? 'warning' : 'success'
                      }`}>
                        {student.fitness_level}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          {students.length === 0 && !error && (
            <div className="text-center text-muted py-4">
              No students registered yet
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Students;
