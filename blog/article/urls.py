from django.contrib import admin
from django.urls import path

from . import views

app_name = "article"

urlpatterns = [
    path('kontrolpaneli/', views.kontrolpaneli, name="kontrolpaneli"),
    path('sertifikalar/', views.sertifikalar, name="sertifikalar"),
    path('sertifikasayfası/', views.sertifikasayfası, name="sertifikasayfası"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
    
]


