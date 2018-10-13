import falcon

from models import Coupon
from util import ResponseUtil

class CouponResource(object):


    def on_get(self, req, resp,id):
        try:
            coupons = Coupon.objects(id = id)
            if len(coupons) == 0 :
                ResponseUtil.makeResponse(404,resp);
                return;
            else :
                ResponseUtil.makeBody(resp,coupons[0].to_json())
        except Exception as e:
            ResponseUtil.error(e,resp)

    def on_post(self, req, resp,id):
        try:
            coupon = Coupon(id = id)
            couponBody = req.json

            for key in couponBody.keys():
                coupon[key] = couponBody[key]

            print(coupon.save())

        except Exception as e:
            ResponseUtil.error(e,resp);
