from django.shortcuts import render,HttpResponse

# Create your views here.
def superadmin(req):
    return HttpResponse("hello Supper  admin")