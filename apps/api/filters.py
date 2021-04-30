from django_filters import rest_framework as filters

from events.models import Event


class EventCustomFilter(filters.FilterSet):
    administrative_unit = filters.CharFilter(method='get_administrative_unit')
    event_type_array = filters.CharFilter(method='get_event_type_array')

    class Meta:
        model = Event
        fields = {
            'date_from': ['gte', 'lte', 'year'],
            'date_to': ['gte', 'lte', 'year'],
            'start_date': ['gte', 'lte', 'year'],
            'indended_for': ['exact'],
            'program': ['exact'],
            'is_internal': ['exact'],
        }

    def get_administrative_unit(self, queryset, name, value, *args, **kwargs):
        if name == 'administrative_unit':
            queryset = queryset.filter(administrative_units__slug=value)
        return queryset

    def get_event_type_array(self, queryset, name, value, *args, **kwargs):
        if name == 'event_type_array':
            event_type_list = value.split(",")  # slugs
            queryset = queryset.filter(event_type__slug__in=event_type_list)
        return queryset