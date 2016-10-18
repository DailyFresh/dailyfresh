from django.db import models
from utils.models import BaseModel


class Address(BaseModel):

    """
    购物车
    """

    user_id = models.IntegerField(help_text='用户ID')

    recipient_name = models.CharField(blank=True,null=True,max_length=32,help_text='收件人姓名')

    recipient_phone = models.CharField(blank=True,null=True,max_length=11,help_text='收件人电话') 

    province = models.CharField(blank=True, null=True, max_length=32,
                                help_text='省')
    city = models.CharField(blank=True, null=True, max_length=32,
                            help_text='市')
    county = models.CharField(blank=True, null=True, max_length=32,
                              help_text='县')
    addr_detail = models.CharField(blank=True, null=True, max_length=64,
                                   help_text='详细地址')

    class Meta:
        db_table = 's_address'

    @classmethod
    def delete_one_address(cls, user_id, addr_id):
        data = cls.objects.get(user_id=user_id, id=addr_id)
        data.delete()
        return data

    @classmethod
    def get_all_address(cls, user_id):
        return cls.objects.filter(user_id=user_id)