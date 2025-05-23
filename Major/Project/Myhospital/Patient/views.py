from rest_framework.views import APIView
from rest_framework.Response import Response
from rest_framework import status
from .serializers import Patient_Signup_api
from .models import Patient_signup
#create your views here 

 class Patient_views_api(APIView):