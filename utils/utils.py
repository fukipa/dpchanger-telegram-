from datetime import datetime
import numpy as np
import cv2
import glob
import random
from PIL import Image

def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}"


def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now()) != convert_time_to_string(prev_time)


def get_background():
    img = random.choice(glob.glob('munch/*.jpg'))
    image = Image.open(img)
    thumb_width = 500
    im_thumb = crop_max_square(image).resize((thumb_width, thumb_width), Image.LANCZOS)
# convert image to numpy array
    data = np.asarray(im_thumb)
    return data#np.zeros((500, 500))

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))
def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

def generate_time_image_bytes(dt):
    image = get_background()
    width, height = image.shape[1], image.shape[0]
    print(width,height)
    font = cv2.FONT_HERSHEY_PLAIN
    text2 ="~~fukipa is NOT a BOT~~" 
    y0, dy =int(image.shape[1]/3),image.shape[0]-20 
    cv2.putText(image,
            text2,
            (y0,dy),
            font,
            1.0, 
            (57, 255, 20),
            2,
            cv2.LINE_AA)
    _, bts = cv2.imencode('.jpg', image)
    return bts.tobytes()
