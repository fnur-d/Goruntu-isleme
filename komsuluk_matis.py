import cv2

res1=cv2.imread("kedi.jpg")

for a in range(0,res1.shape[0],10):
    for b in range(res1.shape[1]):
        res1[a,b]=[0,0,0]

cv2.imshow("resim",res1)
cv2.waitKey(0)
cv2.destroyAllWindows()