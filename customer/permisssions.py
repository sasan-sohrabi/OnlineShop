from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsSuperuserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)