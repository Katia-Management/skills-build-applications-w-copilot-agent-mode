from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from fitness.models import (
    Student, Teacher, Exercise, WorkoutPlan, WorkoutPlanExercise,
    StudentWorkoutPlan, ActivityLog, PerformanceMetric
)
from datetime import date, timedelta
from decimal import Decimal


class Command(BaseCommand):
    help = 'Populates the database with sample data for OctoFit Tracker'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting data population...')
        
        # Create teacher user and profile
        teacher_user, created = User.objects.get_or_create(
            username='teacher',
            defaults={
                'email': 'teacher@school.edu',
                'first_name': 'Paul',
                'last_name': 'Octo',
                'is_staff': True,
            }
        )
        if created:
            teacher_user.set_password('teacher123')
            teacher_user.save()
            self.stdout.write(self.style.SUCCESS('Created teacher user'))
        
        teacher, created = Teacher.objects.get_or_create(
            user=teacher_user,
            defaults={'department': 'Physical Education'}
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created teacher profile'))
        
        # Create sample students
        students_data = [
            {'username': 'john_doe', 'first_name': 'John', 'last_name': 'Doe', 'grade': 10, 'age': 15, 'fitness_level': 'beginner'},
            {'username': 'jane_smith', 'first_name': 'Jane', 'last_name': 'Smith', 'grade': 11, 'age': 16, 'fitness_level': 'intermediate'},
            {'username': 'mike_johnson', 'first_name': 'Mike', 'last_name': 'Johnson', 'grade': 12, 'age': 17, 'fitness_level': 'advanced'},
            {'username': 'emma_wilson', 'first_name': 'Emma', 'last_name': 'Wilson', 'grade': 9, 'age': 14, 'fitness_level': 'beginner'},
            {'username': 'alex_brown', 'first_name': 'Alex', 'last_name': 'Brown', 'grade': 10, 'age': 15, 'fitness_level': 'intermediate'},
        ]
        
        students = []
        for student_data in students_data:
            user, created = User.objects.get_or_create(
                username=student_data['username'],
                defaults={
                    'email': f"{student_data['username']}@school.edu",
                    'first_name': student_data['first_name'],
                    'last_name': student_data['last_name'],
                }
            )
            if created:
                user.set_password('student123')
                user.save()
            
            student, created = Student.objects.get_or_create(
                user=user,
                defaults={
                    'grade': student_data['grade'],
                    'age': student_data['age'],
                    'height_cm': Decimal('165.5'),
                    'weight_kg': Decimal('60.0'),
                    'fitness_level': student_data['fitness_level']
                }
            )
            students.append(student)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(students)} students'))
        
        # Create sample exercises
        exercises_data = [
            {'name': 'Running', 'description': 'Outdoor or treadmill running', 'category': 'cardio', 'calories_per_minute': 10.0},
            {'name': 'Push-ups', 'description': 'Standard push-up exercise', 'category': 'strength', 'calories_per_minute': 7.0},
            {'name': 'Sit-ups', 'description': 'Abdominal crunches', 'category': 'strength', 'calories_per_minute': 6.0},
            {'name': 'Jumping Jacks', 'description': 'Cardio warm-up exercise', 'category': 'cardio', 'calories_per_minute': 8.0},
            {'name': 'Squats', 'description': 'Bodyweight squats', 'category': 'strength', 'calories_per_minute': 7.5},
            {'name': 'Yoga', 'description': 'Flexibility and balance', 'category': 'flexibility', 'calories_per_minute': 4.0},
            {'name': 'Basketball', 'description': 'Team sport activity', 'category': 'sports', 'calories_per_minute': 9.0},
            {'name': 'Swimming', 'description': 'Pool swimming laps', 'category': 'cardio', 'calories_per_minute': 11.0},
            {'name': 'Cycling', 'description': 'Bicycle riding', 'category': 'cardio', 'calories_per_minute': 9.5},
            {'name': 'Stretching', 'description': 'Basic stretching exercises', 'category': 'flexibility', 'calories_per_minute': 3.0},
        ]
        
        exercises = []
        for exercise_data in exercises_data:
            exercise, created = Exercise.objects.get_or_create(
                name=exercise_data['name'],
                defaults={
                    'description': exercise_data['description'],
                    'category': exercise_data['category'],
                    'calories_per_minute': Decimal(str(exercise_data['calories_per_minute']))
                }
            )
            exercises.append(exercise)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(exercises)} exercises'))
        
        # Create sample workout plans
        workout_plans_data = [
            {
                'title': 'Beginner Fitness Program',
                'description': 'A gentle introduction to regular exercise for beginners',
                'difficulty_level': 'beginner',
                'duration_weeks': 4
            },
            {
                'title': 'Cardio Blast',
                'description': 'High-intensity cardio workout for improving endurance',
                'difficulty_level': 'intermediate',
                'duration_weeks': 6
            },
            {
                'title': 'Strength Builder',
                'description': 'Build muscle and strength with this comprehensive program',
                'difficulty_level': 'advanced',
                'duration_weeks': 8
            },
        ]
        
        workout_plans = []
        for plan_data in workout_plans_data:
            plan, created = WorkoutPlan.objects.get_or_create(
                title=plan_data['title'],
                defaults={
                    'description': plan_data['description'],
                    'created_by': teacher,
                    'difficulty_level': plan_data['difficulty_level'],
                    'duration_weeks': plan_data['duration_weeks'],
                    'is_active': True
                }
            )
            workout_plans.append(plan)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(workout_plans)} workout plans'))
        
        # Add exercises to workout plans
        # Beginner plan
        if workout_plans[0].exercises.count() == 0:
            WorkoutPlanExercise.objects.create(
                workout_plan=workout_plans[0],
                exercise=exercises[9],  # Stretching
                duration_minutes=10,
                order=1
            )
            WorkoutPlanExercise.objects.create(
                workout_plan=workout_plans[0],
                exercise=exercises[3],  # Jumping Jacks
                duration_minutes=5,
                order=2
            )
            WorkoutPlanExercise.objects.create(
                workout_plan=workout_plans[0],
                exercise=exercises[1],  # Push-ups
                sets=3,
                reps=10,
                order=3
            )
        
        # Cardio plan
        if workout_plans[1].exercises.count() == 0:
            WorkoutPlanExercise.objects.create(
                workout_plan=workout_plans[1],
                exercise=exercises[0],  # Running
                duration_minutes=30,
                order=1
            )
            WorkoutPlanExercise.objects.create(
                workout_plan=workout_plans[1],
                exercise=exercises[8],  # Cycling
                duration_minutes=20,
                order=2
            )
        
        self.stdout.write(self.style.SUCCESS('Added exercises to workout plans'))
        
        # Assign workout plans to students
        today = date.today()
        for i, student in enumerate(students[:3]):
            StudentWorkoutPlan.objects.get_or_create(
                student=student,
                workout_plan=workout_plans[i % len(workout_plans)],
                defaults={
                    'assigned_by': teacher,
                    'start_date': today - timedelta(days=7),
                    'status': 'active'
                }
            )
        
        self.stdout.write(self.style.SUCCESS('Assigned workout plans to students'))
        
        # Create sample activity logs
        for student in students:
            for i in range(5):
                ActivityLog.objects.get_or_create(
                    student=student,
                    exercise=exercises[i % len(exercises)],
                    date=today - timedelta(days=i),
                    defaults={
                        'duration_minutes': 20 + (i * 5),
                        'intensity': ['low', 'medium', 'high'][i % 3],
                        'notes': f'Great workout session #{i+1}'
                    }
                )
        
        self.stdout.write(self.style.SUCCESS('Created activity logs'))
        
        # Create sample performance metrics
        for student in students:
            PerformanceMetric.objects.get_or_create(
                student=student,
                date=today - timedelta(days=7),
                defaults={
                    'weight_kg': Decimal('60.0'),
                    'pushups_count': 15,
                    'situps_count': 20,
                    'mile_time_seconds': 480,
                    'fitness_score': 65,
                    'recorded_by': teacher
                }
            )
        
        self.stdout.write(self.style.SUCCESS('Created performance metrics'))
        
        self.stdout.write(self.style.SUCCESS('\nDatabase populated successfully!'))
        self.stdout.write(f'Teacher login: username=teacher, password=teacher123')
        self.stdout.write(f'Student login: username=john_doe, password=student123 (or any other student)')
