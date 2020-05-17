from math import ceil

from django.shortcuts import render
from django.http import HttpResponse

# import models or database
from .models import Product
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
    return HttpResponse("WE ARE AT CONTACT")
def tracker(request):
    return HttpResponse("WE ARE AT TRACKER")
def search(request):
    return HttpResponse("WE ARE AT SEARCH")
def prodview(request):
    return HttpResponse("WE ARE AT PRODUCT VIEW")
def checkout(request):
    return HttpResponse("WE ARE AT CHEKOUT")
