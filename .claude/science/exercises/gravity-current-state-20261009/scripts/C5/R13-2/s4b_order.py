# R13-2 s4: Euclidean Monte Carlo (HMC) of the cheapest SIGN-FREE deformation of the energetic N-type compact model.
# PRE-REGISTERED (written before any run):
#  Model (q-basis Trotter/Villain form; weights e^{-S} > 0 by construction):
#   theta_a(x,tau) in [0,2pi): six canonical h slots (diag at sites, off-diag ij at faces x+(e_i+e_j)/2, stored at x).
#   xi_j(x,tau) real: shift (Hubbard-Stratonovich) field of the ENERGETIC vector constraint U_v |G E|^2, mass mu = 1/(4 eps U_v).
#   S = sum beta_t (1 - cos(theta(tau+1)-theta(tau) + (G^T xi)))      [E side made ferro: DeWitt lam = 0 instead of 1/2]
#     + sum mu/2 xi^2 + kappa_s sum (1 - cos (S theta))               [energetic scalar constraint, integer N0914 stencil]
#     + kappa_B/2 sum sin(theta) . B_N . sin(theta)                    [compact N-type potential: small-field = h:R(h), indefinite]
#  Observables (REVISED 20:37Z after a first run showed sin(theta) is gauge-variant and time-uncorrelated; see superseded/):
#   gauge-invariant electric field e = sin(D), D = theta(tau+1)-theta(tau)+G^T xi; G_sector(k,n)=<|proj FT e|^2>, n=1,2;
#   Gaussian reading 1/G(n) = beta_eff + m^2/w_n^2 gives m^2 and Omega_eff^2 = m^2/beta_eff (w_n = 2 sin(pi n/L_t)).
#  Collapse fit: z = slope of log Omega_eff(2pi/L) vs log(2pi/L) over L in {4,6,8}, L_t = L.
#  Operational PRODUCED (worker level, below the registered L>=12 target): z in [0.9,1.1] for B1 and B2 (TT),
#   and E (vector) and both A1 (scalar) channels with slope < 0.3 (not softening).  Anything else: not produced.
import numpy as np, sys, time
from common import *
def run(L, beta_t, kB, ks, mu, ntraj=600, ntherm=200, nmd=10, dt=0.08, seed=1, verbose=False):
    rng=np.random.default_rng(seed); Lt=L
    # --- B_N symbol on stored arrays: M(k) = P^dag T (-R(qhat)) T P
    kk=2*np.pi*np.fft.fftfreq(L)*1.0  # radians
    T=np.diag([1,1,1,1/np.sqrt(2),1/np.sqrt(2),1/np.sqrt(2)])
    offs=[np.zeros(3)]*3+[np.array([.5,.5,0]),np.array([0,.5,.5]),np.array([.5,0,.5])]
    M=np.zeros((L,L,L,6,6),complex)
    for i,a in enumerate(kk):
        for j,b in enumerate(kk):
            for l,c in enumerate(kk):
                k=np.array([a,b,c]); q=2*np.sin(k/2); P=np.diag([np.exp(-1j*k@o) for o in offs])
                M[i,j,l]=P.conj().T@T@(-Rmap(q))@T@P
    # checks: Hermitian, reality M(-k)=conj M(k), 2pi-periodicity
    k=np.array([0.3,-1.1,2.0]); q=2*np.sin(k/2)
    def Msym(k):
        q=2*np.sin(k/2); P=np.diag([np.exp(-1j*k@o) for o in offs]); return P.conj().T@T@(-Rmap(q))@T@P
    per=max(np.abs(Msym(k+2*np.pi*e)-Msym(k)).max() for e in np.eye(3)); real=np.abs(Msym(-k)-Msym(k).conj()).max()
    # --- stencils
    R=lambda f,s,ax: np.roll(f,s,axis=ax)
    def GT(xi):   # xi (...,3) -> canonical shift (...,6): (G^T xi)_jj(y)=xi_j(y-e_j)-xi_j(y); (G^T xi)_ij(y)=xi_j(y)-xi_j(y+e_i)+xi_i(y)-xi_i(y+e_j)
        out=np.empty(xi.shape[:-1]+(6,))
        for j in range(3): out[...,j]=R(xi[...,j],1,j)-xi[...,j]
        for a,(i,j) in zip((3,4,5),((0,1),(1,2),(0,2))):
            out[...,a]=xi[...,j]-R(xi[...,j],-1,i)+xi[...,i]-R(xi[...,i],-1,j)
        return out
    def G(p):     # adjoint of GT
        out=np.empty(p.shape[:-1]+(3,))
        for j in range(3): out[...,j]=R(p[...,j],-1,j)-p[...,j]
        for a,(i,j) in zip((3,4,5),((0,1),(1,2),(0,2))):
            out[...,j]+=p[...,a]-R(p[...,a],1,i); out[...,i]+=p[...,a]-R(p[...,a],1,j)
        return out
    def Sop(q):   # N0914 integer scalar stencil
        out=np.zeros(q.shape[:-1])
        for j in range(3):
            for i in range(3):
                if i!=j: out+=R(q[...,j],-1,i)+R(q[...,j],1,i)-2*q[...,j]
        for a,(i,j) in zip((3,4,5),((0,1),(1,2),(0,2))):
            f=q[...,a]; out-= f-R(f,1,i)-R(f,1,j)+R(R(f,1,i),1,j)
        return out
    def ST(s):    # adjoint
        out=np.zeros(s.shape+(6,))
        for j in range(3):
            for i in range(3):
                if i!=j: out[...,j]+=R(s,1,i)+R(s,-1,i)-2*s
        for a,(i,j) in zip((3,4,5),((0,1),(1,2),(0,2))):
            out[...,a]-= s-R(s,-1,i)-R(s,-1,j)+R(R(s,-1,i),-1,j)
        return out
    # adjoint checks
    A=rng.normal(size=(L,L,L,Lt,6)); X=rng.normal(size=(L,L,L,Lt,3)); s0=rng.normal(size=(L,L,L,Lt))
    adjG=abs(np.sum(GT(X)*A)-np.sum(X*G(A))); adjS=abs(np.sum(Sop(A)*s0)-np.sum(A*ST(s0))); GS=np.abs(Sop(GT(X))).max()
    def BV(s):    # (M * s) per time slice, real
        sh=np.fft.fftn(s,axes=(0,1,2)); out=np.einsum('xyzab,xyztb->xyzta',M,sh); return np.fft.ifftn(out,axes=(0,1,2)).real
    def action(th,xi):
        D=R(th,-1,3)-th+GT(xi); s=np.sin(th)
        return (beta_t*np.sum(1-np.cos(D))+0.5*mu*np.sum(xi**2)+ks*np.sum(1-np.cos(Sop(th)))+0.5*kB*np.sum(s*BV(s)))
    def force(th,xi):
        D=R(th,-1,3)-th+GT(xi); sD=np.sin(D)
        gth=beta_t*(R(sD,1,3)-sD)+ks*ST(np.sin(Sop(th)))+kB*np.cos(th)*BV(np.sin(th))
        gxi=beta_t*G(sD)+mu*xi
        return gth,gxi
    # gradient check
    th=rng.uniform(0,2*np.pi,(L,L,L,Lt,6)); xi=rng.normal(size=(L,L,L,Lt,3))*0.3
    gth,gxi=force(th,xi); dth=rng.normal(size=th.shape)*1e-6; dxi=rng.normal(size=xi.shape)*1e-6
    gchk=abs(action(th+dth,xi+dxi)-action(th-dth,xi-dxi)-2*(np.sum(gth*dth)+np.sum(gxi*dxi)))/abs(2*(np.sum(gth*dth)+np.sum(gxi*dxi)))
    hdr=f"L={L} beta_t={beta_t} kB={kB} ks={ks} mu={mu}: checks periodic={per:.1e} real={real:.1e} adjG={adjG:.1e} adjS={adjS:.1e} S.G^T={GS:.1e} gradrel={gchk:.1e}"
    print(hdr); sys.stdout.flush()
    th=np.zeros((L,L,L,Lt,6))+rng.normal(size=(L,L,L,Lt,6))*0.1; xi=np.zeros((L,L,L,Lt,3))
    acc=0; meas=[]; t0=time.time(); Sold=action(th,xi)
    # sector vectors per axis
    def sect(ax):
        b,c=[i for i in range(3) if i!=ax]
        def comp(i,j):
            v=np.zeros(6); 
            if i==j: v[i]=1
            else:
                key={(0,1):3,(1,0):3,(1,2):4,(2,1):4,(0,2):5,(2,0):5}[(i,j)]; v[key]=1
            return v
        return {'B1':[(comp(b,b)-comp(c,c))/np.sqrt(2)],'B2':[comp(b,c)],'E':[comp(ax,b),comp(ax,c)],'A1a':[comp(ax,ax)],'A1t':[(comp(b,b)+comp(c,c))/np.sqrt(2)]}
    for it in range(ntraj+ntherm):
        pth=rng.normal(size=th.shape); pxi=rng.normal(size=xi.shape)
        H0=Sold+0.5*np.sum(pth**2)+0.5*np.sum(pxi**2)
        t1,x1=th.copy(),xi.copy(); g1,gx=force(t1,x1)
        pth-=0.5*dt*g1; pxi-=0.5*dt*gx
        for m in range(nmd):
            t1+=dt*pth; x1+=dt*pxi; g1,gx=force(t1,x1)
            if m<nmd-1: pth-=dt*g1; pxi-=dt*gx
        pth-=0.5*dt*g1; pxi-=0.5*dt*gx
        S1=action(t1,x1); H1=S1+0.5*np.sum(pth**2)+0.5*np.sum(pxi**2)
        if rng.uniform()<np.exp(min(0,H0-H1)): th,xi,Sold=np.mod(t1,2*np.pi),x1,S1; acc+=1
        if it>=ntherm:
            Dl=R(th,-1,3)-th+GT(xi); s=np.sin(Dl); sh=np.fft.fftn(s,axes=(0,1,2,3))
            rec={}
            for ax in range(3):
                idxk=[0,0,0]; idxk[ax]=1
                k=np.zeros(3); k[ax]=2*np.pi/L
                P=np.diag([np.exp(-1j*k@o) for o in offs])
                for n in (1,2):
                    v=T@P@sh[idxk[0],idxk[1],idxk[2],n,:]
                    for name,vs in sect(ax).items():
                        rec[(name,n)]=rec.get((name,n),0)+sum(abs(u@v)**2 for u in vs)/len(vs)/3
            # condensate diagnostics
            xs=np.indices((L,L,L)).sum(0); stag=((-1.0)**xs)[...,None,None]
            rec['tr_mean']=np.mean(np.abs(np.mean(np.sin(th)*stag,axis=(0,1,2))))   # |staggered sin theta| per slot & slice
            rec['cos_mean']=np.mean(np.cos(Dl))
            meas.append(rec)
    el=time.time()-t0
    names=['B1','B2','E','A1a','A1t']; w1=2*np.sin(np.pi/Lt); res={}
    nb=10; 
    for name in names:
        g1=np.array([m[(name,1)] for m in meas]); g2=np.array([m[(name,2)] for m in meas])
        w2=2*np.sin(2*np.pi/Lt)
        # Gaussian electric propagator <|D(n)|^2> = w_n^2/(beta w_n^2 + m^2)  =>  m^2 = (1/G1-1/G2)/(1/w1^2-1/w2^2), Omega^2=m^2/beta
        def om2(a,b): return (1/a-1/b)/(1/w1**2-1/w2**2)*(a*0+1)
        Rr=om2(g1.mean(),g2.mean())
        bl=len(g1)//nb; Rs=[]
        for b in range(nb):
            mask=np.ones(len(g1),bool); mask[b*bl:(b+1)*bl]=False; Rs.append(om2(g1[mask].mean(),g2[mask].mean()))
        Rs=np.array(Rs); err=np.sqrt((nb-1)*np.var(Rs))
        Om=np.sqrt(max(Rr,0)/ (1/g2.mean()-Rr/w2**2) ) if (1/g2.mean()-Rr/w2**2)>0 else np.nan
        res[name]=(Rr,err,Om)
    print(f"   acc={acc/(ntraj+ntherm):.2f} time={el:.0f}s  <|staggered sin theta|>={np.mean([m['tr_mean'] for m in meas]):+.3f}  <cos D>={np.mean([m['cos_mean'] for m in meas]):.3f}")
    for name in names:
        Rr,err,Om=res[name]; print(f"   {name:4s}: m^2={Rr:.4f}+-{err:.4f}  beta_eff=1/G2-m^2/w2^2  Omega_eff=sqrt(m^2/beta_eff)={Om:.3f}")
    sys.stdout.flush(); return res
if __name__=="__main__":
    pts={'weak':(4.0,4.0,4.0,0.5),'mid':(1.0,1.0,1.0,0.5),'strong':(0.4,0.4,0.4,0.5)}
    which=sys.argv[1]; Ls=[int(x) for x in sys.argv[2].split(',')]; ntraj=int(sys.argv[3]) if len(sys.argv)>3 else 600
    bt,kB,ks,mu=pts[which]; out={}
    for L in Ls:
        out[L]=run(L,bt,kB,ks,mu,ntraj=ntraj,ntherm=ntraj//3,dt=float(sys.argv[4]) if len(sys.argv)>4 else 0.08,nmd=int(sys.argv[5]) if len(sys.argv)>5 else 10)
    if len(Ls)>=3:
        print(f"collapse fit ({which}): slope of log Omega_eff(2pi/L) vs log(2pi/L), L={Ls}")
        for name in ['B1','B2','E','A1a','A1t']:
            x=np.log(2*np.pi/np.array(Ls)); y=np.log([out[L][name][2] for L in Ls]); z=np.polyfit(x,y,1)[0]
            print(f"   {name:4s}: z = {z:.2f}   Omega_eff = {[round(out[L][name][2],3) for L in Ls]}")
