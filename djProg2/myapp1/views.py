from django.shortcuts import render
from django.http      import HttpRequest
from django.http      import HttpResponse
from myapp1.studForm  import StudentForm
from myapp1.DBInsert  import *
# create your views here.
def viewer(request):
    return render(request, "./templates/Welcome.html", {})
def message(request):
    return HttpResponse("<h1>Thank you for being here<h1>")
def dataForm(request):
     return render(request, "./templates/MyForm1.html", {})
def finalView(request):
    myinput=request.GET['tname']
    return HttpResponse(myinput)

def sendData(request):
    student= StudentForm()
    return render(request,"./templates/InputForm.html",{'form':student})
def mydata(request):
    fname=request.POST['firstname']
    lname=request.POST['lastname']
    return HttpResponse(fname+" "+lname+" <br><h1>Thank you for sending data</h1>")
def setMySession(request):
   #  request.session['username']='user123'
     request.session.__setitem__('username','user123')    
     return HttpResponse('Session Ready')
def getMySession(request):
    #myVar=request.session['username']
     try:
          myVar=request.session.__getitem__('username')
          return HttpResponse('My Session Data '+myVar)
     except Exception:
          return HttpResponse('Session already deleted or not created')
def clearMySession(request):
     try:
          request.session.__delitem__('username')
          return HttpResponse('Session entry deleted')
     except Exception:
          return HttpResponse('Session already deleted')
def  personIns(request):
     return render(request,"./templates/PersonForm.html",{})
def  saverec(request):
     varId=request.GET['id']
     varName=request.GET['pname']
     addrec(varId,varName)
     return HttpResponse('Record Added')
def getAllRecords(request):
     text=viewRecord()
     return HttpResponse(text)
     
