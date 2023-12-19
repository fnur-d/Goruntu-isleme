import cv2

resim=cv2.imread("pengu.png")
kesit1=resim[100:400,220:620]
kesit2=resim[400:700,200:600]

cv2.imshow("kesit1",kesit1)
cv2.imshow("kesit2",kesit2)

print(resim[200,200])
print(resim[20,150])
print(resim[90,80])
print(resim[20,150]+resim[90,80])
print(resim[:,:])# tüm pikselleri yazdırdık
toplam=kesit1[:,:]*0.9+kesit2[:,:]*0.1#pikselleri topladık
cv2.imshow("resim toplamlari",toplam)
cv2.waitKey(0)
cv2.destroyAllWindows