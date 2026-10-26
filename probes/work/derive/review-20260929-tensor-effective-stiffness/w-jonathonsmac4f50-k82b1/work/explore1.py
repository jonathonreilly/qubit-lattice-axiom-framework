import numpy as np, itertools, sympy as sp
# numeric exploration: build Q via Gauss quadrature on sphere (numerical, exploratory)
from numpy.polynomial.legendre import leggauss
xs,ws=leggauss(12); nphi=24
pts=[];wts=[]
for x,w in zip(xs,ws):
    for k in range(nphi):
        ph=2*np.pi*(k+.5)/nphi; s=np.sqrt(1-x*x)
        pts.append([s*np.cos(ph),s*np.sin(ph),x]); wts.append(w*2*np.pi/nphi/(4*np.pi))
pts=np.array(pts);wts=np.array(wts)
idx=[(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
def Msym(v6):
    M=np.zeros((3,3))
    for c,(i,j) in zip(v6,idx): M[i,j]=M[j,i]=c
    return M
# orthonormal basis for sym matrices wrt Frobenius
B=[]
for (i,j) in idx:
    E=np.zeros((3,3));
    if i==j:E[i,i]=1
    else:E[i,j]=E[j,i]=1/np.sqrt(2)
    B.append(E)
def Pi(n,lam):
    # matrices of quadratic forms h1 and tt in basis B
    H=np.zeros((6,6));T=np.zeros((6,6))
    for a in range(6):
        for b in range(6):
            Ma,Mb=B[a],B[b]
            za,zb=Ma@n,Mb@n; fa,fb=n@za,n@zb
            H[a,b]=2*(za@zb-fa*fb)
            T[a,b]=np.trace(Ma@Mb)-2*za@zb+fa*fb-(np.trace(Ma)-fa)*(np.trace(Mb)-fb)/2
    return H,T
Q=np.zeros((18,18));QH=np.zeros((18,18));QT=np.zeros((18,18))
for n,w in zip(pts,wts):
    H,T=Pi(n,0.25)
    nn=np.outer(n,n)
    QH+=w*np.kron(H,nn);QT+=w*np.kron(T,nn)
Q=QH-QT/4
ev=np.linalg.eigvalsh(Q);print(np.round(ev,6))
print('QH eig',np.round(np.linalg.eigvalsh(QH),5));print('QT eig',np.round(np.linalg.eigvalsh(QT),5))
np.save('Q.npy',Q);np.save('QH.npy',QH);np.save('QT.npy',QT)
