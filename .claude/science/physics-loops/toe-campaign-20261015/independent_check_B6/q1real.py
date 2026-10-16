# real-parameter search: f^2+|g|^2=1, f,g real covariant trig polys from real basis
import numpy as np, pickle, sys
from scipy.optimize import least_squares
def load(fn):
    rb=pickle.load(open(fn,'rb'))
    offs=sorted({n for b in rb for n in b}); r=int(max(max(abs(x) for x in n) for n in offs)); M=4*r+1
    ks=np.arange(M)*2*np.pi/M
    K=np.stack(np.meshgrid(ks,ks,ks,indexing='ij'),-1).reshape(-1,3)
    Phi=np.zeros((len(rb),K.shape[0],4))
    for t,b in enumerate(rb):
        acc=np.zeros((K.shape[0],4),complex)
        for n,v in b.items():
            e=np.exp(1j*K@np.array([float(int(xx)) for xx in n]))
            acc+=e[:,None]*np.array([complex(x) for x in v])[None,:]
        assert np.abs(acc.imag).max()<1e-9
        Phi[t]=acc.real
    zero=[t for t,b in enumerate(rb) if set(b)=={(0,0,0)}]
    return rb,Phi,zero
def make(Phi):
    def fun(x):
        F=np.einsum('t,tgc->gc',x,Phi); return (F**2).sum(1)-1
    def jac(x):
        F=np.einsum('t,tgc->gc',x,Phi); return 2*np.einsum('gc,tgc->gt',F,Phi)
    return fun,jac
if __name__=="__main__":
    fn,ntry,seed=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
    rb,Phi,zero=load(fn); fun,jac=make(Phi); nb=len(rb)
    rng=np.random.default_rng(seed); found=0; best=[]
    for tr in range(ntry):
        x0=rng.normal(size=nb)*rng.uniform(0.05,0.6)
        s=least_squares(fun,x0,jac=jac,method='lm',xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=20000)
        mov=np.linalg.norm([s.x[t] for t in range(nb) if t not in zero]); r=np.linalg.norm(s.fun)
        best.append(r)
        if r<1e-9 and mov>1e-4:
            found+=1; np.save('q1sol_%s_%d_%d.npy'%(fn.split('.')[0],seed,tr),s.x); print('NONTRIVIAL',tr,r,mov,flush=True)
        if tr%50==0: print(tr,'res %.2e mov %.2e'%(r,mov),flush=True)
    best=np.array(best); print('trials',ntry,'nontrivial',found,'trivial',np.sum(best<1e-9)-found,'min nonzero res',best[best>1e-9].min() if (best>1e-9).any() else None)
