from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def Login(request):
    error = ""
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pwd']
        user = authenticate(username=username, password=password)
        try:
            if user.is_staff:
                login(request,user)
                error = "No"
                return redirect('home')
            else:
                error = "yes"
        except:
            error = "Yes"
    d = {'error' : error}
    return render(request,'login.html',d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def Add_Enquiry(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        emailid = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        try:
            Enquiry.objects.create(name=name, contact=contact, emailid=emailid, age=age, gender=gender)
            error = "No"
        except:
            error = "Yes"
    d = {'error':error}
    return render(request, 'add_enquiry.html', d)


def View_Enquiry(request):
    if not request.user.is_staff:
        return redirect('login')
    enq = Enquiry.objects.all()
    d = {'enq': enq}
    return render(request, 'view_enquiry.html', d)

def Delete_Enquiry(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    enquiry = Enquiry.objects.get(id=pid)
    enquiry.delete()
    return redirect('view_enquiry')

def Add_Plan(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        name = request.POST['name']
        amount = request.POST['amount']
        duration = request.POST['duration']
        try:
            Plan.objects.create(name=name, amount=amount, duration=duration)
            error = "No"
        except:
            error = "Yes"
    d = {'error': error}
    return render(request, 'add_plan.html', d)


def View_Plan(request):
    if not request.user.is_staff:
        return redirect('login')
    plan = Plan.objects.all()
    d = {'plan': plan}
    return render(request, 'view_plan.html', d)

def Delete_Plan(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    plan = Plan.objects.get(id=pid)
    plan.delete()
    return redirect('view_plan')

def Add_Equipment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        unit = request.POST['unit']
        date = request.POST['date']
        description = request.POST['description']
        try:
            Equipment.objects.create(name=name, price=price, unit=unit, date=date, description=description)
            error = "No"
        except:
            error = "Yes"
    d = {'error':error}
    return render(request, 'add_equipment.html', d)

def View_Equipment(request):
    if not request.user.is_staff:
        return redirect('login')
    equipment = Equipment.objects.all()
    d = {'equipment': equipment}
    return render(request, 'view-equipment.html', d)

def Delete_Equipment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    equipment = Equipment.objects.get(id=pid)
    equipment.delete()
    return redirect('view_equipment')
