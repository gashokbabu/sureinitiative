from django.contrib.auth.models import Group
from rest_framework.permissions import BasePermission, BasePermissionMetaclass, IsAuthenticated, SAFE_METHODS
class TrainerAccessPermission(BasePermission):

    def has_permission(self, request, view):
        print(request.user)
        user = request.user
        # group = Group.objects.get(name='teachers')
        # if user.groups.filter(name=group):
        #     return True
        # else:
        #     return  False
        return bool(request.user and request.user.is_authenticated and user.is_staff)


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in ('GET', 'HEAD', 'OPTIONS','PUT')
