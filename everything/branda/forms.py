from django.forms import ModelForm
from django import forms
from branda.models import Barang

class FormBarang(ModelForm):
    class Meta:
        model = Barang
        fields = '__all__'

        widgets = {
            'jenis_barang' : forms.TextInput({'class':'form-control'}),
            'kondisi' : forms.TextInput({'class':'form-control'}),
            'jumlah' : forms.NumberInput({'class':'form-control'}),
            'ukuran' : forms.NumberInput({'class':'form-control'}),
            'produk_id' : forms.Select({'class':'form-control'}),
        }