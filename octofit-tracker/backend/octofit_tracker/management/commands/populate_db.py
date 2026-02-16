
from datetime import date

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from fitness.models import ActivityLog, Exercise, Student

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        team_marvel = 'team marvel'
        team_dc = 'team dc'

        ActivityLog.objects.all().delete()

        hero_users = [
            ('ironman', 'Tony', f'Stark ({team_marvel})', 10, 15),
            ('captain_america', 'Steve', f'Rogers ({team_marvel})', 11, 16),
            ('batman', 'Bruce', f'Wayne ({team_dc})', 12, 17),
            ('superman', 'Clark', f'Kent ({team_dc})', 10, 15),
        ]

        students = []
        for username, first_name, last_name, grade, age in hero_users:
            user, _ = User.objects.get_or_create(
                username=username,
                defaults={
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': f'{username}@octofit.local',
                },
            )
            student, _ = Student.objects.get_or_create(
                user=user,
                defaults={
                    'grade': grade,
                    'age': age,
                },
            )
            students.append(student)

        running, _ = Exercise.objects.get_or_create(
            name='Heroic Running',
            defaults={
                'description': f'Cardio training for {team_marvel} and {team_dc}',
                'category': 'cardio',
                'calories_per_minute': 10,
            },
        )
        strength, _ = Exercise.objects.get_or_create(
            name='Power Strength',
            defaults={
                'description': 'Strength routine for super heroes',
                'category': 'strength',
                'calories_per_minute': 8,
            },
        )

        for index, student in enumerate(students):
            exercise = running if index % 2 == 0 else strength
            intensity = 'high' if index % 2 == 0 else 'medium'
            team_note = team_marvel if index < 2 else team_dc
            ActivityLog.objects.create(
                student=student,
                exercise=exercise,
                date=date.today(),
                duration_minutes=30 + (index * 5),
                intensity=intensity,
                notes=f'Super heroes training session - {team_note}',
            )

        self.stdout.write(self.style.SUCCESS('Populated octofit_db with super heroes test data for team marvel and team dc.'))
