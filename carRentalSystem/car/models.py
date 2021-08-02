from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.core.validators import RegexValidator
fields = [
    ['Audi',
              'Audi'],
    ['Benz',
              'Benz'],
         ['Chevrolet',
              'Chevrolet'],
            ['Dodge',
              'Dodge'],
          ['Ford',
              'Ford'],
           ['Honda',
              'Honda'],
             ['Hyundai',
              'Hyundai'],
              ['Jaguar',
              'Jaguar'],
               ['Kia Motors',
              'Kia Motors'],
             ['Landrover',
              'Landrover'],
              ['Maruti Suzuki',
              'Maruti Suzuki'],
              ['Nissan',
              'Nissan'], ]

class Car(models.Model):
    # alphanumeric = RegexValidator(r'^[ a-zA-Z]*$', 'Only alphabets are allowed.')
    unique_id = models.CharField(max_length=10,unique=True)
    car_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    short_desc = models.CharField(max_length=100,default='')
    mileage=models.IntegerField(default=0)
    top_speed=models.IntegerField(default=0)
    category = models.CharField(max_length=50,choices=fields)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='car/images',default="")


    def __str__(self):
        return self.car_name


# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='')
    subject = models.CharField(max_length=100,default='')
    message = models.CharField(max_length=1000,default='')
    def __str__(self):
        return self.user.username

choice = [
        ['Cash On Delivery', 'Cash On Delivery'],

    ]


class Order(models.Model):
    order_id = models.CharField(max_length=15,default='')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE)
    email = models.EmailField()
    number = models.IntegerField(default=None)
    address = models.CharField(max_length=100,default='')
    city = models.CharField(max_length=50,default='')
    state = models.CharField(max_length=50,default='')
    zip_code = models.IntegerField(default=None)
    mode_of_delivery = models.CharField(max_length=50,choices=choice)
    ordered_date = models.DateTimeField(default=now, blank=True)
    no_of_days=models.IntegerField(default=1)
    total_amount=models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
class Tracker(models.Model):
    tracker_id = models.CharField(max_length=15, default='')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    location=models.CharField(max_length=50,default='')
    message=models.CharField(max_length=150,default='')
    def __str__(self):
        return self.user.username

