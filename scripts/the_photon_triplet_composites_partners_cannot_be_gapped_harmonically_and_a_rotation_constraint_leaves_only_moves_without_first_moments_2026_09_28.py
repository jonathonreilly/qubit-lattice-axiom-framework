#!/usr/bin/env python3
"""The photon-triplet composite: its partners cannot be gapped, and a rotation constraint makes it the soft tensor theory.

Question (the panel's T2, 2026-09-28): probe 11 built a light-cone
helicity-2 channel as a composite, E = curl_1(A~ - I tr A~/2), of a triplet
of photons. Three of the six photon modes (helicity +-1 and 0) are invisible
to E but stay gapless: partners. Can they be gapped or removed while E stays
exactly symmetric with G E = 0, without making the helicity-2 channel soft?
Pre-registered (scratch file): PASS if a local quadratic term gaps the
partners with helicity 2 still linear, or if an exact local constraint that
removes them leaves moves with TT-visible first moments; FAIL otherwise.

Checks:
  A  E's antisymmetric part is a combination of the three photon Gauss laws,
     with the same kernel (rank 3 at every sampled q != 0): E is exactly
     symmetric iff the triplet's Gauss laws hold. So the premise forces
     exact U(1) gauge invariance of each photon.
  B  harmonic regime: for random positive local quadratic forms (kinetic on
     A~, potential on the photons' curls), all six physical modes have
     omega -> 0 linearly in |K| (no gap). A gauge-invariant potential has
     V(0) = 0, so no q^0 term can gap any mode.
  C  cubic covariance: a mechanism acting on one photon index (e.g.
     confining photon z) removes the partners for q along z but helicity-2
     weight for q along x; photon-index-selective gapping cannot remove the
     partners in every direction without touching helicity 2.
  D  the rotation constraint (A~_lj = A~_jl at their common site) is local
     and pointwise; with the Gauss laws it makes A~ a symmetric tensor on
     the landed placement (shifted by s), and on that embedding the three
     Gauss laws equal the landed momentum rule exactly (4^3 torus). On a
     box, the Gauss-only moves keep first moments (rank 9: loop dipoles) but
     the Gauss+rotation moves have vanishing zeroth and first moments and
     nonzero second moments: probe 10's lemma, O(q^4).
  E  harmonic comparator of the rotation-constrained triplet (Maxwell-type
     kinetic on symmetric A~, potential from the Gauss+rotation box-kernel
     moves): both TT modes have omega ~ q^2 (fitted exponent 2.00 +- 0.05).
Reference only: tetrad/teleparallel linearised gravity (a symmetric part of
a vector-potential triplet with local rotations; landed 2026-09-21 note on
the coins' frame); Chandrasekharan-Wiese quantum links.
Prints one line per check, the N5 lines and TOTAL.
"""
import itertools
import numpy as np
import sympy as sp
from scipy.linalg import null_space

AUDIT_TIMEOUT_SEC = 900
PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


rng = np.random.default_rng(20260928)
E3 = np.eye(3); s0 = np.full(3, 0.5)
EPS = np.zeros((3, 3, 3))
for (i, j, k) in itertools.permutations(range(3)):
    EPS[i, j, k] = np.linalg.det(np.eye(3)[[i, j, k]])


def L_symbol(q):           # probe 11: E_ij = sum_kl eps_ikl i K_k A_lj,  A = A~ - I tr A~ / 2
    K = 2 * np.sin(q / 2); L = np.zeros((9, 9), complex)
    for i in range(3):
        for jx in range(3):
            for kx in range(3):
                for l in range(3):
                    if EPS[i, kx, l]:
                        c = EPS[i, kx, l] * 1j * K[kx]
                        L[3 * i + jx, 3 * l + jx] += c
                        if l == jx:
                            for m in range(3):
                                L[3 * i + jx, 3 * m + m] += -0.5 * c
    return L


def photon_gauss(q):       # photon l: sum_j i K_j A~_lj = 0
    K = 2 * np.sin(q / 2); P = np.zeros((3, 9), complex)
    for l in range(3):
        for jx in range(3):
            P[l, 3 * l + jx] = 1j * K[jx]
    return P


def curl_blocks(q):        # each photon's curl on its vector potential a_l (component basis l, j)
    K = 2 * np.sin(q / 2); C = np.zeros((9, 9), complex)
    for l in range(3):
        for i in range(3):
            for kx in range(3):
                for jx in range(3):
                    if EPS[i, kx, jx]:
                        C[3 * l + i, 3 * l + jx] += EPS[i, kx, jx] * 1j * K[kx]
    return C


# ---------------------------------------------------------------- A: E symmetric iff the triplet's Gauss laws
okA = True; ranks = []
for _ in range(30):
    q = rng.uniform(-np.pi, np.pi, size=3)
    Lq = L_symbol(q)
    Anti = np.array([Lq[3 * i + j] - Lq[3 * j + i] for (i, j) in [(0, 1), (1, 2), (0, 2)]])
    Pg = photon_gauss(q)
    r_anti = np.linalg.matrix_rank(Anti, tol=1e-9); r_both = np.linalg.matrix_rank(np.vstack([Anti, Pg]), tol=1e-9)
    ranks.append((r_anti, r_both))
    okA &= r_anti == 3 and r_both == 3
check("A: E's antisymmetric part is a combination of the three photon Gauss laws with the same kernel (rank 3 at every sampled q != 0), so E is exactly symmetric iff each photon's Gauss law holds: the premise forces exact U(1) gauge invariance",
      okA, f"30 random zone momenta: (rank of antisym(E), rank of antisym(E) with the Gauss rows) = {sorted(set(ranks))}")

# ---------------------------------------------------------------- B: harmonic regime, random positive local forms: no gap
def rand_pos(n, scale=1.0):
    X = rng.normal(size=(n, n)); return X @ X.T / n + scale * np.eye(n)


okB = True; rowsB = []
for trial in range(5):
    K0 = rand_pos(9); Kx = [rand_pos(9, 0.1) for _ in range(3)]; W0 = rand_pos(9)
    n = rng.normal(size=3); n /= np.linalg.norm(n); rat = []
    for eps in (0.04, 0.02, 0.01):
        q = eps * n; Kq = K0 + sum((1 - np.cos(q[k])) * Kx[k] for k in range(3))
        C = curl_blocks(q); V = C.conj().T @ W0 @ C
        N = null_space(photon_gauss(q))                                     # 6 transverse components (Gauss kernel)
        w2 = np.sort(np.linalg.eigvals((N.conj().T @ Kq @ N) @ (N.conj().T @ V @ N)).real)
        rat.append(np.sqrt(np.maximum(w2, 0)) / np.linalg.norm(2 * np.sin(q / 2)))
    conv = np.allclose(rat[1], rat[2], rtol=2e-3)
    okB &= conv and rat[2].min() > 1e-3 and len(rat[2]) == 6
    rowsB.append(f"trial {trial}: omega/|K| -> {np.round(rat[2], 3)}")
# gauge invariance forces V(0) = 0: V annihilates K (x) lambda for every q, so V's constant part annihilates all of C^9
Vs = [curl_blocks(1e-8 * rng.normal(size=3)) for _ in range(3)]
okB &= max(np.abs(v).max() for v in Vs) < 1e-7
check("B: harmonic regime: for random positive local quadratic forms (kinetic on A~ with q-dependent parts, potential on the photons' curls) all six physical modes have omega -> 0 linearly in |K|; a gauge-invariant potential vanishes at q = 0, so no q^0 term can gap the partners",
      okB, "; ".join(rowsB))


# ---------------------------------------------------------------- C: cubic covariance: photon-index-selective gapping
def helicity2_projector(khat):
    kh = khat / np.linalg.norm(khat); a = np.array([1., 0, 0]) if abs(kh[0]) < 0.9 else np.array([0, 1., 0])
    u = np.cross(kh, a); u /= np.linalg.norm(u); v = np.cross(kh, u)
    T = [(np.outer(u, u) - np.outer(v, v)) / np.sqrt(2), (np.outer(u, v) + np.outer(v, u)) / np.sqrt(2)]
    B = np.array([t.reshape(-1) for t in T]).T                            # A~_lj flattened as 3 l + j
    return B @ B.T


def photon_subspace(l):
    Pz = np.zeros((9, 9)); Pz[3 * l:3 * l + 3, 3 * l:3 * l + 3] = np.eye(3); return Pz


def transverse(khat):
    kh = khat / np.linalg.norm(khat); Pt = np.eye(3) - np.outer(kh, kh)
    return np.kron(np.eye(3), Pt)                                           # Gauss kernel projector at q -> 0 along khat


ov = {}
for name, kh in (("q along z", np.array([0, 0, 1.])), ("q along x", np.array([1., 0, 0]))):
    Pphys = transverse(kh); Pz = photon_subspace(2) @ Pphys; H2 = helicity2_projector(kh)
    ov[name] = float(np.linalg.norm(H2 @ Pz))
okC = ov["q along z"] < 1e-12 and ov["q along x"] > 0.5
check("C: cubic covariance: gapping one photon index (photon z) removes only partner weight for q along z but removes helicity-2 weight for q along x; photon-index-selective mechanisms cannot remove the partners in every direction without touching helicity 2 (and cubic symmetry treats the three photons alike)",
      okC, f"|P_helicity2 P_photon-z| on the physical modes: q along z {ov['q along z']:.2e}, q along x {ov['q along x']:.3f}")

# ---------------------------------------------------------------- D: the rotation constraint in real space; moments of compatible moves
# slot (cell x, l, j) at x + s - e_l/2 + e_j/2; photon l's Gauss law at site x + s - e_l/2: sum_j [A~_lj(x) - A~_lj(x - e_j)]
def pos(x, l, j):
    return np.array(x, float) + s0 - E3[l] / 2 + E3[j] / 2


def gauss_row(x, l):
    x = np.array(x); d = {}
    for j in range(3):
        d[(tuple(x), l, j)] = d.get((tuple(x), l, j), 0) + 1
        d[(tuple(x - E3[j].astype(int)), l, j)] = d.get((tuple(x - E3[j].astype(int)), l, j), 0) - 1
    return d


def rot_row(x, l, j):      # A~_lj at x equals A~_jl at the cell whose slot sits at the same point: x + e_j - e_l
    x = np.array(x); y = x + E3[j].astype(int) - E3[l].astype(int)
    return {(tuple(x), l, j): 1, (tuple(y), j, l): -1}


def box_kernel(nb, with_rot):
    box = list(itertools.product(range(nb), repeat=3))
    slots = [(c, l, j) for c in box for l in range(3) for j in range(3)]; sidx = {sl_: i for i, sl_ in enumerate(slots)}
    rows = []
    def add(d):
        row = [0] * len(slots); touch = False; outside = False
        for k, v in d.items():
            if k in sidx:
                row[sidx[k]] += v; touch = True
            else:
                outside = True
        return row, touch, outside
    for x in itertools.product(range(-1, nb + 1), repeat=3):
        for l in range(3):
            row, t, _ = add(gauss_row(x, l))
            if t and any(row):
                rows.append(row)
    if with_rot:
        for x in itertools.product(range(-1, nb + 1), repeat=3):
            for l in range(3):
                for j in range(3):
                    if l < j:
                        row, t, o = add(rot_row(x, l, j))
                        if t and any(row):
                            rows.append(row)             # a rotation row touching the box forces both slots (one outside -> slot must vanish)
    basis = []
    for v in sp.Matrix(rows).nullspace():
        den = sp.ilcm(*[sp.fraction(z)[1] for z in v]); w = np.array([int(z * den) for z in v]); basis.append(w // np.gcd.reduce(np.abs(w[w != 0])))
    return slots, sidx, (np.array(basis).T.astype(float) if basis else np.zeros((len(slots), 0)))


def moments(K_, slots):
    M0 = np.zeros((K_.shape[1], 9)); M1 = np.zeros((K_.shape[1], 27)); M2 = np.zeros((K_.shape[1], 81))
    for t in range(K_.shape[1]):
        m0 = np.zeros(9); m1 = np.zeros((9, 3)); m2 = np.zeros((9, 3, 3))
        for i, (c, l, j) in enumerate(slots):
            v = K_[i, t]
            if v:
                p = pos(c, l, j); m0[3 * l + j] += v; m1[3 * l + j] += v * p; m2[3 * l + j] += v * np.outer(p, p)
        M0[t] = m0; M1[t] = m1.ravel(); M2[t] = m2.ravel()
    return M0, M1, M2


slG, siG, KGa = box_kernel(2, False)
slR, siR, KRa = box_kernel(3, True)
m0G, m1G, _ = moments(KGa, slG)
m0R, m1R, m2R = moments(KRa, slR)
rk1G = np.linalg.matrix_rank(m1G, tol=1e-9) if KGa.shape[1] else 0
rk1R = np.linalg.matrix_rank(m1R, tol=1e-9) if KRa.shape[1] else 0
rk2R = np.linalg.matrix_rank(m2R, tol=1e-9) if KRa.shape[1] else 0
# the rotation-compatible moves are symmetric: A~_lj(x) = A~_jl(x + e_j - e_l)
sym_ok = True
for t in range(KRa.shape[1]):
    for (c, l, j), i in siR.items():
        if l != j:
            y = tuple(np.array(c) + E3[j].astype(int) - E3[l].astype(int))
            if (y, j, l) in siR:
                sym_ok &= KRa[i, t] == KRa[siR[(y, j, l)], t]
            else:
                sym_ok &= KRa[i, t] == 0
# exact identification: embed a landed symmetric-tensor configuration p (diag at vertices, faces at (e_i+e_j)/2) into the triplet by
# A~_ll(x) = p_ll(x), A~_ij(c + e_i) = A~_ji(c + e_j) = p_face(ij)(c); then photon l's Gauss law at x equals the landed row (c = x - e_l, j = l)
Lt = 4; FACE = {(0, 1): 3, (1, 2): 4, (0, 2): 5}
cells_t = list(itertools.product(range(Lt), repeat=3)); ci = {c: i for i, c in enumerate(cells_t)}
def lsl(c, a):
    return 6 * ci[tuple(np.array(c) % Lt)] + a
def tsl(c, l, j):
    return 9 * ci[tuple(np.array(c) % Lt)] + 3 * l + j
P = np.zeros((9 * len(cells_t), 6 * len(cells_t)))
for c in cells_t:
    for j in range(3):
        P[tsl(c, j, j), lsl(c, j)] = 1
    for (i, j), f in FACE.items():
        P[tsl(np.array(c) + E3[i].astype(int), i, j), lsl(c, f)] = 1; P[tsl(np.array(c) + E3[j].astype(int), j, i), lsl(c, f)] = 1
Gauss_t = np.zeros((3 * len(cells_t), 9 * len(cells_t))); Gland = np.zeros((3 * len(cells_t), 6 * len(cells_t)))
for c in cells_t:
    x = np.array(c)
    for l in range(3):
        for j in range(3):
            Gauss_t[3 * ci[c] + l, tsl(x, l, j)] += 1; Gauss_t[3 * ci[c] + l, tsl(x - E3[j].astype(int), l, j)] -= 1
    for j in range(3):                                               # landed row (c, j), stored at the Gauss row of site x = c + e_j
        r = 3 * ci[tuple((x + E3[j].astype(int)) % Lt)] + j
        Gland[r, lsl(x + E3[j].astype(int), j)] += 1; Gland[r, lsl(x, j)] -= 1
        for i in range(3):
            if i != j:
                f = FACE[tuple(sorted((i, j)))]; Gland[r, lsl(x, f)] += 1; Gland[r, lsl(x - E3[i].astype(int), f)] -= 1
ident = np.abs(Gauss_t @ P - Gland).max()
okD = ident == 0 and KGa.shape[1] > 0 and KRa.shape[1] > 0 and np.abs(m0G).max() < 1e-12 and rk1G > 0 and np.abs(m0R).max() < 1e-12 and rk1R == 0 and rk2R > 0 and sym_ok
check("D: the rotation constraint (A~_lj = A~_jl at their common site) is local and pointwise, and on the symmetric embedding the three Gauss laws are exactly the landed momentum rule (placement shifted by s); Gauss-only moves keep first moments (loop dipoles), but Gauss+rotation moves are symmetric tensors with vanishing zeroth and first moments and nonzero second moments: probe 10's lemma, so exactly invariant periodic potentials are O(q^4)",
      okD, f"on the {Lt}^3 torus, Gauss laws on the symmetric embedding = the landed momentum rule exactly (max difference {ident:.0f}); Gauss-only box 2^3: {KGa.shape[1]} moves, zeroth moments max {np.abs(m0G).max():.1e}, first-moment rank {rk1G}; Gauss+rotation box 3^3: {KRa.shape[1]} moves, symmetric {sym_ok}, zeroth moments max {np.abs(m0R).max():.1e}, first-moment rank {rk1R}, second-moment rank {rk2R}")


# ---------------------------------------------------------------- E: harmonic comparator of the rotation-constrained triplet
def rhat(Kmat, t, sidx, q):
    out = np.zeros(9, complex)
    for (c, l, j), i in sidx.items():
        v = Kmat[i, t]
        if v:
            out[3 * l + j] += v * np.exp(-1j * q @ pos(c, l, j))
    return out


def tt_sym(khat):          # symmetric TT tensors about khat, flattened (l, j)
    kh = khat / np.linalg.norm(khat); a = np.array([1., 0, 0]) if abs(kh[0]) < 0.9 else np.array([0, 1., 0])
    u = np.cross(kh, a); u /= np.linalg.norm(u); v = np.cross(kh, u)
    return np.array([((np.outer(u, u) - np.outer(v, v)) / np.sqrt(2)).reshape(-1), ((np.outer(u, v) + np.outer(v, u)) / np.sqrt(2)).reshape(-1)]).T


expo = []; okE = True; rowsE = []
for n in [np.array([0, 0, 1.]), np.array([1, 1, 0.]) / np.sqrt(2), np.array([1, 1, 1.]) / np.sqrt(3), np.array([0.3, -0.5, 0.81]) / np.linalg.norm([0.3, -0.5, 0.81])]:
    om = []; Kn = []
    for eps in (0.2, 0.1, 0.05, 0.025):
        q = eps * n; K = 2 * np.sin(q / 2); T = tt_sym(K)
        W = sum(np.outer(rhat(KRa, t, siR, q), rhat(KRa, t, siR, q).conj()) for t in range(KRa.shape[1]))
        Wred = T.conj().T @ W @ T; Kred = T.conj().T @ T                        # Maxwell-type kinetic |A~|^2 on symmetric TT
        om.append(np.sqrt(np.sort(np.linalg.eigvals(Kred @ Wred).real))); Kn.append(np.linalg.norm(K))
    om = np.array(om); fits = [np.polyfit(np.log(Kn), np.log(om[:, m]), 1)[0] for m in range(2)]
    okE &= all(abs(f - 2) < 0.05 for f in fits); expo += fits
    rowsE.append(f"n = {np.round(n, 2)}: exponents {np.round(fits, 3)}, omega/K^2 at |K| = {Kn[-1]:.3f}: {np.round(om[-1] / Kn[-1] ** 2, 3)}")
check("E: harmonic comparator of the rotation-constrained triplet (Maxwell-type kinetic on symmetric A~, potential from the Gauss+rotation box-kernel moves): both TT modes have omega ~ q^2 (fitted exponent 2.00 +- 0.05 on axis, face, body and a generic direction)",
      okE, "; ".join(rowsE))

print("N5 resolution 1: keeping the composite exactly symmetric with G E = 0 is the same as keeping each photon's Gauss law exact.")
print("N5 resolution 2: in the harmonic regime no local gauge-invariant quadratic term gaps the partners; photon-index-selective mechanisms touch helicity 2 in some direction.")
print("N5 resolution 3: removing the partners with the local rotation constraint turns the triplet into probe 10's momentum-diagonal tensor theory: compatible moves lose zeroth and first moments, and the harmonic comparator has omega ~ q^2. Pre-registered outcome: FAIL.")
print("per_element: each symbol identity at 30 zone momenta; each box-kernel move's moments.")
print("per_site: the Gauss and rotation rows at every site touching the boxes (2^3 and 3^3 cells).")
print("per_mode: six photon-triplet modes for 5 random forms; two TT modes of the constrained comparator in four directions.")
print("per_block: the 2^3 Gauss-only and 3^3 Gauss+rotation box kernels.")
print("lattice_wide: checked and not executed - any ground state beyond the harmonic regime, confinement or partial Higgs phases, other constraint sets than the rotation constraint, a phase.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
