import cv2
import opencv_helpers
import os

video_filename = 'MVI_3135.AVI'

input_stream = cv2.VideoCapture(video_filename)

if not input_stream.isOpened():
    print("Не удалось открыть видеофайл")
    exit(0)

width = int(input_stream.get(cv2.CAP_PROP_FRAME_WIDTH))
heigth = int(input_stream.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(input_stream.get(cv2.CAP_PROP_FPS))
fourcc = int(input_stream.get(cv2.CAP_PROP_FOURCC))

output_stream = cv2.VideoWriter('result.' + video_filename.split('.')[1], fourcc, fps, (width, heigth))

haarcascade_path = os.path.join(os.getcwd(), 'haarcascades', 'haarcascade_frontalface_alt2.xml')

while input_stream.isOpened():
    ret, frame = input_stream.read()
    if not ret:
        break

    faces = opencv_helpers.detect_objects_by_haarcascade(frame, haarcascade_path, 1.15, 5, (50, 50))
    for x, y, w, h in faces:
        frame = opencv_helpers.draw_rectangle_image(frame, (x, y), (x + w, y + h), (0, 0, 255), 15)

    output_stream.write(frame)

input_stream.release()
output_stream.release()
