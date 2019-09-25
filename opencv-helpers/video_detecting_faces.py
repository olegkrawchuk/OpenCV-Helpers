import cv2
import opencv_helpers
import os

video_filename = 'videoplayback.mp4'

input_stream = cv2.VideoCapture(video_filename)

if not input_stream.isOpened():
    print("Не удалось открыть видеофайл")
    exit(0)

width = int(input_stream.get(3))
heigth = int(input_stream.get(4))

output_stream = cv2.VideoWriter('result.mp4',
                                cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 25, (width, heigth))

haarcascade_path = os.path.join(os.getcwd(), 'haarcascades', 'haarcascade_frontalface_alt2.xml')

while input_stream.isOpened():
    ret, frame = input_stream.read()
    if not ret:
        break

    faces = opencv_helpers.detect_objects_by_haarcascade(frame, haarcascade_path, 1.2, 5, (50, 50))
    for x, y, w, h in faces:
        frame = opencv_helpers.draw_rectangle_image(frame, (x, y), (x + w, y + h), (0, 0, 255), 15)

    output_stream.write(frame)


input_stream.release()
output_stream.release()
