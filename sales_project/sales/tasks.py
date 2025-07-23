from apscheduler.schedulers.background import BackgroundScheduler
from .data_loader import load_data

def refresh_data():
    load_data()

scheduler = BackgroundScheduler()
scheduler.add_job(refresh_data, 'interval', hours=24)  # Set the interval to 24 hours
scheduler.start()
