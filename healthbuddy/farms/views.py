from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from geopy.geocoders import Nominatim

#form imports
from farms.models import *
# from farms.utils import get_geo, get_center_coordinates, get_zoom

# Create your views here.
def index(request):
    return render(request, 'farms/index.html')

#TODO: Might need to make the form in another view and use the login as changing the page
def loginPage(request):
    context = {}
    return render(request, 'farms/login.html', context)

def loginUser(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            print("loginPage view - " + username + " logged in")
            #redirect user to profile page or somewhere
            return render(request, 'farms/userProfile.html',context)
        else:
            messages.info(request, "Username OR password is incorrect")
            # return render(request, 'farms/login.html', context)
            return render(request, 'farms/login.html', context)
    return render(request, 'farms/login.html', context)

def logoutUser(request):
    logout(request)
    print("logoutUser view - user logout")
    return render(request, "farms/index.html")

def registerUser(request):
    context = {}
    form = RegisterUser()
    #check whether the form method is POST if not don't allow saving for security reasons
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        #(backend) check whether the form is valid or not
        if form.is_valid():
            form.save()
            print("register view.py - User is registered!")
            context = {'form':form}
            return render(request, 'farms/userProfile.html', context)
        else:
            messages.info(request, "An Error Occured! Account Has NOT Been Created.")
    #object to use backend data in html page
    context = {'form':form}
    return render(request, "farms/register.html", context)

#TODO: Might need to make the form in another view and use the register as changing the page
def registerPage(request):
    form = RegisterUser()
    context = {'form':form}
    #renders html file and sends context info to html page
    return render(request, 'farms/register.html', context)

def updateProfile(request):
    if request.method == "POST":
        usertype = request.POST.get('userType')
        print("userType updateProfile view - ", usertype)
        city = request.POST.get('city')
        experience = request.POST.get('experience')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        communication = request.POST.get('communication')
        if usertype == "Personal Trainer":
            form = Trainer(user=request.user, city=city, experience=experience, age=age, gender=gender, communication=communication)
            form.save()
            print("form saved and Trainer is:", Trainer)
        elif usertype == "Babysitter":
            form = Babysitter(user=request.user, city=city, experience=experience, age=age, gender=gender, communication=communication)
            form.save()
        elif usertype == "Gym Buddy":
            form = GymMember(user=request.user, city=city, age=age, gender=gender, communication=communication)
            form.save()
    return render(request, 'farms/userProfile.html')

def userProfile(request):
    username = request.user
    trainer = Trainer.objects.get(user=username)
    city = trainer.city
    context = {'username':username, 'city':city}
    if city != None:
        print("userProfile view - username: ", username, " city: ", city)
    else:
        print("username view is - ", username)
    return render(request, 'farms/userProfile.html')