import cv2
import numpy

dataset = 'dataset'

cam = cv2.VideoCapture(0)
cam.set(3, 648) #Ubah Lebar Camera
cam.set(4, 448) #Ubah Tinggi Camera

# path face and eye
path_face = "haarcascade_frontalface_alt.xml"
path_eye = "haarcascade_eye.xml"

# Deteksi wajah dan mata
faceDetector = cv2.CascadeClassifier(path_face)
eyeDetector = cv2.CascadeClassifier(path_eye)

# Masukkan Data
Nim  = input('Masukkan Nim Anda : ')
Nama = input('Masukkan Nama Anda : ')
ambilData = 1

while True:
    retV, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(gray, 1.3, 5) #frame, scaleFactor, minNeighbors
    for(x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        namaFile = str(Nim)+'.'+str(ambilData)+'.jpg'
        cv2.imwrite(dataset+'/'+namaFile, frame)
        ambilData += 1
        # Deteksi Mata
        roiAbuAbu = gray[y:y+h, x:x+w]
        roiWarna = frame[y:y+h, x:x+w]
        eyes = eyeDetector.detectMultiScale(roiAbuAbu)
        for (xe, ye, we, he) in eyes:
            cv2.rectangle(roiWarna, (xe,ye),(xe+we, ye+he), (0,0,255),1)

    cv2.imshow('Ambil Data', frame)
    key_pressed = cv2.waitKey(1) & 0xFF 
    if key_pressed == 27 or key_pressed == ord('q'):
        break
    elif ambilData > 20:
        break
cam.release()
cv2.destroyAllWindows()