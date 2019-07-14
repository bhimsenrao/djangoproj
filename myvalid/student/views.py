from django.shortcuts import render, redirect  
from student.forms import StudentForm  
from student.models import Student
def stud(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:
	            form.save()
                #return redirect('/stud')  
            except:  
                pass  
    else:  
        form = StudentForm()  
    return render(request,'index.html',{'form':form})  
    