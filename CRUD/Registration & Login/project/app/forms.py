from django import forms
from .models import Studentmodel , Studentquery

class Registrationform(forms.ModelForm):
    confirm_password= forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        label="Confirm Password"
    )
    class Meta:
        model = Studentmodel
        fields = ('stu_name' , 'stu_email' , 'stu_city' , 'stu_mobile' , 'stu_password')
        widgets ={
            'stu_name':forms.TextInput(attrs={'class':'form-control'}),
            'stu_email':forms.EmailInput(attrs={'class':'form-control'}),
            'stu_city':forms.TextInput(attrs={'class':'form-control'}),
            'stu_mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'stu_password':forms.PasswordInput(attrs={'class':'form-control'}),
            }

class Loginform(forms.ModelForm):
    class Meta:
        model = Studentmodel
        fields = ('stu_email',"stu_password")
        widgets = {
            'stu_email':forms.EmailInput(attrs={'class':'form-control'}),
            'stu_password':forms.PasswordInput(attrs={'class':'form-control'}),
        }

class Queryform(forms.ModelForm):
    class Meta:
        model = Studentquery
        fields = ('stu_email',"stu_name","stu_query")
        widgets= {
            "stu_email": forms.EmailInput(attrs={"class":"form-control"}),
            "stu_name": forms.TextInput(attrs={"class":"form-control"}),
            "stu_query":forms.TextInput(attrs={"class":"form-control"}),
        }
