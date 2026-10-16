# (c) explicit walk at b0=11/30, b2=3/20, b1=+sqrt(u*)
import numpy as np, sympy as sp, pickle, itertools, mpmath as mp
from scipy.optimize import minimize
mp.mp.dps=40
B0,B1,B2=sp.symbols('b0 b1 b2',real=True); u=sp.symbols('u')
P=sp.Poly(259200000000*u**4 - 453744000000*u**3 + 12644840000*u**2 + 1185396800*u - 39225499,u)
ustar=sp.real_roots(P)[1]; b=(sp.Rational(11,30),sp.sqrt(ustar),sp.Rational(3,20))
Qm=pickle.load(open('Q.pkl','rb')).subs({B0:b[0],B1:b[1],B2:b[2]})
Q=mp.matrix([[mp.mpf(str(sp.N(Qm[i,j],40))) for j in range(4)] for i in range(4)])
E,Vv=mp.eigsy(Q)
order=sorted(range(4),key=lambda i:-E[i]); print("eig Q:",[mp.nstr(E[i],8) for i in order])
V=np.array([[float(mp.sqrt(max(E[i],0))*Vv[r,i]) for i in order[:3]] for r in range(4)])  # 4x3, Q~V V^T
w=V.T@np.array([1,3,3,1.]); print("|w|=",np.linalg.norm(w))
# orthogonal Householder taking w -> (1,0,0)
e=np.array([1,0,0.]); v=w/np.linalg.norm(w)-e
H=np.eye(3) if np.linalg.norm(v)<1e-15 else np.eye(3)-2*np.outer(v,v)/(v@v)
V=V@H.T; print("(f,h1,h2)(0)=",V.T@np.array([1,3,3,1.]))
print("coefficients of f,h1,h2 on (1,e1,e2,e3):\n",V.T)
b=np.array([float(x) for x in b]); print("b=",b)
t1=np.kron(np.array([[0,1],[1,0]]),np.eye(2)); t2=np.kron(np.array([[0,-1j],[1j,0]]),np.eye(2))
s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1.,-1])]
t3s=[np.kron(np.diag([1.,-1]),sa) for sa in s]
def parts(k):
    c=np.cos(k); sn=np.sin(k)
    phi=np.array([1,c.sum(),c[0]*c[1]+c[0]*c[2]+c[1]*c[2],c.prod()])
    f,h1,h2=V.T@phi
    g=np.array([sn[a]*(b[0]+b[1]*(c[(a+1)%3]+c[(a+2)%3])+b[2]*c[(a+1)%3]*c[(a+2)%3]) for a in range(3)])
    return f,h1,h2,g
def U(k):
    f,h1,h2,g=parts(k); return f*np.eye(4)+1j*(h1*t1+h2*t2)+1j*sum(g[a]*t3s[a] for a in range(3))
# Fourier coefficients (exact via 3^3 DFT)
N=list(itertools.product([-1,0,1],repeat=3))
grid=[2*np.pi*np.array(m)/3 for m in itertools.product(range(3),repeat=3)]
A={n:sum(U(k)*np.exp(-1j*k@np.array(n)) for k in grid)/27 for n in N}
print("hop norms by |n|_1:",{d:max(np.linalg.norm(A[n]) for n in N if sum(map(abs,n))==d) for d in range(4)})
# reconstruct check
rng=np.random.default_rng(1); ks=rng.uniform(-np.pi,np.pi,(20000,3))
rec=max(np.abs(U(k)-sum(A[n]*np.exp(1j*k@np.array(n)) for n in N)).max() for k in ks[:500])
print("Fourier reconstruction err:",rec)
print("max unitarity err ||U U^+ - 1|| over 20000 random k:",max(np.linalg.norm(U(k)@U(k).conj().T-np.eye(4),2) for k in ks))
# covariance check A_{Rn}=W A_n W^+
Rs=[];
for p in itertools.permutations(range(3)):
    for sg in itertools.product([1,-1],repeat=3):
        M=np.zeros((3,3));
        for i in range(3): M[i,p[i]]=sg[i]
        if round(np.linalg.det(M))==1: Rs.append(M)
def D(R):
    # SU(2) lift: axis-angle
    from scipy.spatial.transform import Rotation
    rv=Rotation.from_matrix(R).as_rotvec(); th=np.linalg.norm(rv)
    if th<1e-12: return np.eye(2)
    nn=rv/th; return np.cos(th/2)*np.eye(2)-1j*np.sin(th/2)*sum(nn[a]*s[a] for a in range(3))
cov=0;
for R in Rs:
    Dm=D(R); assert max(np.abs(Dm@s[a]@Dm.conj().T-sum(R[b_,a]*s[b_] for b_ in range(3))).max() for a in range(3))<1e-12
    W=np.kron(np.eye(2),Dm)
    for n in N:
        Rn=tuple((R@np.array(n)).round().astype(int)); cov=max(cov,np.abs(A[Rn]-W@A[n]@W.conj().T).max())
print("max covariance err:",cov)
# bands: eigenphases ±omega, cos omega=f, each doubly degenerate
def om(k): f,h1,h2,g=parts(k); return np.arctan2(np.sqrt(h1*h1+h2*h2+g@g),f)
ev=np.angle(np.linalg.eigvals(U(ks[0]))); print("eigphases at sample k:",np.sort(ev),"omega=",om(ks[0]))
# touching scan: gap function m(k)=min(omega, pi-omega) ; find zeros
L=64; g1=np.linspace(-np.pi,np.pi,L,endpoint=False)
vals=np.array([[[min(om(np.array([x,y,z])),np.pi-om(np.array([x,y,z]))) for z in g1] for y in g1] for x in g1])
print("grid min of min(omega,pi-omega):",vals.min()," min of omega:",np.array([[[om(np.array([x,y,z])) for z in g1] for y in g1] for x in g1]).min())
cands=np.argwhere(vals<0.15); print("candidates",len(cands))
sols=[]
for ci in cands:
    x0=g1[ci]
    r=minimize(lambda k:(lambda f,h1,h2,g:h1*h1+h2*h2+g@g)(*parts(k)),x0,method='BFGS',options={'gtol':1e-14})
    if r.fun<1e-16:
        kk=(r.x+np.pi)%(2*np.pi)-np.pi; kk[np.abs(np.abs(kk)-np.pi)<1e-6]=np.pi
        if not any(np.linalg.norm(kk-q)<1e-5 for q in sols): sols.append(kk)
print("band touchings (sin omega=0):",[ (np.round(q,6), round(parts(q)[0],9)) for q in sols])
# dispersion near 0
for d in [np.array([1,0,0]),np.array([1,1,0])/np.sqrt(2),np.array([1,1,1])/np.sqrt(3)]:
    for eps in [1e-2,1e-3]:
        print("dir",np.round(d,3),"eps",eps,"omega/eps=",om(eps*d)/eps)
print("b0+2b1+b2 =",b[0]+2*b[1]+b[2])
f,h1,h2,g=parts(np.array([1e-3,0,0])); print("h1,h2 at |k|=1e-3:",h1,h2)
for q in itertools.product([0,np.pi],repeat=3):
    q=np.array(q); o=om(q); f,h1,h2,g=parts(q)
    print("corner",(q/np.pi).astype(int),"f=%.9f h=(%.9f,%.9f) omega=%.9f gap@0=2w=%.9f gap@pi=%.9f"%(f,h1,h2,o,2*o,2*(np.pi-o)))
