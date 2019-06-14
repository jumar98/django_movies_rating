
from django.db.models import QuerySet, Sum, Count, FloatField


class MovieQueryset(QuerySet):
    def get_by_year(self, year=None):
        if year:
            return self.filter(release_date__year=year)
        else:
            return self


class MovieRateQueryset(QuerySet):
    def get_rated(self):
        return self.values('movie').annotate(
            rating=Sum('rating', output_field=FloatField())*1.00/Count('movie', output_field=FloatField())).order_by('-rating')