from django.shortcuts import render, redirect
from .forms import GirişForm, KayıtForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def Kayıt(request):
    if request.method == "POST":
        form = KayıtForm(request.POST)
        if form.is_valid():
            Kullanici_Adi = form.cleaned_data.get("Kullanici_Adi")
            Parola = form.cleaned_data.get("Parola")

            newUser = User(username=Kullanici_Adi)
            newUser.set_password(Parola)
            newUser.save()

            login(request, newUser)
            messages.success(request, "Başarıyla Kayıt Oldunuz..")

            return redirect("index")
    else:
        form = KayıtForm()

    context = {
        "form": form
    }

    return render(request, "kayıt.html", context)

def KullanıcıGiriş(request):
    form = GirişForm(request.POST or None)

    bağlam = {
        "form": form
    }

    if form.is_valid():
        kullanıcıadı = form.cleaned_data.get("kullanıcıadı")
        parola = form.cleaned_data.get("parola")

        user = authenticate(username=kullanıcıadı, password=parola)

        if user is None:
            messages.info(request, "Kullanıcı Adı veya Parola Hatalı!")
            return render(request, "giriş.html", bağlam)

        messages.success(request, "Başarıyla Giriş Yapıldı..")
        login(request, user)
        return redirect("index")

    return render(request, "giriş.html", bağlam)

def Çıkış(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")
