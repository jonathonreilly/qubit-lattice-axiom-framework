import numpy as np
exec(open('explore1.py').read().split("Q=np.zeros")[0])
Q=np.load('Q.npy')
ev,U=np.linalg.eigh(Q); K=U[:,ev<1e-9]
q=np.array([0,0,1.]); A=K.T@np.kron(np.eye(6),q.reshape(3,1))
u,s,vt=np.linalg.svd(A); y=vt[-1]
Y=sum(c*Bk for c,Bk in zip(y,B)); print(np.round(Y/np.abs(Y).max(),5))
# build rotation-covariant family y*(q): Y(q)=a*qq^T + b*I with Y(z)=Y
a_b=np.linalg.lstsq(np.stack([np.outer(q,q).ravel(),np.eye(3).ravel()],1),Y.ravel(),rcond=None)[0];print(a_b)
a,b=a_b
M=np.zeros((18,18))
for n,w in zip(pts,wts):
    Yn=a*np.outer(n,n)+b*np.eye(3); yv=np.array([np.sum(Bk*Yn) for Bk in B]); v=np.kron(yv,n); M+=w*np.outer(v,v)
c=np.sum(M*Q)/np.sum(M*M); print('c',c,'resid',np.linalg.norm(Q-c*M)/np.linalg.norm(Q))
print(np.round(np.linalg.eigvalsh(Q-c*M),6))
