import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
images = ["images/foto1.jpg","images/linus_torvald.jpg", "images/v_cyberpunk.png", "images/elon_musk.png","images/jeff_bezos.jpg","images/anti_detection1.png","images/anti_detection2.png","images/anti_detection3.png","images/anti_detection4.png","images/terminator.png"]
#img = cv2.imread('images/jeff bezos.jpg', cv2.COLOR_BGR2GRAY)

def detectHuman(theArray):
    counter = 0
    continueCode = True
    arrayLength = len(theArray)

    while counter < arrayLength and continueCode:
        img = cv2.imread(images[counter], cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(img, 1.2,4)
        for (x , y , w , h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        
        cv2.imshow('image', img)
        key = cv2.waitKey(2000)

        if key == 27:
            cv2.destroyAllWindows()
            continueCode = False
        else:            
            cv2.destroyWindow("image")
            if counter == arrayLength-1:
                counter = 0
            else:
                counter = counter + 1

detectHuman(images)