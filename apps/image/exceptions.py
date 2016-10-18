from utils.exceptions import EcomException


class ImageDoesNotExistException(EcomException):

    code = 2000
    message = '对不起，您访问的图片不存在，请检查参数'
