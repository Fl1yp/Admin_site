from django import forms
from .models import Contact  # Убедитесь, что у вас есть правильный импорт модели

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'number', 'message']  # Укажите поля, которые хотите использовать
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'number': forms.TextInput(attrs={'placeholder': '+79999999999'}),
            'message': forms.TextInput(attrs={'placeholder': 'Дополнительная информация'}),
        }
        labels = {
            'name': '',
            'number': '',
            'message': '',
        }
