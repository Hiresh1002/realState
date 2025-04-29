from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from .models import Student 

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')


def signup(request):
    if request.method == "POST":
        fnm = request.POST.get("fnm")
        lnm = request.POST.get("lnm")
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")

        edata = Student.objects.filter(email=email).exists()
        if edata:
            return render(request, "login.html", {'key': "Email already exists"})
        else:
            ob = Student(fnm=fnm, lnm=lnm, email=email, password=pwd)
            ob.save()
            return render(request, "login.html")
    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if Student.objects.filter(email=email).exists():
            if Student.objects.filter(password=password).exists():
                return render(request,'profile.html')
            else:
                return HttpResponse("Wrong password")
        else:
            return HttpResponse("Email does not exist")
    
    return render(request, "login.html")


