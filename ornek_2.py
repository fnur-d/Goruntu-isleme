#rgb formatındaki bir resmin grey formatına dönüştürüp tam ortasına 100x100 boyutlarında siyah bir kutu çizdiriniz.
import cv2 as cv
resim=cv.imread("pengu.png",0)


"""
print("resmin boyutunu "+ str(resim.size))
print("resmin tipi "+ str(resim.dtype))
print("resmin şekli "+ str(resim.shape))


resim[405:505,332:432]=0

"""
k=int(resim.shape[0]/2-50)
j=int(resim.shape[1]/2-50)
for a in range(k,+100):
    for b in range(j,j+100):
        resim[a,b]=0 #resim 2 boyutlu olduğu için 0 siyahtan başlar 255 beyaza doğru gider.



cv.imshow("degisik resim",resim)
cv.waitKey(0)
cv.destroyAllWindows