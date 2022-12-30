from django.contrib import admin
from django.urls import path, include
from branda.views import *
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base),
    path('branda/', include('branda.urls')),
    path('plus-barang/', plus_barang),
    path('branda/perbarui/<int:id_branda>', perbarui, name='perbarui'),
    path('masuk/', LoginView.as_view(), name='masuk'),
]
