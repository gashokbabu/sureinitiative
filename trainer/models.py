from django.db import models
from users.models import User
# Create your models here.
# class Qualification(models.Model):
#     qualification = models.CharField(max_length=100)
#     def __str__(self):
#         return f'{self.qualification}'

class Teacher(models.Model):
    Choices = (
        ('male','male'),
        ('female','female')
    )
    Qualifications=(
        ('b.tech','b.tech'),
        ('m.tech','m.tech')
    )
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=100,choices=Choices,default="male")  
    phone = models.PositiveBigIntegerField(blank=True, null=True,unique=True)
    qualification = models.CharField(max_length=100,null=True)
    profile_pic = models.ImageField(default="default.jpg",upload_to='profile_pics')

    def __str__(self):
        return f'{self.name}'


