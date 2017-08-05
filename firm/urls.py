from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^firm_login$',views.firm_login,name="firm_login"),
    url(r'^add_firm$',views.add_firm,name="add_firm"),
    url(r'^manage_firms$',views.manage_firms,name="manage_firms"),
    url(r'^(?P<firm_id>[0-9]+)/update_firm$',views.update_firm,name="update_firm"),
    url(r'^(?P<firm_id>[0-9]+)/delete_firm$',views.delete_firm,name="delete_firm"),

]