import cv2
res=cv2.imread("kedi.jpg")
cv2.imshow("resim",res)
degisik=cv2.cvtColor(res,cv2.COLOR_BGR2HSV)
cv2.imshow("degisik",degisik)
cv2.waitKey(0)
cv2.destroyAllWindows()