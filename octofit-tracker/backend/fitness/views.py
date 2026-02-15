from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum, Count, Q
from datetime import datetime, timedelta
from .models import (
    Student, Teacher, WorkoutPlan, Exercise, WorkoutPlanExercise,
    StudentWorkoutPlan, ActivityLog, PerformanceMetric
)
from .serializers import (
    StudentSerializer, StudentRegistrationSerializer, TeacherSerializer,
    WorkoutPlanSerializer, ExerciseSerializer, WorkoutPlanExerciseSerializer,
    StudentWorkoutPlanSerializer, ActivityLogSerializer, PerformanceMetricSerializer,
    DashboardStatsSerializer
)


@api_view(['POST'])
@permission_classes([AllowAny])
def teacher_login(request):
    """Teacher login endpoint"""
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response(
            {'error': 'Please provide both username and password'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        # Check if user is a teacher
        try:
            teacher = user.teacher_profile
            login(request, user)
            serializer = TeacherSerializer(teacher)
            return Response({
                'success': True,
                'teacher': serializer.data,
                'message': 'Login successful'
            })
        except Teacher.DoesNotExist:
            return Response(
                {'error': 'User is not registered as a teacher'},
                status=status.HTTP_403_FORBIDDEN
            )
    else:
        return Response(
            {'error': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )


@api_view(['POST'])
@permission_classes([AllowAny])
def student_register(request):
    """Student registration endpoint"""
    serializer = StudentRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        student = serializer.save()
        return Response(
            StudentSerializer(student).data,
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_view(request):
    """Logout endpoint"""
    logout(request)
    return Response({'message': 'Logged out successfully'})


class StudentViewSet(viewsets.ModelViewSet):
    """ViewSet for Student model"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    @action(detail=True, methods=['get'])
    def dashboard(self, request, pk=None):
        """Get dashboard statistics for a student"""
        student = self.get_object()
        
        # Calculate statistics
        activities = ActivityLog.objects.filter(student=student)
        total_activities = activities.count()
        total_calories = activities.aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0
        total_minutes = activities.aggregate(Sum('duration_minutes'))['duration_minutes__sum'] or 0
        active_plans = StudentWorkoutPlan.objects.filter(
            student=student, 
            status='active'
        ).count()
        
        # Recent activities (last 10)
        recent_activities = activities[:10]
        
        # Fitness trend (last 30 days)
        thirty_days_ago = datetime.now().date() - timedelta(days=30)
        fitness_trend = PerformanceMetric.objects.filter(
            student=student,
            date__gte=thirty_days_ago
        ).values('date', 'fitness_score').order_by('date')
        
        stats_data = {
            'total_activities': total_activities,
            'total_calories': total_calories,
            'total_minutes': total_minutes,
            'active_plans': active_plans,
            'recent_activities': recent_activities,
            'fitness_trend': list(fitness_trend)
        }
        
        serializer = DashboardStatsSerializer(stats_data)
        return Response(serializer.data)


class TeacherViewSet(viewsets.ModelViewSet):
    """ViewSet for Teacher model"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class WorkoutPlanViewSet(viewsets.ModelViewSet):
    """ViewSet for WorkoutPlan model"""
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    
    def perform_create(self, serializer):
        # Assign the teacher creating the plan
        try:
            teacher = self.request.user.teacher_profile
            serializer.save(created_by=teacher)
        except Teacher.DoesNotExist:
            raise ValueError("Only teachers can create workout plans")
    
    @action(detail=True, methods=['post'])
    def add_exercise(self, request, pk=None):
        """Add an exercise to a workout plan"""
        workout_plan = self.get_object()
        serializer = WorkoutPlanExerciseSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(workout_plan=workout_plan)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExerciseViewSet(viewsets.ModelViewSet):
    """ViewSet for Exercise model"""
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class StudentWorkoutPlanViewSet(viewsets.ModelViewSet):
    """ViewSet for StudentWorkoutPlan model"""
    queryset = StudentWorkoutPlan.objects.all()
    serializer_class = StudentWorkoutPlanSerializer
    
    def perform_create(self, serializer):
        # Assign the teacher assigning the plan
        try:
            teacher = self.request.user.teacher_profile
            serializer.save(assigned_by=teacher)
        except Teacher.DoesNotExist:
            raise ValueError("Only teachers can assign workout plans")


class ActivityLogViewSet(viewsets.ModelViewSet):
    """ViewSet for ActivityLog model"""
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer
    
    def get_queryset(self):
        """Filter activities by student if student_id is provided"""
        queryset = ActivityLog.objects.all()
        student_id = self.request.query_params.get('student_id', None)
        if student_id:
            queryset = queryset.filter(student_id=student_id)
        return queryset


class PerformanceMetricViewSet(viewsets.ModelViewSet):
    """ViewSet for PerformanceMetric model"""
    queryset = PerformanceMetric.objects.all()
    serializer_class = PerformanceMetricSerializer
    
    def perform_create(self, serializer):
        # Assign the teacher recording the metric
        try:
            teacher = self.request.user.teacher_profile
            serializer.save(recorded_by=teacher)
        except Teacher.DoesNotExist:
            serializer.save()  # Allow saving without teacher for now
