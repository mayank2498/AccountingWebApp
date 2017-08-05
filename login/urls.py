from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$',views.login_user,name='login_user'),
    url(r'^exit$',views.logout_user,name='logout_user'),
]