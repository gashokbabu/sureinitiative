from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

class TraineeViewset(viewsets.ModelViewSet):
    pagination_class = None
    permission_classes=[IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = TraineeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class ContactUsViewset(viewsets.ModelViewSet):
    pagination_class = None
    permission_classes=[AllowAny]
    serializer_class = ContactUsSerializer
    def get_queryset(self):
        return ContactUs.objects.filter(student__user=self.request.user).order_by('-date')