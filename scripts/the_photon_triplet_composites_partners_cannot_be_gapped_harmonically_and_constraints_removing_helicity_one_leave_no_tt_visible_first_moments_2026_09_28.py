#!/usr/bin/env python3
"""The photon-triplet composite: partners are not gapped by gauge-invariant local harmonic terms; tested constraint sets that remove helicity 1 leave no TT-visible first moments.

Question (the panel's T2, 2026-09-28): probe 11 built a light-cone
helicity-2 channel as a composite, E = curl_1(A~ - I tr A~/2), of a triplet
of photons. Three of the six photon modes are invisible to E but gapless
(partners: helicity +-1 and a helicity-0 transverse trace). Can they be
gapped or removed, keeping E exactly symmetric with G E = 0, without making
the helicity-2 channel soft? Pre-registered in the probe's scratch file.
Revised after the first referee's FAILS verdict: the rotation constraint does
not remove every partner (it keeps the transverse-trace scalar).

Checks:
  A  exact identity: eps_mij E_ij = Gauss_m row for row (difference 0 at 37
     momenta including axes, zone edges and corners), so E is exactly
     symmetric iff every photon Gauss law holds.
  B  harmonic regime, local forms: with a bounded local kinetic form on A~,
     a finite-range potential in the photons' curls and finite-range E-B
     cross terms, gauge invariance makes the potential and the cross block
     vanish at q = 0, so every frequency -> 0 as q -> 0 (random forms with
     cross terms and higher-derivative curl kernels); a Proca mass (not
     gauge-invariant) gaps them. A non-local B (-Delta)^-1 B term would also
     gap, and is excluded by locality.
  C  fixed photon-index projectors: the photon-z block removes only partner
     weight for q along z but helicity-2 weight for q along x.
  D  constraint sets, physical / seen by E / invisible to E: Gauss 6/3/3;
     + rotation 3/2/1 (the transverse-trace partner survives; ker E is
     K K^T - K^2 I); + rotation + trace 2/2/0; + first-index Gauss 4/3/1;
     + first-index Gauss + trace 3/3/0; + trace alone keeps helicity +-1.
     The rotation constraint is pointwise and its Gauss laws equal the landed
     momentum rule exactly on the symmetric embedding (4^3 torus).
  E  moves (integer box kernels, moments at physical positions): Gauss only,
     first-moment rank 9, TT-visible; + rotation (3^3) zeroth and first
     moments 0, second-moment rank 6; + rotation + trace (4^3, float
     kernel) zeroth, first and second moments 0; + first-index Gauss (3^3)
     first-moment rank 1, antisymmetric (eps), TT-invisible; the same with
     the trace added.
  F  all 15 cubic-covariant pointwise constraint sets (unions of the irreps
     I, E, T2, T1 of 3x3 matrices, as allowed values): every set that
     removes helicity +-1 and keeps a TT mode (I+T2, E+T2, I+E+T2) has no
     first-moment space; first moments need T1, which keeps helicity +-1.
  G  harmonic comparators on the full physical space (no hand projection):
     + rotation: all three modes (TT and the scalar partner) omega ~ q^2;
     + rotation + trace: both TT modes omega ~ q^3.
Reference only: Xu (2006), Xu and Horava (arXiv:1003.0009), Gu and Wen
(arXiv:0907.1203), Pretko (arXiv:1604.05329); quantum links.
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


def rot_sym(q):
    R = np.zeros((3, 9), complex)
    for r, (l, j) in enumerate([(0, 1), (1, 2), (0, 2)]):
        R[r, 3 * l + j] = 1; R[r, 3 * j + l] = -1
    return R


def trace_sym(q):
    T = np.zeros((1, 9), complex); T[0, 0] = T[0, 4] = T[0, 8] = 1; return T


def first_gauss(q):        # sum_l i K_l A~_lj = 0
    K = 2 * np.sin(q / 2); P = np.zeros((3, 9), complex)
    for j in range(3):
        for l in range(3):
            P[j, 3 * l + j] = 1j * K[l]
    return P


def curl_blocks(q):
    K = 2 * np.sin(q / 2); C = np.zeros((9, 9), complex)
    for l in range(3):
        for i in range(3):
            for kx in range(3):
                for jx in range(3):
                    if EPS[i, kx, jx]:
                        C[3 * l + i, 3 * l + jx] += EPS[i, kx, jx] * 1j * K[kx]
    return C


# ---------------------------------------------------------------- A: exact identity eps_mij E_ij = Gauss_m
qs = [rng.uniform(-np.pi, np.pi, 3) for _ in range(25)] + [np.array(v, float) for v in
      [(0.3, 0, 0), (0, 0.3, 0), (0, 0, 0.3), (np.pi, 0, 0), (0, np.pi, 0), (np.pi, np.pi, 0), (np.pi, np.pi, np.pi), (np.pi, 0.2, 0), (0.1, np.pi, np.pi), (1.0, 1.0, 1.0), (-np.pi, 0.5, 2.0), (2.0, -2.0, np.pi)]]
diffA = 0.0
for q in qs:
    Lq = L_symbol(q); Pg = photon_gauss(q)
    for m in range(3):
        row = sum(EPS[m, i, j] * Lq[3 * i + j] for i in range(3) for j in range(3))
        diffA = max(diffA, np.abs(row - Pg[m]).max())
check("A: exact identity: eps_mij E_ij equals photon m's Gauss law row for row, so E is exactly symmetric iff every photon's Gauss law holds (the premise forces exact U(1) gauge invariance)",
      diffA < 1e-12, f"max row difference over {len(qs)} momenta (random, axes, zone edges and corners): {diffA:.1e}")

# ---------------------------------------------------------------- B: harmonic regime with local forms, including E-B cross terms
def rand_pos(n, scale=1.0):
    X = rng.normal(size=(n, n)); return X @ X.T / n + scale * np.eye(n)


okB = True; rowsB = []
for trial in range(5):
    K0 = rand_pos(9); Kx = [rand_pos(9, 0.1) for _ in range(3)]; W0 = rand_pos(9); W2 = rand_pos(9, 0.1); Y0 = rng.normal(size=(9, 9)) * 0.3
    n = rng.normal(size=3); n /= np.linalg.norm(n); rat = []
    for eps in (0.04, 0.02, 0.01):
        q = eps * n; K = 2 * np.sin(q / 2); Kq = K0 + sum((1 - np.cos(q[k])) * Kx[k] for k in range(3))
        C = curl_blocks(q); W = W0 + (K @ K) * W2                                   # higher-derivative curl kernel included
        V = C.conj().T @ W @ C; X = Y0 @ C                                            # E-B cross block (Hermitian part used below)
        N = null_space(photon_gauss(q))
        Hm = np.block([[N.conj().T @ V @ N, N.conj().T @ X.conj().T @ N], [N.conj().T @ X @ N, N.conj().T @ Kq @ N]])
        Hm = (Hm + Hm.conj().T) / 2
        if np.linalg.eigvalsh(Hm).min() < 0:                                          # keep the quadratic form stable
            Hm = Hm + (abs(np.linalg.eigvalsh(Hm).min()) + 1e-9) * np.block([[N.conj().T @ V @ N * 0, np.zeros((6, 6))], [np.zeros((6, 6)), np.eye(6)]])
        J = np.block([[np.zeros((6, 6)), np.eye(6)], [-np.eye(6), np.zeros((6, 6))]])
        w = np.sort(np.abs(np.linalg.eigvals(J @ Hm).imag))[::2]
        rat.append(w / np.linalg.norm(K))
    conv = np.allclose(rat[1], rat[2], rtol=5e-3)
    okB &= conv and rat[2].max() < 1e3 and rat[2].min() > 1e-3
    rowsB.append(f"trial {trial}: omega/|K| -> {np.round(rat[2], 3)}")
# control: a Proca mass (not gauge invariant) gaps the photons
q = 0.01 * np.array([0.3, 0.5, 0.81]); N = null_space(photon_gauss(q)); m2 = 0.5
wp = np.sqrt(np.sort(np.linalg.eigvals(N.conj().T @ np.eye(9) @ N @ (N.conj().T @ (curl_blocks(q).conj().T @ curl_blocks(q) + m2 * np.eye(9)) @ N)).real))
okB &= wp.min() > 0.5
check("B: harmonic regime with local forms: a bounded local kinetic form, a finite-range potential in the curls (with higher-derivative kernels) and finite-range E-B cross terms all vanish or stay bounded so that every one of the six frequencies -> 0 as q -> 0 (no gap); a Proca mass, which is not gauge-invariant, gaps them; a non-local B(-Delta)^-1 B term would too and is excluded by locality",
      okB, "; ".join(rowsB) + f"; Proca control (m^2 = 0.5): lowest omega {wp.min():.3f}")


# ---------------------------------------------------------------- C: fixed photon-index projectors
def helicity2_projector(khat):
    kh = khat / np.linalg.norm(khat); a = np.array([1., 0, 0]) if abs(kh[0]) < 0.9 else np.array([0, 1., 0])
    u = np.cross(kh, a); u /= np.linalg.norm(u); v = np.cross(kh, u)
    T = [(np.outer(u, u) - np.outer(v, v)) / np.sqrt(2), (np.outer(u, v) + np.outer(v, u)) / np.sqrt(2)]
    B = np.array([t.reshape(-1) for t in T]).T
    return B @ B.T


ov = {}
for name, kh in (("q along z", np.array([0, 0, 1.])), ("q along x", np.array([1., 0, 0]))):
    kh_ = kh / np.linalg.norm(kh); Pt = np.eye(3) - np.outer(kh_, kh_); Pphys = np.kron(np.eye(3), Pt)
    Pz = np.zeros((9, 9)); Pz[6:9, 6:9] = np.eye(3)
    ov[name] = float(np.linalg.norm(helicity2_projector(kh) @ Pz @ Pphys))
check("C: fixed photon-index projectors: the photon-z block removes only partner weight for q along z but helicity-2 weight for q along x (a fixed-block overlap check; derivative-dependent or cubic-covariant selectors are not covered)",
      ov["q along z"] < 1e-12 and ov["q along x"] > 0.5, f"|P_helicity2 P_photon-z| on the physical modes: q along z {ov['q along z']:.2e}, q along x {ov['q along x']:.3f}")

# ---------------------------------------------------------------- D: constraint sets: physical / seen by E / invisible to E
sets = {"Gauss": [photon_gauss], "Gauss+rotation": [photon_gauss, rot_sym], "Gauss+rotation+trace": [photon_gauss, rot_sym, trace_sym],
        "Gauss+first-index": [photon_gauss, first_gauss], "Gauss+first-index+trace": [photon_gauss, first_gauss, trace_sym], "Gauss+trace": [photon_gauss, trace_sym]}
counts = {}
for name, cons in sets.items():
    out = set()
    for _ in range(15):
        q = rng.uniform(-np.pi, np.pi, 3); N = null_space(np.vstack([c(q) for c in cons]))
        img = np.linalg.matrix_rank(L_symbol(q) @ N, tol=1e-9) if N.shape[1] else 0
        out.add((N.shape[1], int(img), N.shape[1] - int(img)))
    counts[name] = out
# the surviving invisible mode under Gauss+rotation is the transverse trace K K^T - K^2 I
q = rng.uniform(-np.pi, np.pi, 3); K = 2 * np.sin(q / 2)
N = null_space(np.vstack([photon_gauss(q), rot_sym(q)])); ker = N @ null_space(L_symbol(q) @ N)
tt_tr = (np.outer(K, K) - (K @ K) * np.eye(3)).reshape(-1); tt_tr /= np.linalg.norm(tt_tr)
ov_tr = abs(np.vdot(tt_tr, ker[:, 0])) / np.linalg.norm(ker[:, 0])
# helicity +-1 content with the trace constraint alone
kh = K / np.linalg.norm(K); a_ = np.array([1., 0, 0]) if abs(kh[0]) < 0.9 else np.array([0, 1., 0]); u = np.cross(kh, a_); u /= np.linalg.norm(u); v = np.cross(kh, u)
H1 = np.array([np.outer(kh, (u + 1j * v) / np.sqrt(2)).ravel(), np.outer(kh, (u - 1j * v) / np.sqrt(2)).ravel()]).T
h1_trace = np.linalg.norm(H1.conj().T @ null_space(np.vstack([photon_gauss(q), trace_sym(q)])))
okD = (counts["Gauss"] == {(6, 3, 3)} and counts["Gauss+rotation"] == {(3, 2, 1)} and counts["Gauss+rotation+trace"] == {(2, 2, 0)}
       and counts["Gauss+first-index"] == {(4, 3, 1)} and counts["Gauss+first-index+trace"] == {(3, 3, 0)} and ov_tr > 1 - 1e-9 and h1_trace > 0.5)
# exact identification with the landed momentum rule on the symmetric embedding (4^3 torus)
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
    for j in range(3):
        r = 3 * ci[tuple((x + E3[j].astype(int)) % Lt)] + j
        Gland[r, lsl(x + E3[j].astype(int), j)] += 1; Gland[r, lsl(x, j)] -= 1
        for i in range(3):
            if i != j:
                f = FACE[tuple(sorted((i, j)))]; Gland[r, lsl(x, f)] += 1; Gland[r, lsl(x - E3[i].astype(int), f)] -= 1
ident = np.abs(Gauss_t @ P - Gland).max()
okD &= ident == 0
check("D: constraint sets (physical / seen by E / invisible to E): Gauss 6/3/3; +rotation 3/2/1, whose invisible mode is the transverse trace K K^T - K^2 I (a helicity-0 partner survives); +rotation+trace 2/2/0 (TT only); +first-index Gauss 4/3/1; +first-index Gauss+trace 3/3/0; +trace alone keeps helicity +-1; on the symmetric embedding the rotation-constrained Gauss laws are the landed momentum rule exactly",
      okD, f"counts {counts}; overlap of the surviving invisible mode with the transverse trace {ov_tr:.6f}; helicity +-1 weight with the trace constraint alone {h1_trace:.3f}; Gauss = landed momentum rule on the {Lt}^3 torus (max difference {ident:.0f})")


# ---------------------------------------------------------------- E: moves and their moments
def pos(x, l, j):
    return np.array(x, float) + s0 - E3[l] / 2 + E3[j] / 2


def rows_for(nb, which):
    box = list(itertools.product(range(nb), repeat=3))
    slots = [(c, l, j) for c in box for l in range(3) for j in range(3)]; sidx = {sl_: i for i, sl_ in enumerate(slots)}
    rows = []
    for x in itertools.product(range(-1, nb + 1), repeat=3):
        xa = np.array(x); ds = []
        if "gauss" in which:
            for l in range(3):
                d = {}
                for j in range(3):
                    d[(tuple(xa), l, j)] = d.get((tuple(xa), l, j), 0) + 1
                    d[(tuple(xa - E3[j].astype(int)), l, j)] = d.get((tuple(xa - E3[j].astype(int)), l, j), 0) - 1
                ds.append(d)
        if "rot" in which:
            for l in range(3):
                for j in range(3):
                    if l < j:
                        ds.append({(tuple(xa), l, j): 1, (tuple(xa + E3[j].astype(int) - E3[l].astype(int)), j, l): -1})
        if "first" in which:
            for j in range(3):
                d = {}
                for l in range(3):
                    y = tuple(xa + E3[l].astype(int)); d[(y, l, j)] = d.get((y, l, j), 0) + 1; d[(tuple(xa), l, j)] = d.get((tuple(xa), l, j), 0) - 1
                ds.append(d)
        if "trace" in which:
            ds.append({(tuple(xa), l, l): 1 for l in range(3)})
        for d in ds:
            row = [0] * len(slots); t = False
            for k, v in d.items():
                if k in sidx:
                    row[sidx[k]] += v; t = True
            if t and any(row):
                rows.append(row)
    return slots, rows


def int_kernel(nb, which):
    slots, rows = rows_for(nb, which)
    basis = []
    for v in sp.Matrix(rows).nullspace():
        den = sp.ilcm(*[sp.fraction(z)[1] for z in v]); w = np.array([int(z * den) for z in v]); basis.append(w // np.gcd.reduce(np.abs(w[w != 0])))
    return slots, (np.array(basis).T.astype(float) if basis else np.zeros((len(slots), 0)))


def float_kernel(nb, which):
    slots, rows = rows_for(nb, which)
    return slots, null_space(np.array(rows, float))


def moments(K_, slots):
    out0, out1, out2 = [], [], []
    for t in range(K_.shape[1]):
        m0 = np.zeros(9); m1 = np.zeros((9, 3)); m2 = np.zeros((9, 3, 3))
        for i, (c, l, j) in enumerate(slots):
            v = K_[i, t]
            if abs(v) > 1e-12:
                p = pos(c, l, j); m0[3 * l + j] += v; m1[3 * l + j] += v * p; m2[3 * l + j] += v * np.outer(p, p)
        out0.append(m0); out1.append(m1.ravel()); out2.append(m2.ravel())
    return np.array(out0), np.array(out1), np.array(out2)


def tt_visibility(M1):
    best = 0.0
    for _ in range(30):
        n = rng.normal(size=3); n /= np.linalg.norm(n); a = np.array([1., 0, 0]) if abs(n[0]) < 0.9 else np.array([0, 1., 0])
        u = np.cross(n, a); u /= np.linalg.norm(u); v = np.cross(n, u)
        for T in [(np.outer(u, u) - np.outer(v, v)) / np.sqrt(2), (np.outer(u, v) + np.outer(v, u)) / np.sqrt(2)]:
            for m in M1:
                best = max(best, abs(np.sum(T.reshape(-1) * (m.reshape(9, 3) @ n))))
    return best


resE = {}
for name, nb, which, kern in [("Gauss", 2, ("gauss",), int_kernel), ("Gauss+rotation", 3, ("gauss", "rot"), int_kernel), ("Gauss+rotation+trace", 4, ("gauss", "rot", "trace"), float_kernel),
                              ("Gauss+first-index", 3, ("gauss", "first"), int_kernel), ("Gauss+first-index+trace", 3, ("gauss", "first", "trace"), int_kernel)]:
    slots, Kb = kern(nb, which)
    m0, m1, m2 = moments(Kb, slots)
    r1 = np.linalg.matrix_rank(m1, tol=1e-8) if len(m1) else 0
    r2 = np.linalg.matrix_rank(m2, tol=1e-8) if len(m2) else 0
    antisym = None
    if r1 == 1:
        b = np.linalg.svd(m1)[2][0].reshape(3, 3, 3); antisym = np.abs(b + np.transpose(b, (1, 0, 2))).max() < 1e-9 and np.abs(b + np.transpose(b, (0, 2, 1))).max() < 1e-9
    resE[name] = dict(n=Kb.shape[1], m0=float(np.abs(m0).max()) if len(m0) else 0.0, r1=int(r1), r2=int(r2), tt=float(tt_visibility(m1)) if len(m1) else 0.0, antisym=antisym)
okE = (resE["Gauss"]["r1"] == 9 and resE["Gauss"]["tt"] > 0.1
       and resE["Gauss+rotation"]["r1"] == 0 and resE["Gauss+rotation"]["r2"] == 6
       and resE["Gauss+rotation+trace"]["n"] > 0 and resE["Gauss+rotation+trace"]["r1"] == 0 and resE["Gauss+rotation+trace"]["r2"] == 0
       and resE["Gauss+first-index"]["r1"] == 1 and resE["Gauss+first-index"]["antisym"] and resE["Gauss+first-index"]["tt"] < 1e-9
       and resE["Gauss+first-index+trace"]["r1"] == 1 and resE["Gauss+first-index+trace"]["tt"] < 1e-9
       and all(r["m0"] < 1e-9 for r in resE.values()))
check("E: moves (box kernels, moments at physical positions): Gauss only keeps TT-visible first moments (rank 9); +rotation loses zeroth and first moments (second-moment rank 6); +rotation+trace loses second moments too (4^3 box); +first-index Gauss keeps one first moment, totally antisymmetric (eps) and TT-invisible, with or without the trace",
      okE, "; ".join(f"{k}: {v['n']} moves, max|M0| {v['m0']:.0e}, rank M1 {v['r1']}, rank M2 {v['r2']}, TT-visible M1 {v['tt']:.2e}" + (f", eps-antisymmetric {v['antisym']}" if v['antisym'] is not None else "") for k, v in resE.items()))

# ---------------------------------------------------------------- F: all 15 cubic-covariant pointwise constraint sets
def mat(i, j):
    M = np.zeros((3, 3)); M[i, j] = 1; return M


irr = {"I": [np.eye(3).ravel() / np.sqrt(3)], "E": [np.diag([1, -1, 0.]).ravel() / np.sqrt(2), np.diag([1, 1, -2.]).ravel() / np.sqrt(6)],
       "T2": [((mat(i, j) + mat(j, i)) / np.sqrt(2)).ravel() for (i, j) in [(0, 1), (1, 2), (0, 2)]],
       "T1": [((mat(i, j) - mat(j, i)) / np.sqrt(2)).ravel() for (i, j) in [(0, 1), (1, 2), (0, 2)]]}


def crossm(c):
    return np.array([[0, -c[2], c[1]], [c[2], 0, -c[0]], [-c[1], c[0], 0]])


def nullsp_abs(M, tol=1e-9):
    u, s, vh = np.linalg.svd(M); r = int(np.sum(s > tol)); return vh[r:].conj().T


rowsF = []; okF = True
for r_ in range(1, 5):
    for combo in itertools.combinations(["I", "E", "T2", "T1"], r_):
        Wb = np.array([v for k in combo for v in irr[k]]).T; Pw = Wb @ Wb.T
        h1, tt = 0.0, 1.0
        for _ in range(8):
            n = rng.normal(size=3); n /= np.linalg.norm(n); a_ = np.array([1., 0, 0]) if abs(n[0]) < 0.9 else np.array([0, 1., 0])
            u = np.cross(n, a_); u /= np.linalg.norm(u); v = np.cross(n, u); ep = (u + 1j * v) / np.sqrt(2); em = (u - 1j * v) / np.sqrt(2)
            phys = nullsp_abs(np.vstack([np.kron(np.eye(3), n[None, :]), np.eye(9) - Pw]))
            H1 = np.array([np.outer(n, ep).ravel(), np.outer(n, em).ravel()]).T; TT = np.array([np.outer(ep, ep).ravel(), np.outer(em, em).ravel()]).T
            h1 = max(h1, np.linalg.norm(H1.conj().T @ phys) if phys.size else 0.0)
            tt = min(tt, np.linalg.norm(TT.conj().T @ phys) / np.sqrt(2) if phys.size else 0.0)
        cons = []
        for k in range(3):
            Mk = np.zeros((9, 9))
            for a in range(9):
                Bv = np.zeros(9); Bv[a] = 1; Mk[:, a] = (Bv.reshape(3, 3) @ crossm(np.eye(3)[k])).ravel()
            cons.append((np.eye(9) - Pw) @ Mk)
        dimB = nullsp_abs(np.vstack(cons)).shape[1]
        good = h1 < 1e-9 and tt > 1e-3
        if good:
            okF &= dimB == 0
        rowsF.append(f"{'+'.join(combo)}: helicity+-1 {'absent' if h1 < 1e-9 else 'present'}, TT {'present' if tt > 1e-3 else 'absent'}, first-moment dim {dimB}")
okF &= any("I+E+T2+T1" in r and "first-moment dim 9" in r for r in rowsF)
check("F: all 15 cubic-covariant pointwise constraint sets (unions of the irreps I, E, T2, T1 as allowed values, with the photon Gauss laws): every set that removes helicity +-1 and keeps a TT mode has no first-moment space; first moments need T1, which brings helicity +-1 back",
      okF, "; ".join(rowsF))


# ---------------------------------------------------------------- G: harmonic comparators on the full physical space
def rhat(Kmat, t, slots, q):
    out = np.zeros(9, complex)
    for i, (c, l, j) in enumerate(slots):
        v = Kmat[i, t]
        if abs(v) > 1e-12:
            out[3 * l + j] += v * np.exp(-1j * q @ pos(c, l, j))
    return out


slR, KR = int_kernel(3, ("gauss", "rot")); slRT, KRT = float_kernel(4, ("gauss", "rot", "trace"))
def comparator(cons, Kmat, slots, q):
    N = null_space(np.vstack([c(q) for c in cons]))                       # physical electric subspace (orthonormal)
    W = sum(np.outer(rhat(Kmat, t, slots, q), rhat(Kmat, t, slots, q).conj()) for t in range(Kmat.shape[1]))
    Kin = N.conj().T @ N                                                    # Maxwell-type kinetic |A~|^2
    Wred = N.conj().T @ W @ N
    return np.sqrt(np.maximum(np.sort(np.linalg.eigvals(Kin @ Wred).real), 0))
okG = True; rowsG = []
for n in [np.array([0, 0, 1.]), np.array([1, 1, 0.]) / np.sqrt(2), np.array([1, 1, 1.]) / np.sqrt(3)]:
    epsl = [0.2, 0.1, 0.05]
    oR = np.array([comparator([photon_gauss, rot_sym], KR, slR, e * n) for e in epsl]); oRT = np.array([comparator([photon_gauss, rot_sym, trace_sym], KRT, slRT, e * n) for e in epsl])
    Kn = [np.linalg.norm(2 * np.sin(e * n / 2)) for e in epsl]
    fR = [np.polyfit(np.log(Kn), np.log(oR[:, m]), 1)[0] for m in range(oR.shape[1])]
    fRT = [np.polyfit(np.log(Kn), np.log(oRT[:, m]), 1)[0] for m in range(oRT.shape[1])]
    okG &= len(fR) == 3 and all(abs(f - 2) < 0.05 for f in fR) and len(fRT) == 2 and all(abs(f - 3) < 0.1 for f in fRT)
    rowsG.append(f"n = {np.round(n, 2)}: +rotation exponents {np.round(fR, 3)}; +rotation+trace exponents {np.round(fRT, 3)}")
check("G: harmonic comparators on the full physical space (Maxwell-type kinetic term, box-kernel moves, no hand projection): +rotation, all three modes (TT and the transverse-trace partner) have omega ~ q^2; +rotation+trace, both TT modes have omega ~ q^3",
      okG, "; ".join(rowsG))

print("N5 resolution 1: keeping the composite exactly symmetric with G E = 0 is the same as keeping each photon's Gauss law exact (row-for-row identity).")
print("N5 resolution 2: with local bounded forms (cross terms included) no harmonic term gaps the partners; non-local or gauge-breaking masses would.")
print("N5 resolution 3: every tested local constraint set that removes the helicity +-1 partners leaves no TT-visible first moment: the rotation constraint (a helicity-0 partner survives), rotation + trace (TT only, O(q^3) form factors), the first-index Gauss law (with or without trace; antisymmetric first moment), and all cubic-covariant pointwise sets. Pre-registered outcome FAIL.")
print("per_element: the row identity at 37 momenta; each box-kernel move's moments.")
print("per_site: every constraint row touching the boxes (2^3 to 4^3 cells).")
print("per_mode: six photon-triplet modes for 5 random local forms; the constrained comparators' modes in three directions at three momenta.")
print("per_block: the box kernels for five constraint sets; 15 pointwise constraint sets.")
print("lattice_wide: resolves the symbol identities (A, D) at every sampled zone momentum and the moment statements as exact algebra independent of box size for the rotation and first-index families; checked and not executed - non-harmonic phases, derivative or non-linear constraint sets beyond those tested, other composites.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
