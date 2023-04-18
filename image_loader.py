import cv2


def load_image(path: str):
    # Load the image
    img = cv2.imread(path)
    return img


def show_image(img):
    # Display the image in a window
    cv2.imshow('Image', img)
    cv2.waitKey(0)

    # Close the window
    cv2.destroyAllWindows()
