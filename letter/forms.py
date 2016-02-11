from django import forms
from letter.models import Letter

class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = '__all__'
        