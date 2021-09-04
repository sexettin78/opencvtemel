import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

print(img.shape)

img[:] = 255,0,0 #renk kodu

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) #çizgi çekme. //  0,255,0 renk
cv2.putText(img,"sexettin",(250,250),cv2.FONT_HERSHEY_COMPLEX,1,(150,150,150),2) # Fonntan sonraki 1 sayısı KALINLIK

cv2.imshow("kararesim",img)

cv2.waitKey(0)
