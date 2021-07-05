from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from .permissions import TrainerAccessPermission

class TrainerViewset(viewsets.ModelViewSet):
    pagination_class = None
    permission_classes=(TrainerAccessPermission,)
    queryset = Teacher.objects.all()
    serializer_class = TrainerSerializer