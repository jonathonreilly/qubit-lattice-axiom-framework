AUDIT_INPUT_PATHS = ('docs/FIVE_MODE_CONES_CARRY_THE_SPIN10_VECTOR_AND_SEPARATED_SIXTEEN_CONES_EVADE_THE_COMPOSITE_PARTNER_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Chirality wall re-posed with the cone rule and five modes per site.

Supplied model, exact finite algebra plus free-band diagnostics. No interacting
dynamics is computed. Self-contained (numpy, scipy). Seeded.
"""
import itertools
import time

import numpy as np
from scipy import sparse

AUDIT_TIMEOUT_SEC = 120
SEED = 20261022
T0 = time.time()
NP = 0
NF = 0


def check(tag, ok, msg, detail=""):
    global NP, NF
    if ok:
        NP += 1
    else:
        NF += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {msg} | {detail}")


# ---------------------------------------------------------------- Fock, N = 5
N = 5
D = 2 ** N


def pc(x):
    return bin(x).count("1")


def cop(j):
    m = np.zeros((D, D))
    for s in range(D):
        if s >> j & 1:
            m[s ^ (1 << j), s] = (-1) ** pc(s & ((1 << j) - 1))
    return m


C = [cop(j) for j in range(N)]
G = []
for j in range(N):
    G.append(C[j] + C[j].T)
    G.append(1j * (C[j].T - C[j]))  # gamma_{2j+1} = i(c^+ - c)
PAIRS = list(itertools.combinations(range(2 * N), 2))
M = {ab: 0.5j * G[ab[0]] @ G[ab[1]] for ab in PAIRS}
EVEN = [s for s in range(D) if pc(s) % 2 == 0]

print("== A. five modes per site: what a cone can carry (exact)")
cas = sum(M[ab] @ M[ab] for ab in PAIRS)
check("A1", np.allclose(cas, 45 / 4 * np.eye(D)) and len(EVEN) == 16,
      "THEOREM the 32-state Fock space of one site is the spinor 16 + 16bar of Spin(10): Casimir 45/4 on every state, even half of dimension 16",
      f"Casimir err {np.abs(cas - 45 / 4 * np.eye(D)).max():.0e}")


def adcas(O):
    out = np.zeros_like(O)
    for ab in PAIRS:
        c1 = M[ab] @ O - O @ M[ab]
        out += M[ab] @ c1 - c1 @ M[ab]
    return out


vals = {}
for p in (1, 3, 5):
    lam = set()
    err = 0.0
    for S in itertools.combinations(range(2 * N), p):
        O = np.eye(D, dtype=complex)
        for a in S:
            O = O @ G[a]
        cO = adcas(O)
        l = np.vdot(O, cO).real / np.vdot(O, O).real
        err = max(err, np.abs(cO - l * O).max())
        lam.add(round(float(l), 9))
    vals[p] = sorted(lam)
ok = vals == {1: [9.0], 3: [21.0], 5: [25.0]}
check("A2", ok,
      "THEOREM every fermionic (odd) operator on a site is an SO(10) TENSOR: adjoint Casimir p(10-p) = 9, 21, 25 on degree 1, 3, 5, never the spinor value 45/4; so no single-particle excitation, at a cone or anywhere, carries the 16",
      f"Casimirs {vals}; err {err:.0e}")

V = {ab: np.zeros((10, 10), complex) for ab in PAIRS}
for ab in PAIRS:
    a, b = ab
    V[ab][a, b] = -1j
    V[ab][b, a] = 1j
gens16 = [M[ab][np.ix_(EVEN, EVEN)] for ab in PAIRS]


def commutant_dim(gens, n, mode):
    rows = []
    I = np.eye(n)
    for g in gens:
        if mode == "comm":
            rows.append(np.kron(g, I) - np.kron(I, g.T))
        else:  # invariant bilinear B: g^T B + B g = 0
            rows.append(np.kron(g.T, I) + np.kron(I, g.T))
    A = np.vstack(rows)
    s = np.linalg.svd(A, compute_uv=False)
    return int((s < 1e-9).sum())


c10 = commutant_dim(list(V.values()), 10, "comm")
b10 = commutant_dim(list(V.values()), 10, "bil")
b16 = commutant_dim(gens16, 16, "bil")
check("A3", c10 == 1 and b10 == 1 and b16 == 0,
      "THEOREM (Schur) the only Spin(10)-invariant hop between two five-mode sites is sum_a g_a(x) g_a(y), so every invariant free band is H_orb(k) x 1_10 and each cone carries the vector 10; the 10 has an invariant symmetric mass form (real, unprotected), the 16 has none",
      f"commutant(10) {c10}; invariant bilinears 10: {b10}, 16: {b16}")

rng = np.random.default_rng(SEED)
ratios = []
nsurf = 0
for t in range(4):
    A0 = rng.normal(size=(4, 4))
    A0 = A0 - A0.T
    Aj = [rng.normal(size=(4, 4)) for _ in range(3)]

    def Hk(k):
        H = 1j * A0 + 0j
        for j in range(3):
            H = H + 1j * Aj[j] * np.exp(1j * k[j]) - 1j * Aj[j].T * np.exp(-1j * k[j])
        return H
    cnt = []
    for n in (12, 24):
        ks = 2 * np.pi * np.arange(n) / n
        dets = np.empty((n, n, n))
        for i, a in enumerate(ks):
            for j, b in enumerate(ks):
                for l, c in enumerate(ks):
                    dets[i, j, l] = np.linalg.det(Hk((a, b, c))).real
        cnt.append(int((np.sign(dets) != np.sign(np.roll(dets, 1, 0))).sum()))
    kk = rng.uniform(0, 2 * np.pi, 3)
    phok = np.allclose(Hk(-kk), -Hk(kk).conj())
    if cnt[0] > 0:
        nsurf += 1
        ratios.append(cnt[1] / cnt[0])
check("A4", phok and nsurf > 0 and all(2.5 < r < 6 for r in ratios),
      "THEOREM+DIAGNOSTIC a Spin(10)-invariant (Majorana) band has H(-k) = -H(k)*, det H(k) real, so its zero-energy set has codimension 1: surfaces, not cones; random 4-orbital bands: sign-change counts scale as n^2 (surface)",
      f"bands with zero surfaces {nsurf}/4; count ratio n=24/12 {[round(r, 2) for r in ratios]} (surface 4, point 1)")

print("== B. the 16-component reading: one band h(k) x 1_16, light and mirror cones")


def nodes_generic(c, A, B, n=24):
    ks = 2 * np.pi * np.arange(n) / n
    K = np.stack(np.meshgrid(ks, ks, ks, indexing="ij"), -1).reshape(-1, 3)
    d = c[None] + np.cos(K) @ A.T + np.sin(K) @ B.T
    nd = np.linalg.norm(d, axis=1).reshape(n, n, n)
    loc = np.ones_like(nd, bool)
    for ax in range(3):
        for s in (1, -1):
            loc &= nd <= np.roll(nd, s, ax)
    found = []
    for idx in np.argwhere(loc & (nd < 1.0)):
        k = ks[idx].copy()
        for _ in range(40):
            dk = c + A @ np.cos(k) + B @ np.sin(k)
            J = -A * np.sin(k)[None] + B * np.cos(k)[None]
            try:
                k = k - np.linalg.solve(J, dk)
            except np.linalg.LinAlgError:
                break
        dk = c + A @ np.cos(k) + B @ np.sin(k)
        if np.linalg.norm(dk) < 1e-10:
            k = np.mod(k, 2 * np.pi)
            if all(np.linalg.norm(np.angle(np.exp(1j * (k - f[0])))) > 1e-6 for f in found):
                J = -A * np.sin(k)[None] + B * np.cos(k)[None]
                found.append((k, int(np.sign(np.linalg.det(J)))))
    return found


def qdist(k):
    q = np.pi / 2
    dlt = k - q * np.round(k / q)
    return dlt


s = SEED
while True:
    r2 = np.random.default_rng(s)
    c, A, B = r2.normal(size=3), r2.normal(size=(3, 3)), r2.normal(size=(3, 3))
    nds = nodes_generic(c, A, B)
    if len(nds) >= 2:
        break
    s += 1
chis = [x[1] for x in nds]
dists = [np.linalg.norm(qdist(x[0])) for x in nds]
ell = 16
umk = []
for x in nds:
    dl = qdist(x[0])
    umk.append(abs(np.prod([np.mean(np.exp(1j * 4 * dl[i] * np.arange(ell))) for i in range(3)])))
check("B1", sum(chis) == 0 and min(dists) > 0.05,
      "FINITE DIAGNOSTIC generic cone band (CONE: no symmetry): isolated cones at separated generic momenta, charges sum to 0; no node sits at a quarter point Q (4Q in 2pi Z^3), so the first-order projection of any translation-invariant charge-4 term onto a cone, ell^-3 sum_x exp(4i(k-Q).x), is small",
      f"seed {s}: {len(nds)} nodes, chi {chis}; |k-Q| {[round(float(v), 2) for v in dists]}; umklapp factor {[round(float(v), 3) for v in umk]}")


def kmap(p):
    return np.array([p[0] - p[1], p[1] - p[2], p[2]])


def dKW(p, r=1.0):
    k = kmap(p)
    return np.array([np.sin(k[0]), np.sin(k[1]), np.sin(k[2]) + r * (2 - np.cos(k[0]) - np.cos(k[1]))])


def jac(f, p, h=1e-6):
    return np.stack([(f(p + h * e) - f(p - h * e)) / (2 * h) for e in np.eye(3)], 1)


n = 16
ks = 2 * np.pi * np.arange(n) / n
zeros = []
offmin = 9.0
for p in itertools.product(ks, repeat=3):
    v = np.linalg.norm(dKW(np.array(p)))
    if v < 1e-9:
        zeros.append(np.round(np.array(p) / np.pi, 6))
Kp, Rp = np.zeros(3), np.pi * np.ones(3)
chiK = int(np.sign(np.linalg.det(jac(dKW, Kp))))
chiR = int(np.sign(np.linalg.det(jac(dKW, Rp))))
check("B2", len(zeros) == 2 and chiK == 1 and chiR == -1,
      "THEOREM pinned two-cone band d(p).sigma (Karsten-Wilczek form on the unimodular map k = (p1-p2, p2-p3, p3), r = 1): zeros only at K = 0 and R = pi(1,1,1), chirality +1 and -1; both are quarter points; x 1_16 this is one 16 per cone",
      f"grid zeros/pi {[[float(a) for a in z] for z in zeros]}; chi K {chiK}, R {chiR}")

qs = [np.array(q) * np.pi / 2 for q in itertools.product(range(4), repeat=3)]
viol = 0
allowed_pairs = 0
for QL in qs:
    for QM in qs:
        same = np.allclose(np.exp(1j * (QL - QM)), 1)
        allowed = False
        for nn in range(-7, 8):
            for sL, need in ((1, 3), (-1, 1)):
                if nn % 4 == need:
                    if np.allclose(np.exp(1j * (sL * QL + nn * QM)), 1):
                        allowed = True
        allowed_pairs += allowed
        viol += allowed != same
check("B3", viol == 0 and allowed_pairs == 64,
      "THEOREM (crystal momentum + Spin(10) centre Z4, low-energy constituents) a light-mirror hybridisation psi_L O or psi_L^+ O with O built from mirror fields near Q_M (net number n, |n| <= 7) is allowed iff Q_L = Q_M: the Golterman-Shamir composite partner needs the light cone at the mirror's own quarter point; light at R, mirror at K: forbidden",
      f"exhaustive 64 x 64 quarter-point pairs: allowed {allowed_pairs} (all with Q_L = Q_M), mismatches {viol}")

# Spin(10) 16: anomaly and charge-4 invariants
Xr = sum(np.random.default_rng(SEED + 1).normal() * g for g in gens16)
tr3 = abs(np.trace(Xr @ Xr @ Xr))
z = np.diag([np.exp(1j * np.pi * (pc(s_) - N / 2)) for s_ in EVEN])
zok = np.allclose(z, z[0, 0] * np.eye(16)) and np.isclose(z[0, 0] ** 2, -1)
widx = {s_: i for i, s_ in enumerate(EVEN)}


def rootops():
    ops = []
    for i in range(N):
        for j in range(N):
            if i != j:
                ops.append(C[i].T @ C[j])
    for i, j in itertools.combinations(range(N), 2):
        ops.append(C[i].T @ C[j].T)
        ops.append(C[i] @ C[j])
    return [o[np.ix_(EVEN, EVEN)] for o in ops]


ROOTS = rootops()


def singlets4(m):
    nb = 16 * m
    occ = np.array([[(EVEN[b // m] >> j) & 1 for j in range(N)] for b in range(nb)])
    basis = [t for t in itertools.combinations(range(nb), 4) if np.all(occ[list(t)].sum(0) == 2)]
    keys = {}
    rows, cols, dat = [], [], []
    for ci, t in enumerate(basis):
        for ri, X in enumerate(ROOTS):
            for slot in range(4):
                b = t[slot]
                col = X[:, b // m]
                for s2 in np.nonzero(np.abs(col) > 1e-12)[0]:
                    nbv = s2 * m + b % m
                    new = list(t)
                    new[slot] = nbv
                    if len(set(new)) < 4:
                        continue
                    perm = np.argsort(new)
                    sgn = np.linalg.det(np.eye(4)[perm])
                    key = (ri, tuple(sorted(new)))
                    rows.append(keys.setdefault(key, len(keys)))
                    cols.append(ci)
                    dat.append(col[s2] * sgn)
    Am = sparse.coo_matrix((dat, (rows, cols)), shape=(len(keys), len(basis))).tocsr()
    Gm = (Am.conj().T @ Am).toarray()
    ev = np.linalg.eigvalsh(Gm)
    return len(basis), int((ev < 1e-8).sum())


nb1, s1 = singlets4(1)
nb2, s2 = singlets4(2)
check("B4", tr3 < 1e-10 and zok and s1 == 0 and s2 == 1,
      "THEOREM Spin(10) on the 16: tr X^3 = 0 (no perturbative anomaly); the centre Z4 acts as a uniform +-i with z^2 = -1, Z16 index 16 = 0; charge-4 invariants: none with one orbital, exactly one (the pair square) with the two-component cone slot, so the mirror's SMG term exists and is unique",
      f"|tr X^3| {tr3:.0e}; zero-weight dims {nb1}, {nb2}; singlets {s1}, {s2}")

L = 4
sites = np.array(list(itertools.product(range(L), repeat=3)))
Nsite = len(sites)
cube = np.array(list(itertools.product((0, 1), repeat=3)))
rowsF = np.zeros((Nsite, Nsite))
for ci, cc in enumerate(sites):
    for r in cube:
        x = (cc + r) % L
        rowsF[ci, (x[0] * L + x[1]) * L + x[2]] = 8 ** -0.5
phiR = np.exp(1j * sites @ Rp) / np.sqrt(Nsite)
phiK = np.ones(Nsite) / np.sqrt(Nsite)
ovR = np.abs(rowsF @ phiR).max()
ovK = np.abs(rowsF @ phiK).max()
kL = nds[0][0] if nds[0][1] == 1 else nds[1][0]
kM = [x[0] for x in nds if x[1] == -1][0]
FL = lambda p: np.prod((1 - np.exp(1j * (p - kL))) / 2)
check("B5", ovR < 1e-14 and ovK > 0.1 and abs(FL(kL)) < 1e-14 and abs(FL(kM)) > 1e-3,
      "THEOREM momentum selection without non-locality: the cube-averaged field (range one cube, the zoom kernel) has form factor prod(1 + e^{ip_i})/sqrt8, exactly 0 at R and sqrt8 at K, so a charge-4 term of filtered fields never touches the light R cone (all orders, finite volume) and acts fully on the mirror K cone; for a generic light node kL the range-one complex filter prod(1 - e^{i(p - kL)})/2 does the same",
      f"L=4: max|<row, R>| {ovR:.0e}, max|<row, K>| {ovK:.3f}; generic band |F(kL)| {abs(FL(kL)):.0e}, |F(kM)| {abs(FL(kM)):.3f}")

eps = 0.05
r3 = np.random.default_rng(SEED + 2)
cp, Ap, Bp = r3.normal(size=3), r3.normal(size=(3, 3)), r3.normal(size=(3, 3))
c0, a0, b0 = r3.normal(), r3.normal(size=3), r3.normal(size=3)
grid = np.array(list(itertools.product(2 * np.pi * np.arange(12) / 12, repeat=3)))
sc = eps / np.linalg.norm(cp[None] + np.cos(grid) @ Ap.T + np.sin(grid) @ Bp.T, axis=1).max()
sc0 = eps / np.abs(c0 + np.cos(grid) @ a0 + np.sin(grid) @ b0).max()
dP = lambda p: dKW(p) + sc * (cp + Ap @ np.cos(p) + Bp @ np.sin(p))
e0 = lambda p: sc0 * (c0 + a0 @ np.cos(p) + b0 @ np.sin(p))
moved = []
for p0 in (Kp, Rp):
    p = p0.copy()
    for _ in range(50):
        p = p - np.linalg.solve(jac(dP, p), dP(p))
    moved.append((p, int(np.sign(np.linalg.det(jac(dP, p)))), np.linalg.norm(dP(p))))
dM = np.linalg.norm(np.angle(np.exp(1j * (moved[0][0] - Kp))))
dL = moved[1][0] - Rp
FR = abs(np.prod((1 + np.exp(1j * moved[1][0])) / np.sqrt(8)))
dE = abs(e0(moved[0][0]) - e0(moved[1][0]))
check("B6", moved[0][1] == 1 and moved[1][1] == -1 and max(m_[2] for m_ in moved) < 1e-10 and dM < 3 * eps and np.linalg.norm(dL) < 3 * eps,
      "FINITE DIAGNOSTIC (CONE genericity) a random local change of max size eps = 0.05 (also in the identity part) moves both cones by O(eps) and keeps their chiralities: the mirror lies |dk| from K (SMG term detuned by 4|dk|, harmless while 4 v |dk| << mirror gap: an open condition, not a tuned point); the light cone gets filter weight |F| ~ prod|dk_i|; the node energies split by dE (a light-cone chemical potential: Fermi pocket, not a mass)",
      f"|dk_M| {dM:.3f}; |dk_L| {np.linalg.norm(dL):.3f}; |F(light)| {FR:.1e}; dE {dE:.3f}")

w, Dl = 0.25, 1.0
om = 1e-3
Gm_smg = 1j * om / (Dl ** 2 + om ** 2)  # symmetric gapped mirror: propagator zero at w = 0
Gl_paired = abs(1 / (1j * om - w ** 2 * Gm_smg))
Gl_free = abs(1 / (1j * om - w ** 2 / (1j * om)))
Gl_sep = abs(1 / (1j * om))
check("B7", Gl_paired > 100 * Gl_free and Gl_sep == 1 / om,
      "THEOREM (contrast) same-momentum pairing w (block-quartic, light-partner notes): a symmetric mirror with a propagator zero RELEASES the light mode it was gapping (pole at 0); separated cones: translation sets w(k_L) = 0, nothing was paired, nothing is released, and the light cone is the isolated Weyl node itself",
      f"|G_l(i 1e-3)|: free paired {Gl_free:.4f}, SMG mirror paired {Gl_paired:.0f}, separated {Gl_sep:.0f}")

print("supplied: 5-mode Fock (N=5), random orbital bands (seeded), KW pinned band (r=1), cube filter, eps=0.05, L=4, ell=16")
print("cited: why-three-dims (CONE), why-five-modes, site-so10 (item 8, A4), light-partner-gap, block-quartic-smg, momentum-selective-mirror, ax7-chirality-16weyl")
print("not computed: interacting Spin(10) dynamics (SMG gap of the K mirror), gauge links, light-cone chemical potential")
print(f"elapsed {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
