"""
T243 - is the framework's photon massive (Higgs) or massless (Coulomb)?

Settles what R161 could not: rho is gauge invariant and blind to the gauge
sector, so use the FIELD STRENGTH.  For a gauge field of mass m_A the
gauge-invariant field-strength correlator is
        S_F(k) ~ A khat^2/(khat^2 + m_A^2)
    massive : S_F -> 0 as k->0 ; S_F/khat^2 -> A/m_A^2, FLAT
    massless: S_F -> const     ; S_F/khat^2 DIVERGES
"""
import numpy as np, time

L = 16
def run(t, nwarm=3000, nsamp=250, gap=4, seed=131, cone=0.6):
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
    NK = 6
    SF = np.zeros(NK); n = 0
    for _ in range(nsamp):
        for _ in range(gap): sweep()
        U = []
        for ax in range(3):
            z = np.sum(np.conj(psi)*np.roll(psi,-1,ax),axis=-1)
            U.append(z/np.maximum(np.abs(z),1e-300))
        for (mu,nu) in ((0,1),(1,2),(2,0)):
            F = np.angle(U[mu]*np.roll(U[nu],-1,mu)
                         *np.conj(np.roll(U[mu],-1,nu))*np.conj(U[nu]))
            f = np.fft.fftn(F)
            # momentum along the direction ORTHOGONAL to the (mu,nu) plane
            rho_ax = 3-mu-nu
            for m in range(1, NK+1):
                sl = [0,0,0]; sl[rho_ax] = m
                SF[m-1] += np.abs(f[tuple(sl)])**2
        n += 1
    return SF/(n*3*L**3)

kn = 2*np.pi*np.arange(1,7)/L; kh2 = 4*np.sin(kn/2)**2
print(f"L={L}, momentum orthogonal to the plaquette plane\n")
print("    t      " + "".join(f"   S_F(n={m})" for m in range(1,7)))
res = {}
for t in (0.45, 0.70, 1.00):
    t0 = time.time(); SF = run(t); res[t] = SF
    print(f"  {t:4.2f}    " + "".join(f"{v:11.6f}" for v in SF) + f"   [{time.time()-t0:.0f}s]")
print("\n    t      " + "".join(f"  S_F/khat^2 (n={m})" for m in range(1,7)))
for t, SF in res.items():
    print(f"  {t:4.2f}    " + "".join(f"{v:19.5f}" for v in SF/kh2))
print("\n  fit S_F = A khat^2/(khat^2 + m_A^2)   ->   1/S_F = (1/A)(1 + m_A^2/khat^2)")
for t, SF in res.items():
    A_ = np.vstack([np.ones(6), 1.0/kh2]).T
    c, *_ = np.linalg.lstsq(A_, 1.0/SF, rcond=None)
    mA2 = c[1]/c[0] if c[0] != 0 else np.nan
    print(f"   t={t:4.2f}:  A = {1/c[0]:9.5f}   m_A^2 = {mA2:+9.5f}   "
          f"{'MASSIVE (Higgs)' if mA2 > 0.05 else 'massless / Coulomb'}")
