from django.shortcuts import render,redirect
from .models import student
from django.contrib import messages

def index(request):
    data = student.objects.all()
    context = {"data":data}
    return render (request,'index.html',context)

def about(request):
    return render (request,'about.html')

def insertdata(request):
    
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)

        query = student(name=name,email=email,age=age,gender=gender)
        query.save()
        messages.info(request,"DATA INSTERED ")
        return redirect("/")
    return render (request,'index.html')

def updatedata(request,id):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')

        edit = student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        messages.warning(request,"DATA UPDATED ")

        return redirect("/")
    d = student.objects.get(id=id)
    context = {"d":d}

    return render (request,'update.html',context)

def deletedata(request,id):
    d = student.objects.get(id=id)
    d.delete()
    messages.error(request,"DATA DELETED ")

    return redirect("/")