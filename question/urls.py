from django.urls import path
from .views import *


urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('signup/',SignUpView.as_view(),name='signup'),
    path('student/',CreateGetStudentView.as_view(),name='student'),
    path('student/<int:pk>/',UpdateStudentView.as_view(),name='student')

]