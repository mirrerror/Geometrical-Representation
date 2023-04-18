import cv2


def grayscale_conversion(img, save_to_file=False, output_file_name='grayscale.png'):
    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if save_to_file:
        # Save the grayscale image
        cv2.imwrite(output_file_name, gray_img)
    return gray_img


def resize(img, new_size, save_to_file=False, output_file_name='resized.png'):
    # Resize the image
    resized_img = cv2.resize(img, new_size, interpolation=cv2.INTER_AREA)

    if save_to_file:
        # Save the resized image
        cv2.imwrite(output_file_name, resized_img)
    return resized_img


def crop(img, top_left, bottom_right, save_to_file=False, output_file_name='cropped.png'):
    # Set the coordinates of the top-left corner and bottom-right corner of the desired crop area
    # Crop the image
    cropped_img = img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

    if save_to_file:
        # Save the cropped image
        cv2.imwrite(output_file_name, cropped_img)
    return cropped_img


def detect_edge():
    pass


def thresholding():
    pass


def contrast_adjustment():
    pass


def smoothing():
    pass
