from django.http import HttpResponse,JsonResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from .tasks import sendEmail

import requests

def send_email(request) :
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending</h1>")

# def test(request) :
#     if cache.get("test_delay_api") is None :
#         response = requests.get("https://a67eeccc-c8cd-4898-862c-e51fcfd098d0.mock.pstmn.io/test/delay/5")
#         cache.set("test_delay_api",response.json())
#     return JsonResponse(cache.get("test_delay_api")) 

@cache_page(60)
def test(request) :
    response = requests.get("https://a67eeccc-c8cd-4898-862c-e51fcfd098d0.mock.pstmn.io/test/delay/5")
    return JsonResponse(response.json())