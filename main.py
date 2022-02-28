import cv2 #OpenCV package

img = cv2.imread('images\img1.png', cv2.COLOR_BGR2RGB)
img = cv2.resize(img,(0,0), fx=0.5,fy=0.5)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('new_img.png',img) #create a new iamge with the modification
