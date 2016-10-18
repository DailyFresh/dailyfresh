from django.db import models
from utils.models import BaseModel


class Cart(BaseModel):

    """
    购物车
    """

    user_id = models.IntegerField(help_text='用户ID')
    goods_id = models.SmallIntegerField(db_index=True, help_text='商品ID')
    goods_num = models.SmallIntegerField(default=1, help_text='商品数量')

    class Meta:
        db_table = 's_cart'

    @classmethod
    def goods_id_existed(cls, user_id, goods_id):
        return cls.objects.filter(user_id=user_id, goods_id=goods_id).first()

    @classmethod
    def delete_from_cart(cls, user_id, cart_id):
        return cls.objects.get(user_id=user_id, id=cart_id).delete()

    @classmethod
    def get_all_carts(cls, user_id):
        return cls.objects.filter(user_id=user_id)

    @classmethod
    def clear_carts(cls, user_id):
        data = cls.get_all_carts(user_id)
        data.delete()
        return data
