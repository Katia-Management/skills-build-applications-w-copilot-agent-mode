# OctoFit Tracker - Technical Specification

## Technology Stack

### Frontend
| Technology | Version | Purpose |
|------------|---------|---------|
| React | 18.x | UI framework for building component-based interface |
| React Router DOM | 6.x | Client-side routing and navigation |
| Bootstrap | 5.x | Responsive CSS framework for styling |
| Axios | 1.x | HTTP client for API communication |

### Backend
| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.12 | Programming language |
| Django | 4.1.7 | Web framework for backend logic |
| Django REST Framework | 3.14.0 | RESTful API creation |
| django-cors-headers | 4.5.0 | CORS handling for cross-origin requests |
| django-allauth | 0.51.0 | Authentication system |
| dj-rest-auth | 2.2.6 | REST API authentication |

### Database
| Technology | Purpose |
|------------|---------|
| SQLite | Development database (easily upgradeable to PostgreSQL/MongoDB) |
| Django ORM | Object-relational mapping |

## Data Models

### 1. Student Model
Represents a student user in the system.

**Fields:**
- `user` (OneToOne → User): Link to Django User model
- `grade` (Integer): Student's grade (9-12)
- `age` (Integer): Student's age (13-19)
- `height_cm` (Decimal): Height in centimeters
- `weight_kg` (Decimal): Weight in kilograms
- `fitness_level` (Choice): beginner/intermediate/advanced
- `created_at` (DateTime): Registration timestamp
- `updated_at` (DateTime): Last update timestamp

**Relationships:**
- Has many: ActivityLog, PerformanceMetric, StudentWorkoutPlan

### 2. Teacher Model
Represents a teacher/instructor user.

**Fields:**
- `user` (OneToOne → User): Link to Django User model
- `department` (String): Department name (default: Physical Education)
- `created_at` (DateTime): Registration timestamp

**Relationships:**
- Has many: WorkoutPlan (created), StudentWorkoutPlan (assigned), PerformanceMetric (recorded)

### 3. Exercise Model
Represents an individual exercise.

**Fields:**
- `name` (String): Exercise name
- `description` (Text): Detailed description
- `category` (Choice): cardio/strength/flexibility/sports/other
- `calories_per_minute` (Decimal): Average calories burned per minute

**Relationships:**
- Used in: WorkoutPlanExercise, ActivityLog

### 4. WorkoutPlan Model
Represents a structured workout program.

**Fields:**
- `title` (String): Plan title
- `description` (Text): Plan description
- `created_by` (ForeignKey → Teacher): Teacher who created it
- `difficulty_level` (Choice): beginner/intermediate/advanced
- `duration_weeks` (Integer): Plan duration (1-52 weeks)
- `is_active` (Boolean): Whether plan is active
- `created_at` (DateTime): Creation timestamp
- `updated_at` (DateTime): Last update timestamp

**Relationships:**
- Has many: WorkoutPlanExercise, StudentWorkoutPlan, ActivityLog

### 5. WorkoutPlanExercise Model
Links exercises to workout plans with specific parameters.

**Fields:**
- `workout_plan` (ForeignKey → WorkoutPlan): Associated plan
- `exercise` (ForeignKey → Exercise): Associated exercise
- `sets` (Integer): Number of sets (optional)
- `reps` (Integer): Repetitions per set (optional)
- `duration_minutes` (Integer): Duration in minutes (optional)
- `order` (Integer): Order in the workout sequence
- `notes` (Text): Additional instructions

### 6. StudentWorkoutPlan Model
Tracks workout plans assigned to students.

**Fields:**
- `student` (ForeignKey → Student): Student receiving the plan
- `workout_plan` (ForeignKey → WorkoutPlan): Assigned plan
- `assigned_by` (ForeignKey → Teacher): Teacher who assigned it
- `start_date` (Date): Plan start date
- `end_date` (Date): Plan end date (optional)
- `status` (Choice): active/completed/paused
- `assigned_at` (DateTime): Assignment timestamp

### 7. ActivityLog Model
Records individual workout sessions.

**Fields:**
- `student` (ForeignKey → Student): Student who performed activity
- `exercise` (ForeignKey → Exercise): Exercise performed
- `workout_plan` (ForeignKey → WorkoutPlan): Associated plan (optional)
- `date` (Date): Activity date
- `duration_minutes` (Integer): Duration of activity
- `intensity` (Choice): low/medium/high
- `calories_burned` (Decimal): Calories burned (auto-calculated)
- `notes` (Text): Additional notes
- `logged_at` (DateTime): Log creation timestamp

**Auto-calculation:**
- `calories_burned` = exercise.calories_per_minute × duration_minutes × intensity_multiplier

### 8. PerformanceMetric Model
Tracks fitness assessments and measurements over time.

**Fields:**
- `student` (ForeignKey → Student): Student being assessed
- `date` (Date): Assessment date
- `weight_kg` (Decimal): Body weight
- `pushups_count` (Integer): Push-ups completed
- `situps_count` (Integer): Sit-ups completed
- `mile_time_seconds` (Integer): Mile run time in seconds
- `flexibility_cm` (Decimal): Flexibility measurement
- `fitness_score` (Integer): Overall fitness score (0-100)
- `notes` (Text): Assessment notes
- `recorded_by` (ForeignKey → Teacher): Teacher who recorded it
- `created_at` (DateTime): Record creation timestamp

**Constraints:**
- Unique together: student + date (one assessment per student per day)

## API Endpoints Summary

### Authentication
- POST `/api/auth/teacher-login/` - Teacher login
- POST `/api/auth/student-register/` - Student registration
- POST `/api/auth/logout/` - Logout

### Resources (CRUD)
- `/api/students/` - Student operations
- `/api/teachers/` - Teacher operations
- `/api/workout-plans/` - Workout plan operations
- `/api/exercises/` - Exercise operations
- `/api/student-workout-plans/` - Assignment operations
- `/api/activity-logs/` - Activity log operations
- `/api/performance-metrics/` - Performance metric operations

### Special Endpoints
- GET `/api/students/{id}/dashboard/` - Student dashboard statistics
- POST `/api/workout-plans/{id}/add_exercise/` - Add exercise to plan

## Database Schema Diagram

```
User (Django built-in)
├── Student (1:1)
│   ├── ActivityLog (1:N)
│   ├── PerformanceMetric (1:N)
│   └── StudentWorkoutPlan (1:N)
│
└── Teacher (1:1)
    ├── WorkoutPlan (1:N)
    │   ├── WorkoutPlanExercise (1:N)
    │   └── StudentWorkoutPlan (1:N)
    └── PerformanceMetric (1:N)

Exercise
├── WorkoutPlanExercise (1:N)
└── ActivityLog (1:N)
```

## Frontend Architecture

### Component Structure
```
App (Router)
├── Navigation
└── Routes
    ├── Home
    ├── TeacherLogin
    ├── StudentRegister
    ├── TeacherDashboard (protected)
    ├── Students (protected)
    ├── WorkoutPlans (protected)
    └── Exercises (protected)
```

### State Management
- Local component state using React hooks (useState)
- No global state management (can add Redux/Context if needed)
- Authentication state managed in App.js

### API Communication
- Centralized API client in `api.js`
- Axios instance with base URL configuration
- Automatic CORS credentials handling
- Error handling with try/catch

## Security Measures

1. **CSRF Protection**: Django CSRF middleware enabled
2. **Password Validation**: Django password validators
3. **CORS Configuration**: Whitelist specific origins
4. **Session Authentication**: Secure session-based auth
5. **SQL Injection**: Django ORM prevents SQL injection
6. **XSS Prevention**: React escapes output by default

## Performance Considerations

1. **Database Indexes**: Django automatically indexes primary and foreign keys
2. **Query Optimization**: Use select_related() and prefetch_related() where needed
3. **Pagination**: API supports pagination for large datasets
4. **Static Files**: Served efficiently in production with WhiteNoise
5. **Caching**: Can add Redis/Memcached for production

## Scalability

### Current Limitations
- SQLite: Single-file database, not suitable for high concurrency
- Session storage: In database (can move to Redis)
- Static files: Served by Django (should use CDN in production)

### Production Recommendations
1. Upgrade to PostgreSQL or MongoDB
2. Use Redis for caching and sessions
3. Add Celery for background tasks
4. Implement CDN for static/media files
5. Use Gunicorn + Nginx for serving
6. Add monitoring (Sentry, New Relic)
7. Implement CI/CD pipeline

## Testing Strategy

### Backend Testing
- Unit tests for models
- API endpoint tests
- Authentication flow tests
- Data validation tests

### Frontend Testing
- Component rendering tests
- User interaction tests
- API integration tests
- Routing tests

### Current Status
- ✅ Basic test structure in place
- ✅ App.test.js updated
- 🔄 Additional tests can be added as needed

---

**Note**: This is a development/educational version. For production use, follow the scalability recommendations and implement proper security measures, monitoring, and backup strategies.
