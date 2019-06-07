from django.contrib.auth import get_user_model
from django.db import models
import datetime

User = get_user_model()  # Get the default User of django

# Create your models here.
class Person(models.Model):

    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    class Meta:
        abstract = True

    @property
    def age(self):
        today = datetime.date.today()
        return (today.year - self.birth_date.year) - int((today.month, today.day) < (self.birth_date.month,
                                                                                     self.birth_date.day))
    def __str__(self):
        return "{}".format(self.name)

class Profile(models.Model):

    CHOICE_TYPE = [
        ('Admin', 'A'),
        ('User', 'U')
    ]

    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    address = models.CharField(max_length=50)
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=CHOICE_TYPE)

    @property
    def age(self):
        today = datetime.date.today()
        return (today.year - self.birth_date.year) - int((today.month, today.day) < (self.birth_date.month,
                                                                                     self.birth_date.day))
    @property
    def full_name(self):
        return "{} {}".format(self.name, self.last_name)

    def __str__(self):
        return "{}".format(self.user)

class Genre(models.Model):

    name = models.CharField(max_length=25)

    def __str__(self):
        return "{}".format(self.name)

class Language(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.name)

class Movie(models.Model):

    title = models.CharField(max_length=100)
    duration = models.TimeField()
    detail = models.TextField()
    trailer_url = models.URLField()
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    original_language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.title.capitalize())

class Country(models.Model):

    name = models.CharField(max_length=30)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return "{}".format(self.name)

class MovieRate(models.Model):

    RATINGS = [
        ("One",1),
        ("Two",2),
        ("Three",3),
        ("Four",4),
        ("Five",5)
    ]

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(choices=RATINGS)

    class Meta:
        unique_together = ("movie","user")

class MovieActor(Person):
    pass

class MovieDirector(Person):
    pass