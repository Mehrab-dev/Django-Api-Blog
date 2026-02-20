from rest_framework.pagination import PageNumberPagination

class DefaultPagination(PageNumberPagination) :
    page_size = 3
    page_query_param = "page"
    page_size_query_param = "page-size"
    max_page_size = 10
    last_page_strings = ["last-page"]