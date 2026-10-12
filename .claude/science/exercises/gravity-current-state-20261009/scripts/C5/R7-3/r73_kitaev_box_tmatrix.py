"""R7-3 script 1: Kitaev-encoded witness W_K on one qubit per site (brick-wall subgraph of Z^2).
Spin law: H = H_Kitaev(Jx=Jy=0.25, Jz=1; gapped A_z phase) + (lam/N) sum_K Ahat_K^dag Ahat_K,
Ahat_K = spin-string image of A_K = 1/2 sum_k g_K(k) a_{K-k} a_k, a_k = Kitaev Bogoliubov modes
(flux-free sector).  In the flux-free sector the a_k obey CAR, so R6-1's two-line commutator gives
[Q,H] = 0 with Q = sum qhat(k) a_k^dag a_k exactly (proved, same algebra).  Here (checked):
  (1) quasiparticle dispersion eps(k) = 2|Jz - Jx e^{ik1} - Jy e^{ik2}| (momentum measured from the
      band minimum, gauge u_x = u_y = -1), gap and mixed shells;
  (2) on-shell 2->2 T-matrix of the box law: nonzero, non-forward, zero umklapp;
      analytic comparator chi == 1 has umklapp;
  (3) an exact on-shell non-forward process at K = 0 (closed form)."""
import numpy as np
Jx, Jy, Jz = 0.25, 0.25, 1.0

def wrap(k):
    return -(((-k) + np.pi) % (2*np.pi) - np.pi)

def sstep(x):
    x = np.clip(x, 0, 1)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)

A_BOX = 0.49*np.pi; W_EDGE = 0.15*np.pi
def chi1d(t):
    return sstep((A_BOX - np.abs(wrap(t)))/W_EDGE)

def eps(kx, ky):
    return 2*np.abs(Jz - Jx*np.exp(1j*kx) - Jy*np.exp(1j*ky))

def f(kx, ky):
    return np.sin(kx) + 0.3*np.sin(ky)

def sector(L, K, analytic=False):
    kk = 2*np.pi*np.arange(L)/L
    kx, ky = np.meshgrid(kk, kk, indexing='ij'); kx = wrap(kx.ravel()); ky = wrap(ky.ravel())
    k2x = wrap(K[0]-kx); k2y = wrap(K[1]-ky)
    c = np.ones_like(kx) if analytic else chi1d(kx)*chi1d(ky)*chi1d(k2x)*chi1d(k2y)
    g = c*(f(kx, ky) - f(k2x, k2y))
    E2 = eps(kx, ky) + eps(k2x, k2y)
    qsum = np.stack([kx + k2x, ky + k2y], 1)
    return kx, ky, g, E2, qsum

def onshell(L, K, E, lam, eta, dE, analytic=False):
    kx, ky, g, E2, qsum = sector(L, K, analytic)
    N = L*L
    Pi = 0.5*np.sum(np.abs(g)**2/(E + 1j*eta - E2))/N
    denom = 1 - lam*Pi
    sh = np.where(np.abs(E2-E) < dE)[0]
    if len(sh) == 0:
        return None
    gs = g[sh]; qs = qsum[sh]; ks = np.stack([kx[sh], ky[sh]], 1)
    T = lam*np.outer(np.conj(gs), gs)/denom
    absT = np.abs(T)
    dq = np.max(np.abs(qs[:, None, :] - qs[None, :, :]), axis=2)
    # non-forward: out pair {k',K-k'} differs from in pair {k,K-k} as an unordered set
    kin = ks; kin2 = np.stack([wrap(K[0]-ks[:, 0]), wrap(K[1]-ks[:, 1])], 1)
    same = (np.max(np.abs(wrap(kin[:, None, :]-kin[None, :, :])), 2) < 1e-9) | \
           (np.max(np.abs(wrap(kin[:, None, :]-kin2[None, :, :])), 2) < 1e-9)
    nz = absT > 1e-12
    nonfwd = nz & ~same
    umk = nz & (dq > 1e-9)
    classes = sorted(set(tuple(x) for x in np.round((qs - np.array(K))/(2*np.pi)).astype(int)))
    return dict(n=len(sh), classes=classes, nz=int(nz.sum()), nonfwd=int(nonfwd.sum()),
                maxT_nonfwd=float(absT[nonfwd].max()) if nonfwd.any() else 0.0,
                umk=int(umk.sum()), umkfrac=float((absT[umk]**2).sum()/max((absT**2).sum(), 1e-300)),
                maxdq=float(dq[nz].max()) if nz.any() else 0.0)

if __name__ == "__main__":
    kk = np.linspace(-np.pi, np.pi, 401)
    KX, KY = np.meshgrid(kk, kk)
    e = eps(KX, KY)
    print("Kitaev A_z phase Jx=%.2f Jy=%.2f Jz=%.2f: eps min %.4f at k=(%.3f,%.3f), max %.4f (gap 2(Jz-Jx-Jy)=%.4f)"
          % (Jx, Jy, Jz, e.min(), KX.flat[e.argmin()], KY.flat[e.argmin()], e.max(), 2*(Jz-Jx-Jy)))
    print("zone-edge band: min eps on k1=pi line = %.4f (zone-edge quasiparticles exist at every energy >= this)"
          % eps(np.pi, kk).min())
    lam = 3.0; L = 240; eta = 0.05; dE = 0.01
    print("\nbox a=0.49pi, lam=%.1f, L=%d, eta=%.2f, shell |E2-E|<%.2f" % (lam, L, eta, dE))
    for K, E in [((0.3, -0.2), 2.3), ((0.0, 0.0), 2.4), ((0.9, 0.4), 2.7), ((np.pi, 0.0), 3.0)]:
        r = onshell(L, np.array(K), E, lam, eta, dE)
        rc = onshell(L, np.array(K), E, lam, eta, dE, analytic=True)
        if r is None:
            print("K=(%5.2f,%5.2f) E=%4.2f: empty shell" % (K[0], K[1], E)); continue
        print("K=(%5.2f,%5.2f) E=%4.2f shell=%5d classes=%s | W_K: nonzero=%6d non-forward nonzero=%6d max|T|nf=%.3e umklapp=%d max|dQ|=%.1e | analytic chi=1: umklapp=%d frac=%.3f"
              % (K[0], K[1], E, r['n'], r['classes'], r['nz'], r['nonfwd'], r['maxT_nonfwd'], r['umk'], r['maxdq'], rc['umk'], rc['umkfrac']))
    # mixed-shell scan
    hits = []
    for Kx in np.linspace(-np.pi, np.pi, 13):
        for Ky in np.linspace(-np.pi, np.pi, 13):
            K = np.array([Kx, Ky])
            kx, ky, g, E2, qsum = sector(120, K)
            cls = np.round((qsum - K)/(2*np.pi)).astype(int)
            box = np.abs(g) > 1e-3
            for E in np.linspace(1.0, 6.0, 51):
                sh = np.abs(E2-E) < 0.03
                if not (sh & box).any():
                    continue
                bc = set(tuple(x) for x in cls[sh & box]); oc = set(tuple(x) for x in cls[sh]) - bc
                if oc:
                    hits.append((tuple(K), E, sorted(bc), sorted(oc)))
    print("\nmixed shells (box pairs + pairs of another Q class on one (K,E) shell), L=120 scan: %d" % len(hits))
    for K, E, bc, oc in hits[:5]:
        r = onshell(L, np.array(K), E, lam, eta, dE); rc = onshell(L, np.array(K), E, lam, eta, dE, analytic=True)
        if r is None or rc is None:
            continue
        print("  K=(%5.2f,%5.2f) E=%4.2f box=%s other=%s | W_K: nonzero=%d non-forward=%d umklapp=%d max|dQ|=%.1e | analytic: umklapp=%d frac=%.3f"
              % (K[0], K[1], E, bc, oc, r['nz'], r['nonfwd'], r['umk'], r['maxdq'], rc['umk'], rc['umkfrac']))
    # exact non-forward process at K = 0 (Jx = Jy makes eps symmetric under k1 <-> k2)
    k_in = np.array([np.pi/4, 0.0]); k_out = np.array([0.0, np.pi/4])
    Ein = eps(*k_in) + eps(*(-k_in)); Eout = eps(*k_out) + eps(*(-k_out))
    gin = chi1d(k_in[0])**2*chi1d(k_in[1])**2*(f(*k_in) - f(*(-k_in)))
    gout = chi1d(k_out[0])**2*chi1d(k_out[1])**2*(f(*k_out) - f(*(-k_out)))
    print("\nexact K=0 process (pi/4,0),(-pi/4,0) -> (0,pi/4),(0,-pi/4): E_in-E_out=%.1e, g_in=%.6f (sqrt2=%.6f), g_out=%.6f, Born lam*g_out*g_in=%.4f"
          % (Ein-Eout, gin, np.sqrt(2), gout, lam*gout*gin))
    print("  Q_in = Q_out = (0,0) exactly; the process is neither forward nor exchange.")
