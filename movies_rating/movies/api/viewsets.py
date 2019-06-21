from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from movies.api.serializers import MovieSerializer, MovieRateSerializer
from movies.models import Movie, MovieRate
from rest_framework.authentication import TokenAuthentication
from .permission import IsAuthenticatedOrReadOnlyCustom, AuthAndModifyMovieRateCustom
from .filters import MovieFilter


class MovieModelViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyCustom]
    filter_class = MovieFilter
    serializer_classes = {
        'rate': MovieRateSerializer,
        'default': MovieSerializer
    }
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        return self.serializer_classes[self.action] if self.action in self.serializer_classes.keys() else \
        self.serializer_classes['default']

    def get_serializer_context(self):
        context = super(MovieModelViewSet, self).get_serializer_context()
        context.update({'request': self.request})
        return context

    @action(methods=['POST'], detail=True)
    def rate(self, request, pk=None):
        movie = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
        return Response(data=self.get_serializer(serializer.instance).data)


class MovieRateViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AuthAndModifyMovieRateCustom]
    serializer_class = MovieRateSerializer
    queryset = MovieRate.objects.all()
