from rest_framework import serializers 
from django.contrib.auth.models import User 
from .models import *
class SignUpSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(max_length=100)
    class Meta:
    
        model = User 
        fields = ['username','confirm_password','password']
        extra_kwargs =  {'password': {'write_only': True},'confirm_password':{'write_only':True},'username':{'required':True},'email':{'required':True}}
    def validate(self,attrs):
        if attrs.get('confirm_password') != attrs.get('password'):
            raise serializers.ValidationError('The confirm password and password doesnot match')

        
        return attrs

    def create(self,validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user

    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    class Meta():
        fields = ['username','password']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        