import cv2
# Read the image
image = cv2.imread('C:\Users\dilek\Desktop\project\img1.jpeg',0)
# Check if the image was loaded successfully
if image is None:
    print("Error: Could not read the image.")
else:
    cv2.imshow('My Image', image)

    # Wait until a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()

