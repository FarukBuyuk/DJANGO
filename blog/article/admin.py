from django.contrib import admin
from .models import Sertifika

# Register your models here.
@admin.register(Sertifika)
class SertifikaAdmin(admin.ModelAdmin):
    list_display = ["sertifika_adi", "author", "created_date"]
    list_display_links = ["sertifika_adi", "created_date"]

    list_filter = ["created_date", "sertifika_adi"]

    search_fields = ["sertifika_adi"]
