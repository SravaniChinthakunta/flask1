from django.shortcuts import render,redirect
from app1.models import Scheduleclass,Student,Enrolleddetails
from django.core.exceptions import ObjectDoesNotExist
def showindex(request):
    return render(request,"adminlogin.html")
def validateadmin(request):
  un=request.POST.get("t1")
  pwd=request.POST.get("t2")
  if un=='sravanireddy' and pwd=='siri':
      return render(request, "adminwelcome.html")
  else:
      return render(request,'adminlogin.html',{"data":'check your username and password'})

def schedule(request):
    return render(request,"scheduleclass.html")
def savescheduled(request):
    na=request.POST.get("s1")
    fac=request.POST.get("s2")
    date=request.POST.get("s3")
    time=request.POST.get("s4")
    fee=request.POST.get("s5")
    dur=request.POST.get("s6")
    Scheduleclass(name=na,faculty=fac,date=date,time=time,fee=fee,duration=dur).save()
    return render(request,"scheduleclass.html",{"result":'Schedule saved succesfully'})
def viewclasses(request):
    data=Scheduleclass.objects.all()
    return render(request,"viewclass.html",{"data":data})
#def update(request):
    #id=request.GET.get(id)
    #main=Scheduleclass.objects.get(idno=id).update()
    #return render(request,"scheduleclass.html")

def delete(request):
    idd=request.GET.get("id")
    Scheduleclass.objects.get(idno=idd).delete()
    return redirect('schedule')
def student(request):
    return render(request,"main.html")
def courses(request):
    data=Scheduleclass.objects.all()
    return render(request,"viewcourses.html",{"data":data})
def registerstu(request):
    return render(request,"stuRegister.html")
def savestureg(request):
    na=request.POST.get("s1")
    em = request.POST.get("s2")
    cno = request.POST.get("s3")
    pwd = request.POST.get("s4")
    Student(name=na,contact=cno,emial=em,Password=pwd).save()
    return render(request,"stuRegister.html",{"data":'Student registered succesfully'})
def LoginStu(request):
    return render(request,"studentlogin.html")
def savestulog(request):
    un = request.POST.get("r1")
    pwd = request.POST.get("r2")
    try:
        data=Student.objects.get(name=un,Password=pwd)
        return render(request,"welcome_student.html",{"result":data})
    except ObjectDoesNotExist:
        return render(request,"studentlogin.html",{"data":'Invalid user'})
def view_savedcourses(request):
        result=Scheduleclass.objects.all()
        data=Student.objects.all()
        return render(request,"view_savedcourses.html",{"data":result,"result":data})
def save_enroll(request):
    id1=request.GET.get("scno")
    id2=request.GET.get("Cid")
    value=Student.objects.get(contact=id1)
    Enrolleddetails(Studentcontact=value,CourseID=id2).save()
    return render(request,"view_savedcourses.html",{"message":'Student enrolled succesfully'})









# Create your views here.
