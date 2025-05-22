from django.contrib import admin
from django.urls import path, include
from superadmin.views import SuperadminloginView
from django.urls import path
from django.shortcuts import redirect

def redirect_to_login(request):
    return redirect('admin-login')

urlpatterns = [
    path('', redirect_to_login),
    path('admin/', admin.site.urls),
    path('adminlogin/', SuperadminloginView.as_view(), name='admin-login'),
    path('superadmin/', include('superadmin.urls')),
    path('management/', include('management.urls')),
]
