import cv2

img=cv2.imread("moon.jpg",0)

print(img)
print(img.shape)
print(img.ndim)

resized_image=cv2.resize(img,(100,100))
cv2.imshow("Moon", resized_image)
cv2.imwrite("Moon_resized.jpg",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
