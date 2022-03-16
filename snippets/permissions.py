from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        #With this line we will always allows connection with GET methode
        if request.method in permissions.SAFE_METHODS:
            return True
        #This line specifies return boolean : True when there is a match between the user connected and the owner of the object
        return obj.owner == request.user