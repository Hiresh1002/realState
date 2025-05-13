from django import form
from . models import Book

class BookForm(form.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
        widgets = {
            'author': form.CheckboxSelectMultiple()
        }
