from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'(?P<firm_id>[0-9]+)/ledger_home',views.ledger_home,name="ledger_home"),
    url(r'(?P<firm_id>[0-9]+)/add_ledger',views.add_ledger,name="add_ledger"),
    url(r'(?P<firm_id>[0-9]+)/delete_ledger/(?P<ledger_id>[0-9]+)$',views.delete_ledger,name="delete_ledger"),
    url(r'(?P<firm_id>[0-9]+)/update_ledger/(?P<ledger_id>[0-9]+)$',views.update_ledger,name="update_ledger"),
    url(r'(?P<firm_id>[0-9]+)/ledger_info/(?P<ledger_id>[0-9]+)$',views.ledger_info,name="ledger_info"),
    url(r'(?P<firm_id>[0-9]+)/ledger_json',views.ledger_json,name="ledger_json"),
    url(r'(?P<firm_id>[0-9]+)/filtersuppliers$',views.filtersuppliers,name="filtersuppliers"),
    url(r'(?P<firm_id>[0-9]+)/filtercustomer$',views.filtercustomer,name="filtercustomer"),
    url(r'(?P<firm_id>[0-9]+)/filteremployee$',views.filteremployee,name="filteremployee"),
]

