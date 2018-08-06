from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, \
    JsonResponse
from employee.models import Emp

# Create your views here.


def index(request):

    return HttpResponse(content="Hello Django!", charset='utf-8',
                        status=200, reason='Success',
                        content_type="text/html;charset=utf-8")


def rs(request):
    return HttpResponse("重定向的页面")


def test_rs(request):
    return HttpResponseRedirect(redirect_to='/response/rs/')


def return_json(request):
    """测试json"""
    return JsonResponse({'code': 200, 'message': 'success'})


def template(request):

    return render(request, 'test_render.html', {'msg': 'abc'})


def find_emp(request):
    """根据传入的员工编号返回员工信息,返回json"""
    # 获取参数
    pk = request.GET.get('id')
    # 查询数据库
    try:
        emp = Emp.objects.values('empNo', 'ename', 'sal',
                                 'comm', 'hireDate', 'mgr__ename',
                                 'dept__dname').get(pk=pk)
    except Emp.DoesNotExist as e:
        emp = {}

    # 返回结果
    return JsonResponse(emp)


def list_emps(request):
    """获取所有有效员工列表，返回json"""
    # 直接查询数据库
    emps = Emp.objects.values('empNo', 'ename', 'sal',
                                 'comm', 'hireDate', 'mgr__ename',
                                 'dept__dname').filter(isValid=1)

    # 返回结果
    return JsonResponse(list(emps), safe=False)

