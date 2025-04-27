import cv2 as cv

# this is command for showing images through opencv.
image = cv.imread('images/671064.jpg')
cv.imshow('Jiraiya', image)
cv.waitKey(0)









# now this is for working with webcam.
capture = cv.VideoCapture(0)
while True:
    isTrue , frame = capture.read()
    cv.imshow('Live Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()


# this is for working with any video to see any video in the system.
capture = cv.VideoCapture('/path/to/any/video/file')
while True:
    isTrue , frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF == ord('c'):
        break
capture.release()
cv.destroyAllWindows()






# cv.VideoCapture() ==> this command is used for reading and locating the path to any video file or
#                       either for providing the camera access to the library to access it.
#                       It can contain 0,1,2,...,n integers as arguments telling about using the camera number what connected to system.
#                       0 means the default pc camera, 1 meaning the very first camera attached to the pc and so on.


# cv.imshow() ===>      takes two values as arguments, first the name the image or video should have and another the pixels as image
#                       stored in cv.imread() variable/


# cv.imread() ===>      used to provide the file path of the image or say frame.
#                       this returns the image as a matrix of pixels.