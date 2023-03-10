from django.shortcuts import render,redirect
from django.views import View
from category.models import Category
from category.form import CategoryModelForm

from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.
#################################################list all categories################################33333
# class AllCategories(View):
#     def get(self,request):
#         cat=Category.objects.all()
#         return render(request,'listcat.html',context={'category':cat })
    
#########################################another way###############################
class AllCategories(ListView):
#######################5od el data eli gayalak we 7otha fil template eli emsha template_name################
        model=Category
        template_name='listcat.html'
        
################################################################################################################3


############################################Create a new category####################################################
# class CreateCategory(View):
#     def get(self,request):
#         form=CategoryModelForm()
#         return render(request, 'createcat.html',context={'form':form})
    
#     def post(self,request):
#         form=CategoryModelForm(request.POST,request.FILES)
#         if form.is_valid(): 
#             form.save()
#             return redirect('Categories')
#         return render('Categories')
#########################################another way###############################
class CreateCategory(CreateView):
        model = Category
        template_name='createcat.html'
        form_class = CategoryModelForm
        success_url='listcat'
    
#########################################################################################
#################################view########################################################
class ViewCategory(DetailView):
        ###################lazem ab3t el id men 5elal el url (pk)################
    model = Category
    template_name='viewcat.html'
 ########################################################################################
 # ###########################################################update category####################################

class UpdateCategory(UpdateView):
    model = Category
    template_name='editcat.html'
    form_class = CategoryModelForm
    success_url='/category/listcat'
############ /category/ => bayrg3 5atwa######

###############################################################################################333
###############################delete################################################################333

class DeleteCategory(DeleteView):
    model = Category
    template_name='delete.html'
    success_url='/category/listcat'
      
 


