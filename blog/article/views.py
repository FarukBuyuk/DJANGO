from django.shortcuts import get_object_or_404, render, redirect
from .forms import SertifikaFormu
from django.contrib import messages
from .models import Sertifika
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

@login_required(login_url="user:Giriş")
def kontrolpaneli(request):
    return render(request, "kontrolpaneli.html")

@login_required(login_url="user:Giriş")
def sertifikalar(request):
    form = SertifikaFormu(request.POST or None, request.FILES or None)

    if form.is_valid():
        sertifika = form.save(commit=False)
        sertifika.author = request.user
        sertifika.save()

        messages.success(request, "Sertifika Başarıyla Oluşturuldu..")
        return redirect("index")

    return render(request, "sertifikalar.html", {"form": form})

@login_required(login_url="user:Giriş")
def sertifikasayfası(request):
    sertifikalar = Sertifika.objects.filter(author=request.user)
    return render(request, "sertifikasayfası.html", {"sertifikalar": sertifikalar})

@login_required(login_url="user:Giriş")
def update(request, id):
    sertifika = Sertifika.objects.get(id=id)
    if request.method == 'POST':
        form = SertifikaFormu(request.POST, request.FILES, instance=sertifika)
        if form.is_valid():
            form.save()
            messages.success(request, "Sertifika Başarıyla Güncellendi..")
            return redirect("index")
    else:
        form = SertifikaFormu(instance=sertifika)
    return render(request, "update.html", {"form": form})

@login_required(login_url="user:Giriş")
def delete (request ,id):
    sertifika = get_object_or_404(Sertifika,id=id)
    
    sertifika.delete()

    messages.success(request,"Sertifika Başarıyla Silindi")

    return redirect("index")