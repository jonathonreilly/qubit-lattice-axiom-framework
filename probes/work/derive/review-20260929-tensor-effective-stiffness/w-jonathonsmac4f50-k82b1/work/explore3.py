import numpy as np
Q=np.load('Q.npy')
ev,U=np.linalg.eigh(Q); K=U[:,ev<1e-9]   # 18x8 kernel
q=np.array([0,0,1.])
# v = kron(y,q) ; K^T v = 0 -> K^T (I6 kron q) y = 0
A=K.T@np.kron(np.eye(6),q.reshape(3,1))
print(A.shape, np.round(np.linalg.svd(A,compute_uv=False),6))
