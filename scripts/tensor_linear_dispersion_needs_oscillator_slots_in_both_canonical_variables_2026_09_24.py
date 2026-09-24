#!/usr/bin/env python3
"""A linear tensor dispersion needs oscillator slots: both canonical variables must be non-compact.

Setting (all supplied, none adopted): the landed finite-clock tensor note's slots and integer stencils in doubled
coordinates (diagonal slots E_jj at vertex sites, face slots E_ij at plaquette sites, the vector rows (G E)_j on
link sites, the scalar-gauge pattern S^T delta_c as the sum of three planar pieces), and its noncompact linear
comparator H_N = (J/2) sum [E:E - (tr E)^2/2] + (g/2) sum h:R(h). The landed note proves that compact character
dynamics keeping both constraints exactly has every frequency O(k^3), and that H_N escapes that class. This runner
certifies, as finite diagnostics on supplied models, what H_N needs from the slots.

1. The momentum term is only weakly invariant. On a 4^3 torus with the landed integer rows: the scalar-gauge
   shift s = S^T beta is a null direction of the momentum form, s.M0 s = 0 exactly for every beta; the form changes
   under E -> E + s by 2 E.M0 s, which vanishes for every E in ker G (to 1e-12) and not otherwise. So the term is
   invariant on the constraint surface only.
2. Hence a compact E fails: the periodic version of the momentum term (cosines with the same quadratic expansion)
   changes under the continuous scalar-gauge orbit E -> E + theta s even for E in ker G (values at theta = 0.7
   reported), so it does not preserve the constraint subspace. A compact h fails too: the k^2 potential is a
   nonzero quadratic form, and no quadratic form is periodic (its change under h -> h + 2 pi e is reported). A rotor
   slot has one compact variable, so no assignment of roles realizes H_N on rotors. The landed note's cubic bound is
   the compact alternative.
3. The lattice Gaussian symbol on oscillator slots: a Hermitian lattice potential X(k) with G(k) X(k) = 0 is solved
   from the landed pieces (unique, 486 unknowns, residual 1e-13). On the doubly constrained surface (ker G for E
   modulo the scalar gauge, ker S for h modulo the vector gauge) the reduced problem has exactly two modes with
   omega^2 = J g lambda(k), lambda > 0 over the zone (minimum of lambda/|k|^2 reported over 4000 random k), and
   lambda/|k|^2 = 1 at small k in every direction to 1e-3: the isotropic linear dispersion of the continuum comparator. Off the constraint surface the potential is
   indefinite (most negative eigenvalue over |k|^2 reported), so exact constraints, not penalties, are needed.
4. The price of finite emulation: an oscillator slot truncated to N Fock levels keeps the polynomial energies but
   breaks [x, p] = i exactly on the top level: [x_N, p_N] = i (1 - N |N-1><N-1|), certified for N = 8..64. For a
   coherent state of unit amplitude the weight on the top level is e^{-1}/(N-1)!, 7e-5 at N = 8 and 3e-13 at N = 16
   (values reported): the gauge algebra is realized up to a defect exponentially small in the level count, at
   log2 N qubits per slot. The constraints of oscillator slots have continuous spectra, so they are
   not stabilizers; this is recorded, not resolved.

Prints one line per check and TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
from math import lgamma

import numpy as np

AUDIT_TIMEOUT_SEC = 600

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


rng = np.random.default_rng(914)
E3 = np.eye(3, dtype=int)
PAIRS = [(0, 1), (1, 2), (0, 2)]

# ------------------------------------------------ the landed slots, rows and scalar-gauge pattern on a torus
L = 4


def key(x, i, j):
    return (tuple(int(c) % L for c in x), (min(i, j), max(i, j)))


def row_terms(x, j):
    """The landed vector row (G E)_j(x) = E_jj(x + e_j) - E_jj(x) + sum_{i != j} [E_ij(x) - E_ij(x - e_i)]."""
    x = np.array(x)
    t = [(key(x + E3[j], j, j), 1), (key(x, j, j), -1)]
    for i in range(3):
        if i != j:
            t += [(key(x, i, j), 1), (key(x - E3[i], i, j), -1)]
    return t


def planar(x, n_):
    """One planar piece of the landed scalar-gauge pattern S^T delta_x, in the plane normal to axis n_."""
    a, b = [c for c in range(3) if c != n_]
    x = np.array(x)
    v = {}
    for (j, i) in ((a, b), (b, a)):
        for s in (1, -1):
            v[key(x + s * E3[i], j, j)] = v.get(key(x + s * E3[i], j, j), 0) + 1
        v[key(x, j, j)] = v.get(key(x, j, j), 0) - 2
    i, j = min(a, b), max(a, b)
    for sh, c in [((0, 0, 0), -1), (tuple(-E3[i]), 1), (tuple(-E3[j]), 1), (tuple(-E3[i] - E3[j]), -1)]:
        k = key(x + np.array(sh), i, j)
        v[k] = v.get(k, 0) + c
    return v


cells = list(itertools.product(range(L), repeat=3))
slots = [key(x, j, j) for x in cells for j in range(3)] + [key(x, i, j) for x in cells for (i, j) in PAIRS]
sid = {k: n for n, k in enumerate(slots)}
G = np.zeros((3 * L ** 3, len(slots)))
for r, (x, j) in enumerate((x, j) for x in cells for j in range(3)):
    for k, c in row_terms(x, j):
        G[r, sid[k]] += c
Spat = np.zeros((L ** 3, len(slots)))                      # rows: S^T delta_c as slot vectors
for r, c in enumerate(cells):
    for n_ in range(3):
        for k, v in planar(c, n_).items():
            Spat[r, sid[k]] += v
GS = np.abs(G @ Spat.T).max()
weights = np.array([1.0 if k[1][0] == k[1][1] else 2.0 for k in slots])      # E:E counts each face slot twice
diag_of = {c: [sid[key(c, j, j)] for j in range(3)] for c in cells}


def M_form(E):
    """E:E - (tr E)^2 / 2 summed over the torus."""
    tr = np.array([E[diag_of[c]].sum() for c in cells])
    return float(np.sum(weights * E * E) - 0.5 * np.sum(tr * tr))


def M_periodic(E):
    """The cosine version with the same quadratic expansion."""
    tr = np.array([E[diag_of[c]].sum() for c in cells])
    return float(np.sum(weights * 2 * (1 - np.cos(E))) - np.sum(1 - np.cos(tr)))


# ------------------------------------------------ 1. weak invariance of the momentum term
u, sv, vt = np.linalg.svd(G)
null = vt[int(np.sum(sv > 1e-9)):]                          # basis of ker G
null_dim = null.shape[0]
s_null = max(abs(M_form(Spat[r])) for r in range(len(cells)))               # s.M0 s for beta = delta_c
beta = rng.normal(size=len(cells))
s_rand = Spat.T @ beta
s_rand_null = abs(M_form(s_rand))
E_in = null.T @ rng.normal(size=null_dim)                    # random E on the constraint surface
E_off = rng.normal(size=len(slots))
d_in = M_form(E_in + s_rand) - M_form(E_in)
d_off = M_form(E_off + s_rand) - M_form(E_off)
check("the momentum term E:E - (tr E)^2/2 is invariant under the scalar gauge on the constraint surface only",
      GS == 0 and s_null < 1e-12 and s_rand_null < 1e-9 and abs(d_in) < 1e-9 and abs(d_off) > 1e-2,
      f"G S^T = {GS:.0f} exactly on the 4^3 torus; ker G has dimension {null_dim} of {len(slots)}; s.M0 s = {s_null:.0e} for every "
      f"delta_c and {s_rand_null:.0e} for a random beta; change under E -> E + s: {d_in:.0e} for E in ker G, {d_off:.3f} off it")

# ------------------------------------------------ 2. neither variable can be compact
theta = 0.7
d_per = [M_periodic(E_in_ + theta * s_rand) - M_periodic(E_in_) for E_in_ in (null.T @ rng.normal(size=null_dim) for _ in range(3))]
Vq = Spat.T @ Spat                                           # a nonzero gauge-invariant quadratic form in h (the squared pattern)
h0 = rng.normal(size=len(slots))
d_h = [float(h0 @ Vq @ h0 - (h0 + 2 * np.pi * np.eye(len(slots))[i]) @ Vq @ (h0 + 2 * np.pi * np.eye(len(slots))[i])) for i in (0, 7, 300)]
check("neither canonical variable can be compact: the periodic momentum term moves under the scalar-gauge orbit on ker G, and a quadratic potential is not 2 pi periodic",
      min(abs(d) for d in d_per) > 1e-3 and min(abs(d) for d in d_h) > 1e-3,
      f"periodic momentum term, E in ker G, theta = {theta}: changes {', '.join(f'{d:.3f}' for d in d_per)}; a quadratic potential under "
      f"h -> h + 2 pi e_slot: changes {', '.join(f'{d:.1f}' for d in d_h)}")

# ------------------------------------------------ 3. the lattice Gaussian symbol on oscillator slots
FACE_IX = {(0, 1): 3, (1, 2): 4, (0, 2): 5}


def G_k(k):
    Gk = np.zeros((3, 6), dtype=complex)
    for j in range(3):
        Gk[j, j] = np.exp(1j * k[j]) - 1
        for i in range(3):
            if i != j:
                Gk[j, FACE_IX[tuple(sorted((i, j)))]] += 1 - np.exp(-1j * k[i])
    return Gk


def piece_k(k, n_):
    a, b = [c for c in range(3) if c != n_]
    v = np.zeros(6, dtype=complex)
    v[a] = 2 * np.cos(k[b]) - 2
    v[b] = 2 * np.cos(k[a]) - 2
    i, j = min(a, b), max(a, b)
    v[FACE_IX[(i, j)]] = -1 + np.exp(-1j * k[i]) + np.exp(-1j * k[j]) - np.exp(-1j * (k[i] + k[j]))
    return v


MON = list(itertools.product((-1, 0, 1), repeat=3))         # face-face block: sum_m c_m e^{i m.k}, m in {-1,0,1}^3


def X_of(k, c):
    X = np.zeros((6, 6), dtype=complex)
    for n_ in range(3):
        X[n_] = piece_k(k, n_)                                # the diagonal rows are the planar pieces
    for n_ in range(3):
        for f in (3, 4, 5):
            X[f, n_] = np.conj(X[n_, f])
    e = np.array([np.exp(1j * np.dot(m, k)) for m in MON])
    for a in range(3):
        for b in range(3):
            X[3 + a, 3 + b] = e @ (c[a, b, :, 0] + 1j * c[a, b, :, 1])
    return X


nun = 9 * len(MON) * 2


def affine(fun):
    base = fun(np.zeros((3, 3, len(MON), 2)))
    cols = []
    for idx in range(nun):
        c = np.zeros(nun)
        c[idx] = 1
        cols.append(fun(c.reshape(3, 3, len(MON), 2)) - base)
    return np.array(cols).T, base


rows_, rhs_ = [], []
for k in rng.uniform(-np.pi, np.pi, (40, 3)):
    A_, b0 = affine(lambda c: (G_k(k) @ X_of(k, c)).ravel())
    rows_ += [A_.real, A_.imag]
    rhs_ += [-b0.real, -b0.imag]
    A_, b0 = affine(lambda c: (X_of(k, c) - X_of(k, c).conj().T).ravel())
    rows_ += [A_.real, A_.imag]
    rhs_ += [-b0.real, -b0.imag]
Asys, bsys = np.vstack(rows_), np.concatenate(rhs_)
csol, _, rank_sys, _ = np.linalg.lstsq(Asys, bsys, rcond=None)
resid = np.linalg.norm(Asys @ csol - bsys)
csol = csol.reshape(3, 3, len(MON), 2)
M0k = np.diag([1.0, 1, 1, 2, 2, 2]) - 0.5 * np.outer([1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0])


def reduced_modes(k):
    """Two physical modes: omega^2 / (J g) on the doubly constrained surface, using dual bases of the quotients."""
    Gk = G_k(k)
    X = X_of(k, csol)
    s = sum(piece_k(k, n_) for n_ in range(3))               # the scalar-gauge direction in E space (S^T beta)
    KG = np.linalg.svd(Gk)[2][3:].conj().T                    # ker G (3-dim)
    # E representatives: ker G orthogonal to s
    Es = KG @ np.linalg.svd((s.conj() @ KG)[None, :])[2][1:].conj().T          # 2 columns
    # h representatives: ker S = orthogonal complement of s (as the row of S), then orthogonal to the vector gauge G^dagger
    KS = np.linalg.svd(s[None, :])[2][1:].conj().T           # 5-dim
    Gc = Gk.conj().T                                         # gauge directions of h: columns of G^dagger (3)
    proj = KS @ np.linalg.svd((Gc.conj().T @ KS))[2][3:].conj().T           # 2 columns in ker S orthogonal to the gauge
    B = proj.conj().T @ Es                                   # pairing between the h and E representatives
    hs = proj @ np.linalg.inv(B).conj().T                    # dual basis: hs^dagger Es = identity
    Mr = Es.conj().T @ M0k @ Es                             # Hermitian 2x2 forms on the quotients (complex)
    Vr = hs.conj().T @ X @ hs
    return np.sort(np.linalg.eigvals(Mr @ Vr).real), np.linalg.eigvalsh(KG.conj().T @ X @ KG)


lam_ratio = []
for _ in range(200):
    k = rng.uniform(-1, 1, 3) * 0.02
    lam_ratio.append(reduced_modes(k)[0] / np.dot(k, k))
lam_ratio = np.array(lam_ratio)
mins, negs, negoff = [], 0, []
for k in rng.uniform(-np.pi, np.pi, (4000, 3)):
    lam, full = reduced_modes(k)
    mins.append(lam.min() / np.dot(k, k))
    negs += lam.min() < -1e-12
    negoff.append(full.min() / np.dot(k, k))
check("oscillator slots: on the doubly constrained surface two modes with omega^2 = J g lambda, lambda ~ |k|^2 and positive; indefinite off it",
      rank_sys == nun and resid < 1e-10 and negs == 0 and min(mins) > 0.1 and abs(lam_ratio.min() - 1) < 1e-3 and abs(lam_ratio.max() - 1) < 1e-3
      and min(negoff) < -0.5,
      f"lattice potential X(k): {nun} unknowns, rank {rank_sys}, residual {resid:.0e}, G X = 0 and X Hermitian; two reduced modes; "
      f"lambda/|k|^2 at small k in [{lam_ratio.min():.3f}, {lam_ratio.max():.3f}]; over 4000 random k: min lambda/|k|^2 = {min(mins):.3f}, "
      f"negative modes {negs}; without the scalar constraint the potential's most negative eigenvalue over |k|^2 is {min(negoff):.3f}")

# ------------------------------------------------ 4. the price of finite emulation: truncated oscillators
rows4, defect_ok = [], True
for N in (8, 16, 32, 64):
    a = np.diag(np.sqrt(np.arange(1, N)), 1)                # annihilation operator truncated to N levels
    x = (a + a.T) / np.sqrt(2)
    p = 1j * (a.T - a) / np.sqrt(2)
    comm = x @ p - p @ x
    target = 1j * (np.eye(N) - N * np.outer(np.eye(N)[N - 1], np.eye(N)[N - 1]))
    defect_ok &= np.abs(comm - target).max() < 1e-10
    top_weight = np.exp(-1.0 - lgamma(N))                   # coherent state alpha = 1: |<N-1|alpha>|^2 = e^{-1} / (N-1)!
    rows4.append((N, int(np.log2(N)), top_weight))
check("truncated oscillator slots: [x_N, p_N] = i (1 - N |N-1><N-1|) exactly, and a coherent state's weight on the top level is exponentially small",
      defect_ok and rows4[2][2] < 1e-30 and rows4[1][2] < 1e-12,
      "; ".join(f"N = {N} ({q} qubits): top-level weight {w:.1e}" for N, q, w in rows4))

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
