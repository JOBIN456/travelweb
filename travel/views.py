from django.shortcuts import render

# Create your views here.
from .models import first,second

def dm3(request):
     ob1=first.objects.all()
     ob2=second.objects.all()
     return render(request,"welcome.html",{'a1':ob1,'a2':ob2})