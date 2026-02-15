import React, { useState, useEffect } from 'react';
import { getStudents, getWorkoutPlans, getActivityLogs } from '../api';

const TeacherDashboard = () => {
  const [stats, setStats] = useState({
    totalStudents: 0,
    totalWorkoutPlans: 0,
    totalActivities: 0
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [studentsRes, plansRes, activitiesRes] = await Promise.all([
          getStudents(),
          getWorkoutPlans(),
          getActivityLogs()
        ]);

        setStats({
          totalStudents: studentsRes.data.length,
          totalWorkoutPlans: plansRes.data.length,
          totalActivities: activitiesRes.data.length
        });
      } catch (error) {
        console.error('Error fetching dashboard data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
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
      <h1 className="mb-4">Teacher Dashboard</h1>
      
      <div className="row">
        <div className="col-md-4 mb-4">
          <div className="card shadow-sm">
            <div className="card-body text-center">
              <h5 className="card-title text-muted">Total Students</h5>
              <p className="display-4 text-primary">{stats.totalStudents}</p>
            </div>
          </div>
        </div>

        <div className="col-md-4 mb-4">
          <div className="card shadow-sm">
            <div className="card-body text-center">
              <h5 className="card-title text-muted">Workout Plans</h5>
              <p className="display-4 text-success">{stats.totalWorkoutPlans}</p>
            </div>
          </div>
        </div>

        <div className="col-md-4 mb-4">
          <div className="card shadow-sm">
            <div className="card-body text-center">
              <h5 className="card-title text-muted">Total Activities</h5>
              <p className="display-4 text-warning">{stats.totalActivities}</p>
            </div>
          </div>
        </div>
      </div>

      <div className="row mt-4">
        <div className="col-12">
          <div className="card shadow-sm">
            <div className="card-body">
              <h5 className="card-title">Quick Actions</h5>
              <div className="d-grid gap-2 d-md-flex">
                <a href="/students" className="btn btn-primary">
                  View Students
                </a>
                <a href="/workout-plans" className="btn btn-success">
                  Manage Workout Plans
                </a>
                <a href="/exercises" className="btn btn-info text-white">
                  View Exercises
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TeacherDashboard;
