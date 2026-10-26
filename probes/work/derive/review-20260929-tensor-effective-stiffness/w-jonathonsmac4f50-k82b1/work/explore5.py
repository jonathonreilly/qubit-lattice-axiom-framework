import numpy as np
exec(open('explore1.py').read().split("Q=np.zeros")[0])
Q=np.load('Q.npy');QH=np.load('QH.npy');QT=np.load('QT.npy')
# V2 invariant: a1 tr(y^2) q^2 + a2 q y^2 q + a3 (q y q)^2 ; build operator V_{ab,kl} -> evaluate L as sum over n of tr(Pi(n) V2(n))
def V2mat(n,a):
    a1,a2,a3=a
    V=np.zeros((6,6))
    for i,Bi in enumerate(B):
        for j,Bj in enumerate(B):
            V[i,j]=a1*np.sum(Bi*Bj)+a2*0.5*(n@(Bi@Bj+Bj@Bi)@n)+a3*(n@Bi@n)*(n@Bj@n)
    return V
def Lval(a):
    h=t=0
    for n,w in zip(pts,wts):
        H,T=Pi(n,0)
        V=V2mat(n,a); h+=w*np.sum(H*V); t+=w*np.sum(T*V)
    return h,t
for a in [(1,-2,.5),(1,0,0),(0,1,0),(0,0,1)]:
    h,t=Lval(a); 
    # (9/4)<Y^T V Y>, Y=nn-I/3 coordinates
    s=0
    for n,w in zip(pts,wts):
        Yn=np.outer(n,n)-np.eye(3)/3; y=np.array([np.sum(Bk*Yn) for Bk in B]); s+=w*y@V2mat(n,a)@y
    print(a,'H1',h,'TT',t,'H1-TT/4',h-t/4,'9/4<YVY>',2.25*s)
