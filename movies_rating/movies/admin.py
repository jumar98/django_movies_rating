from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Movie, MovieRate, Language, Genre, Profile, Country, Person, Token
from .resources import LanguageResource, CountryResource, GenreResource
from import_export import resources
# Register your models here.


class LanguageAdmin(ImportExportModelAdmin):
    resource_class = LanguageResource


class CountryAdmin(ImportExportModelAdmin):
    resource_class = CountryResource


class GenreAdmin(ImportExportModelAdmin):
    resource_class = GenreResource


admin.site.register(Movie)
admin.site.register(MovieRate)
admin.site.register(Person)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Profile)
admin.site.register(Language,LanguageAdmin)
admin.site.register(Country,CountryAdmin)
admin.site.register(Token)