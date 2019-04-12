from django.shortcuts import render,redirect
from stud.models      import Stud
from django.http      import HttpResponse
from djCRUD            import settings
import  csv
from reportlab.pdfgen import canvas  
#------------------ Generate PDF from python  -------------------------#
def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Dispatcher'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Hello  Friends ")  
    p.showPage()  
    p.save()  
    return response  
#------------------- Loading csv-----------------------------------------------------#
def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    writer = csv.writer(response)  
    writer.writerow(['ID','Name','Location','Profession'])
    writer.writerow(['1001', 'John', 'Hyderabad', 'CA'])  
    writer.writerow(['1002', 'Amit', 'Mumbai', 'IT'])  
    return response  
#----------------------  DJANGO crud operations  -------------------------#
def loadMe(request):
    return render(request,'./templates/StudForm.html',{})
def crudops(request):
   #Creating an entry
    stud = Stud(
        stud_name=request.GET['sname'],
        stud_course=request.GET['scourse']
    )
    stud.save()
    return redirect('../viewAll')   
    
    #return HttpResponse('Saved')
def viewAll(request):
    objs=Stud.objects.all()
    root ="<table border='1'><tr><th>Student name</th><th>Course </th></tr>"
    res=" "
    for cl in objs:
        res=res+"<tr><td>"+cl.stud_name+"</td><td>"+cl.stud_course +"</tr>"
    root=root+""+res+"</table>"
    root=root+"<a href='../loadMe'>back</a>"
    return HttpResponse(root)

def filterByJava(request):
    objs=Stud.objects.filter(stud_course='Java')
    res ='<br/>'
    for cl in objs:
        res=res+cl.stud_name+"  "+cl.stud_course +"<br/>"
    return HttpResponse(res)

def delStud(request,id):
    stud=Stud.objects.get(id=id)
    stud.delete()
    return HttpResponse("Record deleted")    
