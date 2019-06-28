from django.core.management import call_command
from movies_rating.celery import app
from django.core.mail import EmailMessage


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
