from django.db import models
class Scheduleclass(models.Model):
    idno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    faculty=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=False)
    time=models.TimeField()
    fee=models.FloatField()
    duration=models.ImageField(default=True)
class Student(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    emial = models.EmailField(max_length=50,unique=True)
    contact = models.IntegerField(unique=True)
    Password = models.CharField(max_length=50)

class Enrolleddetails(models.Model):
    idno=models.AutoField(primary_key=True)
    Studentcontact=models.IntegerField()
    CourseID=models.IntegerField()


# Create your models here.
