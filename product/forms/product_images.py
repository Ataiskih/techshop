from django import forms
from product.models.product_images import Images


class ImageForm(forms.ModelForm):
    image = forms.ImageField()
    
    class Meta:
        model = Images
        fields = ('image', )