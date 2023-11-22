
import cv2
import numpy

img_white = numpy.ones ((300 , 300))

for row in range (100 , 200) :
    for col in range (135 , 165) :
        img_white[row][col] = 0

for row in range (70 , 100) :
    for col in range (100 , 200) :
        img_white[row][col] = 0

cv2.imshow ("result 5" , img_white)
cv2.waitKey ()
cv2.imwrite ("5_output.jpg" , img_white)