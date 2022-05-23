from django.urls import path
from .views import LoginView, TeacherApi, ClassListApi, CollegeApi,RegisterStudentAPIView



urlpatterns = [

    path('teacherapi/', TeacherApi.as_view()),
    path('teacherapi/<int:pk>/',TeacherApi.as_view()),
    path('classlistapi/', ClassListApi.as_view()),
    path('classlistapi/<int:pk>/',ClassListApi.as_view()),
    path('collegeapi/', CollegeApi.as_view()),
    path('collegeapi/<int:pk>/',CollegeApi.as_view()),
    path('register/',RegisterStudentAPIView.as_view()),
    path('login/',LoginView.as_view()),
    
    
    

]


    