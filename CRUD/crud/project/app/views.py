from django.shortcuts import render

# Create your views here.

def Student_details(request):
    return render(request,'details.html')

def Add_Student(request):
    return render(request,'add.html')
