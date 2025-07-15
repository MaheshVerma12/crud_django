from django.shortcuts import render,redirect 
from .models import Student
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def home(request):
    data=Student.objects.filter(is_delete=False)
    return render(request,'crud_app/home.html',{'data':data})
def form(request):
    if request.method=='POST' and request.FILES:
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        message=request.POST['message']
        profile=request.FILES['profile']
        profile_video=request.FILES['profile_video']

        if int(age)>100 or int(age)<1:
            messages.error(request,'your age should be between 1 to 100')
            return redirect('form')
        try:
            user1=Student(name=name,age=age,email=email,message=message,profile=profile,profile_video=profile_video)  
            user1.full_clean()
            user1.save()
            subject="django training"
            message="focus on your career"
            from_email= "maheshcverma1223@gmail.com"
            recipient_list=[email]
            send_mail(subject,message,from_email,recipient_list,fail_silently=False)
            messages.success(request,f"Hi {name} Your form is successfully submitted.")
            return redirect('form')
        except Exception as e:
            messages.error(request,e)
            return redirect('form')


    return render(request,'crud_app/form.html')

def contact(request):
    return render(request,'crud_app/contact.html')
def about(request):
    return render(request,'crud_app/about.html')
def delete_data(request,id):
    data=Student.objects.get(id=id)
    data.is_delete=True
    data.save()
    return redirect('home')
def update_data(request,id):
    data=Student.objects.get(id=id)
    if request.method=='POST':
        data=Student.objects.get(id=id)
        data.name=request.POST['name']
        data.age=request.POST['age']
        data.email=request.POST['email']
        data.message=request.POST['message']
        data.save()
        return redirect('home')
    return render(request,'crud_app/update.html',{'data':data})
def deleted(request):
    
    data=Student.objects.filter(is_delete=True)
    return render(request,'crud_app/deleted.html',{'data':data})
def restore(request,id):
    student=Student.objects.get(id=id)
    student.is_delete=False
    student.save()
    return redirect('deleted_data')

