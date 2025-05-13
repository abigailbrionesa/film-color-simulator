import cv2 as cv

img = cv.imread("photos/cat_large.jpg")
cv.imshow("cat",img)

def rescaleFrame(frame, scale=0.1):
  
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    print(cv.INTER_AREA, "inter area")
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_img = rescaleFrame(img, 0.9)

cv.imshow("cat - resized", resized_img)

cv.waitKey(0)
