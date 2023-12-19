import cv2
res=cv2.imread("kedi.jpg")
a=res.shape[0]//2-50
b=res.shape[0]//2+50
c=res.shape[1]//2-50
d=res.shape[1]//2+50
res[a:b,c:d]=(0,0,0)
cv2.imshow("kutulu",res)
cv2.waitKey(0)
cv2.destroyAllWindows()