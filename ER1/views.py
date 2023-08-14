from django.shortcuts import render
# django.contrib.auth.models.User(AbstractUser)
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect
from .models import first,second
def dm3(request):
     ob1=first.objects.all()
     ob2=second.objects.all()
     return render(request,"welcome.html",{'a1':ob1,'a2':ob2})
# Create your views here.
def dm1(request):
     if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
             auth.login(request,user)
             return redirect('dm3')
        else:
          messages.info(request,"invalid credentials")
          return redirect('dm1')

     return render(request,'login.html')

def dm(request):
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
                 return redirect('dm')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,"email already taken")
                 return redirect('dm')


            user=User.objects.create_user(username=username,first_name=first_name,last_name=second_name,email=email,password=password)
            user.save();
            print("user created")
    else:
        print("incorect password")


    return render(request,"index.html")
def logout(request):
     auth.logout(request)
     return redirect('dm3')
     
      