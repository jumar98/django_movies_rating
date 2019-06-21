from rest_framework import serializers
from .models import MovieRate, Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class MovieRateSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    movie = serializers.HyperlinkedRelatedField(read_only=True, view_name='movie', lookup_field='pk')
    class Meta:
        model = MovieRate
        fields = ('movie', 'user', 'rating')