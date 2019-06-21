from rest_framework.permissions import BasePermission


class IsAuthenticatedOrReadOnlyCustom(BasePermission):

    def has_permission(self, request, view):
        return (request.method.lower() == 'get' or request.user.is_authenticated) or (request.method.lower() == 'post'
                                                                                      and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method.lower() == 'get' or request.user.is_authenticated) or (request.method.lower() in
                                                             ['delete', 'put'] and request.user.is_authenticated)


class AuthAndModifyMovieRateCustom(BasePermission):

    def has_permission(self, request, view):
        return request.method.lower() == 'get' or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (request.method.lower() == 'get' or request.user.is_authenticated) or request.method.lower() \
        in ['delete', 'put'] and request.user.is_authenticated and request.user.is_superuser
