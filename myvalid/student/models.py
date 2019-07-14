from django.db import models  
class Student(models.Model):  
    stid = models.CharField(max_length=20)  
    sname = models.CharField(max_length=100)  
    
    class Meta:  
        db_table = "student"
