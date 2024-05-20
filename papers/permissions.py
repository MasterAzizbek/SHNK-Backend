from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "POST" or request.method == "POST":
            return True
        return request.user == obj.author or request.user.is_superuser

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.is_staff