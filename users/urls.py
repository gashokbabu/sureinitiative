from django.urls import path,include
from rest_framework import routers
from rest_framework import routers
from .views import *
from django.contrib.auth import views as auth_views


router = routers.DefaultRouter()
router.register(r'', UserViewset)

urlpatterns = [
    path('your-batches/',yourBatches),
    path('batch-posts/<int:id>/',batch_posts),
    path('add-to-course/<int:id>/',add_to_course),
    path('get-token/',get_token),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name = "users/password_reset.html"),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name ="users/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_done.html"), name="password_reset_complete"),
    path('',include(router.urls)),
]