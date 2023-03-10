from django.db import models
from django.shortcuts import reverse,get_list_or_404

from category.models import Category


# Create your models here.
   ########################relation one(category) to many(product)########################
     ####label name ,price#####
class NewProducts(models.Model):
    name = models.CharField(max_length=100,null=True )
    price=models.IntegerField()
    description = models.CharField(max_length=100,null=True)
    privacy=models.CharField(max_length=2,choices=[('1','public'),('2','private')],null=True)
    image = models.ImageField(upload_to='photos/images')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,related_name='category_products')

# class Products(models.Model):
#     ####label name ,price#####
#     name = models.CharField(max_length=100,null=True )
#     price=models.IntegerField()
#     description = models.CharField(max_length=100,null=True)
#     privacy=models.CharField(max_length=2,choices=[('1','public'),('2','private')],null=True)
#     image = models.ImageField(upload_to='photos/images')
#     ########################relation one(category) to many(product)########################
#     category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,related_name='category_products')

    def __str__(self):
        return self.name
    
    def get_image_url(self):
        return f"/media/{self.image}"
    
    def get_show_url(self):
        return reverse('showproducts',args={self.id})
    
    def get_edit_url(self):
        return reverse('editproduct',args={self.id})
    
    def get_delete_url(self):
        return reverse('delete',args={self.id})
    
    @classmethod
    def get_all_products(cls):
        return cls.objects.all()
    


    
   

