# 캠 불러오기
# import cv2
 
# cam = cv2.VideoCapture(0)
# cam.set(3,1280) #CV_CAP_PROP_FRAME_WIDTH
# cam.set(4,720) #CV_CAP_PROP_FRAME_HEIGHT
# #cam.set(5,0) #CV_CAP_PROP_FPS
 
# while True:
#     ret_val, img = cam.read() # 캠 이미지 불러오기
 
#     cv2.imshow("Cam Viewer",img) # 불러온 이미지 출력하기
#     if cv2.waitKey(1) == 27:
#         break  # esc to quit
 

 # import necessary packages
 # pip install cvlib

#-------------------------------------------------------------------------------------
# 캠에 나와있는 사물들 찾아주기
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2

# open webcam (웹캠 열기)
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()
    

# loop through frames
while webcam.isOpened():

    # read frame from webcam 
    status, frame = webcam.read()

    if not status:
        break

    # apply object detection (물체 검출)
    bbox, label, conf = cv.detect_common_objects(frame)

    print(bbox, label, conf)

    # draw bounding box over detected objects (검출된 물체 가장자리에 바운딩 박스 그리기)
    out = draw_bbox(frame, bbox, label, conf, write_conf=True)

    # display output
    cv2.imshow("Real-time object detection", out)

    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# release resources
webcam.release()
cv2.destroyAllWindows()   
# ----------------------------------------------------------------------------
# import cv2
# import cvlib as cv
# import numpy as np

# img = cv2.imread('sample3.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # 얼굴 찾기
# faces, confidences = cv.detect_face(img)

# for (x, y, x2, y2)in faces:

#     # 얼굴 roi 지정
#     face_img = img[y:y2, x:x2]

#     # 성별 예측하기
#     label, confidence = cv.detect_gender(face_img)

#     cv2.rectangle(img, (x, y), (x2, y2), (0, 255, 0), 2)

#     gender = np.argmax(confidence)
#     text = f'{label[gender]}:{confidence[gender]:.1%}'
#     cv2.putText(img, text, (x,y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)

# # 영상 출력
# cv2.imshow('image', img)

# key = cv2.waitKey(0)
# cv2.destroyAllWindows()