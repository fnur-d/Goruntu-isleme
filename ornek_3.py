import cv2 as cv
resim=cv.imread("pengu.png")



print("resmin boyutunu "+ str(resim.size))
print("resmin tipi "+ str(resim.dtype))
print("resmin şekli "+ str(resim.shape))

for i in range(resim.shape[0]):
    for j in range(resim.shape[1]):
        if(i%10==0):
            resim[i,j,:]=0
cv.imshow("degisik resim",resim)

cv.waitKey(0)
cv.destroyAllWindows