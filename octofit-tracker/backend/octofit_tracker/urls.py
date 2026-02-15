"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fitness import views
import os

# Create router for ViewSets
router = DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'teachers', views.TeacherViewSet)
router.register(r'workout-plans', views.WorkoutPlanViewSet)
router.register(r'exercises', views.ExerciseViewSet)
router.register(r'student-workout-plans', views.StudentWorkoutPlanViewSet)
router.register(r'activity-logs', views.ActivityLogViewSet)
router.register(r'performance-metrics', views.PerformanceMetricViewSet)


@api_view(['GET'])
def api_root(request):
    """API root endpoint with links to all endpoints"""
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev"
    else:
        base_url = "http://localhost:8000"
    
    return Response({
        'message': 'Welcome to OctoFit Tracker API',
        'endpoints': {
            'auth': {
                'teacher_login': f'{base_url}/api/auth/teacher-login/',
                'student_register': f'{base_url}/api/auth/student-register/',
                'logout': f'{base_url}/api/auth/logout/',
            },
            'students': f'{base_url}/api/students/',
            'teachers': f'{base_url}/api/teachers/',
            'workout_plans': f'{base_url}/api/workout-plans/',
            'exercises': f'{base_url}/api/exercises/',
            'student_workout_plans': f'{base_url}/api/student-workout-plans/',
            'activity_logs': f'{base_url}/api/activity-logs/',
            'performance_metrics': f'{base_url}/api/performance-metrics/',
        }
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
    path('api/auth/teacher-login/', views.teacher_login, name='teacher-login'),
    path('api/auth/student-register/', views.student_register, name='student-register'),
    path('api/auth/logout/', views.logout_view, name='logout'),
]
