from django import forms

class GirişForm(forms.Form):
    kullanıcıadı=forms.CharField(max_length=50,label="Kullanıcı Adı")
    parola =forms.CharField(max_length=20, label ="Parola",widget = forms.PasswordInput)


class KayıtForm(forms.Form):
    Kullanici_Adi = forms.CharField(max_length=50, label="Kullanıcı Adı")
    Parola = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)
    Onaylama = forms.CharField(max_length=20, label="Parola Doğrula", widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        Kullanici_Adi = cleaned_data.get("Kullanıcı Adı")
        Parola = cleaned_data.get("Parola")
        Onaylama = cleaned_data.get("Onaylama")

        if Parola and Onaylama and Parola != Onaylama:
            raise forms.ValidationError("Parolalar Eşleşmiyor")
        
        return cleaned_data
