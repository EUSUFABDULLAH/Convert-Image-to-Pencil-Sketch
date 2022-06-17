import cv2

image= cv2.imread("img.png")

gray_image= cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

invert_image= 255- gray_image

blur= cv2.GaussianBlur(invert_image , (21,21) , 0)

invert_blur = 255-blur

skatch= cv2.divide(gray_image, invert_blur , scale= 256.0)

cv2.imshow("pencil skatch" , skatch)

cv2.waitKey(0)