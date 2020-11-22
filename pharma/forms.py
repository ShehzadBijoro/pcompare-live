from django import forms

from .models import *




class CreateGenForm(forms.ModelForm):

    class Meta:
        model = Generic
        fields = (
            "__all__"
        )

class CreateDrugForm(forms.ModelForm):

    class Meta:
        model = Drug
        fields = (
            "__all__"
        )
class CreateItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = (
            "__all__"
        )