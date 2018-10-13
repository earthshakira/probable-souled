from app import api
from backend.product import ProductResource
from backend.cart import CartResource
from backend.coupon import CouponResource
from backend.validate import ValidateEndpoint
api.add_route('/api/products', ProductResource())
api.add_route('/api/cart/{userId}',CartResource())
api.add_route('/api/cart/{userId}/{task}',CartResource())
api.add_route('/api/coupon/{id}',CouponResource())
api.add_route('/api/validate/{userId}/{couponId}',ValidateEndpoint())
