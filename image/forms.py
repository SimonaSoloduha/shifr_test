from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image')


class HexForm(forms.Form):
    hex_number = forms.CharField(label='HEX number', max_length=6, min_length=6)
