"""suretrust URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views
from users.views import get_token
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='build/index.html')),
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('get-token/', get_token),
    path('teacher/',include('trainer.urls')),
    path('student/',include('trainee.urls')),
    path('courses/',include('courses.urls')),
    path('users/',include('users.urls')),
    path('discussion/',include('discussion.urls')),  # this urls can use to add data in th comment
    # path('discussion_view/', view_discussion.as_view()),# to see all the data in the disscussion section
]
admin.site.site_header = 'Suretrust Administation'
admin.site.index_title = 'Admin Pannel'
admin.site.site_title = 'Suretrust'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)