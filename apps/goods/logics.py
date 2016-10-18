import json
from .models import Goods
from haystack.query import SearchQuerySet


class GoodsLogic(object):

    """
    商品逻辑
    """

    @classmethod
    def add_one_goods(
            cls, goods_type_id, goods_type_name, goods_name, goods_price,
            goods_ex_price, goods_info, goods_status):
        data = Goods.add_one_object(
            goods_type_id=goods_type_id, goods_type_name=goods_type_name,
            goods_name=goods_name, goods_price=goods_price,
            goods_ex_price=goods_ex_price, goods_info=goods_info,
            goods_status=goods_status)
        return data.canonical()

    @classmethod
    def delete_one_goods(cls, goods_id):
        return Goods.delete_one_goods(goods_id).canonical()

    @classmethod
    def get_goods_info(cls):
        content = []
        data = Goods.get_goods_info()
        for i in data:
            content.append(i.canonical(
                exclude=['id', 'goods_price', 'goods_ex_price', 'goods_info',
                         'goods_status', 'create_time',
                         'update_time', 'extinfo']))
        return content

    @classmethod
    def update_one_goods(
            cls, goods_id, goods_type_id, goods_type_name, goods_name,
            goods_price, goods_ex_price, goods_info, goods_status):
        data = Goods.update_one_goods(
            goods_id, goods_type_id, goods_type_name, goods_name,
            goods_price, goods_ex_price, goods_info, goods_status)
        return data.canonical()

    @classmethod
    def get_one_goods(cls, goods_id):
        data = Goods.get_one_goods(goods_id)
        return data.canonical()

    @classmethod
    def getlist(cls):
        data = Goods.get_all_goods()
        return [i.canonical() for i in data]

    @classmethod
    def search(cls, text):
        s = SearchQuerySet()
        data = s.filter(text=text)
        return [i.canonical() for i in data]
