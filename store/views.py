from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
# Create your views here.
def home(request):
    return render(request, "store/index.html")


def collections(request):
    category = Category.objects.filter(status= 0)
    context = {
        'category': category,
    }
    return render(request,"store/collections.html",context)
def collectionsview(request,slug):
    if Category.objects.filter(slug=slug,status= 0):
        product = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {
            'product':product,
            'category':category,
        }
        return render(request,"store/products/index.html",context)
    else:
        messages.warning(request,"Không có sản phẩm nào")
        return redirect('collections')
    
def productview(request,cate_slug,prod_slug):
    if Category.objects.filter(slug=cate_slug,status= 0):
        if Product.objects.filter(slug=prod_slug,status=0):
            product = Product.objects.filter(slug=prod_slug,status=0).first()
            context = {'product':product}
        else:
            messages.error(request,"Không có sản phẩm")
            return redirect('collections')
    else:
        messages.error(request, "Không có tìm thấy danh mục")
        return redirect('collections')
    return render(request,"store/products/view.html",context)
