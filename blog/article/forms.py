from django import forms
from .models import Sertifika

class SertifikaFormu(forms.ModelForm):
    class Meta:
        model = Sertifika
        fields = ['sertifika_adi', 'belge']
