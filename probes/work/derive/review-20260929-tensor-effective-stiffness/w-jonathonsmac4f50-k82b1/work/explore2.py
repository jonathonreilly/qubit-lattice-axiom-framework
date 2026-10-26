import numpy as np
exec(open('explore1.py').read().split("Q=np.zeros")[0])
Q=np.load('Q.npy')
M6=np.zeros((18,18))
for n,w in zip(pts,wts):
    y=np.array([np.sum(Bk*np.outer(n,n)) for Bk in B]); v=np.kron(y,n); M6+=w*np.outer(v,v)
print(np.round(np.linalg.eigvalsh(M6),6))
# Q vs M6 on common range
ev,U=np.linalg.eigh(M6); r=ev>1e-9
print('rank M6',r.sum())
# is range(Q)==range(M6)?
evq,Uq=np.linalg.eigh(Q); rq=evq>1e-9
P6=U[:,r]@U[:,r].T; PQ=Uq[:,rq]@Uq[:,rq].T
print('range equal',np.linalg.norm(P6-PQ))
# ratio operator
S=U[:,r].T@Q@U[:,r]; D=np.diag(ev[r])
print(np.round(np.linalg.eigvals(np.linalg.solve(D,S)),6))
