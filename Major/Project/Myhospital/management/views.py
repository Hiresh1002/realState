from django.shortcuts import render,HttpResponse

# Create your views here.
def management(req):
    return HttpResponse("hello Management")