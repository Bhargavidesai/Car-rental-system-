from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from . models import Car
admin.site.register(Car)
from . models import Contact
admin.site.register(Contact)
from . models import Order
admin.site.register(Order)
from . models import Tracker
admin.site.register(Tracker)
