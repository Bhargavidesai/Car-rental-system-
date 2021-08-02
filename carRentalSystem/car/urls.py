"""carRentalSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('login/',views.login,name="login"),
    path('signup/',views.Signup,name='signup'),
    path('signin/',views.Signin,name='signin'),
    path('contact/',views.Contacts,name='contact'),
    path('logout/',views.Logout,name='logout'),
    path('order/',views.Orders,name='order'),
    path('orderCar/',views.placeOrder,name='orderCar'),
    path('category/',views.Category,name='category'),
    path('tracker/',views.Track,name='tracker'),
    path('co/',views.Cancelorder,name='co'),
    path('reset/',views.Reset,name='reset'),
    path('subreset/',views.Subreset,name='subreset'),
]


