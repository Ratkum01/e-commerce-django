from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    items= Product.objects.all()
    context={
        'items':items
    }
    return render(request, 'myapp/index.html', context)
def contact(request):
    return render(request, 'myapp/contacts.html')
def show_product(request, prod_id):
    item=Product.objects.get(id=prod_id)
    context={
        'item': item
    }
    return render(request,'myapp/show_product.html',context  )
