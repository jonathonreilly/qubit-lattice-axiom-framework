"""R7-6, script 1 (d = 1; lattice-exact on the ring's own momentum grid).

Question: does R7-1's pairwise Bakamjian-Thomas (BT) box law, summed over pairs in the three-particle
sector, admit ANY exact Poincare representation with the lattice (kinematic) momentum P?

Rep-independent test: if H, P, K satisfy [K,P] = iH, [K,H] = iP, [H,P] = 0, then M^2 = H^2 - P^2
commutes with K and P, and e^{-i eta K} maps the P-fibre to the boosted fibre.  So every discrete
eigenvalue of M^2 (a bound trimer) must be the SAME in every P-fibre on the plateau.  A drift of the
trimer's E(P)^2 - P^2 rules out every boost K for this H (not only the pairwise K_0 + sum K_W,ij).

Law (as R7-1, script 2, with plateau parameters widened for three legs):
  one complex fermion per site of Z_L; eps(k) = sqrt(m^2 + s(k)^2), s(k) = k on |k| <= B;
  pair term at pair momentum P12: W(P12) = c(P12)[sqrt(M^2 + P12^2) - sqrt(M0^2 + P12^2)],
  M = M0 + lam |g><g| in the pair CM momentum q, g odd, C^inf, supp |q| < kappa.
  Three-particle sector: H = H0 + W_12 + W_23 + W_31 (each at fixed third momentum), antisymmetric.
Also: 2+1 threshold (dimer + particle), weight of the trimer in the c < 1 shell (must be ~0),
and the same test with an added three-body BT-type term? (not here; see report).
"""
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla, itertools, sys, time
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
LEG3 = 1.0                     # three-body leg box |k_i| < LEG3 < pi/3 (no umklapp in the 3-sum)
A_BOX = 1.0                    # interaction legs |k_i| < A_BOX
PI1, PI2 = 0.5, 0.75            # pair-momentum plateau of c(P12)
args = dict(a.split('=') for a in sys.argv[1:])
KAP = float(args.get('kap', 0.25))
PI1 = float(args.get('pi1', PI1)); PI2 = float(args.get('pi2', PI2))
LAM = float(args.get('lam', -6.0))
SYM = args.get('sym', 'fermi')   # 'fermi' (the law) or 'dist' (distinguishable, comparator) or 'bose'

def s(k):
    k = wrap(k); r = sstep((B2 - np.abs(k))/(B2 - B))
    return r*k + (1-r)*np.sin(k)
def eps(k): return np.sqrt(m*m + s(k)**2)
def g(q):
    if SYM == 'bose':
        return sstep(1.0 - (q/KAP)**2)          # even form factor for the symmetric comparator
    return q*sstep(1.0 - (q/KAP)**2)/KAP
def cP(P): return sstep((PI2 - np.abs(P))/(PI2 - PI1))

def pair_W(L, n12, lam):
    """R7-1's pair operator at pair momentum P12 = 2 pi n12/L, as an L x L matrix in k1 (k2 = P12 - k1)."""
    k1 = wrap(2*np.pi*np.arange(L)/L); P = wrap(2*np.pi*n12/L); k2 = wrap(P - k1)
    box = (np.abs(k1) < A_BOX) & (np.abs(k2) < A_BOX)
    th1 = np.arcsinh(k1/m); th2 = np.arcsinh(k2/m); v = 0.5*(th1 - th2)
    q = m*np.sinh(v)
    dqdk = 0.5*m*np.cosh(v)*(1/np.sqrt(m*m + k1**2) + 1/np.sqrt(m*m + k2**2))
    gt = np.where(box, g(q)*np.sqrt(dqdk*2*np.pi/L), 0.0)
    M0 = 2*np.sqrt(m*m + q**2)
    idx = np.where(np.abs(gt) > 0)[0]
    W = {}
    if len(idx) > 0 and cP(P) > 0:
        Ms = np.diag(M0[idx]) + lam*np.outer(gt[idx], gt[idx])
        w_, U = np.linalg.eigh(Ms)
        if w_.min() <= 0: raise ValueError('pair mass operator not positive')
        Hs = (U*np.sqrt(w_**2 + P**2))@U.T
        Wb = cP(P)*(Hs - np.diag(np.sqrt(M0[idx]**2 + P**2)))
        W = (idx, Wb)
    return W, P

def dimer(L, n12, lam):
    """lowest pair energy in the pair sector at P12 (antisym for fermi, sym for bose/dist-even)."""
    k1 = wrap(2*np.pi*np.arange(L)/L); P = wrap(2*np.pi*n12/L); k2 = wrap(P - k1)
    H = np.diag(eps(k1) + eps(k2))
    Wd, _ = pair_W(L, n12, lam)
    if Wd: idx, Wb = Wd; H[np.ix_(idx, idx)] += Wb
    perm = np.array([np.argmin(np.abs(wrap(k1 - kk))) for kk in k2]); X = np.eye(L)[perm]
    sg = -1 if SYM == 'fermi' else +1
    Hp = 0.25*(H + sg*H@X + sg*X@H + X@H@X)
    ev = np.linalg.eigvalsh(0.5*(Hp + Hp.T)); ev = ev[np.abs(ev) > 1e-12]
    return ev.min()

def three_body(L, nP, lam, want_vec=False):
    k = wrap(2*np.pi*np.arange(L)/L)
    inleg = np.abs(k) < LEG3
    legs = np.where(inleg)[0]
    states = []
    for n1 in legs:
        for n2 in legs:
            n3 = (nP - n1 - n2) % L
            if inleg[n3]: states.append((n1, n2, n3))
    index = {st: i for i, st in enumerate(states)}
    D = len(states)
    diag = np.array([eps(k[a]) + eps(k[b]) + eps(k[c]) for a, b, c in states])
    rows, cols, vals = [], [], []
    cache = {}
    for (i, j, spec) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        for st in states:
            n12 = (st[i] + st[j]) % L
            if n12 not in cache: cache[n12] = pair_W(L, n12, lam)[0]
            Wd = cache[n12]
            if not Wd: continue
            idx, Wb = Wd
            pos = np.where(idx == st[i])[0]
            if len(pos) == 0: continue
            col = index[st]
            for r, ni_new in enumerate(idx):
                val = Wb[r, pos[0]]
                if val == 0.0: continue
                nj_new = (n12 - ni_new) % L
                new = list(st); new[i] = ni_new; new[j] = nj_new
                new = tuple(new)
                if new in index:
                    rows.append(index[new]); cols.append(col); vals.append(val)
    Hd = sp.csr_matrix((vals, (rows, cols)), shape=(D, D)) + sp.diags(diag)
    # symmetry-adapted basis
    if SYM == 'dist':
        Hs = Hd; V = None
    else:
        sg = -1 if SYM == 'fermi' else +1
        reps = {}
        for st in states:
            key = tuple(sorted(st))
            if SYM == 'fermi' and len(set(st)) < 3: continue
            reps.setdefault(key, None)
        keys = list(reps.keys())
        r_, c_, v_ = [], [], []
        for col, key in enumerate(keys):
            perms = set(itertools.permutations(key))
            norm = 1/np.sqrt(len(perms)) if SYM == 'bose' else 1/np.sqrt(6)
            for pst in perms:
                if pst not in index: continue
                # parity of permutation from key to pst
                p = [key.index(x) for x in pst] if len(set(key)) == 3 else None
                if SYM == 'fermi':
                    inv = sum(1 for a in range(3) for b in range(a+1, 3) if p[a] > p[b])
                    sgn = -1 if inv % 2 else 1
                else:
                    sgn = 1
                r_.append(index[pst]); c_.append(col); v_.append(sgn*norm)
        V = sp.csr_matrix((v_, (r_, c_)), shape=(D, len(keys)))
        Hs = (V.T @ Hd @ V)
    Hs = 0.5*(Hs + Hs.T)
    n = Hs.shape[0]
    if n < 1500:
        w, U = np.linalg.eigh(Hs.toarray()); E0 = w[0]; u0 = U[:, 0]
    else:
        w, U = sla.eigsh(Hs, k=1, sigma=0.0 if False else None, which='SA', tol=1e-13, maxiter=20000)
        E0 = w[0]; u0 = U[:, 0]
    herm = abs(Hd - Hd.T).max()
    out = dict(E0=E0, dim=n, herm=herm, P=wrap(2*np.pi*nP/L))
    if want_vec:
        vec = u0 if V is None else V @ u0
        # weight of the eigenvector on configurations with some pair momentum in the c<1 shell, and max leg
        w_shell = 0.0; maxleg = 0.0; maxP12 = 0.0
        for amp, st in zip(vec, states):
            if abs(amp) < 1e-14: continue
            ks = [k[a] for a in st]
            P12s = [ks[0]+ks[1], ks[1]+ks[2], ks[2]+ks[0]]
            if max(abs(x) for x in P12s) > PI1: w_shell += amp**2
            if amp**2 > 1e-20:
                maxleg = max(maxleg, max(abs(x) for x in ks)); maxP12 = max(maxP12, max(abs(x) for x in P12s))
        out.update(w_shell=w_shell, maxleg=maxleg, maxP12=maxP12)
    return out

out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)

t0 = time.time()
pr('R7-6 script 1: three-particle sector of the pairwise BT box law; sym = %s, m = %.2f, kappa = %.2f, lam = %.2f' % (SYM, m, KAP, LAM))
pr('  leg box |k| < %.2f (3 legs, no umklapp), interaction legs < %.2f, pair plateau |P12| <= %.2f, cut at %.2f' % (LEG3, A_BOX, PI1, PI2))
for L in [int(x) for x in args.get('Ls', '120,160,200').split(',')]:
    Md = dimer(L, 0, LAM)
    thr = Md + m   # 2+1 threshold at P = 0 (dimer at rest + particle at rest); lattice grid has k=0
    pr('L = %d: dimer mass M_b = %.10f (2m = %.2f); 2+1 threshold at P=0: %.10f' % (L, Md, 2*m, thr))
    rows = []
    for frac in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]:
        nP = int(round(frac*L/(2*np.pi)))
        r = three_body(L, nP, LAM, want_vec=True)
        Mtr = np.sqrt(r['E0']**2 - r['P']**2)
        # 2+1 threshold at this P (continuum form, valid on the plateau): sqrt((M_b+m)^2 + P^2)
        thrP = np.sqrt((Md + m)**2 + r['P']**2)
        rows.append((r['P'], r['E0'], Mtr, thrP))
        pr('  P = %+.5f dim = %5d  E0 = %.12f  sqrt(E0^2-P^2) = %.12f  [2+1 thr %.6f, bound by %.2e]  shell wt %.1e  max|k| %.3f  max|P12| %.3f  herm %.0e'
           % (r['P'], r['dim'], r['E0'], Mtr, thrP, thrP - r['E0'], r['w_shell'], r['maxleg'], r['maxP12'], r['herm']))
    Ms = np.array([x[2] for x in rows])
    pr('  L = %d: trimer invariant-mass spread over P in [0, %.3f]: %.3e   (M(P_max) - M(0) = %+.3e)   [%.0f s]'
       % (L, rows[-1][0], Ms.max() - Ms.min(), Ms[-1] - Ms[0], time.time() - t0))
with open(__file__.replace('.py', '_%s_lam%s_kap%s.out' % (SYM, LAM, KAP)), 'w') as fh:
    fh.write('\n'.join(out) + '\n')
