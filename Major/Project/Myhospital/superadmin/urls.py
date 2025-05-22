from django.urls import path
from .views import SuperadminloginView  

urlpatterns = [
    path('superlogin/', SuperadminloginView.as_view(), name='superadmin-login'),
]
