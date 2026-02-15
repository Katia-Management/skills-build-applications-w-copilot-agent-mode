from django.contrib import admin
from .models import (
    Student, Teacher, WorkoutPlan, Exercise, WorkoutPlanExercise,
    StudentWorkoutPlan, ActivityLog, PerformanceMetric
)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'grade', 'age', 'fitness_level', 'created_at']
    list_filter = ['grade', 'fitness_level']
    search_fields = ['user__first_name', 'user__last_name', 'user__email']
    
    def get_full_name(self, obj):
        return obj.user.get_full_name()
    get_full_name.short_description = 'Name'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'department', 'created_at']
    search_fields = ['user__first_name', 'user__last_name', 'user__email']
    
    def get_full_name(self, obj):
        return obj.user.get_full_name()
    get_full_name.short_description = 'Name'


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'calories_per_minute']
    list_filter = ['category']
    search_fields = ['name', 'description']


@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ['title', 'difficulty_level', 'duration_weeks', 'is_active', 'created_at']
    list_filter = ['difficulty_level', 'is_active']
    search_fields = ['title', 'description']


@admin.register(WorkoutPlanExercise)
class WorkoutPlanExerciseAdmin(admin.ModelAdmin):
    list_display = ['workout_plan', 'exercise', 'sets', 'reps', 'duration_minutes', 'order']
    list_filter = ['workout_plan']


@admin.register(StudentWorkoutPlan)
class StudentWorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ['student', 'workout_plan', 'status', 'start_date', 'end_date']
    list_filter = ['status']


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ['student', 'exercise', 'date', 'duration_minutes', 'intensity', 'calories_burned']
    list_filter = ['date', 'intensity']
    search_fields = ['student__user__first_name', 'student__user__last_name']


@admin.register(PerformanceMetric)
class PerformanceMetricAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'fitness_score', 'weight_kg']
    list_filter = ['date']
    search_fields = ['student__user__first_name', 'student__user__last_name']
