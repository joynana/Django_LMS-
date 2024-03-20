from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student, Teacher, Lecture
from .serializers import StudentSerializer, LectureSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# def data(request):
#     data = {"name": "Jun", "age": 17, "city": "Seoul"}
#     return JsonResponse(data)

#학생 데이터 만들기 
def create(request):
    student = Student(ST_id ='goeun1', grade= '중1')
    student.save()

    return HttpResponse(student)

#강의 수강한 기록 만들기 
def create(request):
    student = Student(ST_id ='goeun1', grade= '중1')
    student.save()

    return HttpResponse(student)

@api_view(['GET'])
def student_list(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def lectures_list(request,student_id):
    #student =request.user #토큰을 안받았으니까 이 코드 쓰면 안됌
    student = Student.objects.get(id= student_id) #보고싶은 student id를 가져온다
    lecture = student.lecture_stu.all() #해당 스튜던트가 가지고 있는 강좌 모두 가져와
    serializer = LectureSerializer(lecture, many=True) #lecture를 보여주고 싶다. 
    return Response(serializer.data)


@api_view(['GET'])
def student_view(request,lecture_id):
    #student =request.user #토큰을 안받았으니까 이 코드 쓰면 안됌
    lecture = Lecture.objects.get(id= lecture_id) #보고싶은 lecture id를 가져온다
    student = lecture.students.all() #해당 강좌가 가지고 있는 모든 학생들 가져와 
    serializer = StudentSerializer(student, many=True) #student를 보여주고 싶음
    return Response(serializer.data)