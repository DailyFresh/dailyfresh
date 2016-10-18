from haystack import indexes
from .models import Goods


class GoodsIndex(indexes.SearchIndex, indexes.Indexable):

    """
    商品搜索
    """

    text = indexes.CharField(document=True, use_template=False)
    goods_type_name = indexes.CharField(model_attr='goods_type_name')
    goods_name = indexes.CharField(model_attr='goods_name')

    def get_model(self):
        return Goods
