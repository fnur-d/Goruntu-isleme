import cv2
res=cv2.imread("kedi.jpg")
yeni=cv2.imread("kedi.jpg")
yeni[:,:,:]=[0,0,0]
sutun=res.shape[0]
satir=res.shape[1]
cv2.imshow("eski",res)
for a in range(sutun):
    for b in range(0,satir-10):
        yeni[a,b+10]=res[a,b]
res[:,0:10,:] =[0,0,0]      

cv2.imshow("resim",yeni)

cv2.waitKey(0)
cv2.destroyAllWindows()