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


def detect_edges(img, save_to_file=False, output_file_name='edges.png'):
    # Convert the image to grayscale
    gray = grayscale_conversion(img)

    # Apply Gaussian blur to the image to reduce noise
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Apply Canny edge detection to the image
    edges = cv2.Canny(blurred, 100, 200)

    if save_to_file:
        cv2.imwrite(output_file_name, edges)
    # Return the edge map
    return edges


def thresholding(img, threshold_value, save_to_file=False, output_file_name='thresholding.png'):
    # Convert the image to grayscale
    gray = grayscale_conversion(img)

    # Apply thresholding to the image
    ret, thresh = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

    if save_to_file:
        cv2.imwrite(output_file_name, thresh)
    # Return the binary image
    return thresh


def contrast_adjustment(img, save_to_file=False, output_file_name='contrast.png'):
    # Convert the image to grayscale
    gray = grayscale_conversion(img)

    # Apply histogram equalization to the image
    equalized = cv2.equalizeHist(gray)

    if save_to_file:
        cv2.imwrite(output_file_name, equalized)
    # Return the equalized image
    return equalized


def gaussian_blur(img, save_to_file=False, output_file_name='gaussian_blur.png'):
    # Apply Gaussian blur
    blur = cv2.GaussianBlur(img, (5, 5), 0)

    if save_to_file:
        cv2.imwrite(output_file_name, blur)
    return blur

