from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

class SignupForm(UserCreationForm):
    is_agree = forms.BooleanField(label='you have to agree', error_messages = {
        'required': 'you gotta agree',
        })
    class Meta(UserCreationForm.Meta):
#        fields = ['username', 'email']
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email', None)
        if email:
            User = get_user_model()
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('email exists')
        return email


class SignupForm2(UserCreationForm):
    email = forms.EmailField()
    is_agree = forms.BooleanField(label='agree to thin11122', error_messages = {
        'required': 'you gotta agree',
        })

    def save(self, commit=True):
        user = super(SignupForm2, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    pass
    