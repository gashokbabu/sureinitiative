from django.contrib import admin
from .models import Teacher
# Register your models here.
# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ['name','qualification','gender','phone']
#     list_filter = ('user__date_joined','gender','qualification')
#     search_fields = ('name','qualification','phone')
admin.site.register(Teacher)
