"""
T246 - is the framework's particle ever LIGHT?

R164 measured the defect core action S ~ 4.35 at the Born point: an O(1) lattice
number, hence cutoff-scale.  Scans the coupling from the Born point down toward
lambda_c (t ~ 0.81) to see whether S_core collapses near criticality.
"""
import numpy as np, time
L = 20

def run(t, nwarm=4000, nsamp=50, gap=6, seed=173, cone=0.6):
    rng = np.random.default_rng(seed)
    psi = rng.normal(size=(L,L,L,2)) + 1j*rng.normal(size=(L,L,L,2))
    psi /= np.linalg.norm(psi, axis=-1, keepdims=True)
    idx = np.indices((L,L,L)); masks=[(idx.sum(axis=0)%2==p) for p in (0,1)]
    def sweep():
        for mask in masks:
            prop = psi + cone*(rng.normal(size=psi.shape)+1j*rng.normal(size=psi.shape))
            prop /= np.linalg.norm(prop, axis=-1, keepdims=True)
            wo=np.ones(psi.shape[:3]); wn=np.ones(psi.shape[:3])
            for ax in range(3):
                for sg in (1,-1):
                    nb=np.roll(psi,sg,ax)
                    wo *= (1-t)+t*np.abs(np.sum(np.conj(psi)*nb,axis=-1))**2
                    wn *= (1-t)+t*np.abs(np.sum(np.conj(prop)*nb,axis=-1))**2
            acc=(rng.random(psi.shape[:3])<np.clip(wn/np.maximum(wo,1e-300),0,1))&mask
            psi[acc]=prop[acc]
    for _ in range(nwarm): sweep()
    Sm,Se,dens,mag = [],[],[],[]
    for _ in range(nsamp):
        for _ in range(gap): sweep()
        U=[]
        for ax in range(3):
            z=np.sum(np.conj(psi)*np.roll(psi,-1,ax),axis=-1)
            U.append(z/np.maximum(np.abs(z),1e-300))
        tot=np.zeros(psi.shape[:3]); Fm=np.zeros(psi.shape[:3])
        for (mu,nu) in ((0,1),(1,2),(2,0)):
            F=np.angle(U[mu]*np.roll(U[nu],-1,mu)
                       *np.conj(np.roll(U[mu],-1,nu))*np.conj(U[nu]))
            tot += F-np.roll(F,-1,3-mu-nu); Fm += np.abs(F)/3
        q=np.round(tot/(2*np.pi))
        w={}
        for ax in range(3):
            w[ax]=-np.log(np.maximum((1-t)+t*np.abs(np.sum(np.conj(psi)*np.roll(psi,-1,ax),axis=-1))**2,1e-300))
        S=np.zeros(psi.shape[:3])
        for ax in range(3):
            o1,o2=[a for a in range(3) if a!=ax]
            for da in (0,1):
                for db in (0,1):
                    A=w[ax]
                    if da: A=np.roll(A,-1,o1)
                    if db: A=np.roll(A,-1,o2)
                    S+=A
        m=(q!=0)
        if m.any(): Sm.append(S[m].mean())
        Se.append(S[~m].mean()); dens.append(m.mean()); mag.append(Fm.mean())
    return np.mean(Sm), np.mean(Se), np.mean(dens), np.mean(mag)

print(f"L={L};  lambda = t/(2-t);  lambda_c ~ 0.68 is t ~ 0.81\n")
print("    t    lambda   mean|F|      rho        S(mono)   S(empty)   S_core=excess")
for t in (0.82, 0.86, 0.90, 0.94, 1.00):
    t0=time.time(); Sm,Se,rho,mF = run(t)
    print(f"  {t:4.2f}   {t/(2-t):5.3f}   {mF:7.4f}  {rho:9.6f}   {Sm:8.4f}  {Se:8.4f}   "
          f"{Sm-Se:+8.4f}   [{time.time()-t0:.0f}s]")
