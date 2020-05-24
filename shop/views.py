from math import ceil

from django.shortcuts import render
from django.http import HttpResponse

# import models or database
from .models import Product,Contact
# Create your views here.
def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides= ceil(n/4)
        allProds.append([prod, range(1, nslides), nslides])
    params = {'allProds': allProds}
    return render(request,'shop/index.html',params)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname','')
        lastname = request.POST.get('lastname','')
        email= request.POST.get('email','')
        phone= request.POST.get('contact','')
        username= request.POST.get('username','')
        address= request.POST.get('address','')
        contact= Contact(firstname=firstname,lastname=lastname,email=email,contact=phone,username=username,address=address)
        contact.save()
    return render(request,'shop/contact.html')
def tracker(request):
    return render(request,'shop/tracker.html')
def search(request):
    return render(request, 'shop/search.html')
def prodview(request,myid):
    product = Product.objects.filter(id=myid)
    # product is a list so product[0] in dictionary
    params={'product':product[0]}
    return render(request,'shop/prodView.html',params)
def checkout(request):
    return render(request,'shop/checkout.html')
