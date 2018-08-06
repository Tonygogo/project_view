"""url映射文件"""
from django.urls import path, re_path, register_converter
from . import views
from .convertes.converts import FourDigitYearConverter
app_name = 'articles'

register_converter(FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    # path('articles/<int:year>/', views.year_archive),
    # re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    path('articles/<yyyy:year>/', views.year_archive),


    # path('articles/<int:year>/<int:month>/', views.month_archive),
    re_path(r'^articles/(?P<year>\d{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
    re_path(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>[\w-]+)$', views.article_detail),
]
