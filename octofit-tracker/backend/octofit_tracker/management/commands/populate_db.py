
from django.core.management.base import BaseCommand
from fitness.models import ActivityLog, Student, Exercise
from django.contrib.auth.models import User
from datetime import date

class Command(BaseCommand):
    help = 'Popula o banco octofit_db com dados de teste de atividades.'

    def handle(self, *args, **options):
        ActivityLog.objects.all().delete()
        # Cria usuários de teste se não existirem
        user1, _ = User.objects.get_or_create(username='alice', defaults={'first_name': 'Alice', 'last_name': 'Silva'})
        user2, _ = User.objects.get_or_create(username='bob', defaults={'first_name': 'Bob', 'last_name': 'Souza'})
        user3, _ = User.objects.get_or_create(username='carol', defaults={'first_name': 'Carol', 'last_name': 'Oliveira'})
        student1, _ = Student.objects.get_or_create(user=user1, defaults={'grade': 10, 'age': 15})
        student2, _ = Student.objects.get_or_create(user=user2, defaults={'grade': 11, 'age': 16})
        student3, _ = Student.objects.get_or_create(user=user3, defaults={'grade': 12, 'age': 17})
        # Cria exercícios de teste se não existirem
        ex1, _ = Exercise.objects.get_or_create(name='Corrida', defaults={'description': 'Correr ao ar livre', 'category': 'cardio', 'calories_per_minute': 10})
        ex2, _ = Exercise.objects.get_or_create(name='Ciclismo', defaults={'description': 'Andar de bicicleta', 'category': 'cardio', 'calories_per_minute': 8})
        ex3, _ = Exercise.objects.get_or_create(name='Natação', defaults={'description': 'Nadar na piscina', 'category': 'cardio', 'calories_per_minute': 12})
        # Cria logs de atividades
        ActivityLog.objects.create(student=student1, exercise=ex1, date=date.today(), duration_minutes=30, intensity='medium')
        ActivityLog.objects.create(student=student2, exercise=ex2, date=date.today(), duration_minutes=45, intensity='high')
        ActivityLog.objects.create(student=student3, exercise=ex3, date=date.today(), duration_minutes=60, intensity='low')
        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com dados de teste reais!'))
