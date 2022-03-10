import cv2
from cv2 import destroyAllWindows
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image = cv2.imread("images/v_cyberpunk.png", cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(image, 1.2,4)
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imshow("Image",image)
cv2.waitKey(0)
destroyAllWindows()