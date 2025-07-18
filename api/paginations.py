from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'page_size' 
    page_query_param = 'page-num'
    max_page_size = 1

    # custom pagination 
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page_size,
            'page_size': self.page_size,
            'results': data
        })