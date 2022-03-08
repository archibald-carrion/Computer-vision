import cv2 #OpenCV package

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('images/jeff bezos.jpg', cv2.COLOR_BGR2GRAY)
#img = cv2.imread('images/photo.jpg', cv2.COLOR_BGR2GRAY)
#img = cv2.imread('images/v.jpg', cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img, 1.3,4)
#print("Hello world")

for (x , y , w , h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


