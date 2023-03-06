from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.utils.html import escape
# Create your views here.

def login_request(request):
    if request.method=="POST":
        username=escape(request.POST['username'])
        password=escape(request.POST['password'])
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("home")# included here chat home url!!!!!!!!!
        else:
            return render(request,"account/login.html",{"error":"username or password is incorrect:"})
    return render(request,'account/login.html')
def register_request(request):
    if request.method=="POST":
        firstname=escape(request.POST["firstname"])
        lastname=escape(request.POST["lastname"])
        email=escape(request.POST["email"])
        password=escape(request.POST["password"])
        repassord=escape(request.POST["repassord"])
        username=escape(request.POST["username"])

        if password==repassord:
            if User.objects.filter(username=username).exists():
                return render(request,"account/register.html",{
                    "error":" username is exist:",
                    "email":email,
                    "firstname":firstname,
                    "lastname":lastname,
                    })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,"account/register.html",{
                        "error":"email is exist:",
                        "firstname":firstname,
                        "lastname":lastname,
                        "username":username
                        })
                else:
                    user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,password=password,username=username)
                    user.save()
                    return redirect("login")
        else:
            return render(request,"account/register.html",{
                "error":"password and repead password are not same",
                "email":email,
                "firstname":firstname,
                "lastname":lastname,
                "username":username
                })
      
    return render(request,'account/register.html')
def logout_request(request):
    return redirect('login')