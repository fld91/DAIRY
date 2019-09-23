from django.http import HttpResponse
from django.shortcuts import render

def page(request):
    return render(request, 'login1.html')


def admin(request):
    return render(request, 'admin1.html')

def signup(request):
    return render(request, 'sample.html')
