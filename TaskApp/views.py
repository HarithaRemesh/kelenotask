from django.shortcuts import render,redirect

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')
def nextpage(request):
    return render(request,"nextpage.html")