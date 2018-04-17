from sqlalchemy.exc import DBAPIError
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPBadRequest
from ..sample_data import MOCK_DATA
import requests
import json

from ..models import MyModel


@view_config(
    route_name='home',
    renderer='../templates/base.jinja2',
    request_method='GET')
def index_view(request):
    """
    Directs user to the home template
    """
    return {}


@view_config(
    route_name='detail',
    renderer='../templates/detail.jinja2',
    request_method='GET')
def portfolio_view(request):
    """
    Directs user to their detail template
    """
    return {'data': MOCK_DATA}


# @view_config(
#     route_name='detail',
#     renderer='../templates/detail.jinja2',
#     request_method='GET')
# def detail_view(request):
#     """
#     Directs user to the detail template
#     """
#     upc = request.matchdict['upc']

#     for data in MOCK_DATA:
#         if data['upc'] == upc:
#             return {'data': data}
#     return {}
