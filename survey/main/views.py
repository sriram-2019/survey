from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
# Create your views here.
def inde(request):
    if(request.method=="POST"):
        print("hello")
    return render(request,'index.html')