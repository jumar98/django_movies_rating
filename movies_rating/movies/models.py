from django.contrib.auth import get_user_model
from django.db import models
import datetime
from .queryset import MovieRateQueryset

from .queryset import MovieRateQueryset

User = get_user_model()  # Get the default User of django

# Create your models here.
class Person(models.Model):

    TYPE_PERSON = [
        ('A','Actor'),
        ('D','Director')
    ]

    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    type = models.CharField(max_length=1, choices=TYPE_PERSON)

    @property
    def age(self):
        today = datetime.date.today()
        return (today.year - self.birth_date.year) - int((today.month, today.day) < (self.birth_date.month,
                                                                                     self.birth_date.day))
    def __str__(self):
        return "{}".format(self.name)


class Profile(models.Model):

    CHOICE_TYPE = [
        ('A','Admin'),
        ('U','User')
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


class Token(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    token = models.CharField(max_length=100)

    def __str__(self):
        return "{} : {}".format(self.user.username, self.token)


class Genre(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.name)

class Language(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.name)


class Country(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)

class Movie(models.Model):

    CLASSIFICATION = [
        ('A','Todo publico'),
        ('B','+12'),
        ('B15','+15'),
        ('C','+18'),
        ('D','Películas para adultos')
    ]

    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=25, null=True)
    detail = models.TextField()
    poster = models.ImageField(max_length=255, upload_to='images/', null=True)
    classification = models.CharField(max_length=50, choices=CLASSIFICATION, null=True)
    trailer_url = models.URLField(null=True)
    release_date = models.DateField(null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    original_language = models.ForeignKey(Language, on_delete=models.SET(''), null=True)
    persons = models.ManyToManyField(Person)
    country = models.ForeignKey(Country, on_delete=models.SET(''),null=True)

    def __str__(self):
        return "{}".format(self.title.capitalize())

    def get_absolute_url(self):
        return '/movies/{}'.format(self.pk)


class MovieRate(models.Model):

    RATINGS = [
        (1,"One"),
        (2,"Two"),
        (3,"Three"),
        (4,"Four"),
        (5,"Five")
    ]

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    comment = models.TextField()
    rating = models.IntegerField(choices=RATINGS)

    objects = MovieRateQueryset.as_manager()

    def __str__(self):
        return f'{self.user.username} : {self.rating}'


class Suggest(models.Model):
    type = models.CharField(max_length=5, null=True)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.movies}'
