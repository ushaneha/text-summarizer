from django import forms
from .models import UploadedText

class TextUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedText
        fields = ['text']
