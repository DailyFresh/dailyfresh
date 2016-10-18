from django.http import JsonResponse, HttpResponse
import functools
from apps.passport.exceptions import AnonymousException


def json_view(func):
    def wrapped(request, *args, **kwargs):
        data = func(request, *args, **kwargs)
        return JsonResponse(data)
    return wrapped


def string_view(func):
    def wrapped(request, *args, **kwargs):
        data = func(request, *args, **kwargs)
        return HttpResponse(data)
    return wrapped


def login_required(func):
    @functools.wraps(func)
    def decorator(request, *args, **kwargs):
        if not request.user.is_authenticated():
            raise AnonymousException()
        return func(request, *args, **kwargs)
    return decorator
