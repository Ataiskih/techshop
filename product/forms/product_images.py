from django import forms
from product.models.product_images import Images


class ImageForm(forms.ModelForm):
    image = forms.ImageField()
    model = Images

    class Meta:
        fields = ('image', )
