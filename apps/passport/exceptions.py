from utils.exceptions import EcomException


class AnonymousException(EcomException):

    code = 1000
    message = '对不起，您是匿名用户，请先登录'


class UsernamePasswordException(EcomException):

    code = 1001
    message = '用户名或密码不正确'
