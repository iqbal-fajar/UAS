from django.shortcuts import render, redirect
from branda.models import Barang
from branda.forms import FormBarang
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

def perbarui(request, id_branda):
    branda = Barang.objects.get(id=id_branda)
    template = 'satu/perbarui.html'
    if request.POST:
        form = FormBarang(request.POST, instance=branda)
        if form.is_valid():
            form.save
            messages.success(request, "Data Berhasil Diperbarui")
            return redirect('perbarui', id_branda=id_branda)
    else:
        form = FormBarang(instance=branda)
        konteks = {
            'form':form,
            'branda':branda,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def branda(request):
    barangs = Barang.objects.all()

    konteks = {
        'barangs': barangs,
    }
    return render(request, 'satu/branda.html', konteks)


def plus_barang(request):
    if request.POST:
        form = FormBarang()
        if form.is_valid():
            form.save()
            form = FormBarang()
            pesan = "Data berhasil disimpan"
            konteks = {
                'form': form,
                'pesan': pesan,
            }

            return render(request, 'satu/plus-barang.html', konteks)
    else:
        form = FormBarang()

        konteks = {
            'form': form,
        }
        
    return render(request, 'satu/plus-barang.html', {'form': form})