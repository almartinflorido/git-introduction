import cv2
import numpy as np


def _get_rows_cols(img):
    if len(img.shape) == 3:
        #color image
        rows, cols, _ = img.shape
    else:
        rows, cols= img.shape

    return rows, cols


def scale(img, scale_factor_x, scale_factor_y):
    """Scales an image given a scale factor for x and y axis

    :param img: the input image
    :type img: np.array
    :param scale_factor_x: the scale factor for x axis
    :type scale_factor_x: float
    :param scale_factor_y: the scale factor for y axis
    :type scale_factor_y: float
    :return: the image scaled
    :rtype: np.array
    """
    return cv2.resize(img, None, fx=scale_factor_x, fy=scale_factor_y, interpolation=cv2.INTER_CUBIC)


def translation(img, x, y):
    """Translates a image given a displacement for x,y axis

    :param img: the input image
    :type img: np.array
    :param x: the displacement value for x axis
    :type x: int
    :param y: the displacement value for x axis
    :type y: int
    :return: the translated image
    :rtype: np.array
    """

    rows, cols = _get_rows_cols(img)
    M = np.float32([[1 ,0 , int(x)], [0, 1, int(y)]])
    return cv2.warpAffine(img, M, (cols, rows))


def rotation(img, angle):
    """Rotates an image given an angle in degrees

    :param img: the input image
    :type img: np.array
    :param angle: the rotation angle in degrees
    :type angle: float
    :return: the rotated image
    :rtype: np.array
    """
    rows, cols = _get_rows_cols(img)
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    return cv2.warpAffine(img, M, (cols, rows))