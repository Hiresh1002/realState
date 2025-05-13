from django.shortcuts import render, HttpResponse, redirect
from.form import BookForm  

# Create your views here.
def Index(request):
    form = BookForm()
    return render(request, "user_list.html", {"form": form})
