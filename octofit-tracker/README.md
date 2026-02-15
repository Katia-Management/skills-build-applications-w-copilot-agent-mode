# OctoFit Tracker - Multi-Tier Fitness Management Application

A comprehensive web application for high school gym teachers to manage student fitness programs, track progress, and monitor student health metrics.

## 📋 Features

### For Teachers
- **Teacher Authentication**: Secure login system for teachers
- **Student Management**: View and manage all registered students
- **Workout Plan Creation**: Create and manage customized workout plans
- **Exercise Library**: Comprehensive exercise database with categories
- **Performance Tracking**: Monitor student fitness metrics over time
- **Dashboard**: View statistics and overview of all students

### For Students
- **Student Registration**: Easy signup process with profile creation
- **Activity Logging**: Log daily workouts and exercises
- **Progress Dashboard**: View personal fitness statistics and trends
- **Workout Plans**: Access personalized workout plans assigned by teachers
- **Performance Metrics**: Track fitness improvements over time

## 🏗️ Architecture

### Multi-Tier Design

1. **Presentation Layer (Frontend)**
   - React.js single-page application
   - Bootstrap for responsive UI
   - React Router for navigation
   - Axios for API communication

2. **Logic Layer (Backend)**
   - Django REST Framework
   - RESTful API endpoints
   - Authentication and authorization
   - Business logic processing

3. **Data Layer (Database)**
   - SQLite database (development)
   - Django ORM for data modeling
   - 8 comprehensive data models

## 🛠️ Tech Stack

- **Frontend**: React 18, Bootstrap 5, React Router, Axios
- **Backend**: Python 3.12, Django 4.1.7, Django REST Framework 3.14
- **Database**: SQLite (can be upgraded to PostgreSQL/MongoDB)
- **Development Environment**: GitHub Codespaces

## 📊 Data Models

1. **Student**: Student profile and information
2. **Teacher**: Teacher profile
3. **WorkoutPlan**: Exercise programs
4. **Exercise**: Individual exercises with categories
5. **WorkoutPlanExercise**: Links exercises to plans
6. **StudentWorkoutPlan**: Assigned plans to students
7. **ActivityLog**: Daily activity tracking
8. **PerformanceMetric**: Fitness assessments and metrics

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- Node.js 18+ (LTS)
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd octofit-tracker/backend
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Populate sample data:
```bash
python manage.py populate_data
```

6. Start the development server:
```bash
python manage.py runserver 0.0.0.0:8000
```

The API will be available at `http://localhost:8000/api/`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd octofit-tracker/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The application will be available at `http://localhost:3000/`

## 👤 Demo Credentials

### Teacher Account
- Username: `teacher`
- Password: `teacher123`

### Student Accounts
- Username: `john_doe` (or any other student from sample data)
- Password: `student123`

## 📡 API Endpoints

See [API_DOCUMENTATION.md](./API_DOCUMENTATION.md) for complete API reference.

### Quick Reference
- **Authentication**: `/api/auth/teacher-login/`, `/api/auth/student-register/`
- **Students**: `/api/students/`
- **Teachers**: `/api/teachers/`
- **Workout Plans**: `/api/workout-plans/`
- **Exercises**: `/api/exercises/`
- **Activity Logs**: `/api/activity-logs/`
- **Performance Metrics**: `/api/performance-metrics/`

## 🎨 Application Screenshots

### Home Page
The landing page provides entry points for both teachers and students.

### Teacher Dashboard
Overview of students, workout plans, and activity statistics.

### Student Registration
Easy-to-use registration form for new students.

### Workout Plans
Browse and manage workout plans with different difficulty levels.

### Exercises Library
Comprehensive exercise database categorized by type.

## 🔒 Security Features

- CSRF protection enabled
- CORS properly configured
- Password validation
- User authentication required for sensitive operations
- Session-based authentication

## 📝 Project Structure

```
octofit-tracker/
├── backend/
│   ├── fitness/              # Main Django app
│   │   ├── models.py         # Data models
│   │   ├── serializers.py    # API serializers
│   │   ├── views.py          # API views
│   │   ├── admin.py          # Admin interface
│   │   └── management/       # Management commands
│   ├── octofit_tracker/      # Django project settings
│   ├── requirements.txt      # Python dependencies
│   └── manage.py             # Django management script
└── frontend/
    ├── public/               # Static assets
    ├── src/
    │   ├── components/       # React components
    │   ├── pages/            # Page components
    │   ├── api.js            # API client
    │   └── App.js            # Main app component
    ├── package.json          # Node dependencies
    └── README.md             # Frontend documentation
```

## 🧪 Testing

### Backend Tests
```bash
cd octofit-tracker/backend
python manage.py test
```

### Frontend Tests
```bash
cd octofit-tracker/frontend
npm test
```

## 🌐 Deployment

### Backend Deployment
- Configure production database (PostgreSQL recommended)
- Set `DEBUG = False` in settings
- Configure static file serving
- Set up proper ALLOWED_HOSTS
- Use environment variables for secrets

### Frontend Deployment
```bash
cd octofit-tracker/frontend
npm run build
```

Deploy the `build/` directory to your static hosting service.

## 🤝 Contributing

This is an educational project created with GitHub Copilot. Contributions are welcome!

## 📄 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- Created as part of the GitHub Copilot Skills workshop
- Built for Mergington High School's PE program
- Inspired by the need for modern fitness tracking tools

## 📞 Support

For issues or questions, please open an issue in the GitHub repository.

---

**Built with ❤️ using GitHub Copilot Agent Mode**
