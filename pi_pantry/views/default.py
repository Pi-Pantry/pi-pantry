from sqlalchemy.exc import DBAPIError
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPBadRequest
from pyramid.security import NO_PERMISSION_REQUIRED, remember, forget
from ..sample_data import MOCK_DATA
import requests
import json

from ..models import Account


@view_config(
    route_name='home',
    renderer='../templates/base.jinja2',
    request_method='GET',
    permission=NO_PERMISSION_REQUIRED)
def index_view(request):
    """
    Directs user to the home template
    """
    return {}
