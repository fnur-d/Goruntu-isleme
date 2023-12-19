import cv2

res=cv2.imread("kedi.jpg")
a=res.shape[0]
b=res.shape[1]
res[0:10,:,:]=[0,255,0]
res[:,0:10,:]=[0,255,0]
res[:,b-10:b,:]=[0,255,0]
res[a-10:a,:,:]=[0,255,0]


cv2.imshow("kediresmi",res)
cv2.waitKey(0)
cv2.destroyallwindows()