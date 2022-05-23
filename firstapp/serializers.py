from dataclasses import fields
from rest_framework import serializers
from firstapp.models import *
from rest_framework import status
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password

class ClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassList
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','first_name','last_name','username','email','phone','classlist_id','teacher_id','address']

#Serializer to Register Student

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField( required=True,
    validators=[UniqueValidator(queryset=Student.objects.all())])
    password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    teacher_id = serializers.CharField(required=True)
    classlist_id = serializers.CharField(required=True)


    class Meta:
        model = Student
        fields = ('first_name','last_name','username','email','phone','classlist_id','teacher_id','address','password','password2')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}

        }
    def validate(self, attrs):
        if attrs['password']!= attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields did not match."})
        return attrs

    def create(self, validate_data):
        student = Student.objects.create(
            username=validate_data['username'],
            email=validate_data['email'],
            first_name=validate_data['first_name'],
            last_name=validate_data['last_name'],
            phone=validate_data['phone'],
            address=validate_data['address'],
            teacher_id=validate_data['teacher_id'],
            classlist_id=validate_data['classlist_id'],

        )
        student.set_password(validate_data['password'])
        student.save()
        return student

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(LoginSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token








