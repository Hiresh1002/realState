from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='Gallery'),
    path('services/', views.services, name='Services'),
    path('about/', views.about, name='about'),   
    path('contact/', views.contact, name='Contact'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path("user_profile",views.user_profile,name="user_profile"),
    path('update/<int:id>/', views.user_update, name='user_update'),
    path('delete/<int:id>/', views.user_delete, name='user_delete'),
    path('logout/', views.user_logout, name='user_logout'),





]
