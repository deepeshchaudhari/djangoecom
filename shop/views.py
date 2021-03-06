from math import ceil
from django.shortcuts import render
from django.http import HttpResponse

# import models or database
from .models import Product,Contact,Order,Customer
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
    if request.method == "POST":
        items_json = request.POST.get('itemsJson','its item json')
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        address = request.POST.get('add1', '') + " " + request.POST.get('add2', '')
        country = request.POST.get('country', 'India')
        state = request.POST.get('state', 'UP')
        zip_code = request.POST.get('state','')
        phone1 = request.POST.get('contact','')
        phone2 = request.POST.get('contact2','0000000000')
        order = Order(items_json=items_json,firstname=firstname,lastname=lastname,
                      username=username, email=email,address=address,country=country,
                      state=state,Zip_code=zip_code,phone1=phone1,phone2=phone2)
        print(order.save())
        thank = True
        id = order.order_id
        return render(request,'shop/orderplaced.html',{'thank':thank, 'id': id})
    return render(request,'shop/checkout.html')
def orderplaced(request):
    return render(request,'shop/orderplaced.html')
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if Customer.objects.filter(email=email,password= password):
            id = Customer.objects.filter(email=email,password= password).values('customer_id')
            status = 'logged in'
            print(status)
            return render(request,'shop/success.html',{'status':status,'id': id})
        else:
            status='wrong credentials'
            return render(request,'shop/success.html',{'status':status})
    return render(request,'shop/login.html')

def success(request):
    render(request,'shop/success.html')