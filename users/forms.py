from django  import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','password1','password2']

        widgets = {
            "email":forms.TextInput(attrs={'class':'form-control'}),
            "password1":forms.TextInput(attrs={'class':'form-control'}),
            "password2":forms.TextInput(attrs={'class':'form-control'})
        }
