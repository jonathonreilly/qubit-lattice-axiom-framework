import sys; sys.path.insert(0,'scratch')
from e2 import *
import time
mp.mp.dps=60
def shear_data(nd):
    k0=nd.kap
    comp=[]
    def Nc(i):
        return lambda x,y,z,e: nd.num(x,y,z,k0+e)[0][i]
    def D(i,o):
        return mp.diff(Nc(i),(0,0,0,0),o,h=mp.mpf(10)**-12)
    def vec(o): return [D(i,o) for i in range(3)]
    nx=vec((1,0,0,0)); ny=vec((0,1,0,0))
    c2=[v/2 for v in vec((0,0,2,0))]
    eps=vec((0,0,0,1))
    dot=lambda u,v: sum(a*b for a,b in zip(u,v))
    m=dot(c2,nx)/dot(nx,nx); lam=dot(eps,nx)/dot(nx,nx)
    res_par=max(abs(c2[i]-m*nx[i]) for i in range(3)), max(abs(eps[i]-lam*nx[i]) for i in range(3))
    c3=[v/6 for v in vec((0,0,3,0))]
    nxz=vec((1,0,1,0))
    nb=[c3[i]-m*nxz[i] for i in range(3)]
    # F(X,Y,z,e)=N(X-m z^2-lam e, Y, z, e)
    def F(i): return lambda X,Y,z,e: nd.num(X-m*z**2-lam*e,Y,z,k0+e)[0][i]
    w1=[mp.diff(F(i),(0,0,0,0),(0,0,1,1),h=mp.mpf(10)**-12) for i in range(3)]
    a1=dot(w1,nx)/dot(nx,nx); b1=dot(w1,ny)/dot(ny,ny); ga=dot(w1,nb)/dot(nb,nb)
    return dict(m=m,lam=lam,a1=a1,b1=b1,mu=-ga,nx=nx,ny=ny,nb=nb,res=res_par,
        gram=(dot(nx,ny),dot(nx,nb),dot(ny,nb),dot(nx,nx),dot(ny,ny),dot(nb,nb)),
        resid=[w1[i]-a1*nx[i]-b1*ny[i]-ga*nb[i] for i in range(3)])
for w in ('i','ii'):
    for sg in (1,-1):
        t=time.time()
        nd=Node(w,sg); d=shear_data(nd)
        print(w,sg,'m',mp.nstr(d['m'],12),'lam',mp.nstr(d['lam'],12),'a1',mp.nstr(d['a1'],12),'b1',mp.nstr(d['b1'],12))
        print('  mu',mp.nstr(d['mu'],15),'expected',mp.nstr((nd.J+2)/nd.kap**3,15))
        print('  par residuals',[mp.nstr(r,3) for r in d['res']],'gram offdiag',[mp.nstr(g,3) for g in d['gram'][:3]],'diag',[mp.nstr(g,8) for g in d['gram'][3:]], 'decomp resid',max(abs(r) for r in d['resid']), time.time()-t)
