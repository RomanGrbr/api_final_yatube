# from rest_framework.pagination import PageNumberPagination
# from rest_framework.response import Response
#
#
# class PostsPagination(PageNumberPagination):
#     page_size = 5
#
#     # Если требуется переопределить поля
#     def get_paginator_response(self, data):
#         return Response({
#             'licks': {},
#             'count': self.page.paginator.count,
#             'response': data
#         })
