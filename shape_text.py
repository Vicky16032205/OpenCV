# colors are stored in bgr format and not in rgb format in numpy.


import cv2 as cv
import numpy as np


# we are creating a blank black image here using numpy.

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank', blank)



# modifying colors in the image in certain or full area.

blank[:] = 0,255,0    #changes background color to green.
cv.imshow('Blank', blank)

blank[:] = 0,0,255    #changes background color to red.
cv.imshow('Blank', blank)

blank[:] = 255,0,0    #changes background color to blue.
cv.imshow('Blank', blank)

blank[200:300 , 300:400] = 0,0,255     # prints a red rectangle at a position which is having a small area occupied in the black image.
cv.imshow('image',blank)














# in this area we will be making some shapes like rectangle or circle or line in the image.

cv.rectangle(blank, (0, 0), (250, 500), (0,255,0), thickness=3)    #prints a green boundary across rectangle in a half and other half will be same.


cv.rectangle(blank, (0, 0), (250, 500), (0,255,0), thickness=-1)    #prints a green rectangle in a half and other half will be same.


cv.circle(blank,((blank.shape[1]//2 , blank.shape[0]//2)), 40 , (0,0,255), thickness= 3)   # prints red boundary circle in center of blank black color.

cv.circle(blank,((blank.shape[1]//2 , blank.shape[0]//2)), 40 , (0,0,255), thickness= -1)   # prints red circle in center of blank black color.


cv.line(blank, (0,0) , (250,250) , (255,255,255) , thickness=3)   #for printing a line from top left corner to the mid of the page.














# this code is for printing texts over image.

cv.putText(blank, "Hello Bay!" , (255,255) , cv.FONT_HERSHEY_SIMPLEX , 1.0 , (0,255,0) , 2)          # puts text onto image.

cv.imshow('blank',blank)
cv.waitKey(0)