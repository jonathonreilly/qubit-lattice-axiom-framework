"""
T241 - does the string tension track the monopole density?

Settles (or bounds) R156's open confinement question, which R159 showed changes
G by a factor of 3.  Scans t in  phi = (1-t) + t|<psi|psi'>|^2 , measuring at
each t both the monopole density and the string tension from Creutz ratios.
"""
import numpy as np, time

L, RMAX = 24, 6

def run(t, nwarm=2500, nsamp=250, gap=4, seed=97, cone=0.6):
    rng = np.random.default_rng(seed)
    psi = rng.normal(size=(L,L,L,2)) + 1j*rng.normal(size=(L,L,L,2))
    psi /= np.linalg.norm(psi, axis=-1, keepdims=True)
    idx = np.indices((L,L,L)); masks = [(idx.sum(axis=0)%2==p) for p in (0,1)]
    def sweep():
        for mask in masks:
            prop = psi + cone*(rng.normal(size=psi.shape)+1j*rng.normal(size=psi.shape))
            prop /= np.linalg.norm(prop, axis=-1, keepdims=True)
            wo = np.ones(psi.shape[:3]); wn = np.ones(psi.shape[:3])
            for ax in range(3):
                for sg in (1,-1):
                    nb = np.roll(psi, sg, ax)
                    wo *= (1-t) + t*np.abs(np.sum(np.conj(psi)*nb,axis=-1))**2
                    wn *= (1-t) + t*np.abs(np.sum(np.conj(prop)*nb,axis=-1))**2
            acc = (rng.random(psi.shape[:3]) < np.clip(wn/np.maximum(wo,1e-300),0,1)) & mask
            psi[acc] = prop[acc]
    for _ in range(nwarm): sweep()
    W = np.zeros((RMAX+1, RMAX+1)); rho = []; nF = []
    for _ in range(nsamp):
        for _ in range(gap): sweep()
        U = []
        for ax in range(3):
            z = np.sum(np.conj(psi)*np.roll(psi,-1,ax),axis=-1)
            U.append(z/np.maximum(np.abs(z),1e-300))
        # Wilson loops
        for mu,nu in ((0,1),(0,2),(1,2)):
            Am=[np.ones_like(U[0])]; An=[np.ones_like(U[0])]
            for R in range(1,RMAX+1): Am.append(Am[-1]*np.roll(U[mu],-(R-1),mu))
            for T in range(1,RMAX+1): An.append(An[-1]*np.roll(U[nu],-(T-1),nu))
            for R in range(1,RMAX+1):
                for T in range(1,RMAX+1):
                    W[R,T] += np.real(np.mean(Am[R]*np.roll(An[T],-R,mu)
                                              *np.conj(np.roll(Am[R],-T,nu))*np.conj(An[T])))
        # monopoles
        def plaq(mu,nu):
            return np.angle(U[mu]*np.roll(U[nu],-1,mu)
                            *np.conj(np.roll(U[mu],-1,nu))*np.conj(U[nu]))
        tot = np.zeros(psi.shape[:3])
        for (mu,nu) in ((0,1),(1,2),(2,0)):
            Fm = plaq(mu,nu); r = 3-mu-nu
            tot += Fm - np.roll(Fm,-1,r)
            nF.append(np.mean(np.abs(Fm)))
        q = np.round(tot/(2*np.pi))
        rho.append(np.mean(q != 0))
    return W/(nsamp*3), np.mean(rho), np.mean(nF)

print(f"L={L}, 250 configurations per point.  W(R,R) shown so the noise floor")
print("is visible: a Creutz ratio built from W below ~1e-3 is meaningless.\n")
print("    t    mean|F|      rho      W(2,2)    W(3,3)    W(4,4)    "
      "chi(2,2)   chi(3,3)   chi(4,4)")
for t in (0.35, 0.55, 0.70, 0.85, 1.00):
    t0 = time.time()
    W, rho, mF = run(t)
    chis = []
    for R in (2,3,4):
        num = W[R,R]*W[R-1,R-1]; den = W[R-1,R]*W[R,R-1]
        chis.append(-np.log(num/den) if num > 1e-12 and den > 1e-12 else np.nan)
    print(f"  {t:4.2f}  {mF:8.4f}  {rho:9.5f}  " +
          "  ".join(f"{W[R,R]:8.5f}" for R in (2,3,4)) + "  " +
          "  ".join(f"{c:+9.5f}" for c in chis) + f"   [{time.time()-t0:.0f}s]")
