import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../logo.svg';

const Navigation = ({ isAuthenticated, userType, onLogout }) => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
      <div className="container">
        <Link className="navbar-brand" to="/">
          <img src={logo} alt="OctoFit" height="30" className="d-inline-block align-top me-2" />
          OctoFit Tracker
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ms-auto">
            {!isAuthenticated ? (
              <>
                <li className="nav-item">
                  <Link className="nav-link" to="/">Home</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teacher-login">Teacher Login</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/student-register">Student Register</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/users">Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">Workouts</Link>
                </li>
              </>
            ) : userType === 'teacher' ? (
              <>
                <li className="nav-item">
                  <Link className="nav-link" to="/teacher-dashboard">Dashboard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/students">Students</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workout-plans">Workout Plans</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/exercises">Exercises</Link>
                </li>
                <li className="nav-item">
                  <button className="btn btn-link nav-link" onClick={onLogout}>
                    Logout
                  </button>
                </li>
              </>
            ) : (
              <>
                <li className="nav-item">
                  <Link className="nav-link" to="/dashboard">My Dashboard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">My Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/my-plans">My Plans</Link>
                </li>
                <li className="nav-item">
                  <button className="btn btn-link nav-link" onClick={onLogout}>
                    Logout
                  </button>
                </li>
              </>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;
