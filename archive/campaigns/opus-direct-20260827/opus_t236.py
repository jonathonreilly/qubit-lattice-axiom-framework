"""
T236 - does the framework's own U(1) support a PHOTON?

R155: the record field carries an exact LOCAL U(1) with quantised flux, present
in the axioms as written.  A quantised flux means the U(1) is COMPACT, and a
compact U(1) may or may not confine.  Wilson loops decide it, gauge-invariantly
and without gauge fixing:

    U_{x,mu} = <psi_x|psi_{x+mu}> / |<psi_x|psi_{x+mu}>|      (unit modulus)
    W(R,T)   = < product of U around an R x T rectangle >
    -log W   = sigma*(R*T) + mu*2*(R+T) + c
    sigma > 0  => AREA law, confined, no propagating photon
    sigma ~ 0  => perimeter law, deconfined, a photon can exist
"""
import numpy as np, sys, time

def equilibrate(L, d, n, nsweep, seed=53, cone=0.6):
    rng = np.random.default_rng(seed)
    psi = rng.normal(size=(L,)*d+(n,)) + 1j*rng.normal(size=(L,)*d+(n,))
    psi /= np.linalg.norm(psi, axis=-1, keepdims=True)
    idx = np.indices((L,)*d)
    for s in range(nsweep):
        for parity in (0,1):
            mask = (idx.sum(axis=0) % 2 == parity)
            prop = psi + cone*(rng.normal(size=psi.shape)+1j*rng.normal(size=psi.shape))
            prop /= np.linalg.norm(prop, axis=-1, keepdims=True)
            wo = np.ones(psi.shape[:d]); wn = np.ones(psi.shape[:d])
            for ax in range(d):
                for sg in (1,-1):
                    nb = np.roll(psi, sg, ax)
                    wo *= np.abs(np.sum(np.conj(psi)*nb,axis=-1))**2
                    wn *= np.abs(np.sum(np.conj(prop)*nb,axis=-1))**2
            acc = (rng.random(psi.shape[:d]) < np.clip(wn/np.maximum(wo,1e-300),0,1)) & mask
            psi[acc] = prop[acc]
    return psi

def links(psi, d):
    U = []
    for ax in range(d):
        z = np.sum(np.conj(psi)*np.roll(psi,-1,ax), axis=-1)
        U.append(z/np.maximum(np.abs(z),1e-300))
    return U

def wilson(U, mu, nu, R, T):
    """R sites along mu, T along nu"""
    W = np.ones_like(U[0])
    cur = lambda A, shifts: A if not shifts else cur(np.roll(A, -shifts[0][1], shifts[0][0]), shifts[1:])
    sh = [0]*len(U)
    # bottom edge: R links along mu
    P = np.ones_like(U[0]); off = [0]*len(U)
    def get(ax, off):
        A = U[ax]
        for a,o in enumerate(off):
            if o: A = np.roll(A, -o, a)
        return A
    for _ in range(R):
        P = P*get(mu, off); off[mu] += 1
    for _ in range(T):
        P = P*get(nu, off); off[nu] += 1
    for _ in range(R):
        off[mu] -= 1; P = P*np.conj(get(mu, off))
    for _ in range(T):
        off[nu] -= 1; P = P*np.conj(get(nu, off))
    return P

if __name__ == "__main__":
    for (d, n, L, tag) in ((3, 2, 12, "Z^3 + M2(C)  (axioms as written)"),
                           (4, 4, 8,  "Z^4 + M4(C)  (the proposal)")):
        t0 = time.time()
        psi = equilibrate(L, d, n, 2500)
        U = links(psi, d)
        planes = [(a,b) for a in range(d) for b in range(a+1,d)]
        print(f"\n=== {tag}   L={L}  [{time.time()-t0:.0f}s] ===")
        print("   R  T    -log|W|")
        rows = []
        for R in (1,2,3):
            for T in (1,2,3):
                vals = [np.mean(wilson(U,mu,nu,R,T)) for mu,nu in planes]
                w = np.abs(np.mean(vals))
                rows.append((R,T,-np.log(max(w,1e-300))))
                print(f"   {R}  {T}   {-np.log(max(w,1e-300)):9.4f}")
        A = np.array([[R*T, 2*(R+T), 1.0] for R,T,_ in rows])
        y = np.array([v for _,_,v in rows])
        coef, *_ = np.linalg.lstsq(A, y, rcond=None)
        resid = np.max(np.abs(A@coef - y))
        print(f"   fit -log W = sigma*(RT) + mu*perimeter + c")
        print(f"     sigma = {coef[0]:+.4f}   mu = {coef[1]:+.4f}   c = {coef[2]:+.4f}"
              f"   max resid {resid:.3f}")
        print(f"     => {'AREA law: CONFINED, no photon' if coef[0] > 0.05 else 'sigma ~ 0: perimeter-dominated, photon possible'}")
