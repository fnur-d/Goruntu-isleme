import cv2
res1=cv2.imread("kedi.jpg")
res2=cv2.imread("kopek.jpg")
res3=res2[0:res1.shape[0],0:res1.shape[1]]
fark=res1-res3
cv2.imshow("fark",fark)
cv2.waitKey(0)
cv2.destroyAllWindows()