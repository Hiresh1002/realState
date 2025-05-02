from django.shortcuts import render,redirect

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
        data=Student.objects.filter(email=email).exists()
        if(data):
          pswd=Student.objects.filter(password=password).exists()
          if(pswd):
              request.session["pro_data"]=email
              return redirect("/user_profile")
          else:
              return HttpResponse("wrong password")
        else:
            return HttpResponse("email wrong")
    return render (request,"login.html")

def user_profile(request):
    email=request.session["pro_data"]
    data=Student.objects.get(email=email)
    return render(request,'profile.html',{'key':data})


def user_update(request, id):
    data = Student.objects.get(id=id)
    
    if request.method == "POST":
        fnm = request.POST.get("fnm")
        lnm = request.POST.get("lnm")
        email = request.POST.get("email")
        password = request.POST.get("pwd")
        ob = Student(id=id, fnm=fnm, lnm=lnm, email=email, password=password)
        ob.save()
        return redirect("/login")
    
    # GET request par form dikhega
    return render(request, 'update.html', {"key": data})


def user_delete(request,id):
        ob= Student.objects.get(id=id)
        ob.delete()
        return HttpResponse("delete")

def user_logout(request):
    del request.session['pro_data']
    return redirect("/login")
