from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

from .models import Car,Contact,Order,fields,Tracker
import pyttsx3

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def Reset(request):
    return render(request,'car/reset.html',{'category':'Reset Password'})

def Subreset(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        try:
            user = User.objects.get(username=username)
        except:
            user=None

        if user is None:
            speak('please check your username')
            return render(request,'car/reset.html')
        elif password1==password2 and user.email==email:
            user.set_password(password1)
            user.save()
            auth_login(request,user)
            wish='Password reset successful'
            speak(wish)
            return redirect('home')
        elif password1 != password2:
            speak('mismatched password')
            return redirect('reset')
        else:
            speak("mismatched username and email")
            return redirect('reset')

    return HttpResponse('success')

def index(request):
    allProds = []
    car = Car.objects.all()
    for i in car:
        allProds.append(i.unique_id)

    track = Tracker.objects.all()
    t = []
    all = []

    for i in track:
        t.append(i.tracker_id)

    for i in allProds:
        if i not in t:
            all.append(Car.objects.get(unique_id=i))


    category='Welcome To GoIndia'
    params = {'allProds': all,
              'fields':fields,
              'category':category}
    return render(request, 'car/gallery.html', params)


def login(request):
    return render(request, 'car/login.html')
def Signup(request):
    if request.method == 'POST':
        username=request.POST['username1']
        first_name=request.POST['name1']
        last_name=request.POST['name2']
        email=request.POST['email1']
        password=request.POST['password1']
        user = User.objects.all()
        allUsers=[]
        for i in user:
            allUsers.append(i.username)
        if username in allUsers:
            speak('This username already exists')
            return render(request, 'car/login.html')
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = first_name
            myuser.last_name = last_name
            myuser.save()
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            wish = 'welcome to Go India '
            speak(wish)
            return index(request)
def Signin(request):
    if request.method=='POST':
        username=request.POST['log_username']
        password=request.POST['log_password']
        user = authenticate(username=username, password=password)

        if user is None:
            speak('please check your username or password')
            return render(request,'car/login.html')
        else:
            auth_login(request,user)
            wish='Happy to see you again '
            speak(wish)
            return redirect('home')

def Logout(request):
    logout(request)
    speak('you have been successfully logged out, see you again')
    return render(request, 'car/index.html')
def Contacts(request):
   try:
       if request.method == 'POST':
           name = request.POST['name']
           email = request.POST['email']
           subject = request.POST['subject']
           message = request.POST['message']
           contact = Contact(email=email, user=request.user, name=name, subject=subject, message=message)
           contact.save()
           speak('your message has received successfully')
           return index(request)
       else:
           speak('please log in before sending message')
           return login(request)
   except:
       speak('please log in before sending message')
       return login(request)
def Orders(request):
    if request.method=='POST':
        car_id = request.POST['car_id']
        car = Car.objects.get(unique_id=car_id)
        params = {'user': request.user,
                  'car': car,
                  'category':car}
        return render(request,'car/order.html',params)
def placeOrder(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car = Car.objects.all()
        for i in car:
            if i.unique_id == car_id:
                break
        user=request.user
        number=request.POST['number']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        zip_code=request.POST['zip_code']
        mode_of_delivery=request.POST['mode_of_delivery']
        price=request.POST['price']
        no_of_days=request.POST['no_of_days']
        order=Order(order_id=i.unique_id,user=request.user,car=i,email=user.email,number=number,
                    address=address,city=city,state=state,zip_code=zip_code,mode_of_delivery=mode_of_delivery,no_of_days=no_of_days
                    ,total_amount=int(no_of_days)*int(price))
        order.save()
        tracker=Tracker(tracker_id=order.order_id,user=user,car=i,order=order)
        tracker.save()
        speak('booking successful , your car is on the way')
        return redirect('home')

def Category(request):
    if request.method=='POST':
        allProds=[]
        car= Car.objects.all()
        category=request.POST['category']
        for i in car:
            if i.category==category:
                allProds.append(i.unique_id)

        track = Tracker.objects.all()
        t = []
        all = []

        for i in track:
            t.append(i.tracker_id)
        for i in allProds:
            if i not in t:
                all.append(Car.objects.get(unique_id=i))
        params = {'allProds': all,
                  'fields': fields,
                  'category':category}
        return render(request, 'car/gallery.html', params)

def Track(request):
        tracker=Tracker.objects.all()
        allTrack=[]
        for i in tracker:
            if i.user==request.user:
                allTrack.append(i)
        if len(allTrack)<1 :
            params = {'user': request.user,
                      'tracker': allTrack,
                      'category': 'Tracker Is Empty'}
        else:
            params = {'user': request.user,
                      'tracker': allTrack,
                      'category': 'Track Your Orders'}

        return render(request,'car/tracker.html',params)
def Cancelorder(request):
    if request.method=='POST':
        car_id=request.POST['car_id']
        tracker=Tracker.objects.get(tracker_id=car_id)
        order=Order.objects.get(order_id=car_id)
        tracker.delete()
        order.delete()
        speak('sad to say , your booking is cancelled ')
        return redirect('home')
