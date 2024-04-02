from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from liberyapp.models import Book
from liberyapp.forms import Bookform
# Create your views here.


def home(request):
    return render(request,"home.html")
@login_required
def add(request):

    if(request.method=='POST'):

        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']

        #file fields
        c=request.FILES['c']
        pdf=request.FILES['pdf']


        b=Book.objects.create(title=t,author=a,price=p,cover=c,pdf=pdf)
        b.save()
        return view(request)


    return render(request,"add book.html")


# def add(request):
#
#     if(request.method=='POST'):
#         form=Bookform(request.POST)
#
#         if form.is_valid():
#             form.save()
#
#             return view(request)
#
#     form=Bookform()
#
#     return render(request,"add1.html",{'form':form})


@login_required
def view(request):

    b=Book.objects.all()

    return render(request,"view.html",{'book':b})


def detail(request,n):
    b=Book.objects.get(id=n)
    return render(request,"detail.html",{'b':b})


def delete(request,n):
    b=Book.objects.get(id=n)
    b.delete()
    return view(request)


def edit(request,n):
    b=Book.objects.get(id=n)

    if (request.method == 'POST'):
        form=Bookform(request.POST,request.FILES,instance=b)

        if form.is_valid():
            form.save()

            return view(request)

    form=Bookform(instance=b)

    return render(request,"add1.html",{'form':form})