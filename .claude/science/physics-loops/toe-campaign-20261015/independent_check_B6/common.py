import numpy as np, itertools
def rotations():
    Rs=[]
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1,-1],repeat=3):
            M=np.zeros((3,3),int)
            for i in range(3): M[i,p[i]]=s[i]
            if round(np.linalg.det(M))==1: Rs.append(M)
    return Rs
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1,-1]).astype(complex)
S=[sx,sy,sz]
def axis_angle(R):
    ang=np.arccos(np.clip((np.trace(R)-1)/2,-1,1))
    if abs(ang)<1e-9: return np.array([0,0,1.]),0.
    if abs(ang-np.pi)<1e-9:
        M=(R+np.eye(3))/2; i=np.argmax(np.diag(M)); n=M[:,i]/np.sqrt(M[i,i]); return n,np.pi
    n=np.array([R[2,1]-R[1,2],R[0,2]-R[2,0],R[1,0]-R[0,1]])/(2*np.sin(ang)); return n,ang
def spinJ(j):
    m=np.arange(j,-j-1,-1); d=len(m)
    Jz=np.diag(m).astype(complex); Jp=np.zeros((d,d),complex)
    for a in range(1,d): Jp[a-1,a]=np.sqrt(j*(j+1)-m[a]*(m[a]+1))
    Jx=(Jp+Jp.conj().T)/2; Jy=(Jp-Jp.conj().T)/(2j); return [Jx,Jy,Jz]
from scipy.linalg import expm
def lift(R,j):
    n,a=axis_angle(R); J=spinJ(j)
    return expm(-1j*a*(n[0]*J[0]+n[1]*J[1]+n[2]*J[2]))
def check_half():
    for R in rotations():
        D=lift(R,0.5)
        for j in range(3):
            assert np.allclose(D@S[j]@D.conj().T, sum(R[i,j]*S[i] for i in range(3)))
check_half()
