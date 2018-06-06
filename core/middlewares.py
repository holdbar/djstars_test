import json

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        with open('log.txt', 'a') as log:
            if request.method == "GET":
                log.write(str(request) + '\n')
                log.write(str(request.GET) + '\n')
                log.write(str(request.META) + '\n')
            if request.method == "POST":
                log.write(str(request) + '\n')
                log.write(str(request.POST) + '\n')
                log.write(str(request.META) + '\n')

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response