from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.

# 获取2003的数据
def special_case_2003(request):
    now = datetime.datetime.now()
    html = "It is now %s." % now
    return HttpResponse(html)


# 获取某年的归档数据
def year_archive(request, year):
    return HttpResponse("这是【%s】的数据" % year)


# 获取某年某月的归档数据
def month_archive(request, year, month):
    return HttpResponse("这是【%s】/【%s】的数据" % (year, month))


# 获取某年某月的标记归档数据
def article_detail(request, year, month, slug):
    return HttpResponse("这是【%s】/【%s】的【%s】数据" % (year, month, slug))






