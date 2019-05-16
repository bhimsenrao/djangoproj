from django.shortcuts import render
from django.http      import HttpResponse
# Create your views here.
def viewPage(request):
    return HttpResponse("HelloUser")
def hello(request):
    return HttpResponse("<h1>Welcome</h1>")
def loadMe(request):
    return render(request,'./templates/Hello.html',{})
