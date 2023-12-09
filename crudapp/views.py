from django.shortcuts import render,redirect
from .models import StudentData

# Create your views here.
def home(request):
    sd=StudentData.objects.all()
    return render(request,'home.html',{'sd':sd})

def studentregister(request):
    if request.method=='GET':
        return render(request,'studentregister.html')
    else:
        StudentData(
            fname=request.POST.get('fname'),
            lname=request.POST.get('lname'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            marks1=request.POST.get('marks1'),
            marks2=request.POST.get('marks2'),
            marks3=request.POST.get('marks3'),
            marks4=request.POST.get('marks4')
        ).save()
        sd=StudentData.objects.all()
        return render(request,'home.html',{'sd':sd})
    
def update_data(request,id):
        sd=StudentData.objects.get(id=id)
        return render(request,'update_data_form.html',{'sd':sd})
    
def save_update_data(request,id):
        sd=StudentData.objects.get(id=id)
        sd.fname=request.POST.get('fname')
        sd.lname=request.POST.get('lname')
        sd.email=request.POST.get('email')
        sd.mobile=request.POST.get('mobile')
        sd.marks1=request.POST.get('marks1')
        sd.marks2=request.POST.get('marks2')
        sd.marks3=request.POST.get('marks3')
        sd.marks4=request.POST.get('marks4')
        sd.save()
        return redirect(home)
    
def delete_data(request,id):
        sd=StudentData.objects.get(id=id)
        sd.delete()
        return redirect(home)