from django import forms
from models import UserModels

class Signup_Form(forms.ModelForm):
    class Meta:
        model = UserModels
        fields = ["firstname","lastname","email","username","password","confirmpassword"]

class Login_Form(forms.ModelForm):
    class Meta:
        model = UserModels
        fields = ["username","password"]