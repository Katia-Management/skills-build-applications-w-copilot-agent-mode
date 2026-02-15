# OctoFit Tracker - Setup Guide

## Quick Start

### Using GitHub Codespaces (Recommended)

1. **Open in Codespaces**
   - Click "Code" → "Codespaces" → "Create codespace on main"
   - Wait for the environment to set up (MongoDB, Python, Node.js will be pre-installed)

2. **Set Up Backend**
   ```bash
   cd octofit-tracker/backend
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py populate_data
   python manage.py runserver 0.0.0.0:8000
   ```

3. **Set Up Frontend** (in a new terminal)
   ```bash
   cd octofit-tracker/frontend
   npm install
   npm start
   ```

4. **Access the Application**
   - Frontend: Port 3000 (public)
   - Backend API: Port 8000 (public)
   - Codespaces will provide public URLs automatically

### Local Development

#### Prerequisites
- Python 3.12+
- Node.js 18+ (LTS)
- Git

#### Backend Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd octofit-tracker/backend
   ```

2. Create virtual environment:
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

5. Create sample data:
   ```bash
   python manage.py populate_data
   ```

6. (Optional) Create superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

7. Start the server:
   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://localhost:8000/api/`
   The admin interface will be at `http://localhost:8000/admin/`

#### Frontend Setup

1. Navigate to frontend directory:
   ```bash
   cd octofit-tracker/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start development server:
   ```bash
   npm start
   ```

   The app will open at `http://localhost:3000/`

## Demo Accounts

After running `python manage.py populate_data`, the following accounts are available:

### Teacher Account
- **Username**: teacher
- **Password**: teacher123
- **Features**: Full access to student management, workout plans, and analytics

### Student Accounts
- **Username**: john_doe
- **Password**: student123

Other students: jane_smith, mike_johnson, emma_wilson, alex_brown (all use password: student123)

## API Testing

### Using curl

Test the API root:
```bash
curl http://localhost:8000/api/
```

Teacher login:
```bash
curl -X POST http://localhost:8000/api/auth/teacher-login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"teacher","password":"teacher123"}'
```

List students:
```bash
curl http://localhost:8000/api/students/
```

List exercises:
```bash
curl http://localhost:8000/api/exercises/
```

### Using the Django Admin Interface

1. Access `http://localhost:8000/admin/`
2. Login with the teacher account or a superuser account
3. Explore and manage all data models

## Features Overview

### Teacher Features
- 📊 **Dashboard**: View statistics on students, workout plans, and activities
- 👥 **Student Management**: Browse all registered students
- 🏋️ **Workout Plans**: Create and manage workout programs
- 💪 **Exercise Library**: Access comprehensive exercise database
- 📈 **Performance Tracking**: Monitor student fitness metrics

### Student Features
- ✍️ **Registration**: Easy signup process
- 📝 **Activity Logging**: Record daily workouts
- 📊 **Dashboard**: View personal statistics and progress
- 📋 **Workout Plans**: Access assigned programs
- 📈 **Progress Tracking**: Monitor fitness improvements

## Project Structure

```
octofit-tracker/
├── backend/               # Django backend
│   ├── fitness/          # Main Django app
│   │   ├── models.py     # 8 data models
│   │   ├── serializers.py # API serializers
│   │   ├── views.py      # API views
│   │   ├── admin.py      # Admin configuration
│   │   └── management/   # Custom commands
│   ├── octofit_tracker/  # Project settings
│   ├── db.sqlite3        # SQLite database
│   └── requirements.txt  # Python dependencies
│
├── frontend/              # React frontend
│   ├── public/           # Static assets
│   ├── src/
│   │   ├── components/   # Reusable components
│   │   ├── pages/        # Page components
│   │   ├── api.js        # API client
│   │   └── App.js        # Main component
│   └── package.json      # Node dependencies
│
├── API_DOCUMENTATION.md   # Complete API reference
├── README.md             # Project overview
└── SETUP_GUIDE.md        # This file
```

## Troubleshooting

### Backend Issues

**Issue**: `ModuleNotFoundError: No module named 'django'`
- **Solution**: Activate virtual environment and install dependencies
  ```bash
  source venv/bin/activate
  pip install -r requirements.txt
  ```

**Issue**: `django.db.utils.OperationalError: no such table`
- **Solution**: Run migrations
  ```bash
  python manage.py migrate
  ```

**Issue**: CORS errors when accessing from React
- **Solution**: Ensure Django server is running and CORS is configured in settings.py

### Frontend Issues

**Issue**: `npm: command not found`
- **Solution**: Install Node.js from nodejs.org

**Issue**: Port 3000 already in use
- **Solution**: Kill the process or use a different port
  ```bash
  PORT=3001 npm start
  ```

**Issue**: API calls fail with 404
- **Solution**: Ensure Django backend is running on port 8000

## Next Steps

### For Development
1. Customize the models for your specific needs
2. Add more exercises to the database
3. Create additional workout plans
4. Implement student dashboard views
5. Add charts and graphs for progress visualization
6. Implement team challenges and leaderboards

### For Production
1. Switch to PostgreSQL or MongoDB
2. Set up proper environment variables
3. Configure static file serving (WhiteNoise or S3)
4. Set `DEBUG = False` in Django settings
5. Use production-grade web server (Gunicorn + Nginx)
6. Set up SSL/TLS certificates
7. Configure logging and monitoring
8. Implement backup strategies

## Support

For issues or questions:
1. Check the [README.md](./README.md)
2. Review [API_DOCUMENTATION.md](./API_DOCUMENTATION.md)
3. Open an issue on GitHub

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [React Documentation](https://react.dev/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)

---

**Built with GitHub Copilot Agent Mode** 🚀
