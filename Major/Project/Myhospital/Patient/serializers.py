from rest_framework.serializer import serializer


class Patient_Signup_api(serializer.Serializers):
    First_name=serializer.CharField()
    Last_name=serializer.CharField()
    Contact_number=serializer.CharField()
    Email_iD=serializer.CharField()



    