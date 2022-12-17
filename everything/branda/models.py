from django.db import models

# Create your models here.

class Produk(models.Model):
    brand = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.brand

class Barang(models.Model):
    jenis_barang = models.CharField(max_length=100)
    kondisi = models.CharField(max_length=10)
    jumlah = models.IntegerField(null=True)
    ukuran = models.CharField(max_length=5)
    produk_id = models.ForeignKey(Produk, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.jenis_barang

