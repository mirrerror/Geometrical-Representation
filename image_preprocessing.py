import cv2
from image_loader import load_image
input_image = load_image('mona_lisa.png')
def grayscale_conversion():
    pass


def resize():
    pass


def crop():
    pass


def detect_edge(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the image to reduce noise
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Apply Canny edge detection to the image
    edges = cv2.Canny(blurred, 100, 200)

    # Return the edge map
    return edges
    pass
# Detect edges in the image
edge_map = detect_edge(input_image)

# Display the edge map in a window
cv2.imshow('Edges', edge_map)
cv2.waitKey(0)

def thresholding(img, threshold_value):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to the image
    ret, thresh = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

    # Return the binary image
    return thresh
    pass
thresholded = thresholding(input_image, 128)
# Display the thresholded image in a window
cv2.imshow('Thresholded', thresholded)
cv2.waitKey(0)

def contrast_adjustment(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization to the image
    equalized = cv2.equalizeHist(gray)

    # Return the equalized image
    return equalized
    pass
# Perform contrast adjustment on the image
contrast_adjusted = contrast_adjustment(input_image)
# Display the adjusted image in a window
cv2.imshow('Contrast Adjusted', contrast_adjusted)
cv2.waitKey(0)

def smoothing():
    pass
