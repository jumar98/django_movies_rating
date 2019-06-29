from celery import chord, group
from django.core.management import call_command
from movies_rating.celery import app
from django.core.mail import EmailMessage
from .models import Suggest


@app.task()
def send_email(message):
    email = EmailMessage("Test", str(message), 'jumartinez@lsv-tech.com', to=['jumartinez@lsv-tech.com'])
    email.send()


@app.task()
def download_movie(search_type, search_by):
    print("We sent a message after finish that task")
    if int(search_type) == 0:
        movies = call_command("download", '-s', search_by)
    else:
        movies = call_command("download", search_by)
    return movies


@app.task()
def schedule_task():
    signatures = []
    suggests = Suggest.objects.all()
    if suggests.count() >= 2:
        for suggest in Suggest.objects.all():
            signatures.append(download_movie.s(suggest.type, suggest.name))
            suggest.delete()
        chord(group(*signatures))(send_email.s())



