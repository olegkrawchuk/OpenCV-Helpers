import cv2
import opencv_helpers

image = cv2.imread('img.jpg')

if not opencv_helpers.is_read(image):
    print("Не удалось открыть изображение")
    exit(0)


test = opencv_helpers.draw_line_image(image, (10, 10), (10, 200), (0, 0, 255))

opencv_helpers.show_image(image, "Original", flags=cv2.WINDOW_NORMAL)
opencv_helpers.show_image(test, flags=cv2.WINDOW_NORMAL)

opencv_helpers.pause()
opencv_helpers.close_all_images()
