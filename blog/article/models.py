from django.db import models
from django.contrib.auth.models import User

class Sertifika(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Yazar")
    sertifika_adi = models.CharField(max_length=50, verbose_name="Sertifika Adı")
    belge = models.FileField(upload_to='documents/', verbose_name="Belge")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return self.sertifika_adi
