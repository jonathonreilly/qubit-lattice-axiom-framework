import numpy as np
np.set_printoptions(precision=6,suppress=True)
C=np.array([[0,0,1],[1,0,0],[0,1,0]],float)          # real cyclic permutation (C e_x = e_y), C^3=I
n=np.ones(3)/np.sqrt(3)
eps=np.zeros((3,3,3))
for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]: eps[i,j,k]=1; eps[i,k,j]=-1
Lk=[-1j*eps[k] for k in range(3)]                     # (L_k)_{ij} = -i eps_{kij}
nL=sum(n[k]*Lk[k] for k in range(3))
rng=np.random.default_rng(3); ok1=ok2=True
for _ in range(20):
    a=rng.normal(); b1,b2=rng.normal(size=2); b=b1+1j*b2
    Wm=a*np.eye(3)+b*C+np.conj(b)*C@C
    for sgn in (+1,-1):
        Wpred=(a-b1)*np.eye(3)+3*b1*np.outer(n,n)+sgn*np.sqrt(3)*b2*nL
        if np.allclose(Wm,Wpred): break
    else: ok1=False
    # levels: m=0 -> a+2 b1 ; m=+-1 -> a-b1 -/+ sqrt3 b2
    ev=np.sort(np.linalg.eigvalsh(Wm)); pred=np.sort([a+2*b1,a-b1-np.sqrt(3)*b2,a-b1+np.sqrt(3)*b2])
    ok2&=np.allclose(ev,pred)
print("E1  W = (a-b1)I + 3 b1 n n^T +/- sqrt3 b2 (n.L)  (sign fixed, same for all samples):",ok1, "| sign used:", end=" ")
a=1;b1=.3;b2=.4; b=b1+1j*b2; Wm=a*np.eye(3)+b*C+np.conj(b)*C@C
print("+" if np.allclose(Wm,(a-b1)*np.eye(3)+3*b1*np.outer(n,n)+np.sqrt(3)*b2*nL) else "-")
print("E2  levels a+2b1 (m=0) and a-b1 -/+ sqrt3 b2 (m=+-1):",ok2)
# proper pi-rotation about [1,-1,0] on vectors
R=np.array([[0,-1,0],[-1,0,0],[0,0,-1]],float); print("    det R =",round(np.linalg.det(R)),"; R n =",R@n)
Wneg=lambda b2_: a*np.eye(3)+(b1+1j*b2_)*C+np.conj(b1+1j*b2_)*C@C
print("E3  R W(b2) R^T == W(-b2):",np.allclose(R@Wneg(b2)@R.T,Wneg(-b2)),"; R (n.L) R^T == -(n.L):",np.allclose(R@nL@R.T,-nL))
print("E4  (n.L) is imaginary => K flips it too: conj(nL) == -nL:",np.allclose(np.conj(nL),-nL))
# also: rotation by pi about n itself (proper) leaves W(b2) invariant, C3 about n too
th=2*np.pi/3; K=np.array([[0,-n[2],n[1]],[n[2],0,-n[0]],[-n[1],n[0],0]])
R3=np.eye(3)+np.sin(th)*K+(1-np.cos(th))*K@K
print("E5  C3 about n commutes with W:",np.allclose(R3@Wm@R3.T,Wm), "(R3 is the cyclic permutation:",np.allclose(R3,C) or np.allclose(R3,C.T),")")
