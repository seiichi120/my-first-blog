from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('form/', views.form, name='form'),
    path('index/', views.index, name='index'),
    path('pay/', views.pay, name='pay'),
]
