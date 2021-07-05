from trainer.permissions import ReadOnly
from trainer.serializers import TrainerSerializer
from rest_framework import serializers
from rest_framework.fields import NOT_REQUIRED_DEFAULT, TimeField
from .models import *
from trainee.serializers import TraineeSerializer

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    class Meta:
        model = Batch
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    student = TraineeSerializer(read_only=True)
    class Meta:
        model = Grade
        fields = '__all__'

        