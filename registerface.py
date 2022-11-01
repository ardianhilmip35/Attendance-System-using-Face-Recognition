import cv2

camVideo = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_alt.xml')

Nim = input('Enter Your NIM For Register : ')
sampleNum = 0
while(True):
    ret, img = camVideo.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

        # increment sample number
        sampleNum = sampleNum+1
        # saving the captured face in dataset folder
        cv2.imwrite("dataSet/User."+Nim+'.'+ str(sampleNum)+".jpg", gray[y:y+h, x:x+w])

        cv2.imshow('Register Face', img)
    
    # wait for 500 miliseconds
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 10
    elif sampleNum > 10:
        break
camVideo.release()
cv2.destroyAllWindows()
