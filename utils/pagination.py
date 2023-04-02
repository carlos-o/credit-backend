from rest_framework import pagination
from rest_framework.response import Response
from src import settings
from collections import OrderedDict


def get_url(url: str):
    """
        Method get url from pagination

        :param url: url of next or previous
        :type url: str
        :return: url
    """
    count = 0
    position = 0
    # capture position of chart /
    for i, chart in enumerate(url):
        if "/" == chart:
            position = i
            count = count + 1
        if count > 2:
            break
    # get temporal url
    temporal_url = url[position:]
    return temporal_url


class CustomPagination(pagination.PageNumberPagination):
    page_size = settings.PAGE_SIZE
    url = settings.URL

    def get_paginated_response(self, data):
        next_url = None
        previous_url = None
        if self.get_next_link() is not None:
            temporal_url = get_url(self.get_next_link())
            next_url = self.url + temporal_url
        if self.get_previous_link() is not None:
            temporal_url = get_url(self.get_previous_link())
            previous_url = self.url + temporal_url
        return Response(OrderedDict([
             ('count', self.page.paginator.count),
             ('countItemsOnPage', self.page_size),
             ('current', self.page.number),
             ('next', next_url),
             ('previous', previous_url),
             ('results', data)
         ]))
