from django.contrib.auth import get_user_model
from django.db import models
import datetime

User = get_user_model()  # Get the default User of django

# Create your models here.
class Person(models.Model):

    TYPE_PERSON = [
        ('A','Actor'),
        ('D','Director')
    ]

    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    type = models.CharField(max_length=1, choices=TYPE_PERSON)

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

class Genre(models.Model):

    name = models.CharField(max_length=25)

    def __str__(self):
        return "{}".format(self.name)

class Language(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.name)

class MovieActor(Person):
    pass

class MovieDirector(Person):
    pass

class Country(models.Model):

    name = models.CharField(max_length=30)

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

    title = models.CharField(max_length=100)
    duration = models.TimeField()
    detail = models.TextField()
    poster = models.ImageField(upload_to='images/')
    classification = models.CharField(max_length=5, choices=CLASSIFICATION)
    trailer_url = models.URLField()
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    original_language = models.ForeignKey(Language, on_delete=models.SET(''))
    actors = models.ManyToManyField(MovieActor)
    directors = models.ManyToManyField(MovieDirector)
    country = models.ForeignKey(Country, on_delete=models.SET(''))

    def __str__(self):
        return "{}".format(self.title.capitalize())

class MovieRate(models.Model):

    RATINGS = [
        (1,"One"),
        (2,"Two"),
        (3,"Three"),
        (4,"Four"),
        (5,"Five")
    ]

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(choices=RATINGS)

    class Meta:
        unique_together = ("movie","user")