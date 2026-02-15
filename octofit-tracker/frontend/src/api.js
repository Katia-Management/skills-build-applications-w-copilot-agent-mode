import axios from 'axios';

// Determine the API base URL
const getBaseURL = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME || window.CODESPACE_NAME;
  if (codespace) {
    return `https://${codespace}-8000.app.github.dev/api`;
  }
  return 'http://localhost:8000/api';
};

const API_BASE_URL = getBaseURL();

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Authentication API
export const teacherLogin = (credentials) => {
  return apiClient.post('/auth/teacher-login/', credentials);
};

export const studentRegister = (data) => {
  return apiClient.post('/auth/student-register/', data);
};

export const logout = () => {
  return apiClient.post('/auth/logout/');
};

// Students API
export const getStudents = () => {
  return apiClient.get('/students/');
};

export const getStudent = (id) => {
  return apiClient.get(`/students/${id}/`);
};

export const getStudentDashboard = (id) => {
  return apiClient.get(`/students/${id}/dashboard/`);
};

export const updateStudent = (id, data) => {
  return apiClient.put(`/students/${id}/`, data);
};

// Teachers API
export const getTeachers = () => {
  return apiClient.get('/teachers/');
};

// Workout Plans API
export const getWorkoutPlans = () => {
  return apiClient.get('/workout-plans/');
};

export const getWorkoutPlan = (id) => {
  return apiClient.get(`/workout-plans/${id}/`);
};

export const createWorkoutPlan = (data) => {
  return apiClient.post('/workout-plans/', data);
};

export const updateWorkoutPlan = (id, data) => {
  return apiClient.put(`/workout-plans/${id}/`, data);
};

export const deleteWorkoutPlan = (id) => {
  return apiClient.delete(`/workout-plans/${id}/`);
};

export const addExerciseToWorkoutPlan = (planId, data) => {
  return apiClient.post(`/workout-plans/${planId}/add_exercise/`, data);
};

// Exercises API
export const getExercises = () => {
  return apiClient.get('/exercises/');
};

export const getExercise = (id) => {
  return apiClient.get(`/exercises/${id}/`);
};

export const createExercise = (data) => {
  return apiClient.post('/exercises/', data);
};

// Student Workout Plans API
export const getStudentWorkoutPlans = () => {
  return apiClient.get('/student-workout-plans/');
};

export const assignWorkoutPlan = (data) => {
  return apiClient.post('/student-workout-plans/', data);
};

// Activity Logs API
export const getActivityLogs = (studentId = null) => {
  const params = studentId ? { student_id: studentId } : {};
  return apiClient.get('/activity-logs/', { params });
};

export const createActivityLog = (data) => {
  return apiClient.post('/activity-logs/', data);
};

export const getActivityLog = (id) => {
  return apiClient.get(`/activity-logs/${id}/`);
};

export const updateActivityLog = (id, data) => {
  return apiClient.put(`/activity-logs/${id}/`, data);
};

export const deleteActivityLog = (id) => {
  return apiClient.delete(`/activity-logs/${id}/`);
};

// Performance Metrics API
export const getPerformanceMetrics = () => {
  return apiClient.get('/performance-metrics/');
};

export const createPerformanceMetric = (data) => {
  return apiClient.post('/performance-metrics/', data);
};

export const getPerformanceMetric = (id) => {
  return apiClient.get(`/performance-metrics/${id}/`);
};

export default apiClient;
