from django.db import models
from utils.models import BaseModel


class SOrder(BaseModel):

    """
    订单
    """

    PAYING = 1
    PAYED = 2
    CANCELED = 3
    DELETED = 4

    user_id = models.IntegerField(db_index=True, help_text='用户ID')
    goods_id = models.IntegerField(db_index=True, help_text='商品ID')
    addr_id = models.IntegerField(help_text="地址ID")
    goods_price = models.FloatField(default=0.0, help_text='商品价格')
    goods_num = models.SmallIntegerField(default=1, help_text='商品数量')
    goods_ex_price = models.FloatField(default=0.0, help_text='商品运费')
    order_price = models.FloatField(help_text='订单金额')
    # 1:支付宝  2:微信  3:银行卡
    payment_method = models.SmallIntegerField(help_text='支付方式')
    # 1:待支付  2:已支付  4:已删除
    order_status = models.SmallIntegerField(help_text='订单状态')

    class Meta:
        db_table = 's_order'

    @classmethod
    def get_all_order(cls, user_id):
        return cls.objects.filter(user_id=user_id)

    @classmethod
    def delete_one_order(cls, user_id, order_id):
        data = cls.objects.get(user_id=user_id, id=order_id)
        data.order_status = cls.DELETED
        data.save()
        return data

    @classmethod
    def cancel_one_order(cls, user_id, order_id):
        data = cls.objects.get(user_id=user_id, id=order_id)
        data.order_status = cls.CANCELED
        data.save()
        return data
