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

    Students=Studentmodel.objects.first()
    print("students=",Student)

    Students=Studentmodel.objects.last()
    print("students=",Student)

    Students=Studentmodel.objects.latest('id')
    print(Student)

    check=Studentmodel.objects.filter(name='harshit').exists()
    print(check)

    creation=Studentmodel.objects.create(
        name='harshit',
        age=19,
        city='bpl')
    print("datacreated=",creation)

    update=Studentmodel.objects.filter(id=1).update(age=20)
    print(update)

    delete=Studentmodel.objects.filter(id=4).delete()
    print(delete)

    total=Studentmodel.objects.count()
    print(total)

    Students,created=Studentmodel.objects.get_or_create(
        name='h',
        defaults={
            'age':19,
            'city':'bpl'
        })
    print("students=",Students)
    print("created=",created)

    Students,created=Studentmodel.objects.update_or_create(
        name='r',
        defaults={
            "age":19,
            "city":'delhi'
        })
    print("students=",Students)
    print("created=",created)

    Students=[
        Studentmodel(
            name='ri',
            age=19,
            city='bpl'
        ),
        Studentmodel(
            name='y',
            age=20,
            city='d'
        )]

    bulk=Studentmodel.objects.bulk_create(Students)
    print(bulk)
    