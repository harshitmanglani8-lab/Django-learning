from django.shortcuts import render ,redirect
from app.models import Student

# Create your views here.

def Student_details(request):
    students=Student.objects.all()
    return render(request,'details.html',{'key':students})

def Add_Student(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        city=request.POST.get('city')

        Student.objects.create(
            name=name,
            age=age,
            city=city
        )
        return redirect('student_details')
    
    return render(request,'add.html')

def edit_student(request,id):
    students=Student.objects.get(id=id)

    if request.method=='POST':
            Student.name=request.POST.get('name')
            Student.age=request.POST.get('age')
            Student.city=request.POST.get('city')

            Student.save()

    return render(request,'edit.html')