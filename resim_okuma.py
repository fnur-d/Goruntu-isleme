import cv2 as cv
resim=cv.imread("pengu.png")

cv.imshow("degisik resim",resim)
print(resim)# resmin matriserini yazdırma

cv.waitKey(0)
cv.destroyAllWindows