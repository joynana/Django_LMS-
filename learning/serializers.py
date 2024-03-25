from rest_framework import serializers
from .models import Student,Lecture


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','student', 'grade')
        #extra_kwargs = {"article": {"read_only": True}} - 이건 모르겠다..


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id','teacher', 'title','grade','subject')
        #extra_kwargs = {"article": {"read_only": True}} - 이건 모르겠다..



