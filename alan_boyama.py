import cv2 as cv
resim=cv.imread("pengu.png")


for a in range(150):
    for k in range(80):
        resim[30+a,50+k]=[10,10,10]


cv.imshow("degisik resim",resim)


cv.waitKey(0)
cv.destroyAllWindows