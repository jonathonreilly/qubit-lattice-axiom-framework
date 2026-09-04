"""
T231 - the first simulation of the ACTUAL proposal: Z^4 with M4(C) states.

Everything in the packet so far tested a piece:
  R136-R138, R144 : Z^3 with M2(C)          (the axioms as written)
  R141, R222/223  : Z^4 with S^2 spins      (M2(C) states on a 4D lattice)
The proposed framework is Z^4 with M4(C).  It has never been simulated.

State per site: a pure state of M4(C), i.e. a unit psi in C^4 modulo phase (CP^3).
Edge weight at the Born point (R137/R148):
      phi = Tr(rho rho') = |<psi|psi'>|^2      -- vanishes exactly on orthogonal
                                                  possibilities, which R148 shows
                                                  is what selects it among the six.
Measured: eta from a 3D slice, and z from the dispersion along x4 -- the same two
diagnostics R140/R141 used, so the numbers are directly comparable.
"""
import numpy as np, sys, time

def run(L, nwarm, nmeas, seed=17, want_disp=False):
    rng = np.random.default_rng(seed)
    psi = rng.normal(size=(L,)*4+(4,)) + 1j*rng.normal(size=(L,)*4+(4,))
    psi /= np.linalg.norm(psi, axis=-1, keepdims=True)
    idx = np.indices((L,)*4); A = (idx.sum(axis=0) % 2 == 0); B = ~A
    def nbrs(p):
        out = []
        for ax in range(4):
            out.append(np.roll(p, 1, ax)); out.append(np.roll(p, -1, ax))
        return out
    def weight(p, nb):
        w = np.ones(p.shape[:4])
        for n in nb:
            ov = np.abs(np.sum(np.conj(p)*n, axis=-1))**2
            w *= ov
        return w
    def half(mask, cone):
        nb = nbrs(psi)
        prop = psi + cone*(rng.normal(size=psi.shape) + 1j*rng.normal(size=psi.shape))
        prop /= np.linalg.norm(prop, axis=-1, keepdims=True)
        wo = weight(psi, nb); wn = weight(prop, nb)
        acc = (rng.random(psi.shape[:4]) < np.clip(wn/np.maximum(wo, 1e-300), 0, 1)) & mask
        psi[acc] = prop[acc]
        return acc[mask].mean()
    cone = 1.0
    for t in range(nwarm):
        a = 0.5*(half(A, cone) + half(B, cone))
        if t % 100 == 99:
            cone *= 1.15 if a > 0.55 else (0.87 if a < 0.35 else 1.0)
            cone = min(max(cone, 0.02), 4.0)
    def rho_comps(p):
        return np.einsum('...i,...j->...ij', p, np.conj(p))   # (…,4,4)
    Ssl = np.zeros((L,L,L)); n = 0
    disp = [] if want_disp else None
    for t in range(nmeas):
        half(A, cone); half(B, cone)
        if t % 4 == 0:
            R = rho_comps(psi)
            for s in range(L):
                f = np.fft.fftn(R[:,:,:,s,:,:], axes=(0,1,2))
                Ssl += np.sum(np.abs(f)**2, axis=(-2,-1))
            n += 1
        if want_disp and t % 6 == 0:
            R = rho_comps(psi)
            f = np.fft.fftn(R, axes=(0,1,2))
            disp.append(np.stack([f[mm,0,0,:,:,:] for mm in (1,2,3,4)]))  # 4 modes vs x4
    return Ssl/(n*L), disp, cone

def report(S, L, tag):
    kn = 2*np.pi*np.arange(1,6)/L; kh2 = 4*np.sin(kn/2)**2
    s = np.array([(S[m,0,0]+S[0,m,0]+S[0,0,m])/3 for m in range(1,6)])
    a = s*kh2; b = s*np.sqrt(kh2)
    print(f"  {tag}")
    print(f"     S*khat^2 spread = {a.max()/a.min():5.2f}x  (flat => eta=0, classical 3D)")
    print(f"     S*khat   spread = {b.max()/b.min():5.2f}x  (flat => eta=1, relativistic)")

if __name__ == "__main__":
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    t0 = time.time()
    Ssl, disp, cone = run(L, 4000, 5000, want_disp=True)
    print(f"=== Z^4 with M4(C) states, Born point, L={L}  [{time.time()-t0:.0f}s, "
          f"final cone {cone:.3f}] ===")
    report(Ssl, L, "3D slice of the M4(C) record field")
    # dispersion along x4
    X = np.array(disp)                       # (samples, 4modes, L, 4, 4)
    X = X.reshape(len(disp), 4, L, 16)
    X = X - X.mean(axis=0, keepdims=True)
    print("   n     k       khat      E(k)      E/khat     E/khat^2")
    Es = []; khs = []
    for mi in range(4):
        acc = np.zeros(L)
        for c in range(16):
            g = np.fft.fft(X[:,mi,:,c], axis=1)
            acc += np.mean(np.abs(g)**2, axis=0)
        C = np.fft.ifft(acc).real; C /= C[0]
        es = []
        for t in range(1, L//2):
            num = C[t-1] + C[t+1]
            if C[t] > 0 and num/(2*C[t]) >= 1.0: es.append(np.arccosh(num/(2*C[t])))
        kn = 2*np.pi*(mi+1)/L; kh = 2*np.sin(kn/2)
        if es:
            E = np.median(es[:max(1,len(es)//2)]); Es.append(E); khs.append(kh)
            print(f"   {mi+1}  {kn:6.4f}  {kh:7.4f}  {E:8.5f}  {E/kh:9.4f}  {E/kh**2:9.4f}")
    if len(Es) >= 2:
        Es = np.array(Es); khs = np.array(khs)
        r1 = Es/khs; r2 = Es/khs**2
        print(f"\n  E/khat   spread = {r1.max()/r1.min():5.2f}x  (flat => z=1 RELATIVISTIC)")
        print(f"  E/khat^2 spread = {r2.max()/r2.min():5.2f}x  (flat => z=2 diffusive)")
