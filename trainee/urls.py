from django.urls import path,include
from rest_framework import routers
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('contactus', ContactUsViewset,basename='ContactUs'),
router.register('student', TraineeViewset),

urlpatterns = [
    path('',include(router.urls)),
]