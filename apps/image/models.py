from django.db import models
from utils.models import BaseModel
from apps.goods.models import *


class Image(BaseModel):

    """
    图片存储
    """

    img_product_id = models.ForeignKey(Goods, help_text='商品ID')
    img_url = models.ImageField(
        upload_to='productimages', blank=False, help_text='图片url路径')
    img_type = models.CharField(max_length=64, help_text='图片mime类型')
    img_is_def = models.BooleanField(default=False, help_text='是否默认')

    class Meta:
        db_table = 's_image'

    # @classmethod
    # def upload_image(cls, img_name, img_url, img_width, img_height, img_type):
    #     data = cls.add_one_object(
    #         img_name=img_name, img_url=img_url,
    #         img_width=img_width, img_height=img_height, img_type=img_type)
    #     return data.canonical()

    @classmethod
    def get_image(cls, file_id):
        return cls.objects.filter(img_product_id=file_id).first()
