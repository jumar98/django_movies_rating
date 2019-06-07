from import_export import resources
from .models import Language, Country, Genre

class LanguageResource(resources.ModelResource):

    class Meta:
        model = Language

class CountryResource(resources.ModelResource):

    class Meta:
        model = Country

class GenreResource(resources.ModelResource):

    class Meta:
        model = Genre