from django.urls import path,include
from .import views
urlpatterns=[
    path('',views.home,name='home'),
    path('<slug:c_slug>/', views.home, name='prodt_cat'),
    path('<slug:c_slug>/<slug:product_slug>', views.proddetail, name='details'),
    path('search',views.searching,name='search'),
    path('buy',views.buy,name='buy'),
    path('contact',views.contact,name='contact')

]