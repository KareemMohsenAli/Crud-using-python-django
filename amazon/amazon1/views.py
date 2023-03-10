from django.shortcuts import render,get_list_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from amazon1.models import NewProducts
from category.models import Category
from amazon1.form import PostForm,PostModelForm

# list = [
#     {'id': 1,'name': 'watch','price': 1000,'description': 'watch is the best watch','image':'first.png'},
#     {'id': 2,'name': 'clock','price': 2000,'description': 'clock is the best clock','image':'second.png'},
#     {'id': 3,'name': 'airpods','price': 3000,'description': 'airpods is the best airpods','image':'third.png'},
#     {'id': 3,'name': 'headphone','price': 4000,'description': 'headphone is the best headphone','image':'first.png'},
#     {'id': 3,'name': 'gloves','price': 5000,'description': 'gloves is the best gloves',}]


def productss(request):
    allProducts =NewProducts.get_all_products
    return render(request, 'products.html',context={'list':allProducts})


def showproducts(request,id):
    allProducts=NewProducts.objects.get(id=id)
    # allProducts=get_list_or_404(products,pk=id)
    if allProducts: 
        return render(request, 'viewProduct.html',context={'list':allProducts})
    
@login_required   
def deletepost(request,id):
    allProducts=NewProducts.objects.get(id=id)
    # allProducts=get_list_or_404(products,pk=id)
    allProducts.delete()
    return redirect('products')

def welcomeview(request,name):
    return HttpResponse(f"<h1 style='color:red ; text-align:center'>Welcome {name}!</h1>")

def about(request):
     return render(request, 'about.html')
def contact(request):
     return render(request, 'contact.html')

def create(request):
    print(request)
    if request.method == 'GET':
        # cat=Category.objects.all()
        # return render(request, 'create.html',context={'cat':cat})
        # postform=PostForm()
        postform=PostModelForm()
        return render(request, 'create.html',context={'form':postform})
    
    elif request.method == 'POST':
        postform=PostModelForm(request.POST,request.FILES)
        postform.save()
        return redirect('products')

        #########################################this way for normal dijango form
        # p=products()
        # p.name = request.POST['name']
        # p.description = request.POST['description'] 
        # p.price = request.POST['price']
        # p.privacy = request.POST['privacy']
        # if 'category' in request.POST:
        #     category=Category.get_category(request.POST['category'])
        #     p.category=category
        # if request.FILES:
        #     p.image = request.FILES['image'] 
        # p.save()
        # return redirect('products')
@login_required   
def editproduct(request,id):
    p = NewProducts.objects.get(id=id)
    if request.method == 'GET':
        postform=PostModelForm(instance=p)
        return render(request, 'editForm.html',context={'form':postform})
    
    if request.method=='POST':
        postform = PostModelForm( request.POST, request.FILES, instance=p)
        if postform.is_valid():
            postform.save()
            return redirect(p.get_show_url())


        # return redirect('products')
    

    
    
   
