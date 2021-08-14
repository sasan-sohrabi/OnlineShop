import time

from django.http import HttpResponse

from core.models import Address, User


class DifferenceTimer:
    def __init__(self, get_response_func) -> None:
        self.get_response = get_response_func
        self.total = 0

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        # self.total += duration
        response["PageTime"] = int(duration * 1000)
        print(response['PageTime'])
        return response
