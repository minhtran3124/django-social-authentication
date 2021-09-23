from rest_framework.pagination import PageNumberPagination

from drf_core import apis


class BasePaginationCommon(apis.BasePagination):
    """
    Custom Base class for pagination for getting full data.
    """

    def paginate_queryset(self, queryset, request, view=None):
        """
        Custom pagination queryset for getting full data
        """
        self.default_limit = self.get_count(queryset)

        return super(BasePaginationCommon, self).paginate_queryset(
            queryset, request, view=view)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page'
    max_page_size = 1000
