from mongoengine import *

class Product(Document):
    artist = StringField(required=True, max_length=255)
    category = StringField(required=True, max_length=255)
    product = StringField(required=True, max_length=255)
    price = StringField(required=True, max_length=255)
    images = StringField(required=True, max_length=255)
    productId = DecimalField()
    meta = {'strict': False}


class Cart(Document):
    userId = StringField(required=True,max_length=25)
    items = DictField(default={})

class Coupon(Document):
    id = StringField(max_length=25,primary_key= True)
    artist = StringField(max_length=255)
    category = StringField(max_length=255)
    product = StringField(max_length=255)
    constraints = DictField(default={})
    discounts = DictField(default={})
