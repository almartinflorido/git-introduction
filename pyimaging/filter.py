import cv2
import numpy as np


def sharpen(image):
    """Performs a sharpening filter

    :param image: the input image
    :type image: np.array
    :return: a filtered image
    :rtype: np.array
    """
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)


def shepia(image):
    """Performs a shepia filter

    :param image: the input image
    :type image: np.array
    :return: a filtered image
    :rtype: np.array
    """
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    return cv2.filter2D(image, -1, kernel)


def gaussian_blur(image):
    """Performs a gaussian blur filter

    :param image: the input image
    :type image: np.array
    :return: a filtered image
    :rtype: np.array
    """
    return cv2.GaussianBlur(image, (35, 35), 0)


def emboss(image):
    """Performs a emboss filter

    :param image: the input image
    :type image: np.array
    :return: a filtered image
    :rtype: np.array
    """
    kernel = np.array([[0,-1,-1],
                            [1,0,-1],
                            [1,1,0]])
    return cv2.filter2D(image, -1, kernel)

