from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, FormView
from .models import Movie, MovieRate, Person, Profile
from .forms import PersonForm, MovieForm, MovieRateForm, SearchForm, ProfileForm, QueryMovieForm
from django.contrib.auth import get_user_model
from django.core import management
import json

User = get_user_model()


# Create your views here.
class HomeView(LoginView):
    model = Movie
    template_name = 'home.html'
    extra_context = {'title': "Home page"}

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['object_list'] = Movie.objects.all()
        return context

    def form_invalid(self, form):
        context = super(HomeView, self).form_invalid(form)
        return context


class QueryMoviesApiView(FormView):
    template_name = 'query_movies.html'
    form_class = QueryMovieForm
    success_url = reverse_lazy('movie-list')
    extra_context = {'title':"Movies Search"}

    def form_valid(self, form):
        management.call_command("download", '-s', self.request.POST['search'])
        return super().form_valid(form)

class OutView(LogoutView):
    pass


class SignUpUserView(CreateView):
    model = Profile
    form_class = ProfileForm
    second_form_class = UserCreationForm
    template_name = 'register_profile.html'
    extra_context = {"title": "Register profile"}
    success_url = 'home'

    def get_context_data(self, **kwargs):
        context = super(SignUpUserView, self).get_context_data(**kwargs)
        if "form" not in context:
            context['form'] = self.form_class(self.request.GET)
        if "form1" not in context:
            context['form1'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form1 = self.second_form_class(request.POST)
        if form.is_valid() and form1.is_valid():
            profile = form.save(commit=False)
            profile.user = form1.save()
            profile.type = "U"
            profile.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form, form1=form1, message="Profile don't registered"))


class MovieListView(ListView):
    model = Movie
    extra_context = {'title': "List of the movies"}
    template_name = 'movie_list.html'
    form_class = SearchForm
    # Filter recent movie Movie.objects.filter(release_date__year=str(datetime.now().year)).order_by()
    queryset = Movie.objects.all()

    def get_queryset(self):
        if self.request.GET:
            results = None
            qs = super(MovieListView, self).get_queryset()
            search = self.request.GET['search']
            if qs.filter(title__icontains=search):
                results = qs.filter(title__icontains=search)
            elif qs.filter(release_date__icontains=search):
                results = qs.filter(release_date__icontains=search)
            elif qs.filter(classification__icontains=search):
                results = qs.filter(classification__icontains=search)
            elif qs.filter(duration__icontains=search):
                results = qs.filter(duration__icontains=search)
            elif qs.filter(country__name__icontains=search):
                results = qs.filter(country__name__icontains=search)
            elif qs.filter(original_language__name__icontains=search):
                results = qs.filter(original_language__name__icontains=search)
            elif qs.filter(genre__name__icontains=search):
                results = qs.filter(genre__name__icontains=search)
            elif qs.filter(persons__name__icontains=search):
                results = qs.filter(persons__name__icontains=search)
            return results
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super(MovieListView, self).get_context_data(**kwargs)
        if self.get_queryset():
            context['movies'] = self.get_queryset()
        else:
            messages.add_message(self.request, messages.ERROR, "There is not coincidences in the search!")
        context['rates'] = MovieRate.objects.get_rated()
        context['form'] = self.form_class
        return context


class MovieDetailView(DetailView):
    model = Movie
    extra_context = {"title": "Movie Detail"}
    template_name = 'movie_detail.html'


class CharacterView(CreateView):
    extra_context = {'title': "Create actors and directors"}
    model = Person
    form_class = PersonForm
    template_name = "character_form.html"

    def get_success_url(self):
        return reverse_lazy('character-detail', kwargs={'pk': self.object.pk})


class CharacterDetailView(DetailView):
    model = Person
    extra_context = {'title': 'Person Detail'}
    template_name = "character_detail.html"


class MovieView(CreateView):
    extra_context = {'title': "Create movies"}
    model = Movie
    form_class = MovieForm
    template_name = "movie_form.html"

    def get_success_url(self):
        return reverse_lazy('movie-detail', kwargs={'pk': self.object.pk})


class MovieRateView(CreateView):
    extra_context = {'title': "Rating a movie"}
    model = MovieRate
    form_class = MovieRateForm
    template_name = 'movierate_form.html'

    def get_success_url(self):
        return reverse_lazy('movie-detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie'] = Movie.objects.get(pk=self.kwargs['pk'])
        context['form'] = MovieRateForm(initial={'movie': context['movie']})
        return context
