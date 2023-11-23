
import cv2
import numpy

img_black = numpy.zeros ((255 , 255))

# for row in range (255) :
    # for col in range (255) :
        # img_black[row][col] = 50

cv2.imshow ("result 5" , img_black)
cv2.waitKey ()
# cv2.imwrite ("5_output.jpg" , img_black)