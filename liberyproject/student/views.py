from django.contrib import auth
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from student.models import Students,Teacher
from student.forms import Studentform
from student.forms import Teacherform

from student.models import CustomUser


# Create your views here.

def register(request):

    if(request.method=='POST'):

        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']

        phone=request.POST['phonenumber']
        address=request.POST['address']


        if(cpassword==password):
            s=CustomUser.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email,phone=phone,address=address)
            s.save()
            return redirect('liberyapp:home')
        else:
            return HttpResponse("Password Does Not Match")

    return render(request,"register.html")

def login(request):
    if(request.method=='POST'):

        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)


        if user is not None:
            auth.login(request,user)
            return redirect('liberyapp:home')

        else:
            return HttpResponse("sorry invalid")
  



    return render(request,"login.html")

# def user_login(request):
#     if(request.method=='POST'):
#
#         username=request.POST['username']
#         password=request.POST['password']
#
#         user=authenticate(username=username,password=password)
#
#         if user:
#             login(request,user)
#             return redirect('liberyapp:home')
#         else:
#             return HttpResponse('INVALID CREDENTIALS')
#
#     return render(request,"login.html")

@login_required
def details(request):
    s=Students.objects.all()

    return render(request,"details.html",{'students':s})

# def add(request):
#
#     if(request.method=='POST'):
#         name=request.POST['n']
#         age=request.POST['a']
#         place=request.POST['p']
#
#         s=Students.objects.create(name=name,age=age,place=place)
#         s.save()
#         return details(request)
@login_required
def add(request):
    if (request.method == 'POST'):
        form = Studentform(request.POST)

        if form.is_valid():
            form.save()

            return details(request)

    form = Studentform()

    return render(request, "add student1.html", {'form': form})



# def teacher(request):
#
#     if(request.method=='POST'):
#
#         form=Teacherform(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return viewteacher(request)
#
#     form=Teacherform()
#
#     return render(request,"teacher.html",{'form':form})
@login_required
def teacher(request):

    if(request.method=='POST'):

        name=request.POST['n']
        subject=request.POST['s']
        place=request.POST['p']

        image=request.FILES['image']
        pdf=request.FILES['pdf']

        s=Teacher.objects.create(name=name,subject=subject,place=place,image=image,pdf=pdf)
        s.save()
        return viewteacher(request)
    return render(request,"teacher.html")

@login_required
def viewteacher(request):

    s=Teacher.objects.all()

    return render(request,"viewteacher.html",{'teacher':s})
@login_required
def tdetail(request,n):
    s=Teacher.objects.get(id=n)

    return render(request,"tdetail.html",{'s':s})

@login_required
def editteacher(request,n):

    s=Teacher.objects.get(id=n)

    if(request.method=='POST'):
        form=Teacherform(request.POST,request.FILES,instance=s)

        form.is_valid()
        form.save()
        return viewteacher(request)

    form=Teacherform(instance=s)

    return render(request,"editteacher.html",{'form':form})

@login_required
def deleteteacher(request,n):
    s=Teacher.objects.get(id=n)

    s.delete()
    return viewteacher(request)



def userlogout(request):
    logout(request)
    return redirect('student:login')

# def logout(request):
#
#     auth.logout(request)
#     return redirect('student:login')