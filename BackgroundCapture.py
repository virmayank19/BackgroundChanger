import cv2


#capturing from the web cam
cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret,back=cap.read()
    # Here return is true if web cam is working and false otherwise
    # back is the frames capturing by webcam

    if ret:
        cv2.imshow("image",back);

        if cv2.waitKey(5)==ord('q'):
            #save the image
            cv2.imwrite("image.jpg",back)
            break

cap.release()
cv2.destroyAllWindows()