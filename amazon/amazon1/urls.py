from django.urls import path
from amazon1.views import productss,welcomeview,showproducts,about,contact,deletepost,create,editproduct

urlpatterns = [
    path('pros',productss, name='products'),
    path('show/<int:id>', showproducts, name='showproducts'),
    path('about', about, name='about'),
    path('contact', contact, name='contactus'),
    path('welcome/<name>', welcomeview, name='welcome'),
    path('delete/<int:id>', deletepost, name='delete'),
    path('create',create,name='create'),
    path('editproduct/<int:id>', editproduct, name='editproduct')
] 