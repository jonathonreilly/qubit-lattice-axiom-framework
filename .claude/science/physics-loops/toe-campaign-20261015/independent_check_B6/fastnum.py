# fast LM with analytic Jacobian. modes: unit (V=U^dag) or cplx (V independent). residual U V - I on exact grid.
import numpy as np, pickle, sys
from scipy.optimize import least_squares
def load(fn,m):
    eb=pickle.load(open(fn,'rb'))
    I2=np.eye(2); sx=np.array([[0,1],[1,0]]); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1.,-1])
    Q=[I2,1j*sx,1j*sy,1j*sz]
    from scipy.linalg import sqrtm
    Sh=np.real(sqrtm(np.array([[2.,-1],[-1,2]]))) if m==2 else np.eye(1)
    def mat(b):
        a,i,j=b; E=np.zeros((m,m)); E[i,j]=1; E=Sh@E@np.linalg.inv(Sh); return np.kron(Q[a],E)
    offs=sorted({n for el in eb for n in el}); d=2*m
    R=max(max(abs(x) for x in n) for n in offs); M=4*R+1
    Bg=np.zeros((len(eb),M,M,M,d,d),complex)
    for t,el in enumerate(eb):
        for n,dd in el.items():
            for b,c in dd.items(): Bg[t,n[0]%M,n[1]%M,n[2]%M]+=float(c)*mat(b)
    Bg=np.fft.fftn(Bg,axes=(1,2,3)).reshape(len(eb),-1,d,d)
    const=[t for t,el in enumerate(eb) if (0,0,0) in el]
    return eb,Bg,d,const
def make(Bg,d,unit):
    nb=Bg.shape[0]; I=np.eye(d)
    def split(x):
        c=x[:nb]+1j*x[nb:2*nb]
        e=None if unit else x[2*nb:3*nb]+1j*x[3*nb:4*nb]
        return c,e
    def fun(x):
        c,e=split(x); FU=np.einsum('t,tgab->gab',c,Bg)
        FV=np.conj(FU.transpose(0,2,1)) if unit else np.einsum('t,tgab->gab',e,Bg)
        P=(FU@FV-I).ravel(); return np.concatenate([P.real,P.imag])
    def jac(x):
        c,e=split(x); FU=np.einsum('t,tgab->gab',c,Bg)
        if unit:
            FV=np.conj(FU.transpose(0,2,1))
            dU=Bg; dV=np.conj(Bg.transpose(0,1,3,2))
            Jr=dU@FV+FU@dV          # d/dRe c
            Ji=1j*(dU@FV)-1j*(FU@dV)  # d/dIm c
            J=np.concatenate([Jr,Ji]).reshape(2*nb,-1).T
        else:
            FV=np.einsum('t,tgab->gab',e,Bg)
            A=Bg@FV; Bm=FU@Bg
            J=np.concatenate([A,1j*A,Bm,1j*Bm]).reshape(4*nb,-1).T
        return np.concatenate([J.real,J.imag])
    return fun,jac,nb
if __name__=="__main__":
    fn,m,ntry,seed,mode=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),sys.argv[5]
    eb,Bg,d,const=load(fn,m); fun,jac,nb=make(Bg,d,mode=='unit')
    rng=np.random.default_rng(seed); npar=(2 if mode=='unit' else 4)*nb
    nsol=0
    for tr in range(ntry):
        x0=rng.normal(size=npar)*rng.uniform(0.05,1.0)
        s=least_squares(fun,x0,jac=jac,method='lm',max_nfev=3000*npar,xtol=1e-15,ftol=1e-15,gtol=1e-15)
        c=s.x[:nb]+1j*s.x[nb:2*nb]; mov=np.linalg.norm([c[t] for t in range(nb) if t not in const])
        r=np.linalg.norm(s.fun)
        print(tr,'res %.2e mov %.3e nfev %d'%(r,mov,s.nfev),flush=True)
        if r<1e-9 and mov>1e-4:
            nsol+=1; np.save('sol_%s_%s_%d_%d.npy'%(fn.split('.')[0],mode,seed,tr),s.x)
    print('nontrivial found',nsol)
