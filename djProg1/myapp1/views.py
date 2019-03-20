from django.shortcuts import render
from django.http      import HttpResponse
# Create your views here.
def hello(request):
    text="<h1>Hello!All</h1>"
    return HttpResponse(text)
def test(request):
    message="<body> Testing body</body>"
    return HttpResponse(message)
def call(request): 
        return render(request, "./templates/File1.html", {})
def myInfo(request): 
        return render(request, "./templates/Info.html", {})
def infoCall(request):
        name=request.GET['tname']
        return HttpResponse('<b>'+name+'</b>')