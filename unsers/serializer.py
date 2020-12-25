from rest_framework import serializers

class StudentSeriaizer(serializers.Serializer):
    name = serializers.CharField(required=True,max_length=20)
    sex  = serializers.BooleanField(required=True,default=1)
    age  = serializers.IntegerField(max_value=120,required=True)
    class_num = serializers.CharField(required=True)
    description = serializers.CharField(allow_null=True,allow_blank=True)