from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='Shophome'),
    path('about/',views.about,name='AboutUs'),
    path('contact/',views.contact,name='ContactUs'),
    path('tracker/',views.tracker,name='TrackerStatus'),
    path('search/',views.search,name='ContactUs'),
    path("products/<int:myid>",views.prodview,name='ProductView'),
    path('checkout/',views.checkout,name='CheckOut'),
    path('orderplaced/',views.orderplaced,name='OrderpPlaced'),
    path('login/',views.login,name='Login'),
    path('success/',views.success,name='successfull'),
]