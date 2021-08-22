
from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout



from root.models import *

# Create your views here.



def signup_page(request): 
    if request.method=='POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        user = User.objects.filter(username=username)
        try:
            if user.exists():
                return render(request, 'root/signup.html',{"error":"username already exists !"})
            else:
                user = User(
                    username=username,first_name =firstname,last_name=lastname,password=make_password(password))
                user.save()    
                Password_Table(user=user,password=password).save()


                return render(request, 'root/login.html',{'message':"Account created successfully !"})
        except IntegrityError:
                return render(request, 'root/signup.html',{"error":"User name has already been selected !"})
    return render(request, 'root/signup.html')

def login_page(request):
    if request.method=='POST':
        username = request.POST['username'] 
        password = request.POST['password']
        user = User.objects.filter(username=username)
        if user.exists():
            user = user.first()
            username = user.username
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                print("login successful !") 
                return redirect('calculator_page') 
            else:
                return render(request, 'root/login.html',{"error":"Sorry, Nick (username) or password is incorrect !"})
        else:
            print("dont exists")
            return render(request, 'root/login.html',{"error":"Sorry, Nick (username) or password is incorrect !"})
    return render(request, 'root/login.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')









@login_required(login_url="login_page") 
def calculator_page(request):  
    return render(request, 'root/calculator_page.html')

@login_required(login_url="login_page") 
def perform_calculation(request):  
    expression = request.GET['expression']
    try:result = eval(expression)
    except Exception as e:
        result=str(e)
    Profile(user=request.user,expression=expression,result=result).save()
    return JsonResponse({"result":result})


@login_required(login_url="login_page") 
def history_page(request):   
    entires = Profile.objects.filter(user=request.user).order_by('-id')
    return  render(request, 'root/history_page.html',{"entries":entires})


@login_required(login_url="login_page") 
def profile_page(request):   
    if request.method=='POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        target_user = User.objects.get(username=request.user.username)
        target_user.username=username
 
        target_user.first_name = firstname
        target_user.last_name = lastname
        target_user.set_password(password)

        try: 
            target_user.save()
            login(request, target_user)
        except: return render(request, 'root/profile_page.html',{"error":"username already exists !"})

        new_password = Password_Table.objects.filter(user=target_user).first()
        new_password.password = password
        new_password.save()

        
        password = Password_Table.objects.filter(user=target_user)
        if password:
            password=password.first().password
        return  render(request, 'root/profile_page.html',{"password":password})







    password = Password_Table.objects.filter(user=request.user)
    if password:
        password=password.first().password
    return  render(request, 'root/profile_page.html',{"password":password})




# target_user.set_password(new_password)
 





 
 
 
 


# @csrf_exempt
# @login_required(login_url="loginuser") 