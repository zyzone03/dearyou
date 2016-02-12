from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.core.mail import send_mail
from django.shortcuts import resolve_url
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

def send_signup_confirm_email(request, user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = token_generator.make_token(user)

    context = {
        'user': user,
        'host': request.scheme + '://' + request.META['HTTP_HOST'],
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user),
    }

    subject = render_to_string('accounts/signup_confirm_subject.txt', context).splitlines()[0]
    body = render_to_string('accounts/signup_confirm_body.txt', context)
    to_email = [user.email]

    send_mail(subject, body, None, to_email, fail_silently=False)


class SignupForm(UserCreationForm):
    is_agree = forms.BooleanField(label='you have to agree', error_messages = {
        'required': 'you gotta agree',
        })
    class Meta(UserCreationForm.Meta):

        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email', None)
        if email:
            User = get_user_model()
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('this email already exists')
        return email


class LoginForm(AuthenticationForm):
    pass
    