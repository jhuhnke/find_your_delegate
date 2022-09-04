from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import Delegate

class findDelegate(ModelForm): 
    class Meta: 
        model = Delegate
        fields = ('vote_frequency', 'tags')

