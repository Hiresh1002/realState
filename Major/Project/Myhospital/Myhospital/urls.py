from django.contrib import admin
from django.urls import path, include
from superadmin.views import SuperadminloginView
from django.urls import path


# def redirect_to_login(request):
#     return redirect('admin-login')

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path("", include('Patient.urls')),
    path('superadmin/', include('superadmin.urls')),
    path('management/', include('management.urls')),
    
]
