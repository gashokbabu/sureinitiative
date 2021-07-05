from rest_framework import serializers
from .models import User
from trainee.serializers import TraineeSerializer
from trainer.serializers import TrainerSerializer
class UserDummySerializer(serializers.ModelSerializer):
    student = TraineeSerializer()
    teacher = TrainerSerializer()
    class Meta:
        model = User
        extra_kwargs = {'password':{'write_only':True}}
        fields = ('id','email','password','student','teacher')