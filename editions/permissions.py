from rest_framework.permissions import BasePermission



class IsSuperUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return request.user.is_superuser or request.user.is_staff