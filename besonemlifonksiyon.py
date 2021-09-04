import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
path="resim2.jpg"
img = cv2.imread(path)
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgbugu = cv2.GaussianBlur(img,(5,5),5) #5,5 blur seviyesi
imgcanny = cv2.Canny(imgbugu,100,100)
imggen = cv2.dilate("imgcanny",kernel,1) #cizili resmin çizgileri kalınlaştırmak,kernele göre kalınlaşıyor
imgdar = cr2.erode(imggen,kernel,1) #dilate fonksiyonunun tam tersi.Bu daraltıyor.


cv2.imshow("orijinal",img)
cv2.imshow("gri",imggray)
cv2.imshow("bugulu",imgbugu)
cv2.imshow("ciziliresim",imgcanny) #siyah beyaz çizili resim eğer buğu ile birleştirirsen daha iyi olur.
cv2.imshow("genisletilmisresim",imgcanny)
cv2.imshow("daraltilmisresim",imgcanny)

cv2.waitKey(0)
cv2.destroyAllWindows
