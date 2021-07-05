from django.http.response import JsonResponse
from courses.serializers import BatchSerializer, PostSerializer
from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view,permission_classes
from .serializers import *
from .models import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated,AllowAny
from rest_framework import status
from rest_framework.response import Response
from trainee.models import Student
from trainer.models import Teacher
from courses.models import *
from allauth.account.models import EmailAddress
import random
import datetime
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import Group
class UserViewset(viewsets.ModelViewSet):
    #'list':[IsAdminUser],'retrieve':[IsAdminUser],'update':[IsAuthenticated]
    permission_classes=[IsAuthenticated]
    permission_classes_by_action = {'create':[AllowAny]}
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except:
            return [permission() for permission in self.permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        u = User.objects.get(email=request.data['email'])
        rdm = random.randrange(1111,9999)
        year = datetime.datetime.today().strftime("%y")
        digit = str(year) + str(rdm)
        while(Student.objects.filter(registration_no=int(digit)).exists()):
            rdm = random.randrange(1111,9999)
            year = datetime.datetime.today().strftime("%y")
            digit = str(year) + str(rdm)
        Student.objects.create(user=u,name=request.data['name'],gender=request.data['gender'],phone=request.data['phone'],registration_no=digit,qualification=request.data['qualification'])
        token = Token.objects.get_or_create(user=u)
        e = EmailAddress.objects.create(email=request.data['email'],user=u)
        e.send_confirmation(request)
        e.save()
        print(request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    



@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def yourBatches(request):
    user = request.user
    b = Batch.objects.filter(students__user=user)
    serializer = BatchSerializer(b,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def batch_posts(request,id):
    b = Batch.objects.get(id=id)
    posts = b.post_set.all()
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def add_to_course(request,id):
    if request.method == 'POST':
        course = Course.objects.get(pk=id)
        b = course.batch_set.all().order_by('start_date')
        serializer = BatchSerializer(b,many=True)
        if Batch.objects.filter(students__user=request.user,is_active=True).count() >= 3:
            print(Batch.objects.filter(students__user=request.user).count())
            return Response({'error':'Student is registered in more than 3 batches'})
        if len(b) == 0:
            new_batch = Batch.objects.create(course=course,batch_name="Batch-1")
            new_batch.students.add(request.user.student)
            new_batch.save()
            return Response({'message':f'student is added to {new_batch.batch_name}'})
        elif Batch.objects.filter(students__user=request.user,course__id=id).exists():
            return Response({"error":"student already enrolled"})
        elif len(b[len(b)-1].students.all()) == b[len(b)-1].limit:
            x = int(b[len(b)-1].batch_name[6:])
            x+=1
            new_batch = Batch.objects.create(course=course,batch_name=b[len(b)-1].batch_name[0:6]+str(x))
            new_batch.students.add(request.user.student)
            new_batch.save()
            return Response({'success':f'student is added to new {new_batch.batch_name}'})
        else:
            b[len(b)-1].students.add(request.user.student)
            return Response({'success':f'student is added to {b[len(b)-1].batch_name}'})
    return Response({'error':'something went wrong'})

@api_view(['POST'])
def get_token(request):
    print(request.data)
    u = User.objects.filter(email=request.data['email']).exists()
    if u==True:
        user = EmailAddress.objects.get(email=request.data['email'])
        if user.verified==True:
            u = User.objects.get(email=request.data['email'])
            if check_password(request.data['password'],u.password):
                token = Token.objects.get(user=u)
                print(token)
                if request.data['login_as']=='student':
                    regno = Student.objects.get(user=u).registration_no
                    return Response({"token":token.key,'user_id':u.id,'regno':regno})
                elif request.data['login_as']=='teacher':
                    # group = Group.objects.get(name='teachers')
                    # if u.groups.filter(name=group):
                    if u.is_staff == True:
                        return Response({'token':token.key,'teacher_id':token.user.teacher.id})
                    else:
                        return Response({"error":"please register as teacher"})                    
            else:
                return Response({"error":"password incorrect"})
        else:
            return Response({'error':'please verify the email before login'})
    else:
        return Response({"error":"please register first before login"})

