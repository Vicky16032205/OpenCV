import cv2 as cv

# this function works for all, either image, pre recorded video or live video.
def rescaleFrame(frame,scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


# provided one video path and called the rescale Frame function to reduce the size of the video by 3/4 of original one.
capture = cv.VideoCapture('video.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

# original video frames calling done here.
    cv.imshow('Tiger', frame)

# frame rescaling is done here as this is playing the video of the reduced frame functions.
    cv.imshow('Resized video',frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()









# now here we will be calling the image rescaling frame function, above we called the rescaling for the videos.
img = cv.imread('images/1027664.jpg')
rescaled_image = rescaleFrame(img)
cv.imshow('Jiraiya Sensai', img)
cv.imshow('Jiraiya Sensai rescaled', rescaled_image)
cv.waitKey(0)








# this works only for the live video.
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)