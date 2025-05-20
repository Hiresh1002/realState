from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('superadmin/')),
    path('admin/', admin.site.urls),
    path('management/', include('management.urls')),
    path('superadmin/', include('superadmin.urls')),
]
