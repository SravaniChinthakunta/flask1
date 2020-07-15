"""flask1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showindex,name="main"),
    path('validateadmin/',views.validateadmin,name="validateadmin"),
    path('schedule/',views.schedule,name="schedule"),
    path('savescheduled/',views.savescheduled,name="savescheduled"),
    path('viewclasses/', views.viewclasses, name="viewclasses"),
    path('update/',views.update,name="update"),
    path('updated/',views.updated,name="updated"),
    path('delete/',views.delete,name="delete"),
    path('student/',views.student,name="student"),
    path('courses/',views.courses,name="courses"),
    path('registerstu/',views.registerstu,name="registerstu"),
    path('savestureg/',views.savestureg,name="savestureg"),
    path('LoginStu/',views.LoginStu,name="LoginStu"),
    path('search/',views.search,name="search"),
    path('contactus/',views.contactus,name="contactus"),
    path('savestulog/',views.savestulog,name="savestulog"),
   # path('Getstudentdetails/',views.Getstudentdetails,name="Getstudentdetails"),
    path('view_savedcourses/',views.view_savedcourses,name="view_savedcourses"),
    path('save_enroll/',views.save_enroll,name="save_enroll"),
    path('view_enroll/',views.view_enroll,name="view_enroll"),
    path('cancel_enrolledcourse/',views.cancel_enrolledcourse,name="cancel_enrolledcourse"),
    path('delete_enroll/',views.delete_enroll,name="delete_enroll")


]
