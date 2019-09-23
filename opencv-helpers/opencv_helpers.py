import cv2
from math import fabs


def is_read(image):
    return image is not None


def convert_to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def show_image(image, window_name='Image', flags=cv2.WINDOW_NORMAL):
    cv2.namedWindow(window_name, flags)
    cv2.imshow(window_name, image)


def pause():
    cv2.waitKey(0)


def close_image(window_name):
    cv2.destroyWindow(window_name)


def close_all_images():
    cv2.destroyAllWindows()


def crop_image(image, x, width, y, height):
    return image[x:x + width, y:y + height]


def get_resolution_and_count_channels(image):
    return image.shape


def resize_image(image, new_width, new_height):
    return cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)


def rotate_image(image, angle):
    (h, w, d) = image.shape
    center = (w // 2, h // 2)
    scale = 1.0 if angle >= 0 else -1.0
    m = cv2.getRotationMatrix2D(center, fabs(angle), scale)
    return cv2.warpAffine(image, m, (w, h))


def convert_to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def convert_to_black_white(image):
    image = convert_to_gray(image)
    ret, threshold_image = cv2.threshold(image, 127, 255, 0)
    return threshold_image


def blur_image(image, strong_blur):
    # если число нечетное отнимаем 1 (делаем его нечетным)
    if strong_blur % 2 == 0:
        strong_blur -= 1

    return cv2.GaussianBlur(image, (strong_blur, strong_blur), 0)




