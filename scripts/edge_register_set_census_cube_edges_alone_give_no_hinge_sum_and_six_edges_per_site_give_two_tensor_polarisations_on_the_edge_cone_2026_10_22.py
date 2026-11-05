AUDIT_INPUT_PATHS = ('docs/EDGE_REGISTER_SET_CENSUS_CUBE_EDGES_ALONE_GIVE_NO_HINGE_SUM_AND_SIX_EDGES_PER_SITE_GIVE_TWO_TENSOR_POLARISATIONS_ON_THE_EDGE_CONE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""edge-modes: linearised Regge mode census for CL-1's edge registers.

Euclidean Regge S_R = sum_t A_t delta_t on the Freudenthal (Kuhn path) complex
of Z^3 x Z_tau (24 path 4-simplices per 4-cell, 15 edge classes; the constant-
tick slice is the 3D Kuhn complex, 7 classes). Bloch stiffness Q(k) in edge
lengths. Then CL-1's register sets: (i) as written, registers on cube edges
only (axis edges); (ii) the spatial Kuhn edges with CL-1's fixed lapse and zero
shift (tick edges fixed, mixed edges slaved). Lorentzian roots from the low-k
form A(k_s) - w^2 C (k_t -> i w). Supplied: carrier, Euclidean continuation,
slaving map. numpy only.
"""
AUDIT_TIMEOUT_SEC = 120
import itertools, time
import numpy as np
from scipy.linalg import eig, null_space

T0 = time.time()
NP = NF = 0
def check(name, ok, msg):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {msg}")

# ---------------- complex ----------------
DIM = 4
CLS = [c for c in itertools.product((0, 1), repeat=DIM) if any(c)]
CLS.sort(key=lambda c: (c[3], sum(c), c))           # spatial classes first
CI = {c: i for i, c in enumerate(CLS)}
NC = len(CLS)
SPAT = [i for i, c in enumerate(CLS) if c[3] == 0]   # 7 spatial Kuhn classes
AXIS = [CI[(1, 0, 0, 0)], CI[(0, 1, 0, 0)], CI[(0, 0, 1, 0)]]
TICK = CI[(0, 0, 0, 1)]
SIMP = []
for p in itertools.permutations(range(DIM)):
    v = [np.zeros(DIM, int)]
    for j in p:
        w = v[-1].copy(); w[j] = 1; v.append(w)
    SIMP.append(v)

def simplex_F_grad(L):
    """L: 5x5 edge lengths. returns grad of F = sum_t A_t theta_t (Schlaefli)."""
    E = np.array([[0.0] * 4 for _ in range(4)])
    G = np.zeros((4, 4))
    for i in range(1, 5):
        for j in range(1, 5):
            G[i-1, j-1] = 0.5 * (L[0, i]**2 + L[0, j]**2 - L[i, j]**2)
    E = np.linalg.cholesky(G)                        # rows = vertex coords
    D = np.linalg.inv(E)                             # columns = duals d_i
    n = [D.sum(axis=1)] + [-D[:, i] for i in range(4)]
    g = np.zeros((5, 5))
    for i, j in itertools.combinations(range(5), 2):
        th = np.arccos(np.clip(-n[i] @ n[j] / np.linalg.norm(n[i]) / np.linalg.norm(n[j]), -1, 1))
        a, b, c = [k for k in range(5) if k not in (i, j)]
        x, y, z = L[a, b], L[b, c], L[a, c]
        A = 0.25 * np.sqrt(max(2*x*x*y*y + 2*y*y*z*z + 2*z*z*x*x - x**4 - y**4 - z**4, 0))
        for (p, q), s, o1, o2 in (((a, b), x, y, z), ((b, c), y, x, z), ((a, c), z, x, y)):
            g[p, q] += th * s * (o1*o1 + o2*o2 - s*s) / (8 * A)
    return g

def build(tau2):
    """flat Freudenthal complex, spatial edge 1, tick edge sqrt(tau2)."""
    def flat_lengths(v):
        L = np.zeros((5, 5))
        for a, b in itertools.combinations(range(5), 2):
            d = v[b] - v[a]
            L[a, b] = L[b, a] = np.sqrt(d[:3] @ d[:3] + tau2 * d[3]**2)
        return L

    PAIRS = list(itertools.combinations(range(5), 2))
    def simplex_hessian(v):  # Richardson of central differences of the Schlaefli gradient
        return (4*_sh(v, 1e-4) - _sh(v, 2e-4))/3
    def _sh(v, h):
        L0 = flat_lengths(v)
        H = np.zeros((10, 10))
        for e, (a, b) in enumerate(PAIRS):
            gs = []
            for s in (+1, -1):
                L = L0.copy(); L[a, b] += s*h; L[b, a] = L[a, b]
                gg = simplex_F_grad(L); gs.append(np.array([gg[p, q] for p, q in PAIRS]))
            H[e] = (gs[0] - gs[1]) / (2*h)
        return 0.5 * (H + H.T)

    HS = [simplex_hessian(v) for v in SIMP]
    ECL = [[CI[tuple(v[b] - v[a])] for a, b in PAIRS] for v in SIMP]
    EAN = [[v[a] for a, b in PAIRS] for v in SIMP]
    NORM = np.array([np.sqrt(sum(c[:3]) + tau2*c[3]) for c in CLS])
    CP = [np.array(c[:3] + (np.sqrt(tau2)*c[3],), float) for c in CLS]

    # triangle classes (hinges), counted once per 4-cell: S_R = 2 pi sum_t A_t - sum_sigma F_sigma
    TRI = {}
    for v in SIMP:
        for tri in itertools.combinations(range(5), 3):
            vs = sorted(tuple(v[i]) for i in tri)
            key = tuple(tuple(np.array(w) - np.array(vs[0])) for w in vs)
            TRI[key] = vs
    def area(x, y, z):
        return 0.25*np.sqrt(2*x*x*y*y + 2*y*y*z*z + 2*z*z*x*x - x**4 - y**4 - z**4)
    def tri_hess(vs):
        """analytic Hessian of Heron's area in the three side lengths."""
        P = [(0, 1), (1, 2), (0, 2)]
        l = np.array([NORM[CI[tuple(np.array(vs[b]) - np.array(vs[a]))]] for a, b in P])
        A = area(*l); s2 = (l**2).sum()
        g = np.array([l[i]*(s2 - 2*l[i]**2)/(8*A) for i in range(3)])
        H = np.zeros((3, 3))
        for i in range(3):
            for j in range(3):
                d = (s2 - 4*l[i]**2) if i == j else 2*l[i]*l[j]
                H[i, j] = d/(8*A) - l[i]*(s2 - 2*l[i]**2)/(8*A*A)*g[j]
        ec = [CI[tuple(np.array(vs[b]) - np.array(vs[a]))] for a, b in P]
        ea = [np.array(vs[a]) for a, b in P]
        return H, ec, ea
    TH = [tri_hess(vs) for vs in TRI.values()]

    def Q(k):
        """raw S_R orientation: Hess S_R = 2 pi sum_t Hess A_t - sum_sigma Hess F_sigma."""
        M = np.zeros((NC, NC), complex)
        for H, ec, ea in TH:
            ph = np.exp(1j * np.array([k @ a for a in ea]))
            M[np.ix_(ec, ec)] += 2*np.pi*H * np.outer(ph.conj(), ph)
        for H, ec, ea in zip(HS, ECL, EAN):
            ph = np.exp(1j * np.array([k @ a for a in ea]))
            M[np.ix_(ec, ec)] -= H * np.outer(ph.conj(), ph)
        return 0.5 * (M + M.conj().T)

    def Gmap(k):  # vertex displacements -> edge lengths
        return np.array([CP[i] * (np.exp(1j * k @ np.array(c)) - 1) / NORM[i]
                         for i, c in enumerate(CLS)])

    SYM = [(i, j) for i in range(4) for j in range(i, 4)]
    def Mmap(k):  # line-averaged metric (10) -> edge lengths
        out = np.zeros((NC, 10), complex)
        for i, c in enumerate(CLS):
            cv = CP[i]; kc = k @ np.array(c, float)
            f = 1.0 if abs(kc) < 1e-12 else (np.exp(1j*kc) - 1) / (1j*kc)
            for s, (a, b) in enumerate(SYM):
                out[i, s] = (1 if a == b else 2) * cv[a] * cv[b] / (2 * NORM[i]) * f
        return out


    return Q, Gmap, Mmap, NORM

Q, Gmap, Mmap, NORM = build(1.0)

def ev(M): return np.linalg.eigvalsh(M)
rng = np.random.default_rng(7)
kr = rng.uniform(-np.pi, np.pi, 4)

# ---------------- A. CL-1's edge set as written ----------------
print("== A. CL-1 edge registers as written (edges of the tilings' cubes)")
Lb = 4
cubeA = [np.array(o) + 0 for o in itertools.product(range(0, Lb, 2), repeat=3)]
cubeB = [np.array(o) + 1 for o in itertools.product(range(0, Lb, 2), repeat=3)]
own = {}
diag = 0
for tag, cubes in (("A", cubeA), ("B", cubeB)):
    for o in cubes:
        for c in itertools.product((0, 1), repeat=3):
            for d in itertools.product((0, 1), repeat=3):
                dv = np.array(d) - np.array(c)
                if np.abs(dv).sum() == 1 and dv.sum() == 1:
                    key = (tuple((o + c) % Lb), tuple((o + d) % Lb))
                    own.setdefault(key, []).append(tag)
nsites = Lb**3
once = all(len(x) == 1 for x in own.values())
vA = {tuple((o + np.array(c)) % Lb) for o in cubeA for c in itertools.product((0, 1), repeat=3)}
vB = {tuple((o + np.array(c)) % Lb) for o in cubeB for c in itertools.product((0, 1), repeat=3)}
check("A1 THEOREM (combinatorics of CL-1 text)", once and len(own) == 3*nsites and len(vA) == nsites == len(vB),
      f"cube edges = all {len(own)} = 3/site axis edges of Z^3, each in exactly one cube; no face or body diagonal is a cube edge; A and B cubes share corners only (each site in one A and one B cube)")
# rigidity: axis-edge lengths vs vertex displacements, 3x3 Bloch map
ks = rng.uniform(-np.pi, np.pi, (200, 3))
ranks = [np.linalg.matrix_rank(np.diag(np.exp(1j*k) - 1)) for k in ks]
cube_edges = [(c, d) for c in itertools.product((0, 1), repeat=3) for d in itertools.product((0, 1), repeat=3)
              if np.abs(np.array(d)-np.array(c)).sum() == 1 and sum(d) > sum(c)]
R1 = np.zeros((12, 24))
for r, (c, d) in enumerate(cube_edges):
    vi = int(''.join(map(str, c)), 2); vj = int(''.join(map(str, d)), 2)
    u = np.array(d) - np.array(c)
    R1[r, 3*vj:3*vj+3] += u; R1[r, 3*vi:3*vi+3] -= u
floppy = 24 - 6 - np.linalg.matrix_rank(R1)
check("A2 THEOREM (rigidity)", min(ranks) == 3 and floppy == 6,
      f"Bloch map u(k) -> axis lengths has rank 3 at every k with all k_i != 0 (min over 200 k: {min(ranks)}): every axis-length field there is a flat-space vertex displacement; one cube with 12 edges keeps {floppy} floppy shears. The register set has no triangle, so CL-3's hinge sum needs non-register lengths")

# ---------------- B. 3D Kuhn slice ----------------
print("== B. constant-tick slice: 3D Kuhn complex (7 classes; main's 3D note)")
# 3D hessian: use simplices of the 3D Kuhn complex directly
SIMP3 = []
for p in itertools.permutations(range(3)):
    v = [np.zeros(3, int)]
    for j in p:
        w = v[-1].copy(); w[j] = 1; v.append(w)
    SIMP3.append(v)
def tet_F_grad(L):
    G = np.array([[0.5*(L[0, i]**2 + L[0, j]**2 - L[i, j]**2) for j in range(1, 4)] for i in range(1, 4)])
    E = np.linalg.cholesky(G); D = np.linalg.inv(E)
    n = [D.sum(axis=1)] + [-D[:, i] for i in range(3)]
    g = np.zeros((4, 4))
    for i, j in itertools.combinations(range(4), 2):
        th = np.arccos(np.clip(-n[i] @ n[j] / np.linalg.norm(n[i]) / np.linalg.norm(n[j]), -1, 1))
        a, b = [k for k in range(4) if k not in (i, j)]
        g[a, b] += th
    return g
P3 = list(itertools.combinations(range(4), 2))
C3 = [c for c in CLS if c[3] == 0]
CI3 = {c[:3]: i for i, c in enumerate(C3)}
def tet_hess(v):
    return (4*_th(v, 1e-4) - _th(v, 2e-4))/3
def _th(v, h):
    L0 = np.zeros((4, 4))
    for a, b in P3:
        d = v[b]-v[a]; L0[a, b] = L0[b, a] = np.sqrt(d @ d)
    H = np.zeros((6, 6))
    for e, (a, b) in enumerate(P3):
        gs = []
        for s in (1, -1):
            L = L0.copy(); L[a, b] += s*h; L[b, a] = L[a, b]
            gg = tet_F_grad(L); gs.append(np.array([gg[p, q] for p, q in P3]))
        H[e] = (gs[0]-gs[1])/(2*h)
    return 0.5*(H+H.T)
H3 = [tet_hess(v) for v in SIMP3]
def Q3(k):
    M = np.zeros((7, 7), complex)
    for H, v in zip(H3, SIMP3):
        ec = [CI3[tuple(v[b]-v[a])] for a, b in P3]
        ph = np.exp(1j*np.array([k @ v[a] for a, b in P3]))
        M[np.ix_(ec, ec)] -= H*np.outer(ph.conj(), ph)
    return 0.5*(M+M.conj().T)
e30 = ev(Q3(np.zeros(3)))
nz3 = int(np.sum(np.abs(e30) < 1e-6))
k3 = rng.uniform(-np.pi, np.pi, 3)
G3 = Gmap(np.r_[k3, 0])[SPAT][:, :3]
gres3 = np.linalg.norm(Q3(k3) @ G3)
check("B1 reproduces main (3D Kuhn)", nz3 == 6 and gres3 < 1e-6,
      f"k=0: 6 metric zeros + 1 massive breathing {e30[np.abs(e30) > 1e-6].round(3)}; 3 vertex-displacement zeros at random k, |Q G| {gres3:.1e}")

# ---------------- C. full 4D Freudenthal ----------------
print("== C. 4D Freudenthal (15 classes; main's 3+1 tick note), every edge a register")
e0 = ev(Q(np.zeros(4))); sc = np.abs(e0).max()
nz0 = int(np.sum(np.abs(e0) < 1e-8*sc))
check("C1 reproduces main at k=0", nz0 == 11 and np.allclose(np.sort(e0)[:4], [-48, -16, -16, -16], atol=1e-6),
      f"{nz0} zeros (10 metric + 1) and massive {np.sort(e0)[:4].round(6)} = main's -48, -16 x3")
Qr = Q(kr); er = ev(Qr); Gr = Gmap(kr)
gres = np.linalg.norm(Qr @ Gr) / np.linalg.norm(Qr)
nzr = int(np.sum(np.abs(er) < 1e-8*np.abs(er).max()))
Nsp = null_space(Qr, rcond=1e-8)
Pg = Gr @ np.linalg.pinv(Gr)
uu, ss, _ = np.linalg.svd((np.eye(NC) - Pg) @ Nsp); fvec = uu[:, 0]
Mr = Mmap(kr)
mres = np.linalg.norm(np.c_[Mr, Gr] @ np.linalg.lstsq(np.c_[Mr, Gr], fvec, rcond=None)[0] - fvec)
fsp = np.linalg.norm(fvec[SPAT])
check("C2 gauge + one zero-action branch at every k", gres < 1e-8 and nzr == 5,
      f"random k: {nzr} exact zeros = 4 displacements (|QG|/|Q| {gres:.0e}) + 1 non-metric flat branch (distance from metric+gauge span {mres:.2f}; weight on spatial edges {fsp:.2f}, rest on tick/mixed edges)")
small = []
for eps in (0.02, 0.01):
    e = np.sort(np.abs(ev(Q(eps*np.array([0.3, 0.5, 0.7, 0.4])))))
    small.append(e)
ratio = small[0][5:11] / small[1][5:11]
check("C3 small-k census", np.allclose(ratio, 4, rtol=0.02) and small[1][11] > 1,
      f"5 zero, 6 ~k^2 (ratio over k-halving {ratio.mean():.3f}: 2 TT + 4 lapse/shift/trace channels), 4 gapped >= {small[1][11]:.1f} (cell scale)")

# Euclidean transfer spectrum: roots z = e^{-E} of det Q(k_s, z) = 0
def tspec(Qf, ks, nmax=2, Nt=16):
    kts = 2*np.pi*np.arange(Nt)/Nt
    Ms = [Qf(np.r_[ks, t]) for t in kts]
    Qn = {n: sum(M*np.exp(-1j*n*t) for M, t in zip(Ms, kts))/Nt for n in range(-Nt//2+1, Nt//2)}
    leak = max(np.abs(Qn[n]).max() for n in Qn if abs(n) > nmax)
    d = Ms[0].shape[0]; p = 2*nmax; P = [Qn[j-nmax] for j in range(p+1)]
    A = np.zeros((d*p, d*p), complex); B = np.eye(d*p, dtype=complex)
    for j in range(p-1): A[j*d:(j+1)*d, (j+1)*d:(j+2)*d] = np.eye(d)
    for j in range(p): A[(p-1)*d:, j*d:(j+1)*d] = -P[j]
    B[(p-1)*d:, (p-1)*d:] = P[p]
    z = eig(A, B, right=False)
    ok = np.isfinite(z) & (np.abs(z) > 1e-30)
    with np.errstate(all="ignore"):
        E = -np.log(z[ok].astype(complex))
    return E, leak, int((~ok).sum())

def sync_map(k, NORM):
    L = np.zeros((NC, 7), complex)
    for j, i in enumerate(SPAT): L[i, j] = 1
    for i, c in enumerate(CLS):
        if c[3] == 1 and i != TICK:
            s_ = c[:3] + (0,); js = SPAT.index(CI[s_])
            L[i, js] = (NORM[CI[s_]] / NORM[i]) * 0.5 * (1 + np.exp(1j * k[3]))
    return L
def axis_sync_map(k, NORM):  # axis registers only; diagonals frozen
    L = sync_map(k, NORM)[:, [SPAT.index(i) for i in AXIS]]
    return L
def mk(Qf, mapf, NORM):
    return lambda k: (lambda Lm: Lm.conj().T @ Qf(k) @ Lm)(mapf(k, NORM))

def classify(E, kk):
    r = E / kk
    light = np.sort(np.abs(r[(np.abs(r.real) > 0.5) & (np.abs(r.real) < 2) & (np.abs(r.imag) < 1e-3)].real))
    zero = int(np.sum(np.abs(E) < 0.1*kk))
    other = E[(np.abs(E) >= 0.1*kk) & ~((np.abs(r.real) > 0.5) & (np.abs(r.real) < 2))]
    return light, zero, other

print("== D. CL-1 register sets inside the hinge sum (4D, fixed lapse, zero shift)")
Qax = lambda k: Q(k)[np.ix_(AXIS, AXIS)]
eax0 = ev(Qax(np.zeros(4)))
check("D1 axis registers only, other lengths frozen: no massless mode", np.min(np.abs(eax0)) > 1,
      f"k=0 eigenvalues {eax0.round(4)}: all three are non-metric strains gapped at the cell scale")
def Qslave(k):
    oth = [i for i in range(NC) if i not in AXIS]; M = Q(k)
    return M[np.ix_(AXIS, AXIS)] - M[np.ix_(AXIS, oth)] @ np.linalg.pinv(M[np.ix_(oth, oth)], rcond=1e-10) @ M[np.ix_(oth, AXIS)]
rsl = max(np.linalg.norm(Qslave(rng.uniform(-np.pi, np.pi, 4))) for _ in range(4)) / np.linalg.norm(Qax(kr))
check("D2 axis registers only, other lengths slaved by stationarity: no stiffness", rsl < 1e-6,
      f"|Q_eff|/|Q_axis| {rsl:.0e}: every axis field completes to a vertex displacement (A2), so no graviton and no response")
Qa = mk(Q, axis_sync_map, NORM)
sp = {}
for nm, d in (("axis", (0, 0, 1)), ("face", (1, 1, 0)), ("body", (1, 1, 1)), ("generic", (0.3, 0.5, 0.8))):
    E, leak, ninf = tspec(Qa, 0.02*np.array(d)/np.linalg.norm(d))
    r = np.abs(E[np.abs(E) < 0.5]) / 0.02
    sp[nm] = np.unique(np.round(r, 3))
far = min(np.min(np.abs(v[v > 0.1] - 1)) for v in sp.values() if np.any(v > 0.1))
check("D3 literal set (axis registers, diagonals frozen) + fixed lapse + zero shift: light strains OFF the edge cone",
      far > 1e-3,
      f"light-root speeds E/|k| {dict((k, [float(x) for x in v]) for k, v in sp.items())}: direction-dependent, none = 1 (closest |c-1| = {far:.1e}); k||axis keeps one branch only")
Qs = mk(Q, sync_map, NORM)
res = {}
for nm, d in (("axis", (0, 0, 1)), ("face", (1, 1, 0)), ("body", (1, 1, 1))):
    for kk in (0.04, 0.02):
        E, leak, ninf = tspec(Qs, kk*np.array(d)/np.linalg.norm(d))
        res[(nm, kk)] = classify(E, kk) + (leak, ninf)
ok = all(len(v[0]) == 4 and v[1] == 8 and np.min(np.abs(v[2].real)) > 0.3 for v in res.values())
la, za, oa, leak, ninf = res[("axis", 0.04)]
check("D4 spatial Kuhn registers + fixed lapse + zero shift: mode census per site", ok,
      f"7 registers -> 2 light branches (4 roots +-E), 4 w=0 branches (8 roots: 3 residual spatial displacements + the fixed-lapse scalar), 1 breathing strain non-dynamical or at |Re E| >= {min(np.min(np.abs(v[2].real)) for v in res.values()):.1f}/tick; {ninf} infinite roots; Fourier leak {leak:.0e}")
devs = {k: 1 - v[0] for k, v in res.items()}
alpha = {nm: np.round((devs[(nm, 0.04)] / 0.04**2), 3) for nm in ("axis", "face", "body")}
scal = {nm: np.round(devs[(nm, 0.04)] / np.where(np.abs(devs[(nm, 0.02)]) > 1e-12, devs[(nm, 0.02)], 1), 2) for nm in ("axis", "face", "body")}
print(f"   1 - E/|k| at |k| = .04: {dict((n, np.round(devs[(n, .04)], 7)) for n in alpha)}")
check("D5 graviton speed = edge cone at O(k^2); lattice correction O(k^2)",
      all(np.max(np.abs(devs[(n, .04)])) < 2e-3 for n in alpha),
      f"alpha in c_g = 1 - alpha (k a)^2 per polarisation: {alpha}; dev ratio over k-halving {scal} (4 = k^2)")
Q7, G7, M7, N7 = build(0.49)
gres7 = np.linalg.norm(Q7(kr) @ G7(kr)) / np.linalg.norm(Q7(kr))
E, leak, ninf = tspec(mk(Q7, sync_map, N7), np.array([0, 0, 0.02]))
l7, z7, o7 = classify(E / 0.7, 0.02)
check("D6 tick edge 0.7 a: graviton on the edges' null cone, E = tau |k|", len(l7) == 4 and np.max(np.abs(l7 - 1)) < 1e-3 and gres7 < 1e-8,
      f"E/(tau |k|) {np.round(l7, 6)}; gauge |QG|/|Q| {gres7:.0e}; zero roots {z7}")

# ---------------- E. independent slab code + the six-edge (5-tetrahedra) triangulation ----------------
print("== E. sync slab built directly from a spatial triangulation (independent code path)")
WO = np.array([1.0, 0.1, 0.01])
PAIRS = list(itertools.combinations(range(5), 2))
def simplex_grad5(L):
    G = np.array([[0.5*(L[0, i]**2 + L[0, j]**2 - L[i, j]**2) for j in range(1, 5)] for i in range(1, 5)])
    E = np.linalg.cholesky(G); D = np.linalg.inv(E)
    n = [D.sum(axis=1)] + [-D[:, i] for i in range(4)]
    g = np.zeros((5, 5))
    for i, j in itertools.combinations(range(5), 2):
        th = np.arccos(np.clip(-n[i] @ n[j]/np.linalg.norm(n[i])/np.linalg.norm(n[j]), -1, 1))
        a, b, c = [k for k in range(5) if k not in (i, j)]
        x, y, z = L[a, b], L[b, c], L[a, c]
        A = 0.25*np.sqrt(2*x*x*y*y + 2*y*y*z*z + 2*z*z*x*x - x**4 - y**4 - z**4)
        for (p, q), s, o1, o2 in (((a, b), x, y, z), ((b, c), y, x, z), ((a, c), z, x, y)):
            g[p, q] += th*s*(o1*o1 + o2*o2 - s*s)/(8*A)
    return np.array([g[p, q] for p, q in PAIRS])
def simplex_hess_X(X):
    L0 = np.linalg.norm(X[:, None, :] - X[None, :, :], axis=2)
    def sh(h):
        H = np.zeros((10, 10))
        for e, (a, b) in enumerate(PAIRS):
            gs = []
            for s in (1, -1):
                L = L0.copy(); L[a, b] += s*h; L[b, a] = L[a, b]; gs.append(simplex_grad5(L))
            H[e] = (gs[0]-gs[1])/(2*h)
        return H
    H = (4*sh(1e-4) - sh(2e-4))/3
    return 0.5*(H + H.T)
def tri_hess_l(l):
    A = 0.25*np.sqrt(2*l[0]**2*l[1]**2 + 2*l[1]**2*l[2]**2 + 2*l[2]**2*l[0]**2 - (l**4).sum())
    s2 = (l**2).sum(); g = l*(s2 - 2*l**2)/(8*A); H = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            d = (s2 - 4*l[i]**2) if i == j else 2*l[i]*l[j]
            H[i, j] = d/(8*A) - l[i]*(s2 - 2*l[i]**2)/(8*A*A)*g[j]
    return H

class Slab:
    """sync slab Regge (fixed lapse tau, zero shift) on a periodic 3D triangulation."""
    def __init__(self, tets, P, tau):
        self.P, self.tau = P, tau
        key = lambda a, b: (tuple(np.mod(a, P)), tuple(b - a))
        self.cls = {}
        def order(vs): return sorted(vs, key=lambda v: v @ WO)
        for T in tets:
            for a, b in itertools.combinations(order([np.array(v) for v in T]), 2):
                self.cls.setdefault(key(a, b), len(self.cls))
        self.n = len(self.cls); self.key = key
        self.simps = []          # (coords 5x4, list of edge descriptors)
        tris = {}
        for T in tets:
            vs = order([np.array(v) for v in T])
            for j in range(4):
                V = [(vs[i], 0) for i in range(j+1)] + [(vs[i], 1) for i in range(j, 4)]
                X = np.array([np.r_[v, tau*t] for v, t in V], float)
                ed = [self.edge(V[a], V[b]) for a, b in PAIRS]
                self.simps.append((simplex_hess_X(X), ed))
                for tri in itertools.combinations(range(5), 3):
                    W = [V[i] for i in tri]
                    sh = np.r_[np.floor_divide(W[0][0], P)*P, W[0][1]]
                    k_ = tuple(sorted(tuple(np.r_[w[0], w[1]] - sh) for w in W))
                    if k_ not in tris:
                        l = np.array([np.linalg.norm(np.r_[W[b][0]-W[a][0], tau*(W[b][1]-W[a][1])]) for a, b in ((0, 1), (1, 2), (0, 2))])
                        tris[k_] = (tri_hess_l(l), [self.edge(W[a], W[b]) for a, b in ((0, 1), (1, 2), (0, 2))])
        self.tris = list(tris.values())
    def edge(self, A, B):
        """edge descriptor: list of (class, anchor 3-vector, t, coefficient)."""
        (a, ta), (b, tb) = A, B
        if a @ WO > b @ WO: (a, ta), (b, tb) = (b, tb), (a, ta)
        if np.array_equal(a, b): return []                       # tick edge: fixed
        c = self.cls[self.key(a, b)]
        if ta == tb: return [(c, a, ta, 1.0)]
        ls = np.linalg.norm(b - a); lm = np.sqrt(ls**2 + self.tau**2)
        t0 = min(ta, tb)
        return [(c, a, t0, 0.5*ls/lm), (c, a, t0+1, 0.5*ls/lm)]
    def row(self, ed, k):
        r = np.zeros(self.n, complex)
        for c, a, t, w in ed: r[c] += w*np.exp(1j*(k[:3] @ a + k[3]*t))
        return r
    def Q(self, k):
        M = np.zeros((self.n, self.n), complex)
        for H, eds in self.tris:
            J = np.array([self.row(e, k) for e in eds]); M += 2*np.pi*J.conj().T @ H @ J
        for H, eds in self.simps:
            J = np.array([self.row(e, k) for e in eds]); M -= J.conj().T @ H @ J
        return 0.5*(M + M.conj().T)

def kuhn_tets():
    out = []
    for p in itertools.permutations(range(3)):
        v = [np.zeros(3, int)]
        for j in p:
            w = v[-1].copy(); w[j] = 1; v.append(w)
        out.append(v)
    return out
def five_tets():
    out = []
    for o in itertools.product((0, 1), repeat=3):
        o = np.array(o); C = [o + np.array(c) for c in itertools.product((0, 1), repeat=3)]
        ev_ = [c for c in C if c.sum() % 2 == 0]; od = [c for c in C if c.sum() % 2 == 1]
        out.append(ev_)
        for q in od:
            out.append([q] + [c for c in ev_ if np.abs(c - q).sum() == 1])
    return out

SK = Slab(kuhn_tets(), 1, 1.0)
E, leak, ninf = tspec(SK.Q, np.array([0, 0, 0.04])); lk, zk, ok_ = classify(E, 0.04)
check("E1 slab code reproduces D4 on the Kuhn slice", np.allclose(lk, res[("axis", 0.04)][0], atol=1e-6) and zk == 8,
      f"light E/|k| {np.round(lk, 6)}, zero roots {zk}")
S5 = Slab(five_tets(), 2, 1.0)
e5 = ev(S5.Q(np.zeros(4))); nz5 = int(np.sum(np.abs(e5) < 1e-8*np.abs(e5).max()))
check("E2 six edges per site (3 axis + the face diagonals joining even-sum sites; 5 tets per cube, alternating)",
      S5.n == 48 and nz5 == 27,
      f"8-site cell: {S5.n} registers = 6/site = metric count, so no non-metric strain exists; k=0 zeros {nz5} = 6 uniform metric + 21 staggered displacements")
out5 = []
for d in ((0, 0, 1), (1, 1, 1), (0.3, 0.5, 0.8)):
    E, leak, ninf = tspec(S5.Q, 0.02*np.array(d)/np.linalg.norm(d)); l5, z5, o5 = classify(E, 0.02)
    soft = o5[np.abs(o5) < 0.5]
    out5.append((len(l5), np.max(np.abs(l5 - 1)) if len(l5) else 9, z5, len(soft), np.max(np.abs(soft)) if len(soft) else 0, np.min(np.abs(o5[np.abs(o5) >= 0.5]))))
check("E3 six-edge slab: exactly the two polarisations are light, on the edge cone",
      all(o[0] == 4 and o[1] < 1e-3 for o in out5),
      "per direction (light roots, max|E/k-1|, w=0 roots, unresolved near-zero roots and their max |E|, lightest massive |E|): " + "; ".join(f"({o[0]}, {o[1]:.0e}, {o[2]}, {o[3]}, {o[4]:.3f}, {o[5]:.2f})" for o in out5))
print(f"elapsed_seconds {time.time()-T0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
