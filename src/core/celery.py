from celery import Celery, schedules


app = Celery("core")
app.config_from_object("core.celeryconf")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "fetch-bookings": {
        "task": "booking.service.tasks.fetch_bookings_tasks",
        "schedule": schedules.crontab(hour=23, minute=59, day_of_week="mon,tuesday,wed,thu,fri,sat,sun")
    },
    "check-flights": {
        "task": "booking.service.tasks.check_flights_task",
        "schedule": schedules.crontab(hour=0, minute=30, day_of_week="mon,tuesday,wed,thu,fri,sat,sun")
    }
}

app.conf.timezone = "Asia/Almaty"
