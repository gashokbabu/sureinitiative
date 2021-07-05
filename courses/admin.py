from django.contrib import admin
from .models import Course,Post,Batch,Grade
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','batch','type',]
    list_filter = ('type','batch','date_time','batch__teacher__name')
    search_fields = ('title','content','batch__teacher__name')
    list_per_page = 50

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','course_name','prerequisites']
    list_filter = ('date',)
    search_fields = ('course_name','prerequisites')
    list_per_page = 10
class BatchAdmin(admin.ModelAdmin):
    list_display = ['id','batch_name','course','teacher']
    list_filter = ('batch_name','course','teacher__name')
    search_fields = ('batch_name','course')
    list_per_page = 10

class GradeAdmin(admin.ModelAdmin):
    list_display = ['id','post','date','marks']
    list_filter = ('post__batch','post__batch__course','post__batch__teacher')
    search_fields = ['post__title']
    list_per_page = 10


admin.site.register(Course,CourseAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Batch,BatchAdmin)
admin.site.register(Grade,GradeAdmin)