import hashlib
from PIL import ImageFile
from .models import Image
from .exceptions import ImageDoesNotExistException


class ImageLogic(object):
    """
    传图逻辑
    """

    # @classmethod
    # def upload_image(cls, image):
    #     parser = ImageFile.Parser()
    #     img_data = image.file.getvalue()
    #     parser.feed(img_data)
    #     img = parser.close()
    #     img_name = hashlib.md5(img_data).hexdigest()
    #     img_width = img.size[0]
    #     img_height = img.size[1]
    #     img_type = parser.image.format
    #     img_type = 'image/' + img_type.lower()
    #     return Image.upload_image(img_name=img_name, img_url=img_url,
    #                               img_width=img_width, img_height=img_height,
    #                               img_type=img_type)

    @classmethod
    def get_image(cls, file_id):
        data = Image.get_image(file_id)
        if not data:
            raise ImageDoesNotExistException()
        return data
