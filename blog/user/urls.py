from django.contrib import admin
from django.urls import path
from .import views

app_name = "user"

urlpatterns = [
    path('Kayıt/', views.Kayıt, name="Kayıt"),
    path('Giriş/', views.KullanıcıGiriş, name="Giriş"),
    path('Çıkış/', views.Çıkış, name="Çıkış"),
]
