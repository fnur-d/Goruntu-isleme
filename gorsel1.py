import cv2 as cv
resim=cv.imread("pengu.png")



print("resmin boyutunu "+ str(resim.size))
print("resmin tipi "+ str(resim.dtype))
print("resmin şekli "+ str(resim.shape))

cv.waitKey(0)
cv.destroyAllWindows