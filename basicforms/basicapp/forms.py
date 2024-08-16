from django import forms
from basicapp.models import UserProfileInfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    # password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class' : "form-control", 'placeholder' : "Password"}))

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

        labels = {
            'username': '',
            'email': '',
            'password' : '',
        }

        widgets = {
            'username' : forms.TextInput(attrs={'class' : "form-control", 'placeholder' : "Username"}),
            'email' : forms.EmailInput(attrs={'class' : "form-control", 'placeholder' : "user@gmail.com"}),
            'password' : forms.PasswordInput(attrs={'class' : "form-control", 'placeholder' : "Password"}),
        }

        help_texts = {
            'username': '',
            'email': '',
            'password' : '',
        }

        error_messages = {
            'username': {
                'max_length': "This username is too long.",
            },
            'email': {
                'invalid': "Enter a valid email address.",
            },
        }


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

        labels = {
            'portfolio_site': '',
            'profile_pic': '',
        }

        widgets = {
            'portfolio_site': forms.URLInput(attrs={'class': "form-control", 'placeholder': "Portfolio Site URL"}),
            'profile_pic': forms.FileInput(attrs={'class': "form-control"}),
        }

        help_texts = {
            'portfolio_site': '',
            'profile_pic': '',
        }
