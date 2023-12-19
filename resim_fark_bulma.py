import cv2
#farklı resimler bul yeniden deneee   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
resim=cv2.imread("pengu.png")
kesit1=resim[100:400,220:620]
kesit2=resim[100:400,220:620]

for i in range(10,70):
    for j in range(15,50):
        kesit1[i,j,2]=180

cv2.imshow("kesit1",kesit1)
cv2.imshow("kesit2",kesit2)

kesit3=kesit1[:,:]+kesit2[:,:]
cv2.imshow("kesit3",kesit3)

cv2.waitKey(0)
cv2.destroyAllWindows