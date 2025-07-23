from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler


class SalesConfig(AppConfig):
    name = 'sales'

    def ready(self):
        from .tasks import refresh_data

        scheduler = BackgroundScheduler()
        if not scheduler.running:
            scheduler.add_job(refresh_data, 'interval', hours=24)
            scheduler.start()
