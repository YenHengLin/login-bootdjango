from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def loginUser(request):
    return render(request,'login/login.html')