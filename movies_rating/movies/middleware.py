from django.conf import settings
from django.shortcuts import redirect

from .models import Token
from django.urls import reverse_lazy, reverse


class AuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if (not request.user.is_authenticated and request.META.get('PATH_INFO') != '/'
                and 'media' not in request.META.get('PATH_INFO')):
            try:
                token = Token.objects.get(token=request.META.get('HTTP_AUTHORIZATION'))
                request.user = token.user
            except Token.DoesNotExist as ex:
                return redirect('home')
        elif request.user.is_authenticated and request.META.get('PATH_INFO') != '/':
            try:
                token = Token.objects.get(user_id=request.user.pk)
                request.user = token.user
            except Token.DoesNotExist as ex:
                return redirect('home')
        elif request.user.is_authenticated and request.META.get('PATH_INFO') == '/':
            try:
                token = Token.objects.get(user_id=request.user.pk)
                request.user = token.user
                return redirect('movie-list')
            except Token.DoesNotExist as ex:
                return redirect('home')
        return self.get_response(request)
