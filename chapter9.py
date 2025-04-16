import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
faceCascade = cv2.CascadeClassifier("workforcv/haarcascade_frontalface_default.xml")
objectType = "Человек"
while True:
    succes, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,10)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)
    cv2.putText(img, objectType,
                (x + (w // 2) + 88, y + (h//2)-83), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                (0, 0, 0), 2)

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break