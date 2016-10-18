from django.db import models
from utils.models import BaseModel
from jsonfield import JSONField


class Goods(BaseModel):

    """
    商品表
    """
    YES = 1
    NO = 2

    ONLINE = 1
    OFFLINE = 2
    DELETED = 3

    goods_type_id = models.SmallIntegerField(default=1, help_text='商品分类ID')
    goods_type_name = models.CharField(
        default="", max_length=32, help_text="商品分类的名字")
    goods_name = models.CharField(default="", max_length=64, help_text='商品名称')
    goods_price = models.FloatField(default=0.0, help_text='商品价格')
    goods_unit = models.IntegerField(default=1,help_text='商品单位')
    goods_ex_price = models.FloatField(default=0.0, help_text='商品运费')
    goods_info = models.TextField(help_text='商品描述')
    goods_status = models.IntegerField(default=ONLINE, help_text='商品状态')

    class Meta:
        db_table = 's_goods'

    @classmethod
    def delete_one_goods(cls, goods_id):
        data = cls.objects.get(id=goods_id)
        data.goods_status = cls.DELETED
        data.save()
        return data

    @classmethod
    def get_goods_info(cls):
        return cls.objects.distinct(*('goods_type_id', 'goods_name'))

    @classmethod
    def update_one_goods(
            cls, goods_id, goods_type_id, goods_type_name, goods_name,
            goods_price, goods_ex_price, goods_info, goods_status):
        data = cls.objects.get(id=goods_id)
        data.goods_type_id = goods_type_id
        data.goods_type_name = goods_type_name
        data.goods_name = goods_name
        data.goods_price = goods_price
        data.goods_ex_price = goods_ex_price
        data.goods_info = goods_info
        data.goods_status = goods_status
        data.save()
        return data

    @classmethod
    def get_one_goods(cls, goods_id):
        return cls.objects.get(id=goods_id)

    @classmethod
    def get_all_goods(cls):
        return cls.objects.all()
