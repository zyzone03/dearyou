# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re
from django import forms
from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
#def min_length_validator(value):
#    if len(value) < 3:
#        raise forms.ValidationError('enter 3 or more char')
        
#def phone_validator(value):
#    number = ''.join(re.findall(r'\d+', value))
#    if not re.match(r'^01[016789]\d{7,8}$', number):
#        raise forms.ValidationError('enter a valid phone number')
        
#class PhoneField(models.CharField):
#    def __init__(self, *args, **kwargs):
#       kwargs.setdefault('max_length', 11)
#        super(PhoneField, self).__init__(*args, **kwargs)
#        self.validators.append(phone_validoator)

@python_2_unicode_compatible
class Member (models.Model):
    name = models.CharField(max_length = 100, 
#    validator=[min_length_validator], 
#    help_text='enter 100 or less',
    blank=True)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    address1 = models.CharField(max_length=100)
    
#no need     
    content = models.TextField(blank=True)
#    address2 = models.CharField()
#    address3 = models.CharField()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Letter (models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    sender_name = models.CharField(max_length=100,
#    help_text='Sender Name',
    blank=True)
    
    title=models.CharField(max_length=100,
#    help_text ='Letter Title',
    blank=True
    )
    
    content=models.TextField(null=False,
#    help_text ='Letter Content'
) 

    receiver_address=models.CharField(max_length=100,
#    help_text ='Receiver Address  metropolitan city / state',
    blank=True)

    receiver_name = models.CharField(max_length=100, blank=True)
#    help_text='Receiver Name',
    
#    receiver_address=receiver_address1+receiver_address2+receiver_address3
    
    def __str__(self):
        return self.sender_name
