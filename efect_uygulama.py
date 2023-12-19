import cv2 as cv
resim=cv.imread("pengu.png")

resim[100,101,0]=150 # saece bir pikseline efect uyguladım    0->blue   1->green   2->red


for a in range(100):
    for b in range(100):
        resim[a,b,2]=100 # bir kısmına efect uyguadım


resim[:,:,1]=200 # resmin tamamına efect uyguladım


resim[150:200,160:300,0]=100 # belirttiğim alanlara efect uyguladım


cv.imshow("degisik resim",resim)

cv.waitKey(0)
cv.destroyAllWindows