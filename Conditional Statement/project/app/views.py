from django.shortcuts import render

# Create your views here.

def home(request):
    data={
        'age':20
    }
    return render(request,'home.html',data)

def about(request):
    data={
        'students':[
            'Harshit',
            'abc',
            'xyz',
        ]
    }
    return render(request,'about.html',data)

