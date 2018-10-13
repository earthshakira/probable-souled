import falcon
class ResponseUtil(object):
    """To be used for getting a predefined response for errors"""
    stati = {
        404:{
            "status": falcon.HTTP_404,
            "message": 'resource not found'
        },
        409:{
            "status": falcon.HTTP_409,
            "message": 'idempotent operation'
        },
        400:{
            "status": falcon.HTTP_400,
            "message": 'operation not supported'
        },
        422:{
            "status": falcon.HTTP_422,
            "message": 'Can\'t do what you want with what I\'ve got valid params'
        }

    }

    @staticmethod
    def get_response(statusCode):
        return ResponseUtil.stati[statusCode]

    @staticmethod
    def makeBody(response,value):
        response.status = falcon.HTTP_200
        response.body = value

    @staticmethod
    def makeJson(response,jsonObject):
        response.status = falcon.HTTP_200
        response.json = jsonObject

    @staticmethod
    def makeResponse(statusCode,response):
        error = ResponseUtil.stati[statusCode]
        response.status = error['status']
        response.json = error;

    @staticmethod
    def success():
        return falcon.HTTP_200

    @staticmethod
    def error(e,response):
        response.status = falcon.HTTP_500
        response.json = {'status' : falcon.HTTP_500, 'except' : str(e)}
