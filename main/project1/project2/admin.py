from django.contrib import admin
from .models import Student, UserProfile  # Corrected to match model case

admin.site.register(Student)
admin.site.register(UserProfile)  # Corrected to match model case
