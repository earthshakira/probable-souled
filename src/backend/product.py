import falcon

from models import Product
from util import ResponseUtil

class ProductResource(object):

    def on_get(self, req, resp):
        """Need to find a better way to pass back json"""
        ResponseUtil.makeBody(resp,Product.objects.to_json())
