from django.contrib.auth.models import AbstractUser
from utils.models import BaseModel
from utils.utils import md5
from utils.logics import model_to_dict


class Passport(AbstractUser, BaseModel):

    """
    账户系统
    """

    class Meta:
        db_table = 's_user_account'

    def set_password(self, raw_password):
        self.password = md5(raw_password)

    def check_password(self, raw_password):
        return self.password == md5(raw_password)