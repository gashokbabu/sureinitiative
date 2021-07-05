from django.contrib import admin
from .models import Student,ContactUs
# Register your models here.
from courses.models import Batch
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','registration_no','gender','phone','batches']
    list_filter = ('user__date_joined','gender',)
    list_per_page = 25
    search_fields = ('name','registration_no')

    def batches(self,obj):
        batch = ''
        for b in Batch.objects.filter(students=obj):
            batch += f'{b.course} {b.batch_name},'
        return batch[0:-1]
        
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['student','subject','resolved']
    list_filter = ['date','resolved']
    list_per_page = 25

admin.site.register(Student,StudentAdmin)
admin.site.register(ContactUs,ContactUsAdmin)