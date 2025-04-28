import cv2 as cv

def rescaleFrame(frame,scale = 0.70):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img = cv.imread('images/4399918.jpg')
image = rescaleFrame(img)
cv.imshow('image',image)



# in order to make color change to gray, we need to use cv.cvtColor() function in which we need to provide image and 
# call the inbuilt function cv.COLOR_BGR2GRAY.

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)



# so for making the image blurr, we use GaussianBlur() function which takes image, total blurr required, some border_default value
# as arguments and this makes the image blurr.
# this method is used to reducee noise and details in image.
# (7,7) is size of Gaussian Kernel(width and height). large kernel size means strong blurr.

blur = cv.GaussianBlur(image,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)




# Edge cascade method is used to detect edges in the image.
# arguments it takes are image, lower threshold1 and upper threshold2.
# lower threshold means pixels below this value are considered non-edges in image.
# high threshold means pixels above this value are considered strong edges.

canny = cv.Canny(image,125,175)
cv.imshow('canny',canny)




# Dilated method in the code is used to perform image dilation, which is a morphological
# operation that increases the size of the white regions (foreground) in a binary image. 
# It is commonly used to emphasize features like edges or to fill small gaps in an image

dilated = cv.dilate(canny, (3,3) , iterations=1)
cv.imshow('dilate', dilated)




# Erode method in the code is used to perform image erosion, which is a morphological 
# operation that reduces the size of the white regions (foreground) in a binary image. 
# It is commonly used to remove noise or small white regions.

eroded = cv.erode(dilated, (3,3) , iterations=1)
cv.imshow('eroded',eroded)




# Resize method 

resized = cv.resize(image, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resize',resized)



# Cropped method is used to crop a image portion from the original image and show it as output.
cropped = image[50:200, 200:400]
cv.imshow('crop', cropped)






cv.waitKey(0)