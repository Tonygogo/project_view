from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

from django.views.decorators.http import require_http_methods,\
    require_GET,require_POST, require_safe

# Create your views here.


@require_http_methods(['POST', 'GET'])
def http_methods(request):
    return HttpResponse("只接收Post和Get请求！")


@require_GET
def http_get(request):
    return HttpResponse("只接收Get请求！")


@require_POST
def http_post(request):
    return HttpResponse("只接收Post请求！")


@require_safe
def http_safe(request):
    return HttpResponse("只接收Get或者Head请求！")

