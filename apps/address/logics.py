from .models import Address


class AddrLogic(object):

    """
    收货地址逻辑
    """

    @classmethod
    def add_one_address(
            cls, user_id, province, city, county, addr_detail):
        data = Address.add_one_object(
            user_id=user_id, province=province, city=city, county=county,
            addr_detail=addr_detail)
        return data.canonical()

    @classmethod
    def delete_one_address(cls, user_id, addr_id):
        return Address.delete_one_address(user_id, addr_id).canonical()

    @classmethod
    def getlist(cls, user_id):
        data = Address.get_all_address(user_id=user_id)
        return [i.canonical() for i in data]

    @classmethod
    def search(cls, text):
        pass
