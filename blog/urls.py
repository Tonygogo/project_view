"""url映射文件"""
from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('page<int:num>/', views.query, name='query'),
]
