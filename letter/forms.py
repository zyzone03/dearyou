from django import forms
from django.forms import Textarea
from letter.models import Letter, Contact

class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = '__all__'
        exclude = ('author',)
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        
class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args,**kwargs)
        self.fields['message'].label=""

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'message': Textarea(attrs={'cols': 80, 'rows': 10, 'placeholder':'write a message'}),
        }

