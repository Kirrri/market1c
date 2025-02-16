from django import forms
from .models import LegalEntity

class LegalEntityForm(forms.ModelForm):
    class Meta:
        model = LegalEntity
        fields = ['inn', 'organization_name', 'ownership_form', 'phone', 'address']
        widgets = {
            'inn': forms.TextInput(attrs={'placeholder': 'Введите ИНН'}),
            'organization_name': forms.TextInput(attrs={'placeholder': 'Введите наименование организации'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Введите телефон'}),
            'address': forms.TextInput(attrs={'placeholder': 'Введите адрес'}),
        }