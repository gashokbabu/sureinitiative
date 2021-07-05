from django.urls import path,include
from rest_framework import routers
from .views import *
from .models import *

router = routers.DefaultRouter()
router.register('discussiondummy', DiscussionDummyViewset,basename='discussion_Comment')
router.register('discussion', DiscussionViewset,basename='discussion_Comment')


urlpatterns = [
    path('',include(router.urls)),
]