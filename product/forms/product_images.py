from django import forms
from product.models.product_images import Images


class ImageForm(forms.ModelForm):
    image = forms.ImageField()
    model = Images

    # def __init__(self, *args, **kwargs):
    #     super(ImageForm, self).__init__(*args, **kwargs)
    
    #     if 'instance' in kwargs:
    #         images = kwargs['instance']

    class Meta:
        fields = ('image', )
