from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Person, Movie, MovieRate, Profile
from django.core.exceptions import ValidationError

class PersonForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = Person
        fields = ['name', 'birth_date', 'type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit', 'Save character'))


class QueryMovieForm(forms.Form):
    choices = (
        (0, 'All'),
        (1, 'One'),
    )
    search_type = forms.CharField(widget=forms.Select(attrs={'class':'form-control mr-sm-2'}, choices=choices))
    search = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder':
                                                                                                    'Search movie'}))


class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user','type',)


class MovieForm(forms.ModelForm):
    release_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    duration = forms.IntegerField(min_value=0)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieRateForm(forms.ModelForm):


    class Meta:
        model = MovieRate
        fields = ('comment', 'rating',)

    def __init__(self, user, movie, *args, **kwargs):
        self.user = user
        self.movie = movie
        super(MovieRateForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = super(MovieRateForm, self).clean()
        if MovieRate.objects.filter(user=self.user, movie=self.movie).exists():
            raise ValidationError(f'Movie rate with user {self.user.username} and movie {self.movie.title} already exists')
        return data

    def save(self, commit=True):
        instance = super(MovieRateForm, self).save(commit=False)
        instance.user = self.user
        instance.movie = self.movie
        instance.save()
        return instance


class MovieRateUpdateForm(MovieRateForm):

    class Meta:
        model = MovieRate
        fields = ('comment', 'rating',)

    def __init__(self, user, movie, *args, **kwargs):
        super(MovieRateUpdateForm, self).__init__(user=user, movie=movie, *args, **kwargs)

    def clean(self):
        pass

    def save(self, commit=True):
        return super(MovieRateUpdateForm, self).save(commit=False)


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mr-sm-2', 'placeholder':'Search movie'}))