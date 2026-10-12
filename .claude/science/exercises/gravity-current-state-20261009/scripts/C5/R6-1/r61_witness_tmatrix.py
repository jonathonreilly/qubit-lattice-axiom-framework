"""R6-1 witness W (d = 2): spinless lattice fermions, strictly local free hopping, plus a
rank-one-per-K p-wave pair interaction  H_int = (lam/N) sum_K A_K^dag A_K,
A_K = (1/2) sum_k g_K(k) a_{K-k} a_k,  g_K(k) = chi(k) chi(K-k) [f(k) - f(K-k)],
chi = C^infinity plateau bump supported in the open box S = (-a,a)^2, a < pi/2.
Exact claim (algebraic): [Q, A_K] = -qhat2(K) A_K with Q = sum_k qhat(k) n_k (sawtooth lift),
so [Q, H] = 0.  Here: finite-L numerical check of the on-shell 2->2 T-matrix (checked).
Comparator: chi == 1 (analytic form factor) -> umklapp transitions with nonzero amplitude."""
import numpy as np

def wrap(k):                       # representative in (-pi, pi]
    return -(((-k) + np.pi) % (2*np.pi) - np.pi)

def sstep(x):                      # C^inf step: 0 for x<=0, 1 for x>=1
    x = np.clip(x, 0, 1)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)

A_BOX = 0.49*np.pi; W_EDGE = 0.15*np.pi
def chi1d(t):
    return sstep((A_BOX - np.abs(wrap(t)))/W_EDGE)

def make_disp(kind):
    if kind == 'NN':
        return lambda kx, ky: -2*(np.cos(kx)+np.cos(ky))
    if kind == 'NNN':                # strictly local, nearly degenerate minima at 0 and (pi,pi)
        return lambda kx, ky: -2*(np.cos(2*kx)+np.cos(2*ky)) - 0.2*(np.cos(kx)+np.cos(ky))
    raise ValueError

def f(kx, ky):
    return np.sin(kx) + 0.3*np.sin(ky)

def sector(L, K, disp, analytic=False):
    kk = 2*np.pi*np.arange(L)/L
    kx, ky = np.meshgrid(kk, kk, indexing='ij'); kx = wrap(kx.ravel()); ky = wrap(ky.ravel())
    k2x = wrap(K[0]-kx); k2y = wrap(K[1]-ky)
    if analytic:
        c = np.ones_like(kx)
    else:
        c = chi1d(kx)*chi1d(ky)*chi1d(k2x)*chi1d(k2y)
    g = c*(f(kx, ky) - f(k2x, k2y))
    E2 = disp(kx, ky) + disp(k2x, k2y)
    qsum = np.stack([kx + k2x, ky + k2y], 1)
    return g, E2, qsum

def onshell_check(L, K, E, disp, lam, eta, dE, analytic=False):
    g, E2, qsum = sector(L, K, disp, analytic)
    N = L*L
    Pi = 0.5*np.sum(np.abs(g)**2/(E + 1j*eta - E2))/N
    denom = 1 - lam*Pi
    sh = np.where(np.abs(E2-E) < dE)[0]
    if len(sh) == 0:
        return None
    gs = g[sh]; qs = qsum[sh]
    T = lam*np.outer(np.conj(gs), gs)/denom
    absT = np.abs(T)
    dq = np.max(np.abs(qs[:, None, :] - qs[None, :, :]), axis=2)
    classes = sorted(set(np.round((qs - qs[0])/(2*np.pi)).astype(int).tolist().__iter__().__class__ and
                         [tuple(x) for x in np.round((qs - np.array(K))/(2*np.pi)).astype(int)]))
    tol = 1e-12
    nz = absT > tol
    umk = nz & (dq > 1e-9)
    return dict(n=len(sh), classes=classes, nz=int(nz.sum()), maxT=float(absT.max()),
                umk=int(umk.sum()), umkfrac=float((absT[umk]**2).sum()/max((absT**2).sum(), 1e-300)),
                maxdq=float(dq[nz].max()) if nz.any() else 0.0)

def scan_mixed_shells(L, disp, Ks, Es, dE):
    """find shells that contain BOTH pairs with g != 0 (box pairs) and pairs of a different Q class"""
    hits = []
    for K in Ks:
        g, E2, qsum = sector(L, np.array(K), disp)
        cls = np.round((qsum - np.array(K))/(2*np.pi)).astype(int)
        box = np.abs(g) > 1e-3
        for E in Es:
            sh = np.abs(E2 - E) < dE
            if not (sh & box).any():
                continue
            boxcls = set(tuple(x) for x in cls[sh & box])
            other = set(tuple(x) for x in cls[sh]) - boxcls
            if other:
                hits.append((K, E, sorted(boxcls), sorted(other)))
    return hits

if __name__ == "__main__":
    lam = 3.0; L = 240; eta = 0.05; dE = 0.02
    print("witness W: box a = 0.49 pi, plateau |k_j| < 0.34 pi, lam = %.1f, L = %d, eta = %.2f, shell |E2-E| < %.2f" % (lam, L, eta, dE))
    for kind in ['NN', 'NNN']:
        disp = make_disp(kind)
        print("\n== free part:", kind)
        cases = [((0.3, -0.2), -5.0 if kind == 'NN' else -6.0), ((0.9, 0.4), -6.0 if kind == 'NN' else -5.0),
                 ((2.0, 1.5), -1.0), ((np.pi, 0.0), 0.0)]
        for K, E in cases:
            r = onshell_check(L, np.array(K), E, disp, lam, eta, dE)
            rc = onshell_check(L, np.array(K), E, disp, lam, eta, dE, analytic=True)
            if r is None:
                print("K=(%5.2f,%5.2f) E=%5.2f : empty shell" % (K[0], K[1], E)); continue
            print("K=(%5.2f,%5.2f) E=%5.2f shell=%5d Q-classes=%s | W: nonzero T=%6d max|T|=%.3e umklapp-nonzero=%d max|dQ|(nonzero)=%.1e | analytic: umklapp-nonzero=%d, umklapp |T|^2 frac=%.3f"
                  % (K[0], K[1], E, r['n'], r['classes'], r['nz'], r['maxT'], r['umk'], r['maxdq'], rc['umk'], rc['umkfrac']))
        Ks = [(x, y) for x in np.linspace(-np.pi, np.pi, 13) for y in np.linspace(-np.pi, np.pi, 13)]
        Es = np.linspace(-9, 9, 73)
        hits = scan_mixed_shells(120, disp, Ks, Es, 0.03)
        print("mixed shells (box pairs + pairs of another Q class on the same (K,E) shell), L=120 scan: %d found" % len(hits))
        for K, E, bc, oc in hits[:4]:
            r = onshell_check(L, np.array(K), E, disp, lam, eta, dE)
            rc = onshell_check(L, np.array(K), E, disp, lam, eta, dE, analytic=True)
            if r is None or rc is None:
                continue
            print("  K=(%5.2f,%5.2f) E=%5.2f box-classes=%s other=%s | W: nonzero T=%d umklapp-nonzero=%d max|dQ|=%.1e | analytic: umklapp-nonzero=%d frac=%.3f"
                  % (K[0], K[1], E, bc, oc, r['nz'], r['umk'], r['maxdq'], rc['umk'], rc['umkfrac']))
