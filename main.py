import cv2 #OpenCV package
#import time
#from datetime import datetime

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#img = cv2.imread('images/jeff bezos.jpg', cv2.COLOR_BGR2GRAY)
img = cv2.imread('images/star_wars.png', cv2.COLOR_BGR2GRAY)
#img = cv2.imread('images/photo.jpg', cv2.COLOR_BGR2GRAY)
#img = cv2.imread('images/v.jpg', cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img, 1.3,4)
#print("Hello world")

for (x , y , w , h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

#tick = 60
contador = 0
while contador<3000000 :
    cv2.imshow('image', img)
    contador = contador +1
#cv2.waitKey(0)
#how to show the image for 5 second without having a "grey screen" ?
#time.sleep(5)
cv2.destroyAllWindows()


