
from django.conf.urls import url,include
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('login.urls', namespace="login")),
    url(r'^firm/', include('firm.urls', namespace="firm")),
    url(r'^home/', include('home.urls', namespace="home")),
    url(r'^transaction/', include('transaction.urls', namespace="transaction")),
]
