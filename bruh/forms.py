from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, Textarea
from .models import CustomUser, Contact


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'is_staff', 'is_active',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'is_staff', 'is_active',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',)
        widgets = {
            'name': Textarea(attrs={'cols': 1,
                                    'rows': 1,
                                    'style': 'border-radius: 3px; resize:none;'}),
            'email': Textarea(attrs={'cols': 1,
                                    'rows': 1,
                                    'style': 'border-radius: 3px; resize:none;'}),
            'message': Textarea(attrs={'style': 'border-radius: 3px; height: 10em;'}),
        }
