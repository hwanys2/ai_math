import numpy as np
A = np.array([[0,0,0,1,0,1,1,0,0],[0,0,0,1,1,0,1,0,0],[0,1,1,0,2,0,0,0,0],[1,0,0,0,0,0,0,1,1]])

## full SVD
U, s, VT = np.linalg.svd(A, full_matrices=True) # linalg.svd 특이값 분해의 결과 / 대각행렬이 아님
U.round(2)
s.round(2)
S = np.zeros((4,9)) # 대각 행렬의 크기인 4X9의 임의의 행렬 생성
S[:4, :4] = np.diag(s) # 특이값을 대각행렬에 삽입
S.round(2)  # 대각행렬

VT.round(2) # 9x9 직교행렬 VT가 생성(V의 전치 행렬)
print(np.allclose(A, np.dot(np.dot(U,S),VT).round(2)))  # allclose() 2개의 행렬이 동일하면 True

S=S[:2,:2]  # 대각행렬 상위 2개만 남기고 제거
S.round(2)
U=U[:,:2]   #직교행렬 2개만 남기고 제거
U.round(2)
VT=VT[:2,:] #전치행렬 2개만 남기고 제거
VT.round(2)

A_prime=np.dot(np.dot(U,S), VT)
print(A)
print(A_prime.round(2))

