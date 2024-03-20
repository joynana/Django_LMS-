from django.db import models

# Create your models here.

#학생 모델을 만듭니다. 
class Student(models.Model):
    #학생ID , 학년
    student = models.CharField(max_length=10)
    grade = models.CharField(max_length=10)
#강사 모델
class Teacher(models.Model):
#학생ID , 학년
    #teacher = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    subject = models.CharField(max_length=10)


#강의 모델 만들기 (강사와 1:N의 관계를 맺는다. )
class Lecture(models.Model):
    #학생ID , 학년
    #Foriegn 키로 설정해야 하는데 
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE ) #강사 모델을 안만들었어
    students = models.ManyToManyField(Student, related_name = 'lecture_stu')
    title = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    subject = models.CharField(max_length=10)


