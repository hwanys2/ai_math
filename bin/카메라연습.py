# # 실시간으로 캠 사용하는 코드
# import cv2

# cap = cv2.VideoCapture(0)

# print('width :%d, height : %d' % (cap.get(3), cap.get(4)))

# while(True):
#     ret, frame = cap.read()    # Read 결과와 frame

#     if(ret) :
#         gray = cv2.cvtColor(frame,  cv2.COLOR_BGR2GRAY)    # 입력 받은 화면 Gray로 변환

#         cv2.imshow('frame_color', frame)    # 컬러 화면 출력
#         cv2.imshow('frame_gray', gray)    # Gray 화면 출력
#         if cv2.waitKey(1) == ord('q'):
#             break
# cap.release()
# cv2.destroyAllWindows()

# 이미지 불러오는 코드
# import cv2

# img_file = "C:/Users/User/Desktop/python folder/alll.jpg" # 표시할 이미지 경로     이 경로에 파일이름 한글이면 오류나는듯 
# img = cv2.imread(img_file)    # 이미지를 읽어서 img 변수에 할당 ---②

# if img is not None:
#   cv2.imshow('IMG', img)      # 읽은 이미지를 화면에 표시      --- ③
#   cv2.waitKey()               # 키가 입력될 때 까지 대기      --- ④
#   cv2.destroyAllWindows()     # 창 모두 닫기            --- ⑤
# else:
#     print('No image file.')

# 사진 찍는 코드

# import cv2

# cap = cv2.VideoCapture(0)                       # 0번 카메라 연결
# if cap.isOpened() :
#     while True:
#         ret, frame = cap.read()                 # 카메라 프레임 읽기
#         if ret:
#             cv2.imshow('camera',frame)          # 프레임 화면에 표시
#             if cv2.waitKey(1) != -1:            # 아무 키나 누르면
#                 cv2.imwrite('photo.jpg', frame) # 프레임을 'photo.jpg'에 저장
#                 break
#         else:
#             print('no frame!')
#             break
# else:
#     print('no camera!')
# cap.release()
# cv2.destroyAllWindows()
 