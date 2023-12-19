import cv2

resim1=cv2.imread("kedi.jpg")
resim2=cv2.imread("kopek.jpg")
cv2.imshow("kop",resim2)
resim1=cv2.resize(resim1,(100,100))
resim2=cv2.resize(resim2,(100,100))
toplam=resim1[:,:]*0.9+resim2[:,:]*0.1
cv2.imshow("res",toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()