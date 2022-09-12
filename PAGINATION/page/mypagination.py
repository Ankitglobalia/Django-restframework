# pagenumber pagination
# from rest_framework.pagination import PageNumberPagination


# class Mypaginationnumber(PageNumberPagination):
#     page_size=5
#     page_query_param='p'
#     page_size_query_param='records'
#     max_page_size=5
#     last_page_strings='end'

# # Listoffset pagination
# from rest_framework.pagination import LimitOffsetPagination


# class Limitoffset(LimitOffsetPagination):
#    pass


from rest_framework.pagination import CursorPagination


class cursorpagination(CursorPagination):

   page_size=3
   ordering='name'
