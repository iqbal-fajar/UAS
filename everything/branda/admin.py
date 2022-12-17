from django.contrib import admin
from branda.models import Barang, Produk
# Register your models here.

class BarangAdmin(admin.ModelAdmin):
    list_display = ['jenis_barang', 'kondisi','jumlah', 'ukuran']
    search_fields = ['jenis_barang', 'kondisi','jumlah', 'ukuran']
    list_filter = ('produk_id',)
    list_per_page = 2
    

admin.site.register(Barang, BarangAdmin)
admin.site.register(Produk)