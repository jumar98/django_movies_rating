from rest_framework import serializers
from movies.models import MovieRate, Movie


class MovieSerializer(serializers.ModelSerializer):
    pk = serializers.HyperlinkedIdentityField(source='id',view_name='api-movie:movie-detail', lookup_field='pk')

    class Meta:
        model = Movie
        fields = '__all__'


class MovieRateSerializer(serializers.ModelSerializer):
    pk = serializers.HyperlinkedIdentityField(source='id', view_name='api-movie:movierate-detail', lookup_field='pk')
    user = serializers.StringRelatedField()
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = MovieRate
        fields = ('pk', 'user', 'rating', 'movie',)
