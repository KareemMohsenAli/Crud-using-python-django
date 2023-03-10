from django.urls import path
from category.views import AllCategories,CreateCategory,ViewCategory,UpdateCategory,DeleteCategory
#######################################authorization in class based on only urls not as decorator on function
from django.contrib.auth.decorators import login_required


urlpatterns = [
    
    path('listcat',AllCategories.as_view(), name='Categories'),
    path('create',CreateCategory.as_view(), name='CreateCategory'),
    ####################you must write pk as primary key when using 
    path('<int:pk>',ViewCategory.as_view(), name='ViewCategory'),
    path('editcat/<int:pk>',login_required(UpdateCategory.as_view()), name='UpdateCategory'),
    path('delete/<int:pk>',login_required(DeleteCategory.as_view()), name='DeleteCategory')

    # path('show/<int:id>', showproducts, name='showproducts'),
    # path('about', about, name='about'),
    # path('contact', contact, name='contactus'),
    # path('welcome/<name>', welcomeview, name='welcome'),
    # path('delete/<int:id>', deletepost, name='delete'),
    # path('create',create,name='create'),
    # path('editproduct/<int:id>', editproduct, name='editproduct')
] 