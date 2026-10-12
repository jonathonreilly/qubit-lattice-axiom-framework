"""R7-1, script 2 (d = 1 numerics; the construction is d-independent): an interacting
lattice law whose two-body box sector is a Bakamjian-Thomas (BT) Poincare-invariant system.

One complex fermion mode per site of a ring Z_L.  Free part as in script 1 (d = 1):
  eps(k) = sqrt(m^2 + s(k)^2), s(k) = k on |k| <= B = 2.6 (C^inf, periodic).
Two-body interaction (number conserving, box supported, momentum conserving without umklapp):
  at total lattice momentum P, in the box sector (k1, k2 = P - k1 both in (-a, a), a < pi/2):
  q(P,k1) = CM-frame momentum of particle 1 (rapidity half-difference), M0 = 2 sqrt(m^2+q^2)
  M = M0 + lam |g><g|,  g(q) odd, C^inf, supported in |q| < kappa
  W(P) = c(P) [ sqrt(M^2 + P^2) - sqrt(M0^2 + P^2) ]   (c = C^inf plateau cutoff in P)
  second-quantized: H = sum_k eps(k) n_k + (1/2) sum_P sum W(P; k1', k1) a+_{k1'} a+_{P-k1'} a_{P-k1} a_{k1}.
Checks (checked = numerics here):
  (i)  bound state: E_b(P)^2 - P^2 is P-independent on the plateau (BT => exact M_b);
       comparator: the same g used as a Galilean pair potential in lattice relative momentum.
  (ii) support: W(P) vanishes outside supp g x supp g; total momentum conserved with no umklapp.
  (iii) real-space kernel of W: quasi-local (super-polynomial decay).
  (iv) scattering is nonzero: internal on-shell T-matrix t(q) and phase shift.
"""
import numpy as np
np.set_printoptions(linewidth=150)

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)

def wrap(k):
    return -(((-k) + np.pi) % (2*np.pi) - np.pi)

B, B2, m = 2.6, 3.0, 0.3
A_BOX = 0.45*np.pi            # interaction box for each leg
KAP = 0.25                    # internal momentum support of g
PI1, PI2 = 0.7, 1.0           # P plateau / P support of c(P)
LAM_BOUND = -2.0              # attractive coupling (bound state check)

def s(k):
    k = wrap(k); r = sstep((B2 - np.abs(k))/(B2 - B))
    return r*k + (1-r)*np.sin(k)

def eps(k):
    return np.sqrt(m*m + s(k)**2)

def g(q):
    return q*sstep(1.0 - (q/KAP)**2) / KAP

def cP(P):
    return sstep((PI2 - np.abs(P))/(PI2 - PI1))

out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line); out.append(line)

def sector(L, nP):
    """lattice two-body sector at P = 2 pi nP / L, ordered pairs (k1, P - k1)."""
    k1 = wrap(2*np.pi*np.arange(L)/L)
    P = wrap(2*np.pi*nP/L)
    k2 = wrap(P - k1)
    box = (np.abs(k1) < A_BOX) & (np.abs(k2) < A_BOX)
    th1 = np.arcsinh(k1/m); th2 = np.arcsinh(k2/m)
    q = m*np.sinh(0.5*(th1 - th2))
    # dq/dk1 at fixed P (k2 = P - k1): dq/dk1 = m cosh(v)/2 * (1/eps1 + 1/eps2), v = (th1-th2)/2
    v = 0.5*(th1 - th2)
    dqdk = 0.5*m*np.cosh(v)*(1/np.sqrt(m*m + k1**2) + 1/np.sqrt(m*m + k2**2))
    return P, k1, k2, box, q, dqdk

def bt_W(L, nP, lam):
    P, k1, k2, box, q, dqdk = sector(L, nP)
    dk = 2*np.pi/L
    gt = np.where(box, g(q)*np.sqrt(dqdk*dk), 0.0)
    M0 = 2*np.sqrt(m*m + q**2)
    H0 = eps(k1) + eps(k2)
    # sanity: on the box sector sqrt(M0^2 + P^2) = eps1 + eps2 exactly
    kin_err = np.max(np.abs(np.sqrt(M0**2 + P**2) - H0)[box]) if box.any() else 0.0
    idx = np.where(np.abs(gt) > 0)[0]
    W = np.zeros((L, L))
    if len(idx) > 0:
        Ms = np.diag(M0[idx]) + lam*np.outer(gt[idx], gt[idx])
        w_, U = np.linalg.eigh(Ms)
        Hs = (U*np.sqrt(w_**2 + P**2))@U.T
        W[np.ix_(idx, idx)] = cP(P)*(Hs - np.diag(np.sqrt(M0[idx]**2 + P**2)))
    return P, k1, k2, box, q, H0, W, gt, kin_err

# ---------------- (i) bound state dispersion ----------------
L = 600
pr('(i) ring L = %d, m = %.2f, kappa = %.2f, lam = %.2f, P plateau |P| <= %.2f' % (L, m, KAP, LAM_BOUND, PI1))
rows = []
for nP in [0, 10, 25, 40, 55, 66, 80, 95]:
    P, k1, k2, box, q, H0, W, gt, kin_err = bt_W(L, nP, LAM_BOUND)
    H = np.diag(H0) + W
    # antisymmetric (odd) sector: project with the exchange k1 <-> P - k1
    perm = np.array([np.argmin(np.abs(wrap(k1 - kk))) for kk in k2])
    X = np.eye(L)[perm]
    Hodd = 0.25*(H - H@X - X@H + X@H@X)   # Pi_odd H Pi_odd, Pi_odd = (1-X)/2
    ev = np.linalg.eigvalsh(0.5*(Hodd + Hodd.T))
    ev = ev[np.abs(ev) > 1e-12]
    Emin = ev.min()
    # comparator: Galilean pair potential with the same g in lattice relative momentum
    kr = wrap(k1 - P/2)
    gg = np.where(box, g(kr)*np.sqrt(2*np.pi/L), 0.0)
    Hg = np.diag(H0) + LAM_BOUND*np.outer(gg, gg)
    Hgo = 0.25*(Hg - Hg@X - X@Hg + X@Hg@X)
    evg = np.linalg.eigvalsh(0.5*(Hgo + Hgo.T)); evg = evg[np.abs(evg) > 1e-12]
    rows.append((P, Emin, np.sqrt(max(Emin**2 - P**2, 0)), evg.min(), np.sqrt(max(evg.min()**2 - P**2, 0)), kin_err, cP(P)))
    pr('(i) P = %+.4f c(P) = %.3f | BT: E_min = %.12f  sqrt(E^2-P^2) = %.12f | Galilean comparator: E_min = %.8f sqrt(E^2-P^2) = %.8f | kin. identity err %.1e'
       % (P, cP(P), Emin, rows[-1][2], evg.min(), rows[-1][4], kin_err))
plateau = [r for r in rows if r[6] == 1.0]
mb = np.array([r[2] for r in plateau]); mg = np.array([r[4] for r in plateau])
pr('(i) threshold 2m = %.4f (bound state iff M_b < 2m)' % (2*m))
pr('(i) on the plateau: BT invariant mass spread = %.2e (M_b = %.10f, 2m = %.2f); Galilean comparator spread = %.2e'
   % (mb.max() - mb.min(), mb.mean(), 2*m, mg.max() - mg.min()))
# finite-L convergence of M_b at P = 0 and at the largest plateau P
for LL in [200, 300, 400, 600, 800]:
    vals = []
    for frac in [0.0, 0.6]:
        nP = int(round(frac*LL/(2*np.pi)))
        P, k1, k2, box, q, H0, W, gt, _ = bt_W(LL, nP, LAM_BOUND)
        H = np.diag(H0) + W
        perm = np.array([np.argmin(np.abs(wrap(k1 - kk))) for kk in k2]); X = np.eye(LL)[perm]
        Ho = 0.25*(H - H@X - X@H + X@H@X); ev = np.linalg.eigvalsh(0.5*(Ho+Ho.T)); ev = ev[np.abs(ev) > 1e-12]
        vals.append(np.sqrt(ev.min()**2 - P**2))
    pr('(i) L = %d : M_b(P=0) = %.14f  M_b(P~0.6) = %.14f  diff = %.1e' % (LL, vals[0], vals[1], vals[1]-vals[0]))

# ---------------- (ii) support and momentum bookkeeping ----------------
P, k1, k2, box, q, H0, W, gt, _ = bt_W(L, 40, LAM_BOUND)
supp = np.abs(gt) > 0
off = np.abs(W)[~np.outer(supp, supp)].max() if (~np.outer(supp, supp)).any() else 0.0
pr('(ii) max |W| outside supp g x supp g = %.1e ; legs inside interaction box on supp: %s ; max |k1+k2-P| (real) on supp = %.1e'
   % (off, bool(box[supp].all()), np.max(np.abs(k1[supp] + k2[supp] - P))))
pr('(ii) max over supp of |k_i| = %.4f  < a = %.4f < pi/2' % (max(np.abs(k1[supp]).max(), np.abs(k2[supp]).max()), A_BOX))

# ---------------- (iii) real-space kernel of W ----------------
Lr = 160
Wfull = np.zeros((Lr, Lr, Lr))            # index order (k1', P, k1)
for nP in range(Lr):
    _, _, _, _, _, _, Wp, _, _ = bt_W(Lr, nP, LAM_BOUND)
    Wfull[:, nP, :] = Wp.T if False else Wp  # Wp[k1', k1]
# w(r, d, x2) = sum exp(i k1' r + i P d + i k1 x2) W(P; k1', k1): r = x1'-x2', d = x2'-x2, x1 = 0
wr = np.fft.ifftn(Wfull)                  # inverse transform over all three momenta
absw = np.abs(wr)
coords = np.fft.fftfreq(Lr)*Lr
R = np.maximum(np.maximum(np.abs(coords)[:, None, None], np.abs(coords)[None, :, None]), np.abs(coords)[None, None, :])
for rr in [0, 2, 5, 10, 20, 30, 40, 60, 79]:
    sel = (R >= rr)
    pr('(iii) max |w| over max-separation >= %2d : %.2e' % (rr, absw[sel].max()))
Fwin = np.abs(wr).max()
pr('(iii) (normalisation: max |w| = %.3e; at L = %d the floor is set by L, not by the law)' % (Fwin, Lr))

# ---------------- (iv) nonzero scattering (continuum internal problem; P-independent by construction) ----------------
qq = np.linspace(-0.6, 0.6, 24001); dq = qq[1]-qq[0]
M0q = 2*np.sqrt(m*m + qq**2)
for lam in [LAM_BOUND, +2.0]:
    pr('(iv) lam = %+.1f:' % lam)
    for q0 in [0.05, 0.1, 0.15, 0.2]:
        E = 2*np.sqrt(m*m + q0**2)
        G = np.sum(g(qq)**2/(E + 1e-4j - M0q))*dq
        t = lam*g(q0)**2/(1 - lam*G)
        pr('(iv)   q = %.2f : on-shell internal t = %+.4e %+.4ej  |t| = %.3e' % (q0, t.real, t.imag, abs(t)))

with open(__file__.replace('.py', '.out'), 'w') as fh:
    fh.write('\n'.join(out) + '\n')
