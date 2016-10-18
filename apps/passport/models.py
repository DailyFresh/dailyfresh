from django.contrib.auth.models import AbstractUser
from utils.models import BaseModel
from utils.utils import md5
from utils.logics import model_to_dict
from .exceptions import UsernamePasswordException


class Passport(AbstractUser, BaseModel):

    """
    账户系统
    """

    class Meta:
        db_table = 's_user_account'

    def canonical(self, exclude=[
            'password', 'is_staff', 'is_superuser', 'is_active']):
        return model_to_dict(self, exclude=exclude)

    def set_password(self, raw_password):
        self.password = md5(raw_password)

    def check_password(self, raw_password):
        return self.password == md5(raw_password)

    def reset_password(self, old_password, new_password):
        _old_password = md5(old_password)
        if self.password == _old_password:
            self.password = md5(new_password)
            self.save(update_fields=['password'])
            return self
        raise UsernamePasswordException()

    @classmethod
    def get_user(cls, user_id):
        return cls.objects.get(id=user_id)

    @classmethod
    def create_one_passport(cls, username, email, password):
        return cls.objects.create_user(username=username, email=email,
                                       password=password)
