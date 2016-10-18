from .models import SOrder


class OrderLogic(object):

    """订单逻辑
    """

    @classmethod
    def add_one_order(
            cls, user_id, goods_id, addr_id, goods_price, goods_num,
            goods_ex_price, payment_method, order_status):
        order_price = goods_price * goods_num + goods_ex_price
        data = SOrder.add_one_object(
            user_id=user_id, goods_id=goods_id, addr_id=addr_id,
            goods_price=goods_price, goods_num=goods_num,
            goods_ex_price=goods_ex_price, order_price=order_price,
            payment_method=payment_method, order_status=order_status)
        return data.canonical()

    @classmethod
    def getlist(cls, user_id):
        data = SOrder.get_all_order(user_id)
        return [i.canonical() for i in data]

    @classmethod
    def delete_one_order(cls, user_id, order_id):
        data = SOrder.delete_one_order(user_id, order_id)
        return data.canonical()

    @classmethod
    def cancel_one_order(cls, user_id, order_id):
        data = SOrder.cancel_one_order(user_id, order_id)
        return data.canonical()
