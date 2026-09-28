from django.shortcuts import render

# Create your views here.

def home(request,pk):
    data=pk
    return render(request,'home.html',{'key':data})

def about(request,rm):
    data=rm
    return render(request,'about.html',{'key':data})