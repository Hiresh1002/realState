from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Superadmin_data
from .serializers import Superadminlogin


class SuperadminloginView(APIView):
    def post(self, request):
        serializer = Superadminlogin(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            password = serializer.validated_data["psw"]
            try:
                user = Superadmin_data.objects.get(name=name, psw=password)

                return Response({'message': 'login Successfully'}, status=status.HTTP_200_OK)
            except Superadmin_data.DoesNotExist:
                return Response({"error": "invalid credential"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
