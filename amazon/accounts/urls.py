from django.urls import path,include
# from category.views import AllCategories,CreateCategory,ViewCategory,UpdateCategory,DeleteCategory
from accounts.views import RegisterUser,ProfileView



urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('register',RegisterUser.as_view(),name='regitser'),
    path('profile/',ProfileView.as_view(),name='ProfileView')

] 