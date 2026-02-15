import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import './App.css';

// Components
import Navigation from './components/Navigation';

// Pages
import Home from './pages/Home';
import TeacherLogin from './pages/TeacherLogin';
import StudentRegister from './pages/StudentRegister';
import TeacherDashboard from './pages/TeacherDashboard';
import Students from './pages/Students';
import WorkoutPlans from './pages/WorkoutPlans';
import Exercises from './pages/Exercises';

function App() {
  const [user, setUser] = useState(null);
  const [userType, setUserType] = useState(null); // 'teacher' or 'student'

  const handleLogin = (type, userData) => {
    setUserType(type);
    setUser(userData);
  };

  const handleLogout = () => {
    setUser(null);
    setUserType(null);
  };

  return (
    <Router>
      <div className="App">
        <Navigation 
          isAuthenticated={!!user} 
          userType={userType} 
          onLogout={handleLogout}
        />
        
        <Routes>
          <Route path="/" element={<Home />} />
          <Route 
            path="/teacher-login" 
            element={<TeacherLogin onLogin={handleLogin} />} 
          />
          <Route path="/student-register" element={<StudentRegister />} />
          
          {/* Teacher Routes */}
          <Route 
            path="/teacher-dashboard" 
            element={
              userType === 'teacher' ? <TeacherDashboard /> : <Navigate to="/teacher-login" />
            } 
          />
          <Route 
            path="/students" 
            element={
              userType === 'teacher' ? <Students /> : <Navigate to="/teacher-login" />
            } 
          />
          <Route 
            path="/workout-plans" 
            element={
              userType === 'teacher' ? <WorkoutPlans /> : <Navigate to="/teacher-login" />
            } 
          />
          <Route 
            path="/exercises" 
            element={
              userType === 'teacher' ? <Exercises /> : <Navigate to="/teacher-login" />
            } 
          />
          
          {/* Catch all route */}
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
