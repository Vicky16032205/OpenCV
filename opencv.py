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