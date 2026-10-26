# Ground-state Cauchy-Schwarz bound used in the kill note:
#   |<0|[A,C]|0>| <= sqrt(m_-1(A^dag) m_1(C)) + sqrt(m_-1(A) m_1(C^dag)),
#   m_j(X) = sum_n w_n^j |<n|X|0>|^2  (n over excited states, w_n = E_n - E_0 > 0).
# Hence max(m_-1(A), m_-1(A^dag)) >= |<[A,C]>|^2 / (2 (m_1(C)+m_1(C^dag))).
import numpy as np
rng=np.random.default_rng(1)
for trial in range(5):
    d=40
    H=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d)); H=H+H.conj().T
    w,V=np.linalg.eigh(H); w=w-w[0]
    A=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d)); C=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
    def mom(X,j):
        x=V.conj().T@X@V[:,0]  # <n|X|0>
        return float(np.sum((w[1:]**j)*np.abs(x[1:])**2))
    comm=V[:,0].conj()@(A@C-C@A)@V[:,0]
    lhs=abs(comm); rhs=np.sqrt(mom(A.conj().T,-1)*mom(C,1))+np.sqrt(mom(A,-1)*mom(C.conj().T,1))
    M=max(mom(A,-1),mom(A.conj().T,-1)); bound=lhs**2/(2*(mom(C,1)+mom(C.conj().T,1)))
    print(f"trial {trial}: |<[A,C]>|={lhs:.4f} <= {rhs:.4f} : {lhs<=rhs+1e-9};   max m_-1(A)={M:.4f} >= {bound:.4f} : {M>=bound-1e-9}")
