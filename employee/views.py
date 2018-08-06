from django.shortcuts import render
from .models import *
from django.db import transaction
from django.http import HttpResponse, QueryDict
from django.views.decorators.http import require_http_methods


# Create your views here.


def list_emp(request):
    """把所有的emp表中的数据展示出来"""
    lst = Emp.objects.all()
    return render(request, "list_emp.html", {'objs':lst})


def list_dept(request):
    """查询所有部门信息"""
    lst = Dept.objects.all()
    return render(request, "list_dept.html", {'objs': lst})


def lst(request, model):
    """通用视图"""
    print(model)
    r = model.objects.all()
    model_name = model.__name__.lower()
    return render(request, "list_%s.html" % model_name, {'objs': r})


import json
def find_salegrade(request, pk):
    print(request.is_ajax()) # 打印是否是ajax请求
    try:
        # 根据主键get()查询数据，有可能会提示错误,返回字典
        s = SaleGrade.objects.values('grade', 'lowsal', 'higsal').get(pk=pk)
        # 将字典转化成json串--序列化，调用json模块中的dumps方法
        j = json.dumps(s, ensure_ascii=False)
        # 要返回一个json数据，一定要添加媒体类型
        return HttpResponse(j, content_type='application/json;charset=utf-8')
    except SaleGrade.DoesNotExist as e: # 没有找到等级
        context = {'code': 500} # 返回500的code 方便前台左判断
        return HttpResponse(json.dumps(context, ensure_ascii=False),
                            content_type='application/json;charset=utf-8')


@require_http_methods(['PUT', 'DELETE'])
def put_delete(request):
    """测试获取put, delete请求"""
    params = request.body.decode(encoding='utf-8')
    print(QueryDict(params))
    return HttpResponse(json.dumps({'code': 200, 'message': 'success'}),
                        content_type='application/json;charset=utf-8')

