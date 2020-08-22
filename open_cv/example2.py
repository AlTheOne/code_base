"""
Поиск лиц.
"""

import cv2


def main(path):
    face_cascade = cv2.CascadeClassifier(
        'haarcascade_frontalface_default.xml')

    img = cv2.imread(path)
    gray_im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.2)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('{} face(s) found'.format(len(faces)), img)
    cv2.waitKey(0)


if __name__ == '__main__':
    path = 'faces.jpg'
    main(path)
