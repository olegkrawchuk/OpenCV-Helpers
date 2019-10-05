import cv2
import opencv_helpers
import os

image_filename = 'faces.jpeg'

image = cv2.imread(image_filename)

if not opencv_helpers.is_read(image):
    print("Не удалось открыть изображение")
    exit(0)

haarcascades_path = os.path.join(os.getcwd(), 'haarcascades')
files = [i for i in os.listdir(haarcascades_path) if i.lower().startswith('haarcascade_') != -1
         and os.path.isfile(os.path.join(haarcascades_path, i))]

for i, file in enumerate(files, start=1):
    fullpath = os.path.join(haarcascades_path, file)
    print(i, fullpath)

    faces = opencv_helpers.detect_objects_by_haarcascade(image, fullpath, 1.3, 10, (100, 100))
    print('Found', len(faces))

    image_result = image.copy()
    for x, y, w, h in faces:
        image_result = opencv_helpers.draw_rectangle_image(image_result, (x, y), (x + w, y + h), (0, 0, 255), 15)

    opencv_helpers.show_image(image_result, file)
    # opencv_helpers.save_image(file.split('.')[0] + '.' + image_filename.split('.')[1], image_result)

opencv_helpers.pause()
opencv_helpers.close_all_images()

# faces_res = opencv_helpers.detect_objects_by_haarcascade(image, haarcascade_path, 1.1, 5, (50, 50))
# print(len(faces_res))
#
# image_result = image.copy()

#
# opencv_helpers.show_image(image, "Original")
# opencv_helpers.show_image(image_result)
# opencv_helpers.pause()
# opencv_helpers.close_all_images()

#
# test = opencv_helpers.draw_line_image(image, (10, 10), (10, 200), (0, 0, 255))
#
# opencv_helpers.show_image(image, "Original", flags=cv2.WINDOW_NORMAL)
# opencv_helpers.show_image(test, flags=cv2.WINDOW_NORMAL)
#
# opencv_helpers.pause()
# opencv_helpers.close_all_images()


# haarcascade_filename = 'haarcascade_frontalface_alt2.xml'
#
# haarcascade_path = ''
# base_path = os.path.join(os.getcwd())
# haarcascade_foldernames = [i for i in os.listdir(base_path) if os.path.isdir(i) and i.lower().find('haar') != -1]
#
# if len(haarcascade_foldernames) == 0:
#     print("Нет папки haarcascades. Это не позволит вам использовать функции обнаружения (detecting)")
# else:
#     haarcascade_path = os.path.join(base_path, haarcascade_foldernames.pop(0))
#
# haarcascade_path = os.path.join(haarcascade_path, haarcascade_filename)
# print(haarcascade_path)