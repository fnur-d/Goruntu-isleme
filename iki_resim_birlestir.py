import cv2 

res1=cv2.imread("kedi.jpg")
res2=cv2.imread("kopek.jpg")
k=res1.shape
res3=res2[0:res1.shape[0],0:res1.shape[1]]

a=0.30
b=0.70
birlesik=cv2.addWeighted(res1,a,res3,b,0.0)
cv2.imshow("kedi",birlesik)

cv2.waitKey(0)
cv2.destroyAllWindows
