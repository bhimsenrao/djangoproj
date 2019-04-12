from django.db import models

# Create your models here.
class Stud(models.Model):
    stud_name=models.CharField(max_length=30)
    stud_course=models.CharField(max_length=10)
    class Meta:
        db_table="stud"

# then apply the following command at prompt 
# python manage.py syncdb
# python manage.py makemigrations stud
# python manage.py migrate
#check your database for new table