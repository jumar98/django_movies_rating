from django.contrib import admin
from django.urls import path

from movies.views import ListCreateMovieApi, MethodWithPK
from .views import HomeView, CharacterView, MovieView, MovieRateView, MovieListView, MovieDetailView, \
    CharacterDetailView, SignUpUserView, LogOutMovie, DownloadMovieView, ApiMovieList, ApiMovieDetail, ApiMovieListXML, \
    MyRate, MovieRateApi, UpdateRateView, DeleteRateView
"""ListCreateMovieApi, MethodWithPK"""


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('download/', DownloadMovieView.as_view(), name="download-movie"),
    path('rates/', MyRate.as_view(), name="my-rates"),
    path('movie_list/api/', ApiMovieList.as_view(), name="movie_api"),
    path('movie/xml/', ApiMovieListXML.as_view(), name="xml"),
    path('movie_detail/api/<int:pk>',ApiMovieDetail.as_view(),name="movie_detail_api"),
    path('logout/', LogOutMovie.as_view(), name="logout"),
    path('register/profile', SignUpUserView.as_view(), name='signup'),
    path('characters', CharacterView.as_view(), name="character-create"),
    path('movies', MovieView.as_view(), name="movie-create"),
    path('movies/<int:pk>', MovieDetailView.as_view(), name="movie-detail"),
    path('rate/<int:pk>', UpdateRateView.as_view(),name='rate-update'),
    path('movies/list', MovieListView.as_view(), name="movie-list"),
    path('movies/rating/<int:pk>', MovieRateView.as_view(), name="movie-rating"),
    path('characters/<int:pk>', CharacterDetailView.as_view(), name='character-detail'),
    path('movie_rates/<int:pk>', MovieRateApi.as_view(), name='movie_rates'),
    path('movies/', ListCreateMovieApi.as_view(), name='movie_list'),
    path('movies/<int:pk>', MethodWithPK.as_view(), name='movie'),
    path('rate/<int:pk>/delete', DeleteRateView.as_view(), name='delete-rate')

]