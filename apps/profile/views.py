from django.views.decorators.http import require_POST
from .logics import ProfileLogic
from utils.views import json_view
from utils.views import login_required


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
