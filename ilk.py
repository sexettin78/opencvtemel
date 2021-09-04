#kütüphaneyi import ettik
import cv2

#resmi okuması.Eğer ("resim.jpg",0) yaparsan resim gri olur.
resim = cv2.imread("resim6.jpg")
resim2 = cv2.imread("resim5.jpg")

#resimi kaydetme (hangi adda istiyorsanız o adda yapın.ben griresim.jpg olarak ayarladım.)
#cv2.imwrite("griresim.jpg",resim)

#resmi ekranda göstermek
cv2.imshow("cerceve",resim)
cv2.imshow("cerceve2",resim2)

#resmin ekranda kalmasını sağlar waitkey.Waitkey(1000) yaparsan 1 saniye kalır
cv2.waitKey(0)
cv2.destroyAllWindows()
