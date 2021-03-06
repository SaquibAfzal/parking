from telnetlib import AUTHENTICATION
import time
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib.messages import constants as messages
from home.models import parkingSpots
import datetime

# Create your views here.


def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
        # Do something for authenticated users.
    return render(request, 'index.html')
    # Do something for anonymous users.


def search(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
        # Do something for authenticated users.
    return render(request, 'search.html')


def display(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
        # Do something for authenticated users.
    return render(request, 'display.html')


def details(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
        # Do something for authenticated users.
    return render(request, 'details.html')


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('/login')


def search(request):
    req = None
    message = ""
    k = False
    if request.method == 'POST':
        ownername = request.POST.get('ownername')
        vno = request.POST.get('vno')
        if parkingSpots.objects.filter(vehicle_no=vno):
            req = parkingSpots.objects.get(vehicle_no=vno)
        if req == None:
            message = "Vehicle not found"
            k = False
        else:
            message = "Vehicle found!!"
            k = True

    return render(request, 'search.html', {'req': req, 'message': message, 'flag': k})


def display(request):
    p1 = None
    vac = "VACANT"
    p1 = parkingSpots.objects.all()[0]
    p2 = parkingSpots.objects.all()[1]
    p3 = parkingSpots.objects.all()[2]
    p4 = parkingSpots.objects.all()[3]
    p5 = parkingSpots.objects.all()[4]
    p6 = parkingSpots.objects.all()[5]
    p7 = parkingSpots.objects.all()[6]
    p8 = parkingSpots.objects.all()[7]
    p9 = parkingSpots.objects.all()[8]
    p10 = parkingSpots.objects.all()[9]
    p11 = parkingSpots.objects.all()[10]
    p12 = parkingSpots.objects.all()[11]
    return render(request, 'display.html', {'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4, 'p5': p5, 'p6': p6, 'p7': p7, 'p8': p8, 'p9': p9, 'p10': p10, 'p11': p11, 'p12': p12, 'vac': vac})


def exit(request):
    message = ""
    req = None
    k = False
    o_name = ""
    v_number = ""
    v_type = ""
    r_no = 0
    p_no = 0
    intiming = None
    inepoch = 0
    outtiming = None
    outepoch = 0
    timespent = 0
    charges = 0
    if request.method == 'POST':
        ownername = request.POST.get('ownername')
        vno = request.POST.get('vno')
        if parkingSpots.objects.filter(vehicle_no=vno):
            req = parkingSpots.objects.get(vehicle_no=vno)
        if req == None:
            message = "Vehicle was not found in the parking lot"
            k = False
        else:
            message = "Vehicle found!!"
            k = True
            o_name = req.owner_name
            v_number = req.vehicle_no
            v_type = req.vehicle_type
            r_no = req.row_no
            p_no = req.pos_no
            intiming = req.in_time
            inepoch = req.in_epoch
            outtiming = datetime.datetime.now().time()
            outepoch = time.time()
            timespent = outepoch-inepoch
            charges = round((timespent/60))
            parkingSpots.objects.filter(vehicle_no=vno).update(
                vehicle_no=0, vehicle_type="", owner_name="", occupancy=0, in_time=datetime.datetime.now().time(), in_epoch=0)

    return render(request, 'exit.html', {'message': message, 'flag': k, 'rate': "Parking rate is Rs. 60 per hour", 'oname': o_name, 'v_number': v_number, 'v_type': v_type, 'r_no': r_no, 'p_no': p_no, 'intiming': intiming, 'outtiming': outtiming, 'charges': charges})


def entry(request):
    message = ""
    k = None
    if request.method == 'POST':
        ownername = request.POST.get('ownername')
        vno = request.POST.get('vno')
        vtype = request.POST.get('vtype')
        rno = request.POST.get('rno')
        pno = request.POST.get('pno')
        if (parkingSpots.objects.get(row_no=rno, pos_no=pno).occupancy == 0):
            parkingSpots.objects.filter(row_no=rno, pos_no=pno).update(
                vehicle_no=vno, vehicle_type=vtype, owner_name=ownername, occupancy=1, in_time=datetime.datetime.now().time(), in_epoch=time.time())
            message = "Vehicle Parked"
            k = 1
        else:
            message = "Parking Spot is occupied"
            k = 0
    return render(request, 'entry.html', {'message': message, 'k': k})
