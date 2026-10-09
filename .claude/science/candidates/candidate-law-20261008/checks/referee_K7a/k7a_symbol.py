"""K7a part 2 (gravity): 4D staggered linearized Einstein-Hilbert on Z^4, symbol level.

Half-shift convention (A25): every difference has symbol i*s_k, s_k = 2 sin(k_k/2).  Lattice
position classes: h_{mu nu} at x + (e_mu+e_nu)/2 (class {mu} xor {nu} of the 16 half-shift classes),
xi_mu at x + e_mu/2.  All derivative products land on a single class (checked in the real-space
script).  Here: symbolic checks (sympy) + numeric scans on the Bloch symbol.

G1 exact gauge invariance  K(s) D(s) = 0  (symbolic, all s)
G2 W(B4) covariance: Q(g H g^T ; g s) = Q(H ; s) for generators (symbolic) and all 384 (numeric)
G3 spectrum: rank 6, nonzero eigenvalues proportional to s^2 = sum_mu s_mu^2 (symbolic ratio)
G4 de Donder gauge fixing: K + K_gf = (1/4) s^2 (G - 1/2 t t^T): every component has propagator 1/s^2
   photon: K_A + gf = s^2 * 1 : same operator.  Zeros of sum_mu s_mu^2 on the lattice BZ.
G5 temporal-gauge reduction == A25/A23 (M, V) and constraint rows; leapfrog with tau = a_t
G6 no extra modes: nullity of K(s) == 4 at every sampled k != 0 incl. all 16 zone corners
G7 counts: hypercubic-invariant 2-derivative quadratic forms (A23 C5 = 9) vs O(4)-invariant ones;
   gauge-invariant ones; dimension-4 anisotropic (non-O(4)) forms that exact gauge symmetry removes
G8 CFL: leapfrog with tau = a_s (hypercubic Q) is unstable; tau = a_s/2 is stable
"""
import itertools, sys, time
import numpy as np
import sympy as sp

t0 = time.time()
rng = np.random.default_rng(20261008)
np.set_printoptions(precision=6, suppress=True, linewidth=140)
PAIRS = [(i, j) for i in range(4) for j in range(i, 4)]        # 10 comps; time = index 3
SQ2 = sp.sqrt(2)


def say(*a):
    print(*a); sys.stdout.flush()


# ---------------------------------------------------------------- symbolic symbol
s = sp.symbols('s1:5', real=True)
q = sp.symbols('q0:10', real=True)           # orthonormal coordinates: H:H = sum q^2
H = sp.zeros(4, 4)
for c, (i, j) in enumerate(PAIRS):
    if i == j:
        H[i, i] = q[c]
    else:
        H[i, j] = H[j, i] = q[c] / SQ2
sv = sp.Matrix(s)
s2 = sum(x ** 2 for x in s)
trH = H.trace()
Hs = H * sv
Qform = sp.Rational(1, 4) * (s2 * (H.T * H).trace() - 2 * (Hs.T * Hs)[0] + 2 * (sv.T * H * sv)[0] * trH - s2 * trH ** 2)
Qform = sp.expand(Qform)
K = sp.hessian(Qform, q)                      # Q = 1/2 q^T K q   (K = Hessian)
K = K.applyfunc(sp.expand)

# gauge generator D: xi (4) -> q (10): (D xi)_{mu nu} = s_mu xi_nu + s_nu xi_mu  (orthonormal coords)
D = sp.zeros(10, 4)
for c, (i, j) in enumerate(PAIRS):
    if i == j:
        D[c, i] = 2 * s[i]
    else:
        D[c, j] += s[i] / SQ2
        D[c, i] += s[j] / SQ2
        D[c, j] = D[c, j]
# note: h_ij = (s_i xi_j + s_j xi_i) ; orthonormal q = sqrt2 * h_ij -> sqrt2*(...) ; fix:
D = sp.zeros(10, 4)
for c, (i, j) in enumerate(PAIRS):
    if i == j:
        D[c, i] = 2 * s[i]
    else:
        D[c, j] += SQ2 * s[i]
        D[c, i] += SQ2 * s[j]
G1 = (K * D).applyfunc(sp.expand)
say(f'G1 gauge invariance K(s) D(s) = 0 identically in s: {G1 == sp.zeros(10, 4)}   (K is {K.shape}, symmetric: {K == K.T})')

# ---------------------------------------------------------------- G2 hypercubic covariance
def signed_perms(n):
    out = []
    for p in itertools.permutations(range(n)):
        for sg in itertools.product((1, -1), repeat=n):
            R = np.zeros((n, n), dtype=int)
            for i in range(n):
                R[p[i], i] = sg[i]            # R e_i = sg_i e_{p(i)}
            out.append(R)
    return out


W4 = signed_perms(4)
say(f'|W(B4)| = {len(W4)}')


def Q_numeric(Hn, sn):
    s2n = sn @ sn
    Hs_ = Hn @ sn
    t = np.trace(Hn)
    return 0.25 * (s2n * np.sum(Hn * Hn) - 2 * Hs_ @ Hs_ + 2 * (sn @ Hn @ sn) * t - s2n * t * t)


worst = 0.0
for R in W4:
    for _ in range(3):
        sn = rng.normal(size=4)
        A = rng.normal(size=(4, 4)); Hn = A + A.T
        worst = max(worst, abs(Q_numeric(R @ Hn @ R.T, R @ sn) - Q_numeric(Hn, sn)))
say(f'G2 W(B4) covariance Q(R H R^T; R s) = Q(H; s): all 384 elements, max |dev| = {worst:.2e}')
# symbolic for generators
gens = [np.array([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]),
        np.array([[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]),
        np.diag([-1, 1, 1, 1])]
Hsym = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'H{min(i,j)}{max(i,j)}', real=True))
def Qsym(Hm, sm):
    s2_ = (sm.T * sm)[0]; Hs_ = Hm * sm; t = Hm.trace()
    return sp.Rational(1, 4) * (s2_ * (Hm.T * Hm).trace() - 2 * (Hs_.T * Hs_)[0] + 2 * (sm.T * Hm * sm)[0] * t - s2_ * t ** 2)
ok = True
for R in gens:
    Rm = sp.Matrix(R.tolist())
    ok &= sp.expand(Qsym(Rm * Hsym * Rm.T, Rm * sv) - Qsym(Hsym, sv)) == 0
say(f'   symbolic invariance under generators (axis swap, 4-cycle t->x, reflection): {ok}')

# ---------------------------------------------------------------- G3 spectrum
Kf = sp.lambdify(s, K, 'numpy')
Df = sp.lambdify(s, D, 'numpy')
eigratio = []
for _ in range(2000):
    sn = rng.normal(size=4)
    w = np.linalg.eigvalsh(np.array(Kf(*sn), float))
    eigratio.append(np.sort(w / (sn @ sn)))
eigratio = np.array(eigratio)
say(f'G3 eigenvalues of K(s)/s^2 over 2000 random s (should be s-independent): spread {np.ptp(eigratio, axis=0).max():.1e}')
say(f'   values: {np.round(eigratio[0], 10)}  -> multiplicities: {dict(zip(*np.unique(np.round(eigratio[0], 8), return_counts=True)))}')

# ---------------------------------------------------------------- G4 gauge fixing / photon
# de Donder: add  1/2 (d_mu h_mu nu - 1/2 d_nu h)^2 -> Q_gf
dd = Hs - sp.Rational(1, 2) * sv * trH
Qgf = sp.expand(sp.Rational(1, 2) * (dd.T * dd)[0])
Kgf = sp.hessian(Qgf, q)
Gm = sp.eye(10)                               # H:H = sum q^2
tvec = sp.Matrix([1 if i == j else 0 for (i, j) in PAIRS])   # trace = t.q
target = sp.Rational(1, 4) * s2 * (sp.eye(10) - sp.Rational(1, 2) * tvec * tvec.T) * 2   # Hessian of (1/4)s^2(H:H - 1/2 trH^2) = (1/2) s^2 (1 - 1/2 t t^T)
target = sp.Rational(1, 2) * s2 * (sp.eye(10) - sp.Rational(1, 2) * tvec * tvec.T)
diff = (K + Kgf - target).applyfunc(sp.expand)
say(f'G4 K + K_gf = (1/2) s^2 (1 - 1/2 t t^T)  (so every h-bar component has propagator ~ 1/s^2): {diff == sp.zeros(10, 10)}')
# photon: Q_A = 1/4 F^2 -> K_A = s^2 1 - s s^T ; Feynman gauge adds s s^T
a = sp.symbols('a0:4', real=True)
Fsq = sum((s[m] * a[n] - s[n] * a[m]) ** 2 for m in range(4) for n in range(m + 1, 4))
KA = sp.hessian(sp.expand(Fsq / 2), a)          # (1/4) F_{mn}F_{mn} = 1/2 sum_{m<n} F^2
say(f'   photon: K_A = s^2 1 - s s^T : {(KA - (s2 * sp.eye(4) - sv * sv.T)).applyfunc(sp.expand) == sp.zeros(4, 4)}; Feynman gauge -> s^2 * 1')
say('   => graviton (h-bar) and photon (A) both have Euclidean propagator 1/ (sum_mu s_mu^2), s_mu = 2 sin(k_mu/2): identical poles at all k (tree level).')

# zeros of sum s_mu^2 on the real BZ: only k=0.  Euclid: continue k_4 -> i w.
kz = np.linspace(-np.pi, np.pi, 41)
mn = min(((2 * np.sin(np.array(k) / 2)) ** 2).sum() for k in itertools.product(kz, repeat=4) if any(abs(x) > 1e-9 for x in k))
say(f'   min of sum_mu s_mu^2 over the BZ grid (k != 0): {mn:.4f}  (>0: no doubler, single zero at k = 0)')

# ---------------------------------------------------------------- G5 temporal gauge == A23/A25 (M, V)
# A23 orthonormal 3D basis order: (11,22,33,12,13,23); ours: PAIRS order (00,01,02,03,11,12,13,22,23,33)
sp3 = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
idx4 = [PAIRS.index(p) for p in sp3]
sys.path.insert(0, '/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/test_K7a/ref')
import stag2
Vref = stag2.V_EH_orth; Mref = stag2.M_orth_GR()

worstV = worstM = 0.0
Kt_sym = K.subs({s[0]: 0, s[1]: 0, s[2]: 0, s[3]: 1})          # s_4^2 block
spatial_rows = idx4
for _ in range(50):
    sn = rng.normal(size=4)
    Kn = np.array(Kf(*sn), float)
    blockV = Kn[np.ix_(idx4, idx4)].copy()
    # potential part: set s_4 = 0 in the symbol -> spatial block should be V_EH(s_sp)
    Kn0 = np.array(Kf(sn[0], sn[1], sn[2], 0.0), float)
    worstV = max(worstV, np.abs(Kn0[np.ix_(idx4, idx4)] - Vref(sn[:3])).max())
Kt = np.array(Kt_sym.tolist(), float)[np.ix_(idx4, idx4)]
Minv = np.linalg.inv(Kt)
worstM = np.abs(Minv - Mref).max()
say(f'G5 spatial block of 4D symbol at s_4 = 0 vs A23/A25 V_EH(s): max dev {worstV:.1e};  inverse of s_4^2 kinetic block vs A23 M=2(-1/2,1,1): max dev {worstM:.1e}')
# constraint rows from h_44 (lapse) and h_4i (shift): derivative of Q w.r.t. those comps at h_4mu = 0
c44 = PAIRS.index((3, 3)); c4i = [PAIRS.index((i, 3)) for i in range(3)]
row_lapse = K[c44, idx4]
row_shift = [K[c, idx4] for c in c4i]
# A23 Hamiltonian row r(s) = s^2 tr h - s h s in orthonormal coordinates (spatial s)
sx = sp.Matrix(s[:3])
def r_row(sm):
    out = []
    for (i, j) in sp3:
        if i == j:
            out.append(sum(x ** 2 for x in sm) - sm[i] ** 2)
        else:
            out.append(-SQ2 * sm[i] * sm[j])
    return sp.Matrix([out])
rl = (row_lapse.subs(s[3], 0))
say(f'   lapse row  dQ/dh_44|(h_4mu=0) at s_4=0 = -(1/2) * A23 Hamiltonian row R: {(rl + sp.Rational(1,2) * r_row(sx)).applyfunc(sp.simplify) == sp.zeros(1, 6)}')
# shift rows ~ s_4 * (s_j (h_ij - delta_ij tr h)) : verify against divergence of the kinetic momentum
def shift_expected(i):
    out = []
    for (a_, b_) in sp3:
        Hm = sp.zeros(3, 3)
        if a_ == b_:
            Hm[a_, a_] = 1
        else:
            Hm[a_, b_] = Hm[b_, a_] = 1 / SQ2
        mom = Hm - sp.eye(3) * Hm.trace()
        out.append(sum(sx[j] * mom[i, j] for j in range(3)))
    return sp.Matrix([out])
okshift = True
for i in range(3):
    e = row_shift[i]
    e = sp.Matrix([[sp.expand(x) for x in e]])
    ratio_ok = (e - s[3] * shift_expected(i) * sp.Rational(-1, 1) * sp.Rational(1, 2) * 2).applyfunc(sp.expand)
    # find proportionality constant c with e = c s_4 * expected
    cands = [sp.simplify(e[0, k] / (s[3] * shift_expected(i)[0, k])) for k in range(6) if shift_expected(i)[0, k] != 0]
    okshift &= len(set(cands)) == 1
say(f'   shift rows dQ/dh_4i (h_4mu = 0) are s_4 * [s_j (h_ij - delta_ij tr h)] up to one constant {set(cands)}: {okshift}  (momentum constraint = d_j pi_ij with pi = (dh/dt - delta tr dh/dt)/2)')

# leapfrog from temporal-gauge discrete Lorentzian action: h_{t+1}-2h_t+h_{t-1} = -tau^2 M V h_t   (same K P K)
def leapfrog_U(sn3, tau):
    V = Vref(2 * np.sin(sn3 / 2) * 0 + sn3)  # sn3 already holds s
    I6, Z6 = np.eye(6), np.zeros((6, 6))
    Kk = lambda a: np.block([[I6, a * Mref], [Z6, I6]])
    Pp = lambda b: np.block([[I6, Z6], [-b * V, I6]])
    return Kk(tau / 2) @ Pp(tau) @ Kk(tau / 2), V

# G5b: verify eigenphase formula cos(theta) = 1 - tau^2 lam/2 for the 4 non-unit eigenvalues, lam = s^2 (3D) , photon same
err = 0.0
for _ in range(200):
    kv = rng.uniform(-np.pi, np.pi, 3); sn3 = 2 * np.sin(kv / 2)
    tau = 0.4
    U, V = leapfrog_U(sn3, tau)
    ev = np.linalg.eigvals(U)
    ph = np.sort(np.abs(np.angle(ev[np.abs(ev - 1) > 1e-3])))
    nonunit = ph
    lam = sn3 @ sn3
    th = np.arccos(1 - tau ** 2 * lam / 2)
    err = max(err, np.abs(nonunit - th).max())
    # exactly 4 non-unit eigenvalues (2 polarizations)
    assert len(nonunit) == 4, len(nonunit)
say(f'G5b leapfrog K P K from the temporal-gauge 4D action: exactly 4 non-unit eigenvalues (2 polarizations) at 200 random k; phase vs arccos(1 - tau^2 s^2/2): {err:.1e}')
# photon Yee leapfrog (E,B or A,E): transverse part, phase from omega^2 = s^2 : identical formula by construction (Maxwell symbol s^2 delta - s s^T)
# explicit numeric: photon A in temporal gauge: A'' = -(s^2 - s s^T) A ; leapfrog U_A
err_ph = 0.0
for _ in range(200):
    kv = rng.uniform(-np.pi, np.pi, 3); sn3 = 2 * np.sin(kv / 2); tau = 0.4
    Vp = (sn3 @ sn3) * np.eye(3) - np.outer(sn3, sn3)
    I3, Z3 = np.eye(3), np.zeros((3, 3))
    Kk = lambda a: np.block([[I3, a * I3], [Z3, I3]])
    Pp = lambda b: np.block([[I3, Z3], [-b * Vp, I3]])
    U = Kk(tau / 2) @ Pp(tau) @ Kk(tau / 2)
    evp = np.linalg.eigvals(U); ph = np.sort(np.abs(np.angle(evp[np.abs(evp - 1) > 1e-3])))
    th = np.arccos(1 - tau ** 2 * (sn3 @ sn3) / 2)
    err_ph = max(err_ph, np.abs(ph - th).max())
say(f'   photon Yee leapfrog (same tau, same s): non-unit phases = same arccos(1 - tau^2 s^2/2): dev {err_ph:.1e}  => graviton and photon phases coincide at ALL k, tree level')

# ---------------------------------------------------------------- G6 nullity scan incl. zone corners
bad = 0
nz = []
pts = [np.array(c) * np.pi for c in itertools.product((0, 1), repeat=4)]
pts += [rng.uniform(-np.pi, np.pi, 4) for _ in range(2000)]
for kvec in pts:
    sn = 2 * np.sin(kvec / 2)
    if np.allclose(sn, 0):
        continue
    Kn = np.array(Kf(*sn), float)
    w = np.linalg.eigvalsh(Kn)
    nz.append(int(np.sum(np.abs(w) < 1e-9 * max(1, np.abs(w).max()))))
say(f'G6 nullity of K(s) at {len(nz)} momenta (k != 0, incl. all 15 nonzero zone corners): set {sorted(set(nz))} (4 = pure gauge only: no doublers, no extra zero modes)')

# ---------------------------------------------------------------- G7 counting of invariants
def sym_basis(n):
    B, pairs = [], []
    for i in range(n):
        for j in range(i, n):
            E = np.zeros((n, n))
            if i == j: E[i, i] = 1.0
            else: E[i, j] = E[j, i] = 1 / np.sqrt(2)
            B.append(E); pairs.append((i, j))
    return B, pairs
B4, _ = sym_basis(4)
def coords(h): return np.array([np.sum(E * h) for E in B4])
def rep(R):
    m = len(B4); Dm = np.zeros((m, m))
    for J, EJ in enumerate(B4): Dm[:, J] = coords(R @ EJ @ R.T)
    return Dm
n, m = 4, 10
dim = m * m * n * n
def Tg(R):
    Dm = rep(R); return np.kron(np.kron(Dm, Dm), np.kron(R, R))
P = sum(Tg(R.astype(float)) for R in W4) / len(W4)
idx = np.arange(dim).reshape(m, m, n, n)
p1 = idx.transpose(1, 0, 2, 3).ravel(); p2 = idx.transpose(0, 1, 3, 2).ravel(); p12 = idx.transpose(1, 0, 3, 2).ravel()
PS = 0.25 * (P + P[:, p1] + P[:, p2] + P[:, p12]); PS = 0.5 * (PS + PS.T)
w, v = np.linalg.eigh(PS)
basis = v[:, w > 0.5]
say(f'G7 W(B4)-invariant 2-derivative quadratic forms on Sym^2(R^4): {basis.shape[1]}  (A23 C5: 9)')
# O(4)-invariant subspace: further invariant under a generic rotation (angles) -> common fixed space
th1, th2 = 0.37, 0.61
def rot(i, j, t):
    R = np.eye(4); R[i, i] = R[j, j] = np.cos(t); R[i, j] = -np.sin(t); R[j, i] = np.sin(t); return R
cons = []
for R in (rot(0, 1, th1), rot(1, 2, th2), rot(0, 3, th1)):
    cons.append((Tg(R) @ basis - basis))
Acons = np.vstack(cons)
u, sv_, vt = np.linalg.svd(Acons, full_matrices=False)
null = vt[np.sum(sv_ > 1e-9):].T
say(f'   of which O(4)-invariant (also fixed by generic rotations): {null.shape[1]}')
# gauge-invariant among the 9
rows = []
for _ in range(40):
    sn = rng.normal(size=4)
    gv = np.array([coords(np.outer(sn, e) + np.outer(e, sn)) for e in np.eye(4)]).T      # 10 x 4
    for c in range(4):
        row = []
        for a_ in range(basis.shape[1]):
            C = basis[:, a_].reshape(m, m, n, n)
            Ck_ = np.einsum('IJab,a,b->IJ', C, sn, sn)
            row.append(Ck_ @ gv[:, c])
        rows.append(np.array(row).T)
Ag = np.vstack(rows)
u, sg, vt = np.linalg.svd(Ag, full_matrices=False)
Ng = vt[np.sum(sg > 1e-9):].T
say(f'   gauge-invariant (delta h = s xi + xi s) among W(B4)-invariant: {Ng.shape[1]}  => hypercubic + exact linearized diffeo => unique, necessarily O(4)-invariant EH')
say(f'   => without exact gauge invariance W(B4) alone allows {basis.shape[1] - null.shape[1]} O(4)-BREAKING dim-4 (2-derivative) graviton forms (speed/birefringence differences)')
# direct symbol-level uniqueness for photon: general W(B4) form  c1 s^2 delta + c2 s s^T + c3 diag(s_mu^2) + c4 delta*? ... gauge inv requires K s = 0
c1, c2, c3 = sp.symbols('c1 c2 c3')
KAg = c1 * s2 * sp.eye(4) + c2 * sv * sv.T + c3 * sp.diag(*[x ** 2 for x in s])
sol = sp.solve(list((KAg * sv).applyfunc(sp.expand)), [c1, c2, c3], dict=True)
say(f'   photon: general W(B4)-invariant symbol c1 s^2 1 + c2 s s^T + c3 diag(s_mu^2): K s = 0 forces {sol} -> unique Maxwell (the extra diag(s^2) form is a pure dim-4 anisotropy; gauge invariance kills it)')

# ---------------------------------------------------------------- G8 CFL
def tt_maxeig(tau, ngrid=13):
    g = np.linspace(-np.pi, np.pi, ngrid); mx = 0.0
    for kv in itertools.product(g, repeat=3):
        if np.allclose(kv, 0): continue
        sn3 = 2 * np.sin(np.array(kv) / 2)
        U, V = leapfrog_U(sn3, tau)
        ev = np.linalg.eigvals(U); ev = ev[np.abs(ev - 1) > 1e-2]      # drop Jordan-block unit eigenvalues (numerical noise)
        if len(ev): mx = max(mx, np.abs(ev).max())
    return mx
for tau, lab in ((1.0, 'tau = a_s (= 2 Z^3 sites; hypercubic a_t = a_s)'), (0.5, 'tau = a_s/2 (= 1 Z^3 site)'), (0.99 / np.sqrt(3), 'tau sqrt3 = 0.99')):
    say(f'G8 leapfrog max|eig| for {lab}: {tt_maxeig(tau):.6f}')
say(f'done in {time.time() - t0:.1f}s')
