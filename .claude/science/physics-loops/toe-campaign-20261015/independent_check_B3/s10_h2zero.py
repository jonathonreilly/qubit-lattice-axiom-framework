# (d) explicit walk with h2==0 at rank-2 point; plus slice check at b0=11/30,b2=3/20
import numpy as np, pickle, sympy as sp, mpmath as mp
mp.mp.dps=40
B=[sp.Symbol(n,real=True) for n in ('b0','b1','b2')]
Qsym=pickle.load(open('Q.pkl','rb')); Qf=sp.lambdify(B,Qsym,'mpmath')
for uu in [0.039,0.0410,0.0440]:
    print("slice u=%.4f eig(Q)="%uu,np.round(np.linalg.eigvalsh(np.array(mp.matrix(Qf(11/30,np.sqrt(uu),3/20)).tolist(),float)),6))
x=min(mp.polyroots([27,-153432,32])); b2=mp.sqrt(x); b0=b2*(1587357*x**2-9020420424*x+472448)/236224
for sgn in (1,-1):
    b1=sgn*mp.sqrt(mp.sqrt(-(2037123*x**4-11576290482*x**3-561032*x**2)/236224))
    M=mp.matrix(Qf(b0,b1,b2)); E,V=mp.eigsy(M)
    Vn=np.array([[float(mp.sqrt(max(E[i],0))*V[r,i]) for i in (2,3)] for r in range(4)])
    w=Vn.T@np.array([1,3,3,1.]); th=np.arctan2(w[1],w[0]); Rm=np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])
    Vn=Vn@Rm; print("\nb=",[mp.nstr(t,12) for t in (b0,b1,b2)],"eig",[mp.nstr(e,5) for e in E]," (f,h1)(0)=",Vn.T@[1,3,3,1])
    bb=np.array([float(b0),float(b1),float(b2)])
    t1=np.kron([[0,1],[1,0]],np.eye(2)); s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1.,-1])]
    def U(k):
        c,sn=np.cos(k),np.sin(k); phi=np.array([1,c.sum(),c[0]*c[1]+c[0]*c[2]+c[1]*c[2],c.prod()]); f,h1=Vn.T@phi
        g=[sn[a]*(bb[0]+bb[1]*(c[(a+1)%3]+c[(a+2)%3])+bb[2]*c[(a+1)%3]*c[(a+2)%3]) for a in range(3)]
        return f*np.eye(4)+1j*h1*t1+1j*sum(g[a]*np.kron(np.diag([1,-1]),s[a]) for a in range(3)),f
    ks=np.random.default_rng(2).uniform(-np.pi,np.pi,(20000,3))
    print(" max unitarity err:",max(np.linalg.norm(U(k)[0]@U(k)[0].conj().T-np.eye(4),2) for k in ks))
    fs=np.array([U(k)[1] for k in ks]); r=np.linalg.norm(ks,axis=1)
    print(" v=b0+2b1+b2=",bb[0]+2*bb[1]+bb[2]," min 1-f^2 for |k|>0.3:",(1-fs**2)[r>0.3].min())
    import itertools
    print(" corner omegas:",{tuple(q):round(float(np.arccos(np.clip(U(np.pi*np.array(q))[1],-1,1))),6) for q in itertools.product([0,1],repeat=3)})
