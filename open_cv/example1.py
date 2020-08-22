import cv2


def print_data(img):
    print(img)
    print('Type:', type(img))
    print('Shape:', img.shape)
    print('Top-left pixel:', img[0, 0])


def show_gray(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Grayscale', gray_img)
    cv2.waitKey(0)


def use_threshold(img):
    ret, custom_thresh_im = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('custom_thresh_img', custom_thresh_im)
    cv2.waitKey(0)


def main(path):
    img = cv2.imread(path)
    cv2.imshow('Test', img)
    cv2.waitKey(0)

    show_gray(img)
    use_threshold(img)


if __name__ == '__main__':
    path = 'C:\\Users\\altheone\\Downloads\\ttt.jpg'
    main(path)
