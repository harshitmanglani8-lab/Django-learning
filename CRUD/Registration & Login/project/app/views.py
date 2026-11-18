from django.shortcuts import render
from app.forms import Registrationform , Studentmodel , Loginform
from .models import *

# Create your views here.
def home(request):
    form=Registrationform()
    if request.method=="POST":      
        form=Registrationform(request.POST)
    
        if form.is_valid():
            stu_name=form.cleaned_data["stu_name"]
            stu_email=form.cleaned_data["stu_email"]
            stu_city=form.cleaned_data["stu_city"]
            stu_mobile=form.cleaned_data["stu_mobile"]
            stu_password=form.cleaned_data["stu_password"]   
            print(stu_name,stu_email,stu_city,stu_mobile)
            user = Studentmodel.objects.filter(stu_email=stu_email)
            if user:
                msg = "Email already exit"
                form = Registrationform()
                return render(request,"home.html",{"form":form,"msg":msg})
            else:
                form.save()
                msg="Registration succesfull"
                form=Registrationform()
                return render(request,"home.html",{"form":form,"msg":msg})
            
    else:
        return render(request,'home.html',{"form":form})

def login(request):
    form= Loginform()
    if request.method=="POST":
        data= Loginform(request.POST)
        if data.is_valid():
            email=data.cleaned_data['stu_email']
            password=data.cleaned_data['stu_password']
            print(email,password)
            user= Studentmodel.objects.filter(stu_email=email)

            if user:
                user= Studentmodel.objects.get(stu_email=email)
                print(user.stu_password)
            if user.stu_password==password:
                name=user.stu_name
                email=user.stu_email
                mobile=user.stu_mobile
                city=user.stu_city
                password=user.stu_password
                data={
                    'name':name,
                    'email':email,
                    'mobile':mobile,
                    'city':city,
                    'password':password,
                }
                return render(request,'dashboard.html',{'data':data})
            else:
                msg="Email & Password not matched"
    return render(request,'login.html')