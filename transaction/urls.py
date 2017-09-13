from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'(?P<firm_id>[0-9]+)/impress_home',views.impress_home,name="impress_home"),
    url(r'(?P<firm_id>[0-9]+)/add_impress',views.add_impress,name="add_impress"),
    url(r'(?P<firm_id>[0-9]+)/add_journal',views.add_journal,name="add_journal"),
    url(r'(?P<firm_id>[0-9]+)/expense_home',views.expense_home,name="expense_home"),
    url(r'(?P<firm_id>[0-9]+)/add_expense',views.add_expense,name="add_expense"),
    url(r'(?P<firm_id>[0-9]+)/receive_home',views.receive_home,name="receive_home"),
    url(r'(?P<firm_id>[0-9]+)/add_receive',views.add_receive,name="add_receive"),
    url(r'(?P<firm_id>[0-9]+)/transaction_add/(?P<ledger_id>[0-9]+)',views.transaction_add,name="transaction_add"),
    url(r'(?P<firm_id>[0-9]+)/ledger_details/(?P<ledger_id>[0-9]+)',views.ledger_details,name="ledger_details"),
    url(r'(?P<firm_id>[0-9]+)/(?P<type_id>[0-9]+)/filter_suppliers$',views.filter_suppliers,name="filter_suppliers"),
    url(r'(?P<firm_id>[0-9]+)/(?P<type_id>[0-9]+)/filter_customers$',views.filter_customers,name="filter_customers"),
    url(r'(?P<firm_id>[0-9]+)/(?P<type_id>[0-9]+)/filter_employees$',views.filter_employees,name="filter_employees"),
    url(r'(?P<firm_id>[0-9]+)/(?P<type_id>[0-9]+)/add_transaction/(?P<ledger_id>[0-9]+)$',views.add_transaction,name="add_transaction"),
]























