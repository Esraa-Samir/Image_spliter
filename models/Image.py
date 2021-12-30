import os
import constants
import requests
from PIL import Image
from io import BytesIO


class ImageSpliter:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ImageSpliter.__instance == None:
            ImageSpliter()
        return ImageSpliter.__instance

    def __init__(self, url):
        """ Virtually private constructor. """
        if ImageSpliter.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ImageSpliter.__instance = self
            self.url = url

    def split(self, x_parts=2, y_parts=2, k=0):
        response = requests.get(self.url)
        im = Image.open(BytesIO(response.content))
        imgwidth, imgheight = im.size
        height = imgheight // y_parts
        width = imgwidth // x_parts
        for i in range(0, y_parts):
            for j in range(0, x_parts):
                box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
                a = im.crop(box)
                k += 1
                a.save(os.path.join(constants.OUTPUT_PATH, "Img-%s.png" % k))
