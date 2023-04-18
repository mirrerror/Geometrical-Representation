import cv2

# Load the image
img = cv2.imread('mona_lisa.png')

# Display the image in a window
cv2.imshow('Image', img)
cv2.waitKey(0)

# Close the window
cv2.destroyAllWindows()
