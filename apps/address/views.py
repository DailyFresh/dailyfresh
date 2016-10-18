from django.views.decorators.http import require_POST
from .logics import AddrLogic
from utils.views import json_view
from utils.views import login_required


@login_required
@require_POST
@json_view
def add_one_address(request):
    user_id = request.user.id
    province = request.POST['province']
    city = request.POST['city']
    county = request.POST['county']
    addr_detail = request.POST['addr_detail']
    content = AddrLogic.add_one_address(
        user_id, province, city, county, addr_detail)
    return {'code': 1, 'content': content}


@login_required
@require_POST
@json_view
def delete_one_address(request):
    user_id = request.user.id
    addr_id = int(request.POST['addr_id'])
    content = AddrLogic.delete_one_address(user_id, addr_id)
    return {'code': 1, 'content': content}


@login_required
@require_POST
@json_view
def getlist(request):
    user_id = request.user.id
    content = AddrLogic.getlist(user_id)
    return {'code': 1, 'content': content}
