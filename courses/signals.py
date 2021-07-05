from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post,Grade


# @receiver(post_save, sender=Post)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.type == 'assignment':
            # batch1 = instance.batch
            # students = batch1.students.all()
            # print(students)
            # for student1 in students:
            #     g = Grade(student=student1,batch=batch1,assignment_name=instance.title)
            #     g.save()


# @receiver(post_save, sender=Post)
# def save_profile(sender, instance, **kwargs):
#     instance.save()
