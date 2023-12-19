import cv2 as cv
resim=cv.imread("pengu.png")

z=resim.shape[0]-150
k=resim.shape[1]-10

for a in range(10):
    for b in range(resim.shape[1]):
        resim[a,b]=[50,80,90]

for c in range(resim.shape[0]):
    for d in range(10):
        resim[c,d]=[50,80,90]

for e in range(resim.shape[0]):
    for f in range(k,resim.shape[1]):
        resim[e,f]=[50,80,90]

for e in range(z,resim.shape[0]):
    for f in range(resim.shape[1]):
        resim[e,f]=150



cv.imshow("degisik resim",resim)


cv.waitKey(0)
cv.destroyAllWindows