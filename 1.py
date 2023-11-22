import cv2
import numpy

img_black = numpy.zeros ((320 , 320))
turn = 1

for repeat in range (8) :
    if turn == 1 :                        #radif fard
        for row in range (repeat * 40 , ((repeat + 1) * 40) - 1) :
            for i in [0 , 2 , 4 , 6] :
                for col in range (i * 40 , (i + 1) * 40) :
                    img_black[row][col] = 255
        turn = 2 
    
    elif turn == 2 :                      #radif zoj
        for row in range (repeat * 40 , ((repeat + 1) * 40) - 1) :
            for i in [1 , 3 , 5 , 7] :
                for col in range (i * 40 , (i + 1) * 40) :
                    img_black[row][col] = 255
        turn = 1

cv2.imshow ("result 1", img_black)
cv2.waitKey ()