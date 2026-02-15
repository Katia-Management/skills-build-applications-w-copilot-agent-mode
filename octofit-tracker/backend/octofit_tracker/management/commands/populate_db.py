from django.core.management.base import BaseCommand
from octofit_api.models import Activity

class Command(BaseCommand):
    help = 'Popula o banco octofit_db com dados de teste de atividades.'

    def handle(self, *args, **options):
        Activity.objects.all().delete()
        Activity.objects.create(user_name='Alice', activity_type='Corrida', duration_minutes=30)
        Activity.objects.create(user_name='Bob', activity_type='Ciclismo', duration_minutes=45)
        Activity.objects.create(user_name='Carol', activity_type='Natação', duration_minutes=60)
        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com dados de teste!'))
