# OctoFit Tracker API Documentation

## Base URL
- Development: `http://localhost:8000/api`
- Codespaces: `https://{CODESPACE_NAME}-8000.app.github.dev/api`

## Authentication Endpoints

### Teacher Login
**POST** `/api/auth/teacher-login/`

Request body:
```json
{
  "username": "teacher",
  "password": "teacher123"
}
```

Response:
```json
{
  "success": true,
  "teacher": {
    "id": 1,
    "user": {
      "id": 1,
      "username": "teacher",
      "email": "teacher@school.edu",
      "first_name": "Paul",
      "last_name": "Octo"
    },
    "full_name": "Paul Octo",
    "department": "Physical Education",
    "created_at": "2024-02-15T22:00:00Z"
  },
  "message": "Login successful"
}
```

### Student Registration
**POST** `/api/auth/student-register/`

Request body:
```json
{
  "username": "new_student",
  "email": "student@school.edu",
  "password": "password123",
  "first_name": "John",
  "last_name": "Doe",
  "grade": 10,
  "age": 15,
  "height_cm": 170.5,
  "weight_kg": 65.0,
  "fitness_level": "beginner"
}
```

### Logout
**POST** `/api/auth/logout/`

## Student Endpoints

### List Students
**GET** `/api/students/`

### Get Student Details
**GET** `/api/students/{id}/`

### Get Student Dashboard
**GET** `/api/students/{id}/dashboard/`

Returns statistics including:
- Total activities
- Total calories burned
- Total exercise minutes
- Active workout plans
- Recent activities
- Fitness trend (last 30 days)

## Teacher Endpoints

### List Teachers
**GET** `/api/teachers/`

## Workout Plan Endpoints

### List Workout Plans
**GET** `/api/workout-plans/`

### Get Workout Plan
**GET** `/api/workout-plans/{id}/`

### Create Workout Plan
**POST** `/api/workout-plans/`

Request body:
```json
{
  "title": "Beginner Fitness Program",
  "description": "A gentle introduction to regular exercise",
  "difficulty_level": "beginner",
  "duration_weeks": 4,
  "is_active": true
}
```

### Update Workout Plan
**PUT** `/api/workout-plans/{id}/`

### Delete Workout Plan
**DELETE** `/api/workout-plans/{id}/`

### Add Exercise to Workout Plan
**POST** `/api/workout-plans/{id}/add_exercise/`

Request body:
```json
{
  "exercise_id": 1,
  "sets": 3,
  "reps": 10,
  "duration_minutes": 15,
  "order": 1,
  "notes": "Focus on form"
}
```

## Exercise Endpoints

### List Exercises
**GET** `/api/exercises/`

### Get Exercise
**GET** `/api/exercises/{id}/`

### Create Exercise
**POST** `/api/exercises/`

Request body:
```json
{
  "name": "Running",
  "description": "Outdoor or treadmill running",
  "category": "cardio",
  "calories_per_minute": 10.0
}
```

## Student Workout Plan Endpoints

### List Student Workout Plans
**GET** `/api/student-workout-plans/`

### Assign Workout Plan to Student
**POST** `/api/student-workout-plans/`

Request body:
```json
{
  "student": 1,
  "workout_plan": 1,
  "start_date": "2024-02-15",
  "end_date": "2024-03-15",
  "status": "active"
}
```

## Activity Log Endpoints

### List Activity Logs
**GET** `/api/activity-logs/`

Query parameters:
- `student_id` (optional): Filter by student ID

### Create Activity Log
**POST** `/api/activity-logs/`

Request body:
```json
{
  "student": 1,
  "exercise_id": 1,
  "workout_plan_id": 1,
  "date": "2024-02-15",
  "duration_minutes": 30,
  "intensity": "medium",
  "notes": "Great workout!"
}
```

Note: `calories_burned` is auto-calculated based on exercise and intensity.

### Get Activity Log
**GET** `/api/activity-logs/{id}/`

### Update Activity Log
**PUT** `/api/activity-logs/{id}/`

### Delete Activity Log
**DELETE** `/api/activity-logs/{id}/`

## Performance Metrics Endpoints

### List Performance Metrics
**GET** `/api/performance-metrics/`

### Create Performance Metric
**POST** `/api/performance-metrics/`

Request body:
```json
{
  "student": 1,
  "date": "2024-02-15",
  "weight_kg": 65.0,
  "pushups_count": 25,
  "situps_count": 30,
  "mile_time_seconds": 480,
  "flexibility_cm": 15.5,
  "fitness_score": 75,
  "notes": "Good improvement"
}
```

### Get Performance Metric
**GET** `/api/performance-metrics/{id}/`

## Response Formats

### Success Response
```json
{
  "data": { ... },
  "message": "Success message"
}
```

### Error Response
```json
{
  "error": "Error message",
  "details": { ... }
}
```

## Status Codes
- `200 OK`: Request succeeded
- `201 Created`: Resource created successfully
- `400 Bad Request`: Invalid request data
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Access denied
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error
