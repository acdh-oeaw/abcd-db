from django_filters import FilterSet
from django.contrib.postgres.search import SearchQuery


class SchrederFilter(FilterSet):

    def search_fulltext(self, queryset, field_name, value):
        # query = SearchQuery(value, config="german", search_type="websearch") ToDo: uncomment after pg-server update
        query = SearchQuery(value, config="german")
        qs = queryset.filter(vector_column=query)

        return qs
