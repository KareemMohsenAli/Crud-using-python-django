from django import forms
from category.models import Category
# from amazon1.models import products

# class PostForm(forms.Form):
#     name =forms.CharField(max_length=100)
#     description = forms.CharField(max_length=200)
#     image= forms.FileField()
#     price= forms.IntegerField()
#     category =forms.ModelChoiceField(Category.objects.all())
    
#     privacy = forms.ChoiceField(
#         choices=[('1', 'Public'), ('2', 'Private')])

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields='__all__'