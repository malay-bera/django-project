from rest_framework.permissions import AllowAny
from django.http import Http404
from .models import *
from .serializers import RegisterSerializer, TeacherSerializer,ClassListSerializer,CollegeSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView


class TeacherApi(APIView):
    def get_object(self, pk):
        try:
            return Teacher.objects.filter(pk=pk).first()
        except Teacher.DoesNotExist:
            raise Http404

    def get(self,request, format=None):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk, format=None):
        teacher = self.get_object(pk)
        teacher.delete()
        return Response(status=status.HTTP_201_CREATED)
    
    def put(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)





class ClassListApi(APIView):
    def get_object(self, pk):
        try:
            return ClassList.objects.filter(pk=pk).first()
        except ClassList.DoesNotExist:
            raise Http404

    def get(self,request, format=None):
        class_list = ClassList.objects.all()
        serializer = ClassListSerializer(class_list, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = ClassListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk, format=None):
        class_list = self.get_object(pk)
        class_list.delete()
        return Response(status=status.HTTP_201_CREATED)
    
    def put(self, request, pk, format=None):
        class_list = self.get_object(pk)
        serializer = ClassListSerializer(class_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



class CollegeApi(APIView):
    def get_object(self, pk):
        try:
            return College.objects.filter(pk=pk).first()
        except College.DoesNotExist:
            raise Http404

    def get(self,request, format=None):
        college = College.objects.all()
        serializer = CollegeSerializer(college, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk, format=None):
        college = self.get_object(pk)
        college.delete()
        return Response(status=status.HTTP_201_CREATED)
    
    def put(self, request, pk, format=None):
        college = self.get_object(pk)
        serializer = CollegeSerializer(college, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class RegisterStudentAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

















