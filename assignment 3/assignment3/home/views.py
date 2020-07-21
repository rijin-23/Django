from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def home(request):
    return render(request,'home.html')

def store_data(request):
    user_name = request.POST['user_name']
    password = request.POST['password']
    phone_no = request.POST['phn_no']
    address = request.POST['address']
    s1 = models.Information(user_name=user_name,password=password,phone_number=phone_no,address=address)
    s1.save()
    return render(request,'final.html')