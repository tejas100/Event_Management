from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                 'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Password'
            }
        )
    )



class SignUpForm(UserCreationForm):
   username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Username'
            }
        )
    )
   password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Password'
            }
        )
    )
   password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Confirm Password'
            }
        )
    )
   email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Email'
            }
        )
    )

   class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_customer')