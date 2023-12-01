import cv2
import serial

class Aifinder:
    FaceDedection = 0
    EyeDedection = 1
    def __init__(self,windowName,mode) -> None:
        self.windowName = windowName
        if mode == Aifinder.FaceDedection:
            self.face_cascade = cv2.CascadeClassifier(r"./cascades/haarcascade_frontalface_default.xml")
        elif mode == Aifinder.EyeDedection:
            self.face_cascade = cv2.CascadeClassifier(r"./cascades/haarcascade_eye.xml")
        self.cap = cv2.VideoCapture(0)
        pass
    def update(self):
        port = serial.Serial('/dev/tty.usbserial-1130',9600)
        while self.cap.isOpened():
            _,img = self.cap.read()

            #img = cv2.imread(r"photos/1588088785877.jpg")
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            faces = self.face_cascade.detectMultiScale(gray,1.1,4)

            for(x,y,w,h) in faces:
                
                cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),3)

            if(len(faces) > 0):
                port.write(b'x')
            else:
                port.write(b'n')
                

            cv2.imshow(self.windowName,img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        pass

