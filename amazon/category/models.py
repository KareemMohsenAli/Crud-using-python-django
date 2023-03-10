from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    discription=models.TextField(null=True, blank=True)
    image=models.ImageField(null=True, blank=True ,upload_to='categories/images')

    def __str__(self):
        return self.name
    
    def get_image_url(self):
        return f"/media/{self.image}"
    
    def get_show_url(self):
        return reverse('ViewCategory',args={self.id})
    
    def get_edit_url(self):
        return reverse('UpdateCategory',args={self.id})
    
    def get_delete_url(self):
        return reverse('DeleteCategory',args={self.id})
    
    @classmethod
    def get_category(cls,id):
        try:
            category=cls.objects.get(pk=id)
            return category
        except  Exception as e:
            return None

