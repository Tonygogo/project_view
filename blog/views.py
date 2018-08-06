from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
# Create your views here.


def index(request):
    1/0
    return HttpResponse("这是首页。。。")


def query(request, num=1):
    raise PermissionDenied()
    return HttpResponse('查询页码【%d】的数据。。' % num)
