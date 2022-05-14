import cv2
from random import randrange
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#img = cv2.imread('RDJ.jpg')
#img = cv2.imread('2people.jpg')
webcam = cv2.VideoCapture(0)
#webcam = cv2.VideoCapture('video.mp4')

#iterate forever over frames
while True:
    successful_frame_read, frame = webcam.read()
   
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256),randrange(256),randrange(256)), 2)


    cv2.imshow('Clever Programmer Face Detector', frame)
    key = cv2.waitKey(1)

    #stop if Q key is pressed
    if key==81 or key==113:
        break

#release the video capture object
webcam.release()

"""
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#training algorithm to detect facest
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)


#print(face_coordinates)
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256),randrange(256),randrange(256)), 2)


cv2.imshow('Clever Programmer Face Detector', img)
cv2.waitKey()
"""
print("code complete")
