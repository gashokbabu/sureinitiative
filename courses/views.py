from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated,AllowAny
from trainer.permissions import TrainerAccessPermission,ReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from trainee.serializers import TraineeSerializer
from rest_framework.parsers import FileUploadParser
from trainer.models import Teacher
class CourseViewset(viewsets.ModelViewSet):
    permission_classes=[TrainerAccessPermission|ReadOnly]
    serializer_class = CourseSerializer
    pagination_class=None
    def get_queryset(self):
        if self.request.user.is_staff:
            return Course.objects.filter(batch__teacher__user=self.request.user).distinct()
        else:
            return Course.objects.filter(batch__students=self.request.user.student,batch__is_active=True).distinct()

class BatchViewset(viewsets.ModelViewSet):
    permission_classes=[TrainerAccessPermission|ReadOnly]
    serializer_class = BatchSerializer
    pagination_class=None
    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_staff:
            course_id = self.request.headers['course-id']
            course_id = int(course_id)
            return Batch.objects.filter(teacher__user=self.request.user,course__id=course_id)
        else:
            return Batch.objects.filter(students=self.request.user.student)
class PostViewset(viewsets.ModelViewSet):
    permission_classes=[TrainerAccessPermission|ReadOnly]
    serializer_class = PostSerializer
    pagination_class=PageNumberPagination
    def get_queryset(self):
        batch_id = self.request.headers['batch-id']
        batch_id = int(batch_id)
        if self.request.user.is_staff:
            return Post.objects.filter(batch__teacher__user=self.request.user,batch__id=batch_id).order_by('-date_time')
        else:
            # course_id = self.request.headers['course-id']
            # batch_id = Batch.objects.filter(students__user=self.request.user,course__id=course_id)[0]
            return Post.objects.filter(batch__students__user=self.request.user,batch__id=batch_id).order_by('-date_time')
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        if serializer.data['type'].lower() == 'assignment':
            post = Post.objects.get(id=serializer.data['id'])
            batch1 = Batch.objects.get(id=serializer.data['batch'])
            students = batch1.students.all()
            print(students)
            for student1 in students:
                g = Grade(student=student1,post=post)
                g.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class GradeViewSet(viewsets.ModelViewSet):
    pagination_class = None
    permission_classes=[TrainerAccessPermission|ReadOnly]
    serializer_class = GradeSerializer
    def get_queryset(self):
        if self.request.user.is_staff:
            user = self.request.user
            post_id = self.request.headers['post-id']
            return Grade.objects.filter(post__id=post_id).order_by('-date')
        else:
            post_id = self.request.headers['post-id']
            return Grade.objects.filter(post__id=post_id,student__user=self.request.user).order_by('-date')


@api_view(['POST'])
@permission_classes([TrainerAccessPermission])
def studentsOfBatch(request):
    if request.method == 'POST':
        batch_id = request.data['batch_id']
        batch=Batch.objects.get(id=batch_id)
        students = batch.students.all()
        serializer = TraineeSerializer(students,many=True)
        return Response(serializer.data)
    else:
        return Response({'error':'only post request is allowed'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assignmentPosts(request):
    if request.user.is_staff:
        batch_id = request.data['batch_id']
        posts = Post.objects.filter(batch__teacher__user=request.user,type='assignment',batch__id=batch_id).order_by('-date_time')
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    else:
        course_id = request.data['course_id']
        batch = Batch.objects.filter(students__user=request.user,course__id=course_id).first()
        posts = Post.objects.filter(batch=batch,type="assignment").order_by('-date_time')
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)


    


@api_view(['Get'])
@permission_classes([AllowAny])
def getAllCourses(request):
    courses = Course.objects.all().order_by('id')
    serializer = CourseSerializer(courses,many=True)
    return Response(serializer.data)

@api_view(['Get'])
@permission_classes([AllowAny])
def getCourse(request,id):
    course = Course.objects.get(id=id)
    serializer = CourseSerializer(course)
    return Response(serializer.data)

@api_view(['Get'])
@permission_classes([AllowAny])
def getCourseTeachers(request,id):
    course = Course.objects.get(id=id)
    batches = course.batch_set.values('teacher').order_by('batch_name')
    li = []
    for i in batches:
        if i['teacher'] == None:
            continue
        li.append(i['teacher'])
    print(li)
    teachers = Teacher.objects.filter(id__in=li).distinct()
    serializer = TrainerSerializer(teachers,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def PostALL(request):
    batches = Batch.objects.filter(is_active=True)
    print(request.data)
    for batch in batches:
        request.data.update({'batch':batch.id})
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({'error':'something went wrong'})
    return Response({'success':'message send to all students'})







