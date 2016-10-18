from .models import Profile
from apps.passport.models import Passport


class ProfileLogic(object):

    """
    用户资料逻辑
    """

    @classmethod
    def create_user_profile(cls, user_id, sex, realname, province, city,
                            county, addr_detail):
        return Profile.create_user_profile(
            user_id, sex, realname, province, city, county, addr_detail)

    @classmethod
    def update_profile(cls, user_id, sex, realname, province, city, county,
                       addr_detail):
        data = Profile.update_profile(user_id, sex, realname, province, city,
                                      county, addr_detail)
        return data.canonical()

    @classmethod
    def get_profile(cls, user_id):
        content = {}
        data = Profile.get_one_object({'user_id': user_id})
        content.update(data.canonical())
        data = Passport.get_one_object({'id': user_id})
        content.update(data.canonical())
        return content
