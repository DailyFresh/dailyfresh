from django.db import transaction
from .models import Passport
from apps.profile.models import Profile


class PassportLogic(object):

    """
    用户账户逻辑
    """

    @classmethod
    def register(cls, username, password, email, sex, realname, province, city,
                 county, addr_detail, user_type=1):
        content = {}
        with transaction.atomic():
            data = Passport.create_one_passport(username, email, password)
            content.update(data.canonical())
            user_id = data.id
            data = Profile.create_user_profile(
                user_id, sex, realname, province, city, county, addr_detail)
            content.update(data.canonical())
        return content

    @classmethod
    def reset_password(cls, user_id, old_password, new_password):
        user = Passport.get_user(user_id)
        data = user.reset_password(old_password, new_password)
        return data.canonical()
