from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label    ="Kullanıcı Adı")
    password = forms.CharField(label    = "Şifre", widget=forms.PasswordInput)



class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanıcı Adı")
    password = forms.CharField(max_length=20,label="Şifre",widget=forms.PasswordInput)
    confirm  = forms.CharField(max_length=20,label="Şifre Doğrula",widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        confirm = self.cleaned_data["confirm"]

        if password and confirm and password != confirm :
            raise forms.ValidationError("Şifreler Uyuşmuyor")

        values = {

            "username" : username,
            "password" : password
            
        }
        return values
