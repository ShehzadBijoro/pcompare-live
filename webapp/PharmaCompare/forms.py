from django import forms
from django import forms
from django.forms import ModelForm

from .models import Generic
from django.contrib.auth.forms import UserCreationForm



class CreateGenForm(forms.ModelForm):

    class Meta:
        model = Generic
        fields = (
            "__all__"
        )