from django.shortcuts import render, HttpResponse, redirect
from .forms import BookForm
from .models import Book

# Create your views here.
def Index(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Saved successfully")
    form = BookForm()
    return render(request, "user_list.html", {"form": form})

def Book_list(request):
    books = Book.objects.all()
    return render(request, "user_book.html", {"books": books})

def book_update(request,pk):
    book = get_object_or_404 (Book, pk=pk)
    if request.method =='POST':
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return HttpResponse("Succes")
    else:
        form = BookForm(instance=book)
    return render(request,'book_from.html',{'form':form})