import falcon

from models import Cart
from util import ResponseUtil

class CartResource(object):

    def on_get(self, req, resp,userId):
        try:
            carts = Cart.objects(userId = userId)
            if len(carts) == 0 :
                ResponseUtil.makeResponse(404,resp);
                return;
            else :
                ResponseUtil.makeBody(resp,carts[0].to_json())
        except Exception as e:
            ResponseUtil.error(e,resp)


    def on_post(self, req, resp,userId):
        try:
            cart = Cart(userId = userId)
            carts = Cart.objects(userId = userId)
            if len(carts) == 0 :
                cartResp = cart.save()
                ResponseUtil.makeBody(resp, cartResp.to_json())
            else :
                ResponseUtil.makeResponse(409,resp)
        except Exception as e:
            ResponseUtil.error(e,resp);

    # FIXME: This farzi patch lel
    def on_patch(self,req,resp,userId,task):
        try:
            cartEntry = req.json
            cart = Cart.objects(userId = userId)
            key = 'items.' + str(cartEntry['productId']);
            if len(cart) == 0:
                ResponseUtil.makeResponse(400,resp)
                return
            cartUpdate = None
            if task == 'add' :
                cartUpdate = cart.update_one(__raw__={'$set':{key:cartEntry}})
            elif task == 'remove' :
                cartUpdate = cart.update_one(__raw__={'$unset':{key:1}})
            else :
                ResponseUtil.makeResponse(400,resp);
                return
            ResponseUtil.makeJson(resp,{"update":cartUpdate})
        except Exception as e:
            ResponseUtil.error(e,resp)
