import falcon

from models import Coupon
from models import Cart
from util import ResponseUtil

class ValidateEndpoint(object):

    def on_get(self, req, resp,userId,couponId):
        try:
            couponResult = Coupon.objects(id = couponId)
            cartResult = Cart.objects(userId = userId)
            if len(couponResult) == 0 or len(cartResult) == 0:
                ResponseUtil.makeResponse(409,resp);
                return;
            coupon = couponResult[0];
            cart = cartResult[0];
            ResponseUtil.makeJson(resp,{'cart':cart.to_json(),'coupon':coupon.to_json()});
        except Exception as e:
            ResponseUtil.error(e,resp)
