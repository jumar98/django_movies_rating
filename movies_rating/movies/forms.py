from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Person, Movie, MovieRate, Profile

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
    search = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Search movie'}))

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

    movie = forms.ChoiceField(widget=forms.TextInput(attrs={'disabled':'disabled'}))

    class Meta:
        model = MovieRate
        fields = '__all__'


class SearchForm(forms.Form):

    search = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mr-sm-2', 'placeholder':'Search movie'}))