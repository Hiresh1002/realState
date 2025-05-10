from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Student, UserProfile

# Create your views here.

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

        # Check if the email already exists
        edata = Student.objects.filter(email=email).exists()
        if edata:
            messages.error(request, "Email already exists.")
            return redirect('login')  # Redirect to login instead of re-rendering signup
        else:
            # Create a new student record
            ob = Student(fnm=fnm, lnm=lnm, email=email, password=pwd)
            ob.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect('login')
    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            student = Student.objects.get(email=email)
            if student.password == password:
                request.session["pro_data"] = email
                return redirect("user_profile")  # Use named URL for redirection
            else:
                messages.error(request, "Wrong password.")
                return redirect('login')  # Redirect back to login if password is wrong
        except Student.DoesNotExist:
            messages.error(request, "Email does not exist.")
            return redirect('login')  # Redirect back to login if email is not found

    return render(request, "login.html")


def user_profile(request):
    if 'pro_data' not in request.session:
        return redirect('login')  # Redirect to login if no session exists

    email = request.session["pro_data"]
    try:
        data = Student.objects.get(email=email)
        return render(request, 'profile.html', {'key': data})
    except Student.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('login')  # Redirect to login if user does not exist


def user_update(request, id):
    try:
        data = Student.objects.get(id=id)
    except Student.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('home')  # Redirect to home if the user does not exist
    
    if request.method == "POST":
        fnm = request.POST.get("fnm")
        lnm = request.POST.get("lnm")
        email = request.POST.get("email")
        password = request.POST.get("pwd")

        # Update student record
        data.fnm = fnm
        data.lnm = lnm
        data.email = email
        data.password = password
        data.save()

        messages.success(request, "Profile updated successfully.")
        return redirect("user_profile")  # Use named URL for redirection
    
    return render(request, 'update.html', {"key": data})


def user_delete(request, id):
    try:
        ob = Student.objects.get(id=id)
        ob.delete()
        messages.success(request, "Account deleted successfully.")
        return redirect("home")  # Redirect to home or another page
    except Student.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect("home")  # Redirect to home if the user does not exist


def user_logout(request):
    if 'pro_data' in request.session:
        del request.session['pro_data']
    messages.success(request, "You have logged out successfully.")
    return redirect("login")  # Redirect to login after logout


def update_profile(request):
    if request.method == "POST":
        email = request.session.get("pro_data")
        if email:
            try:
                student = Student.objects.get(email=email)
            except Student.DoesNotExist:
                messages.error(request, "User not found.")
                return redirect('login')  # Redirect to login if user not found

            pic = request.FILES.get("pic")

            # Get or create the user profile
            profile, created = UserProfile.objects.get_or_create(fkey=student)

            if pic:
                profile.image = pic
                profile.save()

            messages.success(request, "Profile picture updated successfully.")
            return redirect("user_profile")

        else:
            messages.error(request, "You need to log in to update the profile.")
            return redirect("login")

    return render(request, 'Proupdate.html')
