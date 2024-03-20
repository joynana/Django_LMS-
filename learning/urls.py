from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    # path(' ', views.data),
    
    path("", views.student_list),
     #유저가 들은 강의 목록을 만들어 주고 싶어
    path("student/<int:student_id>/lectures/", views.lectures_list),
    path("lecture/<int:lecture_id>/student/", views.student_view),
    
]