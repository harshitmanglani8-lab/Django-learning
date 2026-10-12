from django.shortcuts import render

# Create your views here.

def home(request):

    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        skills=request.POST.getlist('skills')

        print(name)
        print(email)
        print(age)
        print(gender)
        print(skills)

    return render(request,'home.html')