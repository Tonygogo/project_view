from django.urls import path
from . import views


urlpatterns = [

    path('http_methods/', views.http_methods, name='http_methods'),
    path('http_get/', views.http_get, name='http_get'),
    path('http_post/', views.http_post, name='http_post'),
    path('http_safe/', views.http_safe, name='http_safe'),
]