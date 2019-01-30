from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    url(r'^form/$', views.form, name='form'), # 追加する
]
