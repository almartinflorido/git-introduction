import os
import sys
import cv2


def load_image(image_absolute_path, color=True):
    if not os.path.exists(image_absolute_path):
        print('Image {} not found'.format(image_absolute_path))
        sys.exit(-1)

    if color:
        return cv2.imread(image_absolute_path, cv2.IMREAD_COLOR)
    return cv2.imread(image_absolute_path, cv2.IMREAD_GRAYSCALE)


def write_image(image_absolute_path, image):
    if image_absolute_path.endswith('.jpg') or image_absolute_path.endswith('.png'):
        cv2.imwrite(image_absolute_path, image)
        return True
    return False
