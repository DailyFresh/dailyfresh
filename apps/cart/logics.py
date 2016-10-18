from .models import Cart


class CartLogic(object):

    """购物车逻辑
    """

    @classmethod
    def add_to_cart(cls, user_id, goods_id, goods_num):
        res = Cart.goods_id_existed(user_id, goods_id)
        if not res:
            res = Cart.add_one_object(
                user_id=user_id, goods_id=goods_id, goods_num=goods_num)
        else:
            res.goods_num += goods_num
            res.save()
        return res.canonical()

    @classmethod
    def delete_from_cart(cls, cart_id):
        data = Cart.delete_from_cart(cart_id)
        return data.canonical()

    @classmethod
    def getlist(cls, user_id):
        data = Cart.get_all_carts(user_id)
        content = []
        for i in data:
            content.append(i.canonical())
        return content

    @classmethod
    def clear_carts(cls, user_id):
        data = Cart.clear_carts(user_id=user_id)
        content = []
        for i in data:
            content.append(i.canonical())
        return content
