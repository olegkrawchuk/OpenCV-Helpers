import cv2
import opencv_helpers

image = cv2.imread('img.jpg')

if not opencv_helpers.is_read(image):
    print("Не удалось открыть изображение")
    exit(0)


blur = opencv_helpers.blur_image(image, 10)


opencv_helpers.show_image(image, "Original", flags=cv2.WINDOW_NORMAL)
opencv_helpers.show_image(blur, flags=cv2.WINDOW_NORMAL)

opencv_helpers.pause()
opencv_helpers.close_all_images()
