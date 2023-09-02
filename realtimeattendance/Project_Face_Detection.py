
import cv2
from mtcnn import MTCNN
from .Project_Prediction import facepredict
from student.models import Student, Attendance

def opencamera(faculty, semester, section):
    detector = MTCNN()
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        if ret == True:
            result = detector.detect_faces(frame)
            for i in result:
                x,y,width,height = i['box']
                cropped = frame[y:y+height, x:x+width]
                name = facepredict(cropped)
                student = Student.objects.get(fname=name.split(' ')[0], lname=name.split(' ')[1])
                newattendance = Attendance(faculty=faculty, semester=semester, section=section, studentid=student)
                newattendance.save()
                cv2.rectangle(frame,pt1=(x,y),pt2=(x+width,y+height),color=(255,0,0),thickness=4)
                cv2.imshow('Frame',frame)
            if cv2.waitKey(2) & 0xFF == ord('q'):
                    break
        else:
            break
    capture.release()
    cv2.destroyAllWindows()  

