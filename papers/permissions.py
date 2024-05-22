from rest_framework.permissions import BasePermission
from rest_framework import permissions
from users.models import CustomUser

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user == obj.author:
            return True
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.is_staff
    
class IsReviewer(BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.filter(is_reviewer=True)
        if request.user in user:
            return True
        return request.user.is_superuser or request.user.is_staff 