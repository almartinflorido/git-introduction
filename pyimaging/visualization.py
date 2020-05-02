import cv2


def visualize_image(window_title, image, wait=True, scale_factor=1.0):
    """A method to visualize images

    :param window_title: the window title
    :type window_title: str
    :param image: the image to show
    :type window: np.array
    :param wait: a flag to wait while the image is showing
    :type wait: boolean
    :param scale_factor: a scale factor to scale the image
    :type scale_factor: float
    :return: None
    """
    window_width = int(image.shape[1] * scale_factor)
    window_height = int(image.shape[0] * scale_factor)

    cv2.namedWindow(window_title, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_title,(window_width, window_height))
    cv2.imshow(window_title, image)
    if wait:
        cv2.waitKey()
        cv2.destroyWindow(window_title)