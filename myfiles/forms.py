from django import forms

from .models import Sotib_olinganlar

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Sotib_olinganlar
        exclude = ['product']
        fields = '__all__'