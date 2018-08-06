from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
"""编写一个由test跳转到另外rs的地址"""


def test_rs(request, pk):
    return HttpResponse("这是测试重定向，来吧。。。。%d" % pk)


def test01(request):
    return HttpResponseRedirect(reverse('rs:test_rs', args=(123,)))


def test02(request):
    return render(request, "test_revers.html")


