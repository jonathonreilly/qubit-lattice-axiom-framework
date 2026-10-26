import numpy as np, time, sys, pickle
from lib import *
ferm = sys.argv[1]=='F'
n,bonds=torus_bonds((4,4))
N=8; Nup=4
t0=time.time()
H,codes=build_sector(n,bonds,N,Nup,ferm)
print("built",H.shape,time.time()-t0,flush=True)
rng=np.random.default_rng(1)
w,v=sla.eigsh(H,k=3,which='SA',tol=1e-13,v0=rng.standard_normal(H.shape[0]))
o=np.argsort(w); w=w[o]; v=v[:,o]
E0=w[0]; psi=v[:,0]
print("E0",repr(E0),"next",w[1:],"E0/n",E0/n,flush=True)
# residual
print("resid",np.linalg.norm(H@psi-E0*psi))
# bond energies by direction
def bondexp(wts):
    Hb,_=build_sector(n,bonds,N,Nup,ferm,wts=wts); return psi@(Hb@psi)
ex=bondexp([1.0 if b[2]==0 else 0.0 for b in bonds]); ey=bondexp([1.0 if b[2]==1 else 0.0 for b in bonds])
print("e_x,e_y total",ex,ey,ex+ey-E0,flush=True)
res={}
for q in [(1,0),(2,0),(1,1),(2,1),(2,2),(0,1)]:
    qq=[np.pi/2*m for m in q]
    al=[]
    for (a,b,j,t,c) in bonds:
        c2=list(c); c2[j]+=1
        al.append((np.cos(qq[0]*c[0]+qq[1]*c[1])+np.cos(qq[0]*c2[0]+qq[1]*c2[1]))/2)
    al=np.array(al)
    H1,_=build_sector(n,bonds,N,Nup,ferm,wts=al)
    H2,_=build_sector(n,bonds,N,Nup,ferm,wts=al**2/2)
    held=psi@(H2@psi)
    g=H1@psi
    first=psi@g
    rhs=g-psi*first
    # solve (H-E0+|psi><psi|) x = rhs
    A=sla.LinearOperator(H.shape,matvec=lambda x:H@x-E0*x+psi*(psi@x),dtype=float)
    x,info=sla.cg(A,rhs,rtol=1e-12,atol=0,maxiter=5000)
    relax=-(rhs@x)
    E2=held+relax
    print("q",q,"first",first,"held/n",held/n,"relax/n",relax/n,"Pi=E2/n",E2/n,"cg",info,"time",time.time()-t0,flush=True)
    res[q]=(first,held,relax,E2)
pickle.dump(res,open("t4_%s.pkl"%sys.argv[1],"wb"))
