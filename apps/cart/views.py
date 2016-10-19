from django.views.decorators.http import require_POST
from .logics import CartLogic
from utils.views import json_view
from utils.views import login_required
from django.shortcuts import render


@login_required
@require_POST
@json_view
def add_to_cart(request):
    user_id = request.user.id
    goods_id = int(request.POST['goods_id'])
    goods_num = int(request.POST['goods_num'])
    content = CartLogic.add_to_cart(user_id, goods_id, goods_num)
    return {'code': 1, 'content': content}


@login_required
@require_POST
@json_view
def delete_from_cart(request):
    user_id = request.user.id
    cart_id = int(request.POST['cart_id'])
    content = CartLogic.delete_from_cart(user_id, cart_id)
    return {'code': 1, 'content': content}


@login_required
@require_POST
@json_view
def getlist(request):
    user_id = request.user.id
    content = CartLogic.getlist(user_id)
    return {'code': 1, 'content': content}


@login_required
@require_POST
@json_view
def clear_carts(request):
    user_id = request.user.id
    content = CartLogic.clear_carts(user_id)
    return {'code': 1, 'content': content}


def cart(request):
    return render(request, 'cart.html')
