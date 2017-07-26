# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from models import UserModels
from django.shortcuts import render,redirect
from datetime import datetime
from forms import Signup_Form, Login_Form
from django.contrib.auth.hashers import make_password

# Create your views here.

def signup_view(request):
    if request.method == "POST":
        form = Signup_Form(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data["firstname"]
            lastname = form.cleaned_data["lastname"]
            email = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirmpassword = form.cleaned_data["confirmpassword"]
            user = UserModels(firstname=firstname,lastname=lastname,email=email,username=username,
                              password=make_password(password),confirmpassword=password)
            user.save()
            return  render(request,"success.html")
    elif request.method == "GET":
        form = Signup_Form

    date = datetime.now()
    return render(request,"index.html",{"form":form,"date":date})

def login_view(request):
    if request.method == "POST":
        form = Login_Form(request.POST)
        if form.is_valid():
            user = 
            return  render(request,"success.html")
    elif request.method == "GET":
        form = Login_Form

    date = datetime.now()
    return render(request,"index.html",{"form":form,"date":date})