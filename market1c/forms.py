from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Имя пользователя",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'E-mail'
        }))
    first_name = forms.CharField(max_length=30, required=False, 
        label="Имя пользователя",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Имя'
        }))
    last_name = forms.CharField(max_length=30, required=False,
        label="Имя пользователя",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Фамилия'
        }))
    middle_name = forms.CharField(max_length=30, required=True, label="Имя пользователя",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Отчество'
        }))
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )
    password2 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Подтвердить Password'
        })
    )
    accept_terms = forms.BooleanField(required=False, label="Я являюсь юридическим лицом",
    widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'checkbox'
        })
    )
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'middle_name', 'password1', 'password2', 'accept_terms')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = "legal" if self.cleaned_data.get("accept_terms") else "individual"
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'E-mail'
        })
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )
