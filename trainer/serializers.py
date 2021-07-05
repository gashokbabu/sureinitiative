from rest_framework import serializers
from .models import *

class TrainerSerializer(serializers.ModelSerializer):
    # profile_pic = serializers.ImageField(max_length=None,allow_empty_file=False,allow_null=True,required=False)
    class Meta:
        model = Teacher
        fields = ["id","name","gender","phone","profile_pic","qualification"]


