import cv2 as cv
resim=cv.imread("pengu.png")


a=resim.shape[0]-800
b=resim.shape[1]-200



resim[0:10,0:resim.shape[1],0]=100    #üst
resim[0:resim.shape[0],0:10,0]=100    #sol
resim[resim.shape[0]-150:resim.shape[0],0:resim.shape[1],0]=100  #alt
resim[0:resim.shape[0],resim.shape[1]-10:resim.shape[1],0]=100   #sağ çerçeve

cv.imshow("degisik resim",resim)


cv.waitKey(0)
cv.destroyAllWindows