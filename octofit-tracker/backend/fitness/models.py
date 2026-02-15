from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    """Model representing a student user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    grade = models.IntegerField(validators=[MinValueValidator(9), MaxValueValidator(12)])
    age = models.IntegerField(validators=[MinValueValidator(13), MaxValueValidator(19)])
    height_cm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fitness_level = models.CharField(
        max_length=20,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
        ],
        default='beginner'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} (Grade {self.grade})"

    class Meta:
        ordering = ['grade', 'user__last_name']


class Teacher(models.Model):
    """Model representing a teacher user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    department = models.CharField(max_length=100, default='Physical Education')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Teacher: {self.user.get_full_name()}"


class WorkoutPlan(models.Model):
    """Model representing a workout plan"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='workout_plans')
    difficulty_level = models.CharField(
        max_length=20,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
        ],
        default='beginner'
    )
    duration_weeks = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(52)])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Exercise(models.Model):
    """Model representing an individual exercise"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(
        max_length=50,
        choices=[
            ('cardio', 'Cardio'),
            ('strength', 'Strength Training'),
            ('flexibility', 'Flexibility'),
            ('sports', 'Sports Activity'),
            ('other', 'Other'),
        ]
    )
    calories_per_minute = models.DecimalField(max_digits=5, decimal_places=2, default=5.0)
    
    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        ordering = ['category', 'name']


class WorkoutPlanExercise(models.Model):
    """Model linking exercises to workout plans"""
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True)
    reps = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True)
    duration_minutes = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True)
    order = models.IntegerField(default=0)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.workout_plan.title} - {self.exercise.name}"

    class Meta:
        ordering = ['workout_plan', 'order']


class StudentWorkoutPlan(models.Model):
    """Model representing a workout plan assigned to a student"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='assigned_plans')
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('completed', 'Completed'),
            ('paused', 'Paused'),
        ],
        default='active'
    )
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.workout_plan.title}"

    class Meta:
        ordering = ['-assigned_at']


class ActivityLog(models.Model):
    """Model representing a logged activity/workout session"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='activity_logs')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    duration_minutes = models.IntegerField(validators=[MinValueValidator(1)])
    intensity = models.CharField(
        max_length=20,
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        ],
        default='medium'
    )
    calories_burned = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)
    logged_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Auto-calculate calories if not provided
        if not self.calories_burned and self.exercise:
            intensity_multiplier = {'low': 0.8, 'medium': 1.0, 'high': 1.3}.get(self.intensity, 1.0)
            self.calories_burned = float(self.exercise.calories_per_minute) * self.duration_minutes * intensity_multiplier
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.exercise.name} on {self.date}"

    class Meta:
        ordering = ['-date', '-logged_at']


class PerformanceMetric(models.Model):
    """Model for tracking student performance metrics over time"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='performance_metrics')
    date = models.DateField()
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    # Fitness test results
    pushups_count = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    situps_count = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    mile_time_seconds = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    flexibility_cm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    # Overall metrics
    fitness_score = models.IntegerField(
        null=True, 
        blank=True, 
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    notes = models.TextField(blank=True)
    recorded_by = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.date}"

    class Meta:
        ordering = ['-date']
        unique_together = ['student', 'date']
