from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .logics import ImageLogic
from utils.views import json_view


# @require_POST
# @json_view
# def upload_image(request):
#     """
#     上传图片
#     """
#     image = request.FILES.get('image', None)
#     print(image)
#     content = ImageLogic.upload_image(image)
#     return {'code': 1, 'content': content}


def get_image(request, file_id):
    data = ImageLogic.get_image(file_id)
    img_url = data.img_url
    img_type = data.img_type
    return HttpResponse(img_url, content_type=img_type)
