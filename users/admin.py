# from __future__ import unicode_literals
# from django.contrib import admin
# from .models import User
# # from django.contrib.auth.admin import UserAdmin

# # Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     fields=('email','first_name','last_name','password','is_active','is_staff','is_superuser','groups','user_permissions','last_login','date_joined')
#     list_filter = ['groups']
#     list_per_page = 25
# admin.site.register(User,UserAdmin)


from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['id','email', 'is_superuser']
    list_filter = ['is_superuser','groups']
    # fields=('email','first_name','last_name','password','is_active','is_staff','is_superuser','groups','user_permissions','last_login','date_joined')
    fieldsets = (
        (None, {'fields': ('email', 'password','is_active','is_staff','groups','last_login','date_joined')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_superuser',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password','password_2')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    list_per_page = 25
    filter_horizontal = ()


admin.site.register(User, UserAdmin)