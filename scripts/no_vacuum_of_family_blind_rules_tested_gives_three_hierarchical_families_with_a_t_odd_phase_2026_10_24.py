AUDIT_INPUT_PATHS = ('docs/NO_VACUUM_OF_FAMILY_BLIND_RULES_TESTED_GIVES_THREE_HIERARCHICAL_FAMILIES_WITH_A_T_ODD_PHASE_ADJOINT_VACUA_CANNOT_ENTER_MASSES_AND_QUARTIC_ALIGNMENT_IS_T_EVEN_BOUNDED_THEOREM_NOTE_2026-10-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""spontaneous-family-breaking (BACKLOG 5b): can a vacuum break the family U(3) of the
family-blind adopted rules into three families with a hierarchy and a T-odd phase?

Sections: A0 triality of mass terms, A1 Spin(10) bilinear singlets, A2 Wick/exchange sign,
B family Stoner on a supplied half-filled lattice Dirac band, C det channel of the forced
far-wall term, D Z3 character vacuum, E two-adjoint vacuum alignment (J, spectra, theta).
Self-contained (numpy/scipy). Seeded. Prints < 6000 chars.
"""
import numpy as np
from scipy.optimize import minimize
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 120
rng = np.random.default_rng(20261024)
PASS = 0
FAIL = 0


def check(name, ok, info=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"{'PASS' if ok else 'FAIL'} {name}: {info}")


def null_dim(gens, tol=1e-9):
    C = sum(g.conj().T @ g for g in gens)
    w = np.linalg.eigvalsh((C + C.conj().T) / 2)
    return int(np.sum(np.abs(w) < tol * max(1.0, np.max(np.abs(w)))))


# ---------------- A0: triality of a light mass term ----------------
# su(3) generators (Gell-Mann/2) on 3; adj via commutator; Sym^2(3) rep.
lam = np.zeros((8, 3, 3), complex)
lam[0][0, 1] = lam[0][1, 0] = 1
lam[1][0, 1] = -1j; lam[1][1, 0] = 1j
lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1
lam[4][0, 2] = -1j; lam[4][2, 0] = 1j
lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j
lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
T3 = [l / 2 for l in lam]
I3 = np.eye(3)
# adjoint on 3x3 matrices X -> [T, X], as 9x9
adj = [np.kron(t, I3) - np.kron(I3, t.T) for t in T3]
# Sym^2(3) basis
symb = []
for i in range(3):
    for j in range(i, 3):
        E = np.zeros((3, 3)); E[i, j] = E[j, i] = 1
        symb.append(E.flatten() / np.linalg.norm(E))
S = np.array(symb).T  # 9x6
sym = [S.T @ (np.kron(t, I3) + np.kron(I3, t)) @ S for t in T3]
I9, I6 = np.eye(9), np.eye(6)
g_aa6 = [np.kron(np.kron(a, I9), I6) + np.kron(np.kron(I9, a), I6) + np.kron(np.kron(I9, I9), s)
         for a, s in zip(adj, sym)]
d_aa6 = null_dim(g_aa6)
g_a6 = [np.kron(a, I6) + np.kron(I9, s) for a, s in zip(adj, sym)]
d_a6 = null_dim(g_a6)
g_66 = [np.kron(s, I6) + np.kron(I6, s) for s in sym]  # 6x6 contains no singlet either
g_6b6 = [np.kron(s, I6) - np.kron(I6, s.T) for s in sym]
check("A0 triality: SU(3) singlets in adj x adj x 6 and adj x 6 (mass term from adjoint vacua)",
      d_aa6 == 0 and d_a6 == 0 and null_dim(g_66) == 0 and null_dim(g_6b6) == 1,
      f"dims {d_aa6},{d_a6}; 6x6 {null_dim(g_66)}, 6bar x 6 {null_dim(g_6b6)}")

# ---------------- A1: Spin(10) 16 x 16 and 16 x 16bar singlets ----------------
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
I2 = np.eye(2)


def kronlist(ms):
    out = np.array([[1.0 + 0j]])
    for m in ms:
        out = np.kron(out, m)
    return out


G = []
for k in range(5):
    G.append(kronlist([sz] * k + [sx] + [I2] * (4 - k)))
    G.append(kronlist([sz] * k + [sy] + [I2] * (4 - k)))
chi = kronlist([sz] * 5)
P = np.where(np.isclose(np.diag(chi).real, 1))[0]
gens16 = []
for a in range(10):
    for b in range(a + 1, 10):
        Sab = 0.25j * (G[a] @ G[b] - G[b] @ G[a])
        gens16.append(Sab[np.ix_(P, P)])
I16 = np.eye(16)
d1616 = null_dim([np.kron(t, I16) + np.kron(I16, t) for t in gens16])
d1616b = null_dim([np.kron(t, I16) - np.kron(I16, t.T) for t in gens16])
check("A1 Spin(10): singlets in 16x16 and 16x16bar", d1616 == 0 and d1616b == 1,
      f"{d1616}, {d1616b} (scalar gauge-singlet family bilinear only light x mirror)")

# ---------------- A2: Wick / exchange sign ----------------
nm = 6  # 2 sites x 3 families, JW


def cop(j, n):
    return kronlist([sz] * j + [np.array([[0, 1], [0, 0]], complex)] + [I2] * (n - j - 1))


c = [cop(j, nm) for j in range(nm)]
errs = []
for t in range(20):
    Uo = np.linalg.qr(rng.normal(size=(nm, nm)) + 1j * rng.normal(size=(nm, nm)))[0]
    vac = np.zeros(2 ** nm, complex); vac[0] = 1  # all-empty is index 0 with this c (annihilates |0>)
    # with c = |0><1| on each qubit, |0> = occupied? use number op to fix convention
    st = np.zeros(2 ** nm, complex); st[-1] = 1.0
    ncheck = sum(ci.conj().T @ ci for ci in c)
    if abs(st.conj() @ ncheck @ st) > 0.5:  # st is full, take empty
        st = np.zeros(2 ** nm, complex); st[0] = 1.0
        if abs(st.conj() @ ncheck @ st) > 0.5:
            st = np.zeros(2 ** nm, complex); st[-1] = 1.0
    psi = st
    for k in range(3):
        bdag = sum(Uo[i, k] * c[i].conj().T for i in range(nm))
        psi = bdag @ psi
    psi /= np.linalg.norm(psi)
    Gm = np.array([[psi.conj() @ c[i].conj().T @ c[j] @ psi for j in range(nm)] for i in range(nm)])
    n = [c[i].conj().T @ c[i] for i in range(3)]  # site 0 families
    E = sum(psi.conj() @ n[i] @ n[j] @ psi for i in range(3) for j in range(i + 1, 3)).real
    Gs = Gm[:3, :3]
    pred = 0.5 * (np.trace(Gs).real ** 2 - np.trace(Gs @ Gs).real)
    errs.append(abs(E - pred))
check("A2 Wick: <sum_{i<j} n_i n_j> = ((trG)^2 - trG^2)/2 on a site of a Slater state", max(errs) < 1e-12,
      f"max err {max(errs):.1e}; exchange -trG^2/2 favours family polarisation (adjoint attractive)")

# ---------------- B: family Stoner on half-filled lattice Dirac band ----------------
L = 24
k = 2 * np.pi * np.arange(L) / L
KX, KY, KZ = np.meshgrid(k, k, k, indexing="ij")
e = np.sqrt(np.sin(KX) ** 2 + np.sin(KY) ** 2 + np.sin(KZ) ** 2).ravel()
eall = np.sort(np.concatenate([-e, e]))
Nk = e.size
cum = np.concatenate([[0.0], np.cumsum(eall)]) / Nk
def Eband(d):
    m = (1.0 + d) * Nk
    return np.interp(m, np.arange(cum.size), cum)
E0 = Eband(np.array(0.0))
h = 0.005
xs = np.arange(-1, 1 + h / 2, h)
X, Y = np.meshgrid(xs, xs, indexing="ij")
Z = -X - Y
ok = np.abs(Z) <= 1 + 1e-12
EX, EY, EZ = Eband(X) - E0, Eband(Y) - E0, Eband(np.clip(Z, -1, 1)) - E0
pats = []
gc = None
for g in np.arange(0.0, 8.01, 0.1):
    F = EX + EY + EZ - 0.5 * g * (X ** 2 + Y ** 2 + Z ** 2)
    F = np.where(ok, F, np.inf)
    i = np.unravel_index(np.argmin(F), F.shape)
    d = np.sort([X[i], Y[i], Z[i]])
    nd = 1 + int(d[1] - d[0] > 0.02) + int(d[2] - d[1] > 0.02)
    lab = "U3" if np.max(np.abs(d)) < 0.02 else ("U2xU1" if nd == 2 else "U1^3")
    if lab != "U3" and gc is None:
        gc = g
    if not pats or pats[-1][0] != lab:
        pats.append((lab, round(float(g), 2), tuple(float(x) for x in np.round(d, 2))))
bw = np.sqrt(3)
alpha = 1 / 137.036
print("  B pattern sequence (label, g onset, deltas):", pats)
check("B1 finite Stoner threshold on the Dirac sea, far above a Gauss-law (alpha) coupling",
      gc is not None and 0.1 * bw <= gc <= 3 * bw and alpha < 0.05 * gc,
      f"g_c = {gc:.2f} (bandwidth {bw:.2f}); alpha/g_c = {alpha / gc:.1e}")
final = pats[-1]
check("B2 strong-coupling family-density vacuum is U(1)^3 at the vertex (1,0,-1)",
      final[0] == "U1^3" and np.allclose(final[2], (-1, 0, 1), atol=0.02),
      f"final {final}; equally spaced (no hierarchy), real density (T-even), Lorentz-vector order")

# ---------------- C: det channel of the forced far-wall term ----------------
nz = 0; asym = 0
for t in range(150):
    a, b, dd = rng.uniform(0.1, 2, 3); cc = rng.uniform(0, 1); g = rng.uniform(4, 40)
    def F(s):
        return np.sum(a * s ** 2 + b * s ** 4 + dd * s ** 6) + cc * np.sum(s) ** 2 - g * np.prod(s)
    best = None
    for s0 in rng.uniform(0, 1.5, (6, 3)):
        r = minimize(F, s0, method="L-BFGS-B", bounds=[(0, None)] * 3)
        if best is None or r.fun < best.fun:
            best = r
    s = best.x
    if np.max(s) > 1e-3:
        nz += 1
        if np.ptp(s) > 1e-4 * np.max(s):
            asym += 1
check("C1 det channel: minimum of convex symmetric cost - g*prod(sigma) has equal sigma",
      asym == 0 and nz > 20, f"{nz}/150 condensed, {asym} asymmetric; M = sigma*U keeps a locked SU(3)")

# ---------------- D: Z3 character vacuum ----------------
w = np.exp(2j * np.pi / 3)
gaps = []
for t in range(20):
    def f(p):
        H = np.zeros((3, 3), complex)
        iu = np.triu_indices(3, 1)
        H[np.diag_indices(3)] = p[:3]
        H[iu] = p[3:6] + 1j * p[6:9]
        H = H + np.triu(H, 1).conj().T
        return abs(np.trace(expm(1j * H))) ** 2, H
    r = minimize(lambda p: f(p)[0], rng.normal(size=9), method="BFGS")
    Uv = expm(1j * f(r.x)[1])
    ph = np.sort(np.angle(np.linalg.eigvals(Uv)) % (2 * np.pi))
    dg = np.diff(np.concatenate([ph, [ph[0] + 2 * np.pi]]))
    gaps.append(np.max(np.abs(dg - 2 * np.pi / 3)))
check("D1 tr U = 0 forces the equally spaced (Z3 character) spectrum", max(gaps) < 1e-5,
      f"max gap error {max(gaps):.1e}: unique orbit, U(3) -> U(1)^3 if |trU|^2 coeff > 0 (sign unfixed)")
U0 = np.diag([1, w, w ** 2]); P23 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
sv = np.linalg.svd(U0, compute_uv=False)
Hu = U0 + U0.conj().T + 0.3 * U0 @ U0 + 0.3 * (U0 @ U0).conj().T
Hd = 2 * U0 + 2 * U0.conj().T - 0.7j * (U0 - U0.conj().T)
check("D2 Z3 vacuum: T x P23 kept, equal singular values, commuting mass functions",
      np.allclose(U0.conj(), P23 @ U0 @ P23) and np.allclose(sv, 1) and np.allclose(Hu @ Hd, Hd @ Hu),
      "no hierarchy (R3 FAIL), V = 1 and J = 0 (R2 FAIL)")
Js = []
for t in range(200):
    def herm():
        M = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); M = M + M.conj().T
        return 0.5 * (M + P23 @ M.conj() @ P23)
    A, B = herm(), herm()
    Js.append(abs(np.linalg.det(A @ B - B @ A)) / (np.linalg.norm(A) * np.linalg.norm(B)) ** 3)
check("D3 generalized-CP lemma with X = P23 (family-permuting antiunitary)", max(Js) < 1e-13,
      f"max |det[Hu,Hd]|/norm^6 {max(Js):.1e}")


# ---------------- E: two Hermitian adjoints, vacuum alignment ----------------
def Wmat(t12, t13, t23, dl):
    c12, s12, c13, s13, c23, s23 = np.cos(t12), np.sin(t12), np.cos(t13), np.sin(t13), np.cos(t23), np.sin(t23)
    e_ = np.exp(1j * dl)
    return np.array([[c12 * c13, s12 * c13, s13 / e_],
                     [-s12 * c23 - c12 * s23 * s13 * e_, c12 * c23 - s12 * s23 * s13 * e_, s23 * c13],
                     [s12 * s23 - c12 * c23 * s13 * e_, -c12 * s23 - s12 * c23 * s13 * e_, c23 * c13]])


def build(p):
    A = np.diag(p[:3]).astype(complex)
    W = Wmat(*p[6:10])
    B = W @ np.diag(p[3:6]) @ W.conj().T
    return A, B


def V(p, cp):
    A, B = build(p)
    A2, B2, AB = A @ A, B @ B, A @ B
    tr = lambda M: np.trace(M).real
    return (cp[0] * tr(A2) + cp[1] * tr(B2) + cp[2] * tr(A2 @ A) + cp[3] * tr(B2 @ B)
            + cp[4] * tr(A2) ** 2 + cp[5] * tr(A2 @ A2) + cp[6] * tr(B2) ** 2 + cp[7] * tr(B2 @ B2)
            + cp[8] * tr(AB) + cp[9] * tr(A2) * tr(B2) + cp[10] * tr(A2 @ B2) + cp[11] * tr(AB @ AB)
            + cp[12] * tr(AB) ** 2 + cp[13] * tr(A2 @ B) + cp[14] * tr(A @ B2))


def scan(nsets, mode):
    res = []
    for t in range(nsets):
        if mode == "plin":  # every W-dependent term linear in P = |W|^2
            cp = np.concatenate([rng.uniform(-2, -0.5, 2), rng.uniform(-1, 1, 2), rng.uniform(0.3, 1, 4),
                                 [rng.uniform(-1, 1), rng.uniform(-0.3, 0.3), rng.uniform(-0.3, 0.3)],
                                 [0.0, 0.0], rng.uniform(-1, 1, 2)])
        elif mode == "wide":  # full quartic, wide box
            cp = np.concatenate([rng.uniform(-2, 0.5, 2), rng.uniform(-1, 1, 2), rng.uniform(0.2, 1, 4),
                                 [rng.uniform(-1, 1) * rng.integers(0, 2), rng.uniform(-0.5, 0.5), rng.uniform(-0.5, 1)],
                                 [rng.uniform(-1, 1.5), rng.uniform(-0.5, 0.5)], rng.uniform(-1, 1, 2) * rng.integers(0, 2)])
        else:  # "k4": tr(ABAB) dominant and positive, no tr(AB), no mixed cubics
            cp = np.zeros(15); cp[0] = cp[1] = -1; cp[2:4] = rng.uniform(-1, 1, 2); cp[4:8] = rng.uniform(0.3, 1, 4)
            cp[9] = rng.uniform(0, 0.3); cp[10] = rng.uniform(0, 0.5); cp[11] = rng.uniform(0.2, 1.0)
        best = None
        for s in range(5):
            p0 = np.concatenate([rng.normal(size=6), rng.uniform(0, np.pi, 3), rng.uniform(0, 2 * np.pi, 1)])
            with np.errstate(all="ignore"):
                r = minimize(V, p0, args=(cp,), method="L-BFGS-B")
            if np.isfinite(r.fun) and (best is None or r.fun < best.fun):
                best = r
        if best is None:
            continue
        A, B = build(best.x)
        nA, nB = np.linalg.norm(A), np.linalg.norm(B)
        if nA > 30 or nB > 30 or nA < 1e-3 or nB < 1e-3:
            continue
        C = A @ B - B @ A
        com = np.linalg.norm(C) / (nA * nB)
        Iodd = abs(np.linalg.det(C)) / (nA * nB) ** 3
        da = np.sort(np.linalg.eigvalsh(A)); db = np.sort(np.linalg.eigvalsh(B))
        dist = lambda d, n: 1 + int(d[1] - d[0] > 1e-3 * n) + int(d[2] - d[1] > 1e-3 * n)
        res.append((com, Iodd, dist(da, nA), dist(db, nB)))
    return np.array(res)


r1 = scan(18, "plin")
check("E1 P-linear potentials (no tr(ABAB), (trAB)^2): minimum aligned, [A,B] = 0",
      len(r1) > 10 and np.max(r1[:, 0]) < 1e-3, f"{len(r1)} bounded sets, max |[A,B]|/|A||B| {np.max(r1[:, 0]):.1e}")
r2 = scan(60, "wide")
r3 = scan(24, "k4")
for nm_, rr in (("wide", r2), ("k4-dominant", r3)):
    print(f"  E2 {nm_}: {len(rr)} bounded; misaligned {np.mean(rr[:, 0] > 1e-3):.2f}; "
          f"T-odd {np.mean(rr[:, 1] > 1e-6):.2f} (max {np.max(rr[:, 1]):.1e}); 1+1+1 both {np.mean((rr[:, 2] == 3) & (rr[:, 3] == 3)):.2f}")
check("E2 full quartic: misaligned vacua need chosen couplings (dominant tr(ABAB) > 0), and every minimum found is T-even",
      len(r2) > 30 and len(r3) > 12 and np.mean(r3[:, 0] > 1e-3) > np.mean(r2[:, 0] > 1e-3)
      and np.max(r2[:, 1]) < 1e-6 and np.max(r3[:, 1]) < 1e-6,
      "J = 0 at every quartic minimum found (pre-run prediction of T-odd minima FAILED)")
dets = []
for t in range(200):
    M = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); M = M + M.conj().T
    Mf = M @ M @ M - 0.4 * M + 0.2 * np.eye(3)
    dets.append(abs(np.linalg.det(Mf).imag) / abs(np.linalg.det(Mf)))
check("E3 Hermitian mass functions of adjoints: arg det in {0, pi}", max(dets) < 1e-12,
      f"max |Im det|/|det| {max(dets):.1e} (but A0: adjoints cannot enter a 16.16 mass term)")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
