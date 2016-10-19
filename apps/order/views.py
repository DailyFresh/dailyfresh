from django.views.decorators.http import require_POST
from .logics import OrderLogic
from utils.views import json_view
from utils.views import login_required
from django.shortcuts import render


@login_required
@require_POST
@json_view
def add_one_order(request):
    user_id = request.user.id
    goods_id = int(request.POST['goods_id'])
    addr_id = int(request.POST['addr_id'])
    goods_price = float(request.POST['goods_price'])
    goods_num = int(request.POST['goods_num'])
    goods_ex_price = float(request.POST['goods_ex_price'])
    payment_method = int(request.POST['payment_method'])
    order_status = int(request.POST['order_status'])
    content = OrderLogic.add_one_order(
        user_id, goods_id, addr_id, goods_price, goods_num, goods_ex_price,
        payment_method, order_status)
    return {'code': 1, 'content': content}


@login_required
@require_POST
@json_view
def delete_one_order(request):
    user_id = request.user.id
    order_id = int(request.POST['order_id'])
    content = OrderLogic.delete_one_order(user_id, order_id)
    return {'code': 1, 'content': content}


@login_required
@require_POST
@json_view
def cancel_one_order(request):
    user_id = request.user.id
    order_id = int(request.POST['order_id'])
    content = OrderLogic.cancel_one_order(user_id, order_id)
    return {'code': 1, 'content': content}


@login_required
@require_POST
@json_view
def getlist(request):
    user_id = request.user.id
    content = OrderLogic.getlist(user_id)
    return {'code': 1, 'content': content}

def my_order(request):
    return render(request, 'user_center_order.html')
