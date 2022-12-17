from django.shortcuts import render
from branda.models import Barang

def branda(request):
    barangs = Barang.objects.all()

    konteks = {
        'barangs': barangs,
    }
    return render(request, 'satu/branda.html', konteks)
