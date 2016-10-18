from django.views.decorators.http import require_POST
from .logics import GoodsLogic
from utils.views import json_view
from utils.views import login_required
from django.shortcuts import render


def home_list_page(request):
    return render(request,'index.html')


# @require_POST
# @json_view
# def add_one_goods(request):
#     goods_type_id = int(request.POST['goods_type_id'])
#     goods_type_name = request.POST['goods_type_name']
#     goods_name = request.POST['goods_name']
#     goods_price = float(request.POST['goods_price'])
#     goods_ex_price = float(request.POST['goods_ex_price'])
#     file_ids = request.POST['file_ids']
#     goods_status = int(request.POST['goods_status'])
#     content = GoodsLogic.add_one_goods(
#         goods_type_id, goods_type_name, goods_name, goods_price,
#         goods_ex_price, file_ids, goods_status)
#     return {'code': 1, 'content': content}


# @login_required
# @require_POST
# @json_view
# def delete_one_goods(request):
#     goods_id = int(request.POST['goods_id'])
#     content = GoodsLogic.delete_one_goods(goods_id)
#     return {'code': 1, 'content': content}


@json_view
def get_goods_info(request):
    content = GoodsLogic.get_goods_info()
    return {'code': 1, 'content': content}


# @login_required
# @require_POST
# @json_view
# def update_one_goods(request):
#     goods_id = int(request.POST['goods_id'])
#     goods_type_id = int(request.POST['goods_type_id'])
#     goods_type_name = request.POST['goods_type_name']
#     goods_name = request.POST['goods_name']
#     goods_price = float(request.POST['goods_price'])
#     goods_ex_price = float(request.POST['goods_ex_price'])
#     file_ids = request.POST['file_ids']
#     goods_status = int(request.POST['goods_status'])
#     content = GoodsLogic.update_one_goods(
#         goods_id, goods_type_id, goods_type_name, goods_name, goods_price,
#         goods_ex_price, file_ids, goods_status)
#     return {'code': 1, 'content': content}


@login_required
@require_POST
@json_view
def get_one_goods(request):
    goods_id = int(request.POST['goods_id'])
    content = GoodsLogic.get_one_goods(goods_id)
    return {'code': 1, 'content': content}


@json_view
def getlist(request):
    content = GoodsLogic.getlist()
    return {'code': 1, 'content': content}


@login_required
@require_POST
@json_view
def search(request):
    text = request.POST['text']
    content = GoodsLogic.search(text)
    return {'code': 1, 'content': content}
