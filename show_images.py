import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("photos/cat.jpg", cv.IMREAD_GRAYSCALE)

surf = cv.xfeatures2d.SURF_create(400)

surf.setHessianThreshold(50000)

kp, des = surf.detectAndCompute(img,None)

print( len(kp) )

img2 = cv.drawKeypoints(img,kp,None,(255,0,0),4)

plt.imshow(img2),plt.show()

cv.imshow("Cat", img)

cv.waitKey(0)