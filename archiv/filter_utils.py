from django_filters import FilterSet
from django.db.utils import ProgrammingError
from django.contrib.postgres.search import SearchQuery


class SchrederFilter(FilterSet):
    def search_fulltext(self, queryset, field_name, value):
        search_type = "websearch"
        search_term = value
        if value and value.endswith("*"):
            search_type = "raw"
            search_term = value.replace("*", ":*")
            query = SearchQuery(search_term, config="german", search_type=search_type)
            qs = queryset.filter(vector_column=query)
            try:
                qs.count()
            except ProgrammingError:
                print(f"### processed search value: {search_term} is not valid")
                return queryset
        else:
            query = SearchQuery(value, config="german", search_type=search_type)
            qs = queryset.filter(vector_column=query)
        return qs
