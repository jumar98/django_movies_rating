from django_filters import rest_framework as filters


class MovieFilter(filters.FilterSet):

    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
