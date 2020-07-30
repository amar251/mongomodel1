from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import MyModel


def index(request):
    return render(request,'loginapp/index.html')


def login(request):
    return render(request,'loginapp/login.html')

def create_user(request):
    if request.method=='POST':
        name=request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        down_letter_array = request.POST['a']
        press_time_array = request.POST['b']
        down_time = request.POST['c']
        up_time = request.POST['d']
        up_letter_array = request.POST['e']


        MyModel.objects.create(
            name=name,
            email=email,
            password=password,
            down_letter_array=down_letter_array,
            press_time_array = press_time_array,
            down_time = down_time,
            up_time = up_time,
            up_letter_array = up_letter_array

        )
        return HttpResponse('')




