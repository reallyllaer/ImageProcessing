import cv2

## 함수 선언부


## 전역 변수부
src1, dest1 = None, None
path1 = 'c:/gitStudy/ImageProcessing/Images/picture08.jpg'


## 메인 코드부
src1 = cv2.imread(path1)



cv2.imshow('src1', src1)



# 마무리
cv2.waitKey(0)
cv2.destroyAllWindows()

