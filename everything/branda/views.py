from django.shortcuts import render
from branda.models import Barang
from branda.forms import FormBarang

def branda(request):
    barangs = Barang.objects.all()

    konteks = {
        'barangs': barangs,
    }
    return render(request, 'satu/branda.html', konteks)


def plus_barang(request):
    form = FormBarang()

    konteks = {
        'form': form,
    }

    return render(request, 'satu/plus-barang.html', konteks)