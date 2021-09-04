import cv2
path = "resim3.jpg"
img = cv2.imread(path)
print(img.shape) #boyutu yazdırır. ilk genişlik sonra yükseklik
width,height = 400,400

imgres = cv2.resize(img,(width,height))
imgcrop = img[200:450,0:690]
imgcropres = cv2.resize(imgcrop,(img.shape[1],img.shape[0])) #kesilen resmi eski haline getirme

cv2.imshow("normal",img)
cv2.imshow("resize",imgres)
cv2.imshow("kirpilmis",imgcrop)
cv2.imshow("kirpilmis res",imgcropres)

cv2.waitKey(0)
cv2.destroyAllWindows()
