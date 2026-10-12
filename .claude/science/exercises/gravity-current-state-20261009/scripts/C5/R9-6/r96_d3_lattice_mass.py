"""R9-6, script 2 (d = 3, on the lattice): the two-body box law with the p-wave TRIPLET channel at fixed lattice
total momentum P on an L^3 torus of k1 (k2 = P - k1).  Rep-independent necessary conditions for an exact Poincare
algebra WITH rotations: the bound triplet's invariant mass sqrt(E^2 - P^2) is the same at every P on the plateau,
in every direction (axes, face and body diagonals, generic), and the triplet stays degenerate.
The supp-W block decouples exactly at fixed P (H0 diagonal in k1); W is applied in low-rank form:
  W_ij = (2 pi/L)^3 c(|P|) (q_i . q_j) b_i b_j Omega(P^2; |q_i|, |q_j|) sqrt(Jq_i Jq_j),
  Omega interpolated in u = |q|^2 on n_c Chebyshev nodes (checked against the direct Woodbury kernel),
and the lowest eigenvalues come from Lanczos (scipy eigsh) on the supp block.
Comparator: the same triplet as a Galilean pair potential in lattice relative momentum k1 - P/2.
Usage: python r96_d3_lattice_mass.py L [Pi1 Pi2 B]   (optional plateau / box overrides for probe (d))
"""
import numpy as np, sys, time
from scipy.sparse.linalg import eigsh, LinearOperator
from r81_common import sstep, wrap, BoxLaw, BTKernel

L = int(sys.argv[1]) if len(sys.argv) > 1 else 64
m, KAP, MU_B = 0.5, 0.8, 0.85
PI1 = float(sys.argv[2]) if len(sys.argv) > 2 else 0.6
PI2 = float(sys.argv[3]) if len(sys.argv) > 3 else 1.2
BB = float(sys.argv[4]) if len(sys.argv) > 4 else 2.6
LEG = 2.0 if len(sys.argv) <= 2 else float(sys.argv[5])   # pair-state mask; must contain supp W
TAG = '' if len(sys.argv) <= 2 else '_Pi%.2f_%.2f_B%.2f_B2_%s' % (PI1, PI2, BB, sys.argv[6] if len(sys.argv) > 6 else 'auto')

class BTKernel3(BTKernel):
    """d = 3: <g_x|f|g_x> = int q_x^2 b^2 f d^3q = (4 pi/3) int r^4 b(r^2)^2 f(r) dr."""
    def __init__(self, m, kappa, lam, nq=6001, ns=(-36.0, 56.0, 0.12)):
        self.m, self.kappa, self.lam, self.d = m, kappa, lam, 3
        s0, s1, ds = ns
        self.svals = np.arange(s0, s1 + ds/2, ds); self.tvals = np.exp(self.svals)
        self.cw = ds*self.tvals*np.sqrt(self.tvals)/np.pi
        rr = np.linspace(0.0, kappa, nq); w = np.full(nq, rr[1]-rr[0]); w[0] = w[-1] = 0.5*w[0]
        self.qg = rr; self.wq = w
        self.gg2 = (4*np.pi/3)*rr**4*self.b(rr**2)**2
        self.ng = np.sum(self.gg2*self.wq); self.M0g = self.M0(self.qg)
K0 = BTKernel3(m, KAP, -1.0)
lam = -1.0/np.sum(K0.gg2*K0.wq/(K0.M0g - MU_B))
Kk = BTKernel3(m, KAP, lam)
BB2 = float(sys.argv[6]) if len(sys.argv) > 6 else min(BB + 0.4, 3.1)
law = BoxLaw(m, B=BB, B2=BB2)
cP = lambda P: sstep((PI2 - np.abs(P))/(PI2 - PI1))
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)
pr('L = %d, m = %.2f, kappa = %.2f, lam = %.6f (triplet M_b = %.2f, continuum check %.10f), plateau |P| <= %.2f (c = 0 at %.2f), box B = %.2f, legs < %.2f'
   % (L, m, KAP, lam, MU_B, Kk.bound_mass() or np.nan, PI1, PI2, BB, LEG))

# Chebyshev interpolation of Omega in u = r^2 on [0, kappa^2]
NC = 40
th = np.pi*(np.arange(NC) + 0.5)/NC; uc = 0.5*KAP**2*(1 - np.cos(th)); rc = np.sqrt(uc)
bw = (-1.0)**np.arange(NC)*np.sin(th)            # barycentric weights (Chebyshev 1st kind)
def lagr(u):
    d = u[:, None] - uc[None, :]
    exact = np.isclose(d, 0.0, atol=1e-15)
    d = np.where(exact, 1.0, d); T = bw[None, :]/d; T = T/T.sum(1, keepdims=True)
    hit = exact.any(1); T[hit] = exact[hit].astype(float)
    return T
def omega_check(P2):
    rs = np.random.default_rng(1).uniform(0, KAP, 60)
    D = Kk.Omega(P2, rs, rs); Lr = lagr(rs**2); I = Lr @ Kk.Omega(P2, rc, rc) @ Lr.T
    return np.abs(D - I).max()/np.abs(D).max()

g = 2*np.pi*np.arange(L)/L; gw = wrap(g)
def sector(nP, mode):
    P = wrap(2*np.pi*np.array(nP, float)/L)
    K1 = np.stack(np.meshgrid(gw, gw, gw, indexing='ij'), -1).reshape(-1, 3)
    k2 = wrap(P[None, :] - K1)
    ok = (np.abs(K1) < LEG).all(1) & (np.abs(k2) < LEG).all(1) & (np.abs(K1 + k2 - P).max(1) < 1e-9)
    K1, k2 = K1[ok], k2[ok]
    e1 = np.sqrt(m*m + (K1**2).sum(1)); e2 = np.sqrt(m*m + (k2**2).sum(1))
    H0 = law.eps(K1[:, 0], K1[:, 1], K1[:, 2]) + law.eps(k2[:, 0], k2[:, 1], k2[:, 2])
    P2 = P @ P; Hs = e1 + e2; M0 = np.sqrt(np.maximum(Hs**2 - P2, 1e-30))
    Pk = K1 @ P
    q = K1 + P[None, :]*(Pk/(M0*(Hs + M0)) - e1/M0)[:, None]
    w = np.sqrt(m*m + (q**2).sum(1)); Jq = (w*w*Hs)/(e1*e2*2*w)
    if mode == 'BT':
        r2 = (q**2).sum(1); sel = r2 < KAP**2
        qs = q[sel]; bb = Kk.b(r2[sel])
        D = qs*(bb*np.sqrt(Jq[sel]))[:, None]                  # N x 3
        Lr = lagr(r2[sel]); Oc = Kk.Omega(P2, rc, rc)
        pref = (2*np.pi/L)**3*cP(np.sqrt(P2))
        def Wv(v):
            acc = np.zeros_like(v)
            for a in range(3):
                acc += D[:, a]*(Lr @ (Oc @ (Lr.T @ (D[:, a]*v))))
            return pref*acc
    else:
        kr = wrap(K1 - P[None, :]/2); r2 = (kr**2).sum(1); sel = r2 < KAP**2
        bb = Kk.b(r2[sel]); D = kr[sel]*bb[:, None]
        def Wv(v):
            return (2*np.pi/L)**3*lam*sum(D[:, a]*(D[:, a] @ v) for a in range(3))
    h0 = H0[sel]; N = len(h0)
    op = LinearOperator((N, N), matvec=lambda v: h0*v + Wv(v), dtype=float)
    ev = eigsh(op, k=(5 if not TAG else 12), which='SA', tol=1e-14, maxiter=20000, return_eigenvectors=False)
    return P, np.sort(ev), N

pr('  Omega interpolation (40 Chebyshev nodes in |q|^2) vs direct Woodbury kernel: max rel err %.1e (P = 0), %.1e (|P| = 0.6)'
   % (omega_check(0.0), omega_check(0.36)))
vecs = [(0, 0, 0), (3, 0, 0), (0, 0, 3), (2, 2, 0), (2, 2, 2), (6, 1, -2), (4, -5, 3), (-7, 3, 1), (9, 4, 0),
        (6, 6, 6), (11, 0, 0), (7, 7, -7), (14, 3, 2)]
if TAG:   # probe (d): long vectors along axis, face diagonal, body diagonal
    base = [(1, 0, 0), (1, 1, 0), (1, 1, 1)]
    vecs = [tuple(int(round(t*c*L/(2*np.pi)/np.sqrt(sum(cc*cc for cc in b)))) for c in b)
            for t in (np.array([float(x) for x in sys.argv[7].split(',')]) if len(sys.argv) > 7 else np.arange(0.0, 2.01, 0.25))
            for b in base]
    if len(sys.argv) > 7: TAG += '_scan'
t0 = time.time()
for mode in (['BT', 'Galilean'] if not TAG else ['BT']):
    rows = []
    for v in vecs:
        nP = v if TAG else tuple(int(round(c*L/128)) for c in v)
        P, ev, ns = sector(nP, mode)
        Pn = np.sqrt(P @ P)
        Mall = np.sqrt(np.maximum(ev**2 - Pn**2, 0))
        nedge = int(np.sum(Mall < 0.7))                 # band-bending (edge) pair states below the triplet, if any
        Mb = Mall[Mall >= 0.7][:3]; ev = ev[Mall >= 0.7]
        if len(Mb) < 3: Mb = np.concatenate([Mb, np.full(3 - len(Mb), np.nan)])
        if len(ev) < 4: ev = np.concatenate([ev, np.full(4 - len(ev), np.nan)])
        thr = np.sqrt(4*m*m + Pn**2)
        n = P/Pn if Pn > 0 else P
        rows.append((Pn, cP(Pn), Mb))
        pr('  %-8s nP = %-13s |P| = %.4f n = (%+.2f,%+.2f,%+.2f) c = %.3f  sqrt(E^2-P^2) = %.12f %.12f %.12f  (triplet split %.1e; next %.4f vs threshold %.4f; %d pair states; %d edge states below)'
           % (mode, str(nP), Pn, n[0], n[1], n[2], cP(Pn), Mb[0], Mb[1], Mb[2], Mb.max() - Mb.min(),
              ev[3], thr, ns, nedge))
    pl = np.array([r[2] for r in rows if r[1] == 1.0 and np.all(np.isfinite(r[2]))])
    pr('  %s: plateau spread of the triplet invariant mass (all P, all directions) = %.2e ; max triplet split = %.2e ; mean = %.12f'
       % (mode, pl.max() - pl.min(), (pl.max(1) - pl.min(1)).max(), pl.mean()))
pr('  time %.0fs' % (time.time() - t0))
with open(__file__.replace('.py', '_L%d%s.out' % (L, TAG)), 'w') as fh:
    fh.write('\n'.join(out) + '\n')
