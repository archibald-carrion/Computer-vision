import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
images = ["images/anti-facerecognition2.webp", "images/anti-facerecognition1.webp", "images/linus_torvald.jpg", "images/photo.jpg", "images/star_wars.png", "images/v_cyberpunk.webp", "images/elon_musk.png","images/jeff_bezos.jpg",]

#img = cv2.imread('images/jeff bezos.jpg', cv2.COLOR_BGR2GRAY)

counter = 0
continueCode = True

while counter < 6 and continueCode:
    img = cv2.imread(images[counter], cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.1,4)
    for (x , y , w , h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow('image', img)
    key = cv2.waitKey(2000)

    if key == 27:
        cv2.destroyAllWindows()
        continueCode = False
    else:            
        cv2.destroyWindow("image")
        if counter == 5:
            counter = 0
        else:
            counter = counter + 1