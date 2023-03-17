import cv2 as cv
import numpy

capture = cv.VideoCapture(0)

pretrained_model = cv.CascadeClassifier("face_detector.xml");
while True:
    boolean ,frame = capture.read();
    if boolean:
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY);
        coordinate_list = pretrained_model.detectMultiScale(gray,scaleFactor= 10,minNeighbors = 3,minSize=(30,30))
        for(x,y,w,h) in coordinate_list:
               cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        try:
          if coordinate_list.size >4 :
               print("more than one face found , now we can hit api here ")
          elif coordinate_list.size >0 and coordinate_list.size <5 :
              print("One face is in view ...............")
          else:
              print("No face is in view ")
        except:
          print("Tuple object found ");
        cv.imshow("Live Face Detection",frame)

        if cv.waitKey(20) == ord('x'):
            break
capture.release()
