# # 얼굴인식

# import numpy as np
# import cv2
# # Cascades 디렉토리의 haarcascade_frontalface_default.xml 파일을 Classifier로 사용
# faceCascade = cv2.CascadeClassifier('bin/campractice/haarcascades/haarcascade_frontalface_default.xml')
# cap = cv2.VideoCapture(0)
# cap.set(3,640) # set Width
# cap.set(4,480) # set Height
# while True:
#     ret, img = cap.read()
#     img = cv2.flip(img, 1) # 상하반전(-1이면 거꾸로)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = faceCascade.detectMultiScale(
#         gray,
#         scaleFactor=1.2,
#         minNeighbors=5,
#         minSize=(20, 20)
#     )
#     for (x,y,w,h) in faces:
#         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = img[y:y+h, x:x+w]
#     cv2.imshow('video',img) # video라는 이름으로 출력
#     k = cv2.waitKey(30) & 0xff
#     if k == 27: # press 'ESC' to quit # ESC를 누르면 종료
#         break
# cap.release()
# cv2.destroyAllWindows()


# 내 얼굴이 보이면 사진찍기

# import cv2
# import os

# cam = cv2.VideoCapture(0)
# cam.set(3, 640) # set video width
# cam.set(4, 480) # set video height
# face_detector = cv2.CascadeClassifier('bin/campractice/haarcascades/haarcascade_frontalface_default.xml')

# # For each person, enter one numeric face id
# face_id = input('\n enter user id end press <return> ==>  ')
# print("\n [INFO] Initializing face capture. Look the camera and wait ...")

# # Initialize individual sampling face count
# count = 0
# while(True):
#     ret, img = cam.read()
#     img = cv2.flip(img, 1) # flip video image vertically
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_detector.detectMultiScale(gray, 1.3, 5)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
#         count += 1
#         # Save the captured image into the datasets folder
#         cv2.imwrite("bin/campractice/dateset/" + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
#         cv2.imshow('image', img)
#     k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
#     if k == 27:
#         break
#     elif count >= 30: # Take 30 face sample and stop video
#          break
# # Do a bit of cleanup
# print("\n [INFO] Exiting Program and cleanup stuff")
# cam.release()
# cv2.destroyAllWindows()

# 내 얼굴 정보 저장하기

# import cv2
# import numpy as np
# from PIL import Image
# import os

# # Path for face image database
# path = 'bin/campractice/dateset'  # 지정된 주소
# recognizer = cv2.face.LBPHFaceRecognizer_create()  # 이게 애러뜨면 pip install opencv-contrib-python 설치
# detector = cv2.CascadeClassifier("bin/campractice/haarcascades/haarcascade_frontalface_default.xml");

# # function to get the images and label data
# def getImagesAndLabels(path):
#     imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
#     faceSamples=[]
#     ids = []
#     for imagePath in imagePaths:
#         PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
#         img_numpy = np.array(PIL_img,'uint8')
#         id = int(os.path.split(imagePath)[-1].split(".")[1])
#         faces = detector.detectMultiScale(img_numpy)
#         for (x,y,w,h) in faces:
#             faceSamples.append(img_numpy[y:y+h,x:x+w])
#             ids.append(id)
#     return faceSamples,ids
# print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
# faces,ids = getImagesAndLabels(path)
# recognizer.train(faces, np.array(ids))

# # Save the model into trainer/trainer.yml
# recognizer.write('bin/campractice/trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi
# # Print the numer of faces trained and end program
# print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))


import cv2
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('bin/campractice/trainer/trainer.yml')
cascadePath = "bin/campractice/haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> loze: id=1,  etc
# 이런식으로 사용자의 이름을 사용자 수만큼 추가해준다.
names = ['bini', 'loze', 'ljy', 'chs', 'ksw']

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret, img =cam.read()
    img = cv2.flip(img, 1) # Flip vertically (화면전환 -1, 1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
