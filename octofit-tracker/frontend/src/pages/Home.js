import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="container mt-5">
      <div className="row">
        <div className="col-lg-8 mx-auto text-center">
          <h1 className="display-4 mb-4">Welcome to OctoFit Tracker</h1>
          <p className="lead mb-5">
            A comprehensive fitness tracking application for high school students and teachers.
            Track your workouts, monitor progress, and achieve your fitness goals!
          </p>
          
          <div className="row mb-5">
            <div className="col-md-6 mb-4">
              <div className="card shadow">
                <div className="card-body">
                  <h3 className="card-title">For Teachers</h3>
                  <p className="card-text">
                    Manage student fitness programs, create workout plans, and track student progress.
                  </p>
                  <Link to="/teacher-login" className="btn btn-primary">
                    Teacher Login
                  </Link>
                </div>
              </div>
            </div>
            <div className="col-md-6 mb-4">
              <div className="card shadow">
                <div className="card-body">
                  <h3 className="card-title">For Students</h3>
                  <p className="card-text">
                    Log your activities, follow personalized workout plans, and see your fitness improve!
                  </p>
                  <Link to="/student-register" className="btn btn-success">
                    Get Started
                  </Link>
                </div>
              </div>
            </div>
          </div>

          <div className="row mb-4">
            <div className="col-md-4">
              <div className="card border-0">
                <div className="card-body">
                  <div className="mb-3">
                    <svg className="bi text-primary" width="48" height="48" fill="currentColor">
                      <use xlinkHref="#activity"/>
                    </svg>
                  </div>
                  <h5>Activity Tracking</h5>
                  <p>Log your workouts and exercises with ease</p>
                </div>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card border-0">
                <div className="card-body">
                  <div className="mb-3">
                    <svg className="bi text-success" width="48" height="48" fill="currentColor">
                      <use xlinkHref="#chart"/>
                    </svg>
                  </div>
                  <h5>Progress Monitoring</h5>
                  <p>Track your improvement over time with detailed metrics</p>
                </div>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card border-0">
                <div className="card-body">
                  <div className="mb-3">
                    <svg className="bi text-warning" width="48" height="48" fill="currentColor">
                      <use xlinkHref="#plan"/>
                    </svg>
                  </div>
                  <h5>Personalized Plans</h5>
                  <p>Get workout plans tailored to your fitness level</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <svg xmlns="http://www.w3.org/2000/svg" style={{display: 'none'}}>
        <symbol id="activity" viewBox="0 0 16 16">
          <path d="M11 6.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm-3 0a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm-5 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm3 0a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1z"/>
        </symbol>
        <symbol id="chart" viewBox="0 0 16 16">
          <path d="M0 0h1v15h15v1H0V0Zm14.817 3.113a.5.5 0 0 1 .07.704l-4.5 5.5a.5.5 0 0 1-.74.037L7.06 6.767l-3.656 5.027a.5.5 0 0 1-.808-.588l4-5.5a.5.5 0 0 1 .758-.06l2.609 2.61 4.15-5.073a.5.5 0 0 1 .704-.07Z"/>
        </symbol>
        <symbol id="plan" viewBox="0 0 16 16">
          <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
          <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
        </symbol>
      </svg>
    </div>
  );
};

export default Home;
