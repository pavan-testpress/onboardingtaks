import django_filters

class EventTimeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = EventTimeFilter
        fields = ['price', 'release_date']