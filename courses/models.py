from django.db import models
from trainee.models import Student
from trainer.models import Teacher
# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    prerequisites = models.CharField(max_length=256)
    syllabus = models.FileField(upload_to='syllabus_files')
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.course_name}'

class Batch(models.Model):    
    batch_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True)
    students = models.ManyToManyField(Student)
    limit = models.IntegerField(default=40)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    is_active = models.BooleanField(default=True)
    meeting_code = models.CharField(max_length=100,null=True,blank=True)
    link_active = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.course} {self.batch_name}'
    
    class Meta:
        verbose_name_plural = "Batches"

class Post(models.Model):
    batch = models.ForeignKey(Batch,on_delete=models.SET_NULL,null=True)
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to='posted_materials',null=True,blank=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Grade(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='assignments',null=True,blank=True)
    marks = models.IntegerField(null=True,blank=True)


    def __str__(self):
        return f'{self.post.title}'


# class JitsiLink(models.Model):
#     batch = models.OneToOneField(Batch,on_delete=models.SET_NULL,null=True,blank=True)
#     link = models.CharField(max_length=256)

#     def __str__(self):
#         return f'{self.batch} link'