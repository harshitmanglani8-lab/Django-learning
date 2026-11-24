from django.shortcuts import render
from app.models import *

# Create your views here.

def home(request):
# Multiple objects
    Students=Studentmodel.objects.all() #return all data
    print(Students)

    filter=Studentmodel.objects.filter(city="bpl")
    print("filter=",filter)

    exclude=Studentmodel.objects.exclude(city="bpl")
    print("exclude=",exclude)

    sorting=Studentmodel.objects.order_by("name")
    print("sorting=",sorting)

    sorting=Studentmodel.objects.order_by("-name")
    print("sorting=",sorting)

    dict=Studentmodel.objects.values()
    print("dict=",dict)

    dict=Studentmodel.objects.values("name","city")
    print("dict=",dict)

    tuple=Studentmodel.objects.values_list()
    print("tuple=",tuple)

# Single objects

    Student=Studentmodel.objects.get(id=1)
    print("student=",Student)

    