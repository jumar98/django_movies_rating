import requests
from django.conf import settings
from django.core.management.base import BaseCommand
import pprint
from io import open
from movies.models import Movie, Language, Genre, Country, Person
from django.core.files import File


class Command(BaseCommand):
    help = 'fetch movies from OMDB API'

    def add_arguments(self, parser):
        # positional argument
        parser.add_argument('title', type=str)

        # kwargs like arguments
        parser.add_argument('-s', '--search', action='store_true', default=False)

    def handle(self, *args, **options):
        search = options['search']
        title = options['title']
        movies_results = []
        persons = []
        if search:
            results = requests.get("http://www.omdbapi.com/?s={}&apikey=f0ed2260&type=movie".format(title))
        if results:
            for movies in results.json()['Search']:
                results = requests.get("http://www.omdbapi.com/?i={}&apikey=f0ed2260".format(movies['imdbID'])).json()
                movies_results.append(results)

            ext_image = []
            content = None
            image_url = None
            poster = "images/COMING-SOON.gif"
            for movie in movies_results:
                if movie['Poster'] != 'N/A':
                    ext_image = movie['Poster'].split('.')
                    content = requests.get(movie['Poster']).content
                    image_url = "{}/images/{}.{}".format(settings.MEDIA_ROOT, movie['Title'], ext_image[-1])
                    with open(image_url, 'wb') as file:
                        file.write(content)
                    poster = "images/{}.{}".format(movie['Title'], ext_image[-1])

                language = Language.objects.get_or_create(name=movie['Language'].split(',')[0])
                genre = Genre.objects.get_or_create(name=movie['Genre'].split(',')[0])
                country = Country.objects.get_or_create(name=movie['Country'].split(',')[0])

                movie_instance = Movie.objects.create(title=movie['Title'], classification=movie['Rated'],
                                                      duration=movie['Runtime'], detail=movie['Plot'], poster=poster,
                                                      country=country[0], genre=genre[0],
                                                      original_language=language[0])

                for director in movie['Director'].split(','):
                    persons.append(Person.objects.get_or_create(name=director, type='D'))

                for actor in movie['Actors'].split(','):
                    persons.append(Person.objects.get_or_create(name=actor, type='A'))

                    for person in persons:
                        movie_instance.persons.add(person[0])

        else:
            return "There is not results"

        print("entro")
        # return movies_results
