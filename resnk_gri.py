import cv2
res=cv2.imread("kopek.jpg",0)

for a in range (res.shape[0]):
    for b in range (res.shape[1]):
        if res[a,b]>=100:
            res[a,b]=255

cv2.imshow("degisik",res)
cv2.waitKey(0)
cv2.destroyAllWindows()