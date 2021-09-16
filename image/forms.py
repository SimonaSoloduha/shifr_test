from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image')

    def clean(self):
        cleaned_data = super(ImageForm, self).clean()
        image = cleaned_data.get('image')
        image_format = image.content_type.split('/')[1]
        if image_format not in ('jpeg', 'jpg'):
            msg = 'Загрузите файл формата jpg'
            self.add_error('image', msg)


class HexForm(forms.Form):
    hex_number = forms.CharField(label='HEX number', max_length=6, min_length=6)
