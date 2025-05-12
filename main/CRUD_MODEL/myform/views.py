from django.shortcuts import render, HttpResponse, redirect
from.forms import BookForm  

# Create your views here.
def index(request):
    form = BookForm()
    return render(request, "user_list.html", {"form": form})
