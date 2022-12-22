from django.contrib import admin
from django.urls import path, include
from branda.views import branda, plus_barang

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base),
    path('branda/', include('branda.urls')),
    path('plus-barang/', plus_barang),
]
