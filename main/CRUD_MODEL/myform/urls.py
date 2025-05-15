from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.Index), 
    path('book',views.Book_list),
 ]
