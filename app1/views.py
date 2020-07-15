from django.contrib import messages
from django.http import HttpResponse
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
def update(request):
    id=request.GET.get("id")
    result=Scheduleclass.objects.get(idno=id)
    return render(request,"update.html",{"data":result})
def updated(request):
    id=request.POST.get("u1")
    na=request.POST.get("u2")
    fa=request.POST.get("u3")
    da=request.POST.get("u4")
    ti=request.POST.get("u5")
    fee=request.POST.get("u6")
    dur=request.POST.get("u7")
    Scheduleclass.objects.filter(idno=id).update(name=na,faculty=fa,date=da,time=ti,fee=fee,duration=dur)
    result=Scheduleclass.objects.get(idno=id)
    return redirect('viewclasses')

def delete(request):
    idd=request.GET.get("id")
    Scheduleclass.objects.get(idno=idd).delete()
    return redirect('viewclasses')

#=================================================================================
def student(request):
    return render(request,"main.html")
def courses(request):
    data=Scheduleclass.objects.all()
    return render(request,"viewcourses.html",{"data":data})
def registerstu(request):
    return render(request,"stuRegister.html")


def search(request):
    return render(request,"search.html")


def savestureg(request):
    na=request.POST.get("s1")
    em = request.POST.get("s2")
    cno = request.POST.get("s3")
    pwd = request.POST.get("s4")
    Student(name=na,contact=cno,emial=em,Password=pwd).save()
    return render(request,"stuRegister.html",{"data":'Student registered succesfully'})

def LoginStu(request):
    return render(request,"studentlogin.html")
def contactus(request):
    return render(request,"contactus.html")


def savestulog(request):
    un = request.POST.get("r1")
    pwd = request.POST.get("r2")
    res = Scheduleclass.objects.all()
    try:
        data=Student.objects.get(name=un,Password=pwd)
        request.session['contact']=data.contact
        return render(request,"welcome_student.html",{"result":data,'class':res})
    except Student.DoesNotExist:
        return render(request,"studentlogin.html",{"data":'Invalid user'})

def view_savedcourses(request):
        result = Scheduleclass.objects.all()
        details = Student.objects.all()
        return render(request,"view_savedcourses.html",{"data":result,"student":details})


def save_enroll(request):
    #scno=request.GET.get("scno")
    contact = request.GET.get('contact')
    cid=request.GET.get("cid")
    try:
        Enrolleddetails.objects.get(Studentcontact=contact,CourseID=cid)
        messages.error(request,"Already Entrolled")
        return redirect('view_savedcourses')
    except Enrolleddetails.DoesNotExist:
        Enrolleddetails(Studentcontact=contact,CourseID=cid).save()
        messages.success(request,"Successfully Enrolled")
        return redirect('view_savedcourses')


def view_enroll(request):
    con=request.GET.get('con')

    try:
        res= Enrolleddetails.objects.filter(Studentcontact=con)
        data = [Scheduleclass.objects.get(idno=x.CourseID) for x in res]
        return render(request,"viewenroll.html",{"data":data})
    except:
        messages.error(request,"student does not enrolled")
        return redirect('view_savedcourses')
def cancel_enrolledcourse(request):
    con=request.GET.get('con')
    res=Enrolleddetails.objects.filter(Studentcontact=con)
    data=[Scheduleclass.objects.get(idno=x.CourseID) for x in res]
    return render(request,"cancel_enrolledcourse.html",{"data":data})
def delete_enroll(request):
    cid=request.GET.get("cid")
    scno=request.GET.get("scno")
    Enrolleddetails.objects.get(CourseID=cid,Studentcontact=scno).delete()
    res=Enrolleddetails.objects.filter(Studentcontact=scno)
    data = [Scheduleclass.objects.get(idno=x.CourseID) for x in res]
    return render(request, "cancel_enrolledcourse.html", {"data": data})

