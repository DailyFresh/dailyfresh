from django.db import models
from utils.models import BaseModel
from apps.goods.models import Goods
from apps.passport.models import Passport

class Cart(BaseModel):

    """
    购物车
    """

    user = models.ForeignKey(Passport, help_text='用户')
    goods = models.ForeignKey(Goods, help_text='商品')
    goods_num = models.SmallIntegerField(default=1, help_text='商品数量')

    class Meta:
        db_table = 's_cart'

    # @classmethod
    # def goods_id_existed(cls, user_id, goods_id):
    #     return cls.objects.filter(user_id=user_id, goods_id=goods_id).first()

    # @classmethod
    # def delete_from_cart(cls, user_id, cart_id):
    #     return cls.objects.get(user_id=user_id, id=cart_id).delete()

    @classmethod
    def get_all_carts(cls, user):
        return cls.objects.filter(user=user)

    # @classmethod
    # def clear_carts(cls, user_id):
    #     data = cls.get_all_carts(user_id)
    #     data.delete()
    #     return data
