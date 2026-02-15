from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Student, Teacher, WorkoutPlan, Exercise, WorkoutPlanExercise,
    StudentWorkoutPlan, ActivityLog, PerformanceMetric
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'user', 'full_name', 'grade', 'age', 'height_cm', 
                  'weight_kg', 'fitness_level', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_full_name(self, obj):
        return obj.user.get_full_name()


class StudentRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    grade = serializers.IntegerField(min_value=9, max_value=12)
    age = serializers.IntegerField(min_value=13, max_value=19)
    height_cm = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    weight_kg = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    fitness_level = serializers.ChoiceField(
        choices=['beginner', 'intermediate', 'advanced'],
        default='beginner'
    )

    def create(self, validated_data):
        # Create user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        
        # Create student profile
        student = Student.objects.create(
            user=user,
            grade=validated_data['grade'],
            age=validated_data['age'],
            height_cm=validated_data.get('height_cm'),
            weight_kg=validated_data.get('weight_kg'),
            fitness_level=validated_data.get('fitness_level', 'beginner')
        )
        
        return student


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'full_name', 'department', 'created_at']
        read_only_fields = ['id', 'created_at']

    def get_full_name(self, obj):
        return obj.user.get_full_name()


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'category', 'calories_per_minute']
        read_only_fields = ['id']


class WorkoutPlanExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)
    exercise_id = serializers.PrimaryKeyRelatedField(
        queryset=Exercise.objects.all(),
        source='exercise',
        write_only=True
    )

    class Meta:
        model = WorkoutPlanExercise
        fields = ['id', 'exercise', 'exercise_id', 'sets', 'reps', 
                  'duration_minutes', 'order', 'notes']
        read_only_fields = ['id']


class WorkoutPlanSerializer(serializers.ModelSerializer):
    created_by = TeacherSerializer(read_only=True)
    exercises = WorkoutPlanExerciseSerializer(many=True, read_only=True)
    exercise_count = serializers.SerializerMethodField()

    class Meta:
        model = WorkoutPlan
        fields = ['id', 'title', 'description', 'created_by', 'difficulty_level',
                  'duration_weeks', 'is_active', 'exercises', 'exercise_count',
                  'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_exercise_count(self, obj):
        return obj.exercises.count()


class StudentWorkoutPlanSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    workout_plan = WorkoutPlanSerializer(read_only=True)
    assigned_by = TeacherSerializer(read_only=True)

    class Meta:
        model = StudentWorkoutPlan
        fields = ['id', 'student', 'workout_plan', 'assigned_by', 
                  'start_date', 'end_date', 'status', 'assigned_at']
        read_only_fields = ['id', 'assigned_at']


class ActivityLogSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    exercise = ExerciseSerializer(read_only=True)
    exercise_id = serializers.PrimaryKeyRelatedField(
        queryset=Exercise.objects.all(),
        source='exercise',
        write_only=True
    )
    workout_plan_id = serializers.PrimaryKeyRelatedField(
        queryset=WorkoutPlan.objects.all(),
        source='workout_plan',
        write_only=True,
        required=False
    )

    class Meta:
        model = ActivityLog
        fields = ['id', 'student', 'exercise', 'exercise_id', 'workout_plan',
                  'workout_plan_id', 'date', 'duration_minutes', 'intensity',
                  'calories_burned', 'notes', 'logged_at']
        read_only_fields = ['id', 'calories_burned', 'logged_at']


class PerformanceMetricSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    recorded_by = TeacherSerializer(read_only=True)

    class Meta:
        model = PerformanceMetric
        fields = ['id', 'student', 'date', 'weight_kg', 'pushups_count',
                  'situps_count', 'mile_time_seconds', 'flexibility_cm',
                  'fitness_score', 'notes', 'recorded_by', 'created_at']
        read_only_fields = ['id', 'created_at']


class DashboardStatsSerializer(serializers.Serializer):
    """Serializer for dashboard statistics"""
    total_activities = serializers.IntegerField()
    total_calories = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_minutes = serializers.IntegerField()
    active_plans = serializers.IntegerField()
    recent_activities = ActivityLogSerializer(many=True)
    fitness_trend = serializers.ListField()
