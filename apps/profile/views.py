from django.views.decorators.http import require_http_methods, require_POST
from .logics import ProfileLogic
from utils.views import json_view
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.address.models import Address
from .models import BrowseHistory


@login_required
@require_POST
@json_view
def update_profile(request):
    user_id = request.user.id
    sex = request.POST['sex']
    realname = request.POST.get('realname', None)
    province = request.POST.get('province', None)
    city = request.POST.get('city', None)
    county = request.POST.get('county', None)
    addr_detail = request.POST.get('addr_detail', None)
    content = ProfileLogic.update_profile(user_id, sex, realname, province,
                                          city, county, addr_detail)
    return {'code': 1, 'content': content}


@login_required
@require_POST
@json_view
def get_profile(request):
    user_id = request.user.id
    content = ProfileLogic.get_profile(user_id)
    return {'code': 1, 'content': content}

@login_required
def profile(request):
    try:
        address = Address.objects.get(user=request.user)
    except Address.DoesNotExist:
        address = None 

    # 不支持distinct去重，只能手动去重
    # browse_history = BrowseHistory.objects.filter(user=request.user).order_by('-create_time').distinct('goods')[:5]
    browse_history = BrowseHistory.objects.filter(user=request.user).order_by('-create_time')
    history_goods_li = []
    goods_ids = []
    num = 0
    for item in browse_history:
        goods = item.goods
        if goods.id not in goods_ids:
            num += 1
            goods_ids.append(goods.id)
            goods.price = "%.2f" % goods.goods_price
            goods.img = goods.image_set.all()[0].img_url
            history_goods_li.append(goods)
            if 5 == num:
                break
    return render(request, "user_center_info.html", {"address":address, "history_goods_li":history_goods_li})
