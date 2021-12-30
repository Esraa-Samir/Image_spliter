from models.Image import ImageSpliter
import requests
import constants

if __name__ == '__main__':
    response = requests.get(constants.JSON_URL)
    url = response.json()["data"]["image_url"]
    parts = response.json()["data"]["parts"]
    image = ImageSpliter(url)
    image.split(x_parts=int(parts/2), y_parts=int(parts/2))
