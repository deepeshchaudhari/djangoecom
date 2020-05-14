from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'shop/index.html')
def about(request):
    return HttpResponse("WE ARE AT ABOUT")
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
