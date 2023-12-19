import cv2
import numpy as np

resim=cv2.imread("pengu.png",0)
a=int(resim.shape[0]/2-50)
b=int(resim.shape[0]/2+50)
c=int(resim.shape[1]/2-50)
d=int(resim.shape[1]/2+50)

resim[a:b,c:d]=0


cv2.imshow("resim",resim)
cv2.waitKey(0)
cv2.destroyAllWindows
