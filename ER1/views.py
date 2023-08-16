from django.shortcuts import render
# django.contrib.auth.models.User(AbstractUser)
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect


# Create your views here.
def login(request):
     if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
             auth.login(request,user)
             return redirect('/')
        else:
          messages.info(request,"invalid credentials")
          return redirect('login')

     return render(request,'login.html')

def register(request):
    if request.method=='POST':
       username=request.POST['username']
       first_name=request.POST['first_name']
       second_name=request.POST['last_name']
       email=request.POST['email']
       password=request.POST['password']
       cpassword=request.POST['password1']

       if password==cpassword:
            if User.objects.filter(username=username).exists():
                 messages.info(request,"username taken")
                 return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,"email already taken")
                 return redirect('register')
            else:
                 user=User.objects.create_user(username=username,first_name=first_name,last_name=second_name,email=email,password=password)
                 user.save();
                 print("user created")
                 return redirect('login')
       else:

          messages.info(request,"password not matching")
          return redirect('register')
    return render(request,"index.html")
def logout(request):
     auth.logout(request)
     return redirect('/')
     
      