from django.shortcuts import render

from core.models.request_log import RequestLog

def requests_log(request):
    requests = RequestLog.objects.get_requests()

    return render(request, 'requests_log.html', {'requests': requests})
