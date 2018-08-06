from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.http import require_POST, require_GET
from .models import UserInfo
from django.urls import reverse
from datetime import timedelta
# Create your views here.


def index(request):
    """登录页面"""
    # 先从session中获取登录用户信息，是否存在
    username = request.session.get('userName')

    if username is not None and username.strip() != '':
        return render(request, 'login_success.html', {'userName':username})
    else:
        return render(request, "login.html")


@require_POST
def login(request):

    """登录"""
    # 先获取参数
    username = request.POST.get('userName')
    password = request.POST.get('password')
    # 参数是否为空

    if username is None or username.strip() == '':
        context = {'userNameMessage': '账号不能为空！'}
        return render(request, "login.html", context)
    if password is None or password.strip() == '':
        context = {'passwordMessage': '密码不能为空！', 'username': username}
        return render(request, "login.html", context)
    # 用户名和密码进行匹配（如果数据库中是加密的，那么匹配数据库时，需要对密码进行加密）
    try:
        user = UserInfo.objects.get(userName=username, password=password)
        # 要记住登录状态
        request.session['userName'] = user.userName
        request.session.set_expiry(3600) # 过多少秒过期
        # request.session.set_expiry(timedelta(seconds=10))
        # request.session.set_expiry(0)

        # return render(request, 'login_success.html', {'userName':username})
        # 重定向到首页，方便刷新，统一管理
        return HttpResponseRedirect(redirect_to=reverse('user:index'))
    except UserInfo.DoesNotExist as e:
        """登录失败，没有匹配上"""
        context = {'message': '账号或密码错误！', 'username': username, 'password': password}

        return render(request, "login.html", context)


def logout(request):
    """如果没有编写方法的装饰器，那么能接受所有的类型的请求"""
    """退出，就用户的登录状态删除--删除session中的登录用户名"""
    # del request.session['userName'] # 第一种方式，删除session中的某个值
    request.session.flush() # 第二种方式：flush()方法是删除当前的session
    # request.session.clear() # 第三种方式：清空所有的session
    # return render(request, "login.html")
    # 重定向到index
    return HttpResponseRedirect(reverse('user:index'))



from django.views.generic import View


"""基本视图"""
class UserView(View):
    http_method_names = ['get', 'post', 'head'] # 限制请求方式，如果不在调用http_method_not_allowed方法

    def get(self, request, *args, **kwargs):
        """处理get请求"""
        # 获取get参数
        params = request.GET
        print('接收Get传入的参数：', params)
        return HttpResponse("处理一个get方法。")

    def post(self, request, *args, **kwargs):
        """处理post请求"""
        print('接收Post传入的参数：', request.POST)
        return HttpResponse("处理post请求方法。")

    def put(self, request, *args, **kwargs):
        """处理put请求方法"""
        params = request.body.decode(encoding='utf-8')
        print('接收Put传入的参数：', params)
        return HttpResponse("处理put请求方法。")

    def delete(self, request, *args, **kwargs):
        """处理put请求方法"""
        params = request.body.decode(encoding='utf-8')
        print('接收Delete传入的参数：', params)
        return HttpResponse("处理delete请求方法。")

    @require_GET
    def find(self, request, *args, **kwargs):
        """找不到此方法"""
        return HttpResponse("接收find方法。。。")

    def http_method_not_allowed(self, request, *args, **kwargs):
        print("不允许的方法。。。")
        return HttpResponse("不支持此方法: %s" % request.method, status=405)


"""模板视图"""
from django.views.generic.base import TemplateView
class HomeView(TemplateView):

    # 指定模板名称
    template_name = "home.html"


    # 查询上下文的数据
    def get_context_data(self, **kwargs):
        return {'users': UserInfo.objects.all()}


"""重定基本向视图"""
from django.views.generic.base import RedirectView

class UserRedirectView(RedirectView):
    permanent = True # 为True，禁止重定向
    url = '/user/home/' # 重定向的url
    query_string = True # 允许跳转携带浏览器指定的参数

    # pattern_name = 'user:home' # 重定向采用反向查询


from django.views.generic.list import ListView
class UserListView(ListView):
    model = UserInfo # 指定查询的模型
    # 指定查询的结果集，如果既有model，又有queryset,那么优先考虑queryset
    #queryset = UserInfo.objects.filter(userName__icontains='五')
    # 指定模板名称，默认是小写应用名/小写model名_list.html
    template_name = "user_list.html"

    paginate_by = 1




    # 指定列表遍历的key的名称
    context_object_name = 'users'

    # 第一种获取数据的方式
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     q = UserInfo.objects.filter(userName__icontains='五')
    #     return {'users': q}


from django.views.generic.detail import DetailView
class UserDetailView(DetailView):
    model = UserInfo #  指定查询的model

    # queryset = UserInfo.objects


    context_object_name = 'user' # 指定模板获取数据的key名

    template_name = "user_detail.html"

    # pk_url_kwarg = 'abc' # 修改主键的参数名

    slug_field = 'slugUrl' # 修改查询slug属性
    slug_url_kwarg = 'slug_value' # 获取客户端slug的参数名字


def template(request, pk):
    return TemplateResponse(request, template='login.html')









