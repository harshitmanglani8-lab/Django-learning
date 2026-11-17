from django.shortcuts import render
from forms import Registrationform ,Studentmodel

# Create your views here.

def home(request):
    form = Registrationform()
    if request.method=="POST":
        form=Registrationform(request.POST)

        if form.is_valid():
            stu_name= form.cleaned_data["stu_name"]
            stu_email= form.cleaned_data["stu_email"]
            stu_city= form.cleaned_data["stu_city"]
            stu_mobile= form.cleaned_data["stu_mobile"]
            stu_password= form.cleaned_data["stu_password"]
            user= Studentmodel.objects.filter(stu_email=stu_email)
            if user:
                msg = "Email Already exist"
                form = Registrationform()
                return render(request,"home.html",{"form":form,"msg":msg})
    else:
        return render(request,"home.html",{"form":form})