from rest_framework import permissions

class IsNotAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return False
        return True