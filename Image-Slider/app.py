import cv2

images=["image1.jpg","image2.jpeg","image3.webp","image4.jpeg","image4.jpeg"]
for image in images:
        path=f"images/{image}"
        img=cv2.imread(path)
        resize=cv2.resize(img,(500,500))
        cv2.imshow("Press Any key To Move Slider",resize)
        cv2.waitKey(0)
cv2.destroyAllWindows()