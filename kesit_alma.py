import cv2 as cv
resim=cv.imread("pengu.png")
kesit=resim[150:550,200:450]
cv.imshow("degisik resim",kesit)

#kesiti resimdeki bir başka yere yapıştırma kodu:   ** kesitin alanıyla resimdeki belirttiğimiz alan aynı boyutta olmalı
resim[0:400,0:250]=kesit
cv.imshow("kesitin yapiştirilmiş hali",resim)

cv.waitKey(0)
cv.destroyAllWindows