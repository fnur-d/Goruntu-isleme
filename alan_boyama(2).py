import cv2 as cv
resim=cv.imread("pengu.png")

print("resmin boyutları :"+ str(resim.shape))
for a in range(0,resim.shape[0],50):   #range(başlangıç,bitiş,artış)
    for k in range(0,resim.shape[1],10):
        resim[a,k]=[10,80,100]


cv.imshow("degisik resim",resim)



cv.waitKey(0)
cv.destroyAllWindows