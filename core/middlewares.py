from core.models.request_log import RequestLog

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "GET":
            request_row = RequestLog()
            request_row.request = str(request)
            request_row.parameters = str(request.GET)
            request_row.meta = str(request.META)
            request_row.cookies = str(request.COOKIES)
            request_row.save()
        if request.method == "POST":
            request_row = RequestLog()
            request_row.request = str(request)
            request_row.parameters = str(request.POST)
            request_row.meta = str(request.META)
            request_row.cookies = str(request.COOKIES)
            request_row.save()
        response = self.get_response(request)

        return response