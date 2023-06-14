from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import PresenceModel

class PresenceForm(forms.ModelForm):
    student_name = forms.CharField(max_length=100)
    professor_name = forms.CharField(max_length=100)

    class Meta:
        model = PresenceModel
        fields = ['student_name', 'professor_name']