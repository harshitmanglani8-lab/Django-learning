from django.shortcuts import render , redirect    
from django.http import HttpResponse , JsonResponse

# Create your views here.

def home(request):
    return HttpResponse("home page")

def about(request):
    return redirect("https://www.youtube.com/")

def contact(request):
    data=[
        {'name':'Harshit'},
        {'age':'18'}
    ]
    return JsonResponse(data,safe=False)

def service(request):
    return render(request,'add.html')