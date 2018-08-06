from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.template import loader
from .models import UserInfo
# Create your views here.


def index(request):
    messages.info(request, "这是一个message信息。。。")
    return render(request, "tpl/tpl_index.html", context={'menu': '首页'})


def find(request):
    # 第一步找模板
    template = loader.get_template("tpl/tpl_index.html") # 默认是DjangoTemplates对象
    # 第二步数据渲染
    content = template.render(context = {'content': 'Hello World!', 'menu': '首页'}, request = request)
    print(content)
    # 返回响应
    return HttpResponse(content)


def show_user(request, pk):
    user = UserInfo.objects.get(pk=pk)
    return render(request, 'tpl/tpl_user.html', {'user': user, 'menu': '首页'})


def user_list(request):
    users = UserInfo.objects.all().order_by('-id')
    return render(request, 'tpl/tpl_user_list.html', {'users': users, 'menu': '首页'})


def path(request, year, month, day):
    return render(request, "tpl/tpl_date.html")

import datetime

def filter(request):
    context = {'userName': 'Jack',
               'tags':['很酷', '很帅', '有钱'],
               'gender': 1, 'height':190.254, 'birthday': datetime.datetime.now() }
    return render(request, 'tpl/tpl_filter.html', context=context)


def escape(request):
    context = {'msg': '<h1>这是内容</h1>&lt;script&gt;alert(1)&lt;/script&gt;'}
    return render(request, "tpl/tpl_escape.html", context=context)

def xss(request):
    div = """
        var div = document.createElement('div');
        div.innerHTML="Hello World!";
        document.body.appendChild(div);
    """
    context = {'msg': '<script>%s</script>' % div}
    print(context)
    return render(request, "tpl/tpl_xss.html", context=context)

