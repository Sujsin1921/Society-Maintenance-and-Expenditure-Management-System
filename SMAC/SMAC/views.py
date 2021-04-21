from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def Home(request):
    return render(request,'home.html')

def Members(request):
    return render(request,'Members.html')

def Expences(request):
    return render(request,'Expences.html')

def Collection(request):
    return render(request,'Collection.html')

def Pending(request):
    return render(request,'Pending.html')

def Funds(request):
    return render(request,'Funds.html')