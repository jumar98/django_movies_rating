from django.contrib import admin
from django.urls import path
from .views import HomeView, CharacterView, MovieView, MovieRateView, MovieListView, MovieDetailView, \
    CharacterDetailView, SignUpUserView, OutView, QueryMoviesApiView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('api/movie/', QueryMoviesApiView.as_view(), name="api_movie"),
    path('logout/', OutView.as_view(), name="logout"),
    path('register/profile', SignUpUserView.as_view(), name='signup'),
    path('characters', CharacterView.as_view(), name="character-create"),
    path('movies', MovieView.as_view(), name="movie-create"),
    path('movies/<int:pk>', MovieDetailView.as_view(), name="movie-detail"),
    path('movies/list', MovieListView.as_view(), name="movie-list"),
    path('movies/rating/<int:pk>', MovieRateView.as_view(), name="movie-rating"),
    path('characters/<int:pk>', CharacterDetailView.as_view(), name='character-detail')
]