from django.urls import path,include
from rest_framework import routers
from .views import *
from .models import *

router = routers.DefaultRouter()
router.register(r'course', CourseViewset,basename='Course')
router.register(r'batch',BatchViewset,basename='Batch')
router.register(r'posts',PostViewset,basename='Post')
router.register(r'grades',GradeViewSet,basename='Grade')

urlpatterns = [
    path('students-of-batch/',studentsOfBatch),
    path('assignment-posts/',assignmentPosts),
    path('get-all-courses/',getAllCourses),
    path('get-course/<int:id>/',getCourse),     
    path('get-course-teachers/<int:id>/',getCourseTeachers),
    path('post-all/',PostALL),
    path('',include(router.urls)),
]