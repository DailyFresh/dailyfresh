from django.views.decorators.http import require_POST
from .logics import GoodsLogic
from utils.views import json_view
from utils.views import login_required
from django.shortcuts import render
from .enums import *
from apps.cart.models import Cart
from apps.profile.models import BrowseHistory
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage


def home_list_page(request):
    fruits = GoodsLogic.get_goods_by_type(FRUITS, HOME_ITEM_NUMS) 
    seafood = GoodsLogic.get_goods_by_type(SEAFOOD, HOME_ITEM_NUMS) 
    meat = GoodsLogic.get_goods_by_type(MEAT, HOME_ITEM_NUMS) 
    eggs = GoodsLogic.get_goods_by_type(EGGS, HOME_ITEM_NUMS) 
    vegetables = GoodsLogic.get_goods_by_type(VEGETABLES, HOME_ITEM_NUMS) 
    frozen = GoodsLogic.get_goods_by_type(FROZEN, HOME_ITEM_NUMS) 
    cart = {'goods_num__sum':0}
    if request.user.is_authenticated():
        cart = Cart.objects.filter(user=request.user).aggregate(Sum('goods_num'))
    return render(request,'index.html', {'fruits':fruits, 'seafood':seafood, 'meat':meat, 'eggs':eggs, 'vegetables':vegetables, 'frozen':frozen, 'cart':cart['goods_num__sum']})

def goods_detail(request, goods_id):
    goods = GoodsLogic.get_one_goods(goods_id)
    comments = goods.sordergoods_set.all().order_by('-create_time')[:30]
    for comment in comments:
        comment.ctime = comment.create_time.strftime('%Y-%m-%d %H:%M:%S')
        comment.user = comment.sorder.user.username
    new_goods_li = GoodsLogic.get_goods_by_type(goods.goods_type_id, limit=2, sort='new')
    cart = {'goods_num__sum':0}
    if request.user.is_authenticated():
        cart = Cart.objects.filter(user=request.user).aggregate(Sum('goods_num'))
        BrowseHistory.add_one_object(user=request.user, goods=goods)
    return render(request, 'detail.html', {'goods':goods, 'cart':cart['goods_num__sum'], 'new_goods_li':new_goods_li, 'comments':comments})

def goods_list(request, goods_type_id, page):
    goods_type_id = int(goods_type_id)
    page = int(page)
    sort = request.GET.get('sort', 'default')
    new_goods_li = GoodsLogic.get_goods_by_type(goods_type_id, limit=2, sort='new')
    goods_li_all = GoodsLogic.get_goods_by_type(goods_type_id, sort=sort)
    cart = {'goods_num__sum':0}
    if request.user.is_authenticated():
        cart = Cart.objects.filter(user=request.user).aggregate(Sum('goods_num'))
    paginator = Paginator(goods_li_all, LIST_PAGE_CAPACITY)
    try:
        goods_li = paginator.page(page)
    except EmptyPage:
        goods_li = paginator.page(paginator.num_pages)
        page = paginator.num_pages
    # 分页页数显示计算
    num_pages = paginator.num_pages
    if num_pages <= 5:
        pages = paginator.page_range
    elif (num_pages - page) < 2:
        pages = [x for x in range(num_pages-4, num_pages+1)]
    elif page < 3:
        pages = [x for x in range(1, 6)]
    else:
        pages = [x for x in range(page-2, page+3)]
    pre_page = page - 1
    next_page = page + 1 if page < num_pages else 0

    return render(request, 'list.html', {'sort':sort, 'type_name':GOODS_TYPE[goods_type_id], 'type_id':goods_type_id, 'new_goods_li':new_goods_li, 'goods_li':goods_li, 'cart':cart['goods_num__sum'], 'pre_page':pre_page, 'next_page':next_page, 'pages':pages, 'active_page':page})


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
