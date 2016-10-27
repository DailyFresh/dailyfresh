from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.contrib.auth import authenticate
from django.contrib.auth import login as _login
from django.contrib.auth import logout as _logout
from .logics import PassportLogic
from utils.views import json_view
from utils.views import login_required
from .exceptions import UsernamePasswordException
from apps.tasks.tasks import register_success_email
from django.shortcuts import render, redirect
from django.db import transaction
from .models import Passport


@require_http_methods(["GET", "POST"])
def login(request):
    """
    登录
    """
    if request.method == 'GET':
        return render(request, "login.html", {'error':False})
    else:
        username = request.POST['username']
        password = request.POST['pwd']
        user = authenticate(username=username, password=password)
        if user:
            _login(request, user)
            return redirect('/')
        else:
            return render(request, "login.html", {'error':True})
        #     raise UsernamePasswordException()
        # content = user.canonical()
        # content.pop('backend')
        # return {'code': 1, 'content': content}


@login_required
@require_GET
def logout(request):
    """
    登出
    """
    _logout(request)
    return redirect('/')


@require_http_methods(["GET", "POST"])
def register(request):
    """
    注册
    """
    if request.method == 'GET':
        return render(request, "register.html")
    else:
        username = request.POST['user_name']
        password = request.POST['pwd']
        email = request.POST.get('email', None)
        # sex = request.POST['sex']
        # realname = request.POST.get('realname', None)
        # province = request.POST.get('province', None)
        # city = request.POST.get('city', None)
        # county = request.POST.get('county', None)
        # addr_detail = request.POST.get('addr_detail', None)
        with transaction.atomic():
            Passport.create_one_passport(username, email, password)
            user = authenticate(username=username, password=password)
            _login(request, user)
            # _login(request, user)
        # content = PassportLogic.register(username, password, email)
        register_success_email.delay(username, email)
        return redirect('/')


@login_required
@require_POST
@json_view
def reset_password(request):
    """
    密码重置
    """
    user_id = request.user.id
    old_password = request.POST['old_password']
    new_password = request.POST['new_password']
    print(user_id, old_password, new_password)
    content = PassportLogic.reset_password(user_id, old_password, new_password)
    return {'code': 1, 'content': content}
