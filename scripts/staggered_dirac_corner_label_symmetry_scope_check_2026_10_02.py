#!/usr/bin/env python3
"""Corner-label symmetry scope check for the Block 03 Kawamoto-Smit operator.

Exact integer linear algebra on the 4^3 torus (64 sites) and on the
eight-dimensional carrier of 2-periodic functions (the eight corner plane
waves). Plane waves are handled exactly in Z[w], w = exp(i pi/4).

It checks which lattice operators behind the hw=1 corner-label M_3(C)
algebra are symmetries of the staggered operator D:
  - D moves momentum k to k + pi zeta_mu; only D^2 is diagonal;
  - the translation symmetries S_a of D pairwise anticommute;
  - at most one plain translation commutes with D in every plane-wave
    representative of the single gauge class;
  - the bare axis cycle is a symmetry in the cyclic representative, while
    in eta^0 its covering symmetry does not preserve the hw=1 corner span;
  - the covering rotation symmetries form a representation of the proper
    cubic group with corner character (8, 2, 0, 4, 0);
  - a gauge transform (-1)^(c.x) inside the class relabels n -> n xor c;
  - the cell-momentum sectors K = pi e_a sit at |E| = 1.

Companion: docs/STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md
"""
from __future__ import annotations

import os

for _thread_key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_thread_key] = "1"

import sys
from collections import Counter
from itertools import combinations, permutations, product
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ("docs/STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md",)

ROOT = Path(__file__).resolve().parents[1]
L = 4
N = L ** 3
X = np.array([(x1, x2, x3) for x3 in range(L) for x2 in range(L) for x1 in range(L)], dtype=np.int64)
I64 = np.eye(N, dtype=np.int64)
E = np.eye(3, dtype=np.int64)

ZETA_ETA0 = ((0, 0, 0), (1, 0, 0), (1, 1, 0))  # eta_1 = 1, eta_2 = (-1)^x1, eta_3 = (-1)^(x1+x2)
ZETA_CYCLIC = ((0, 1, 0), (0, 0, 1), (1, 0, 0))  # eta_1 = (-1)^x2, eta_2 = (-1)^x3, eta_3 = (-1)^x1

LABELS = [(n1, n2, n3) for n3 in (0, 1) for n2 in (0, 1) for n1 in (0, 1)]
LAB = {n: i for i, n in enumerate(LABELS)}
L1 = [n for n in LABELS if sum(n) == 1]
L2 = [n for n in LABELS if sum(n) == 2]

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" ({detail})" if detail else ""))


def idx(x) -> int:
    return int(x[0] % L) + L * int(x[1] % L) + L * L * int(x[2] % L)


def xor(a, b):
    return tuple((p + q) % 2 for p, q in zip(a, b))


def translation(mu: int, apbc: bool = False) -> np.ndarray:
    """(T_mu psi)(x) = psi(x + e_mu); APBC puts -1 on the wrap links."""
    t = np.zeros((N, N), dtype=np.int64)
    for i, x in enumerate(X):
        sign = -1 if (apbc and x[mu] == L - 1) else 1
        t[i, idx(x + E[mu])] = sign
    return t


T = [translation(mu) for mu in range(3)]
TA = [translation(mu, apbc=True) for mu in range(3)]


def eta_field(zeta) -> np.ndarray:
    return (-1) ** (X @ np.array(zeta, dtype=np.int64))


def two_d(etas, trans=T) -> np.ndarray:
    """2D = sum_mu (diag(eta_mu) T_mu - T_mu^-1 diag(eta_mu))."""
    m = sum(eta[:, None] * trans[mu] for mu, eta in enumerate(etas))
    return m - m.T


def two_d_zeta(zetas, trans=T) -> np.ndarray:
    return two_d([eta_field(z) for z in zetas], trans)


def plaquettes_minus_one(etas) -> bool:
    for x in X:
        for mu, nu in combinations(range(3), 2):
            prod_ = (etas[mu][idx(x)] * etas[nu][idx(x + E[mu])]
                     * etas[mu][idx(x + E[nu])] * etas[nu][idx(x)])
            if prod_ != -1:
                return False
    return True


def straight_holonomies_plus_one(etas) -> bool:
    for mu in range(3):
        for x in X[X[:, mu] == 0]:
            h = 1
            for t in range(L):
                h *= etas[mu][idx(x + t * E[mu])]
            if h != 1:
                return False
    return True


def commutes(a: np.ndarray, b: np.ndarray) -> bool:
    return np.array_equal(a @ b, b @ a)


def solve_sign_field(a: np.ndarray, b: np.ndarray):
    """Sign field g with g(0) = 1 and diag(g) a diag(g) = b, else None."""
    if not np.array_equal(np.abs(a), np.abs(b)):
        return None
    g = np.zeros(N, dtype=np.int64)
    g[0] = 1
    queue = [0]
    while queue:
        i = queue.pop()
        for j in np.nonzero(a[i])[0]:
            want = g[i] * a[i, j] * b[i, j]
            if g[j] == 0:
                g[j] = want
                queue.append(int(j))
            elif g[j] != want:
                return None
    if np.any(g == 0) or not np.array_equal(g[:, None] * a * g[None, :], b):
        return None
    return g


# Corner carrier: 2-periodic functions, J f(x) = f(x mod 2).
J = np.zeros((N, 8), dtype=np.int64)
for i, x in enumerate(X):
    J[i, LAB[tuple(int(c) % 2 for c in x)]] = 1
H8 = np.array([[(-1) ** (np.dot(n, s)) for s in LABELS] for n in LABELS], dtype=np.int64)


def corner_vector(n) -> np.ndarray:
    return (-1) ** (X @ np.array(n, dtype=np.int64))


def restrict(op: np.ndarray):
    """Exact restriction to the corner carrier in the cell-site basis.

    Returns the 8x8 integer matrix r8 with op J = J r8, or None if op does
    not preserve the carrier of 2-periodic functions.
    """
    r = J.T @ op @ J
    if np.any(r % 8):
        return None
    r8 = r // 8
    if not np.array_equal(op @ J, J @ r8):
        return None
    return r8


def label8(op: np.ndarray):
    """8 x (matrix of op in the corner basis): op v_n = sum_n' (M[n', n] / 8) v_n'."""
    r8 = restrict(op)
    return None if r8 is None else H8 @ r8 @ H8


def label_perm_matrix(f) -> np.ndarray:
    m = np.zeros((8, 8), dtype=np.int64)
    for n in LABELS:
        m[LAB[f(n)], LAB[n]] = 1
    return m


def span_invariant(lab: np.ndarray, labels) -> bool:
    cols = [LAB[n] for n in labels]
    rows = [i for i in range(8) if i not in cols]
    return not np.any(lab[np.ix_(rows, cols)])


# ---------- exact plane waves in Z[w], w = exp(i pi/4), w^4 = -1 ----------
def w_power(exps: np.ndarray) -> np.ndarray:
    exps = exps % 8
    v = np.zeros((4, len(exps)), dtype=np.int64)
    for j in range(8):
        sel = exps == j
        v[j % 4, sel] = 1 if j < 4 else -1
    return v


def w_scalar(e: int) -> np.ndarray:
    return w_power(np.array([e]))[:, 0]


def w_mul(c: np.ndarray, v: np.ndarray) -> np.ndarray:
    out = np.zeros_like(v)
    for i in range(4):
        for l in range(4):
            if i + l < 4:
                out[i + l] += c[i] * v[l]
            else:
                out[i + l - 4] -= c[i] * v[l]
    return out


def plane_wave(e) -> np.ndarray:
    """psi_k(x) = w^(e.x), i.e. exp(i k_mu) = w^(e_mu)."""
    return w_power(X @ np.array(e, dtype=np.int64))


def hop_identity(d2: np.ndarray, zetas, momenta) -> bool:
    """2D psi_k = sum_mu (2i sin k_mu) psi_(k + pi zeta_mu), exactly."""
    for e in momenta:
        lhs = plane_wave(e) @ d2.T
        rhs = np.zeros_like(lhs)
        for mu in range(3):
            c = w_scalar(e[mu]) - w_scalar(-e[mu])
            shifted = tuple(e[nu] + 4 * zetas[mu][nu] for nu in range(3))
            rhs += w_mul(c, plane_wave(shifted))
        if not np.array_equal(lhs, rhs):
            return False
    return True


def section_construction():
    print("== Construction on the 4^3 torus ==")
    d0, dc = two_d_zeta(ZETA_ETA0), two_d_zeta(ZETA_CYCLIC)
    for name, d, z in (("eta^0", d0, ZETA_ETA0), ("cyclic", dc, ZETA_CYCLIC)):
        etas = [eta_field(zz) for zz in z]
        ok = (np.array_equal(d, -d.T) and set(np.unique(d)) <= {-1, 0, 1}
              and np.all(np.count_nonzero(d, axis=1) == 6))
        check(f"{name}: 2D antisymmetric, entries in {{0,+-1}}, 6 links per site", ok)
        check(f"{name}: all 192 plaquettes carry -1, straight loops carry +1",
              plaquettes_minus_one(etas) and straight_holonomies_plus_one(etas))
        lap = sum(T[mu] @ T[mu] + T[mu].T @ T[mu].T - 2 * I64 for mu in range(3))
        check(f"{name}: (2D)^2 = sum_mu (T_mu^2 + T_mu^-2 - 2), diagonal on plane waves",
              np.array_equal(d @ d, lap))
        check(f"{name}: 2D J = 0 (D vanishes on the eight corner plane waves)",
              not np.any(d @ J))
    periodic = [tuple(2 * m for m in ms) for ms in product(range(4), repeat=3)]
    ok = hop_identity(d0, ZETA_ETA0, periodic)
    moving = sum(1 for e in periodic if any((e[mu] // 2) % 2 for mu in (1, 2)))
    check("eta^0 periodic: 2D psi_k = sum_mu 2i sin(k_mu) psi_(k+pi zeta_mu), all 64 k",
          ok and moving == 48, f"D moves momentum for {moving}/64 k")
    d0a = two_d_zeta(ZETA_ETA0, TA)
    apbc = [tuple(2 * m + 1 for m in ms) for ms in product(range(4), repeat=3)]
    ok = hop_identity(d0a, ZETA_ETA0, apbc)
    check("eta^0 APBC: same hop identity for all 64 momenta (2m+1)pi/4, labels n -> n xor zeta_mu",
          ok)
    check("eta^0 APBC: (2D)^2 = -6 I, no zero modes, every mode at |q_mu| = pi/4 from a corner",
          np.array_equal(d0a @ d0a, -6 * I64))
    ok = all(np.array_equal(eta_field(z) * corner_vector(n), corner_vector(xor(n, z)))
             for z in ZETA_ETA0 + ZETA_CYCLIC for n in LABELS)
    check("eta_mu v_n = v_(n xor zeta_mu) for all corners and both representatives", ok)
    return d0, dc


def section_shift_symmetries(d0):
    print("== Translation symmetries of D in eta^0 ==")
    b = [(0, 1, 1), (0, 0, 1), (0, 0, 0)]
    s = [corner_vector(bb)[:, None] * T[a] for a, bb in enumerate(b)]
    check("S_a = (-1)^(b_a.x) T_a with b = (011, 001, 000) commute with 2D",
          all(commutes(sa, d0) for sa in s))
    anti64 = all(not np.any(s[a] @ s[c] + s[c] @ s[a]) for a, c in combinations(range(3), 2))
    s8 = [restrict(sa) for sa in s]
    anti8 = all(m is not None for m in s8) and all(
        not np.any(s8[a] @ s8[c] + s8[c] @ s8[a]) for a, c in combinations(range(3), 2))
    check("S_a S_b = -S_b S_a for a != b, on the torus and on the corner carrier",
          anti64 and anti8, "no joint eigenvector of two of them")
    uniq = True
    for a in range(3):
        g = solve_sign_field(d0, T[a] @ d0 @ T[a].T)
        uniq &= g is not None and np.array_equal(g, corner_vector(b[a]))
    check("link solve: sign fields s with [s T_a, D] = 0 are exactly +-(-1)^(b_a.x)", uniq)
    sq = [sa @ sa for sa in s]
    ok = (all(commutes(q, d0) for q in sq) and all(commutes(p, q) for p, q in combinations(sq, 2))
          and all(np.array_equal(q @ J, J) for q in sq))
    check("two-site translations S_a^2 commute with D and each other, act as +1 on corners", ok)
    ok = all(np.array_equal(label8(s[a]), 8 * np.array(
        [[(-1) ** n[a] if m == xor(n, b[a]) else 0 for n in LABELS] for m in LABELS]))
        for a in range(3))
    check("S_a v_n = (-1)^(n_a) v_(n xor b_a): S_1, S_2 move corner labels", ok)
    moved = all(not set(xor(n, bb) for n in L1) <= set(L1) for bb in LABELS if any(bb))
    check("no nonzero b maps the hw=1 labels into themselves (all 7 checked)", moved)
    return b


def section_plain_translations(d0, dc):
    print("== Plain translations and the corner-label algebra ==")
    comm = [d0 @ T[a] - T[a] @ d0 for a in range(3)]
    ok = (not np.any(comm[2]) and all(np.any(comm[a]) and np.max(np.abs(comm[a])) == 2 for a in (0, 1)))
    check("eta^0: [T_3, 2D] = 0, [T_1, 2D] and [T_2, 2D] nonzero with max |entry| 2", ok)
    check("cyclic: no plain translation commutes with 2D",
          all(not commutes(T[a], dc) for a in range(3)))
    t_lab = [label8(T[mu]) for mu in range(3)]
    ok = all(m is not None and np.array_equal(m, 8 * np.diag([(-1) ** n[mu] for n in LABELS]))
        for mu, m in enumerate(t_lab))
    check("H_8 T_mu|_8 H_8 = 8 diag((-1)^(n_mu)): plain translations give the corner characters", ok)
    counts = Counter()
    gauge_ok = lift_ok = True
    zero_rows = Counter()
    for bits in product((0, 1), repeat=6):
        z = [[0] * 3 for _ in range(3)]
        for (mu, nu), bit in zip(combinations(range(3), 2), bits[:3]):
            z[mu][nu], z[nu][mu] = bit, 1 - bit
        for mu in range(3):
            z[mu][mu] = bits[3 + mu]
        d = two_d_zeta(z)
        gauge_ok &= solve_sign_field(d0, d) is not None
        counts[sum(commutes(T[a], d) for a in range(3))] += 1
        zero_rows[sum(not any(z[mu]) for mu in range(3))] += 1
        lifts = [corner_vector([z[nu][a] for nu in range(3)])[:, None] * T[a] for a in range(3)]
        lift_ok &= all(commutes(sa, d) for sa in lifts) and all(
            not np.any(lifts[a] @ lifts[c] + lifts[c] @ lifts[a]) for a, c in combinations(range(3), 2))
    check("all 64 plane-wave representatives are sign-gauge transforms of eta^0 on the torus", gauge_ok)
    check("commuting plain translations per representative: 0 in 40, 1 in 24, 2+ in 0",
          dict(counts) == {0: 40, 1: 24}, f"{dict(sorted(counts.items()))}")
    check("at most one zeta_mu is zero in every representative, so D moves labels in 2+ directions",
          max(zero_rows) <= 1, f"{dict(sorted(zero_rows.items()))}")
    check("in every representative the lifts S_a (b_nu = (zeta_nu)_a) commute with D and anticommute",
          lift_ok)
    pc = rotation_perm(np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]))
    c_lab = label8(pc)
    cyc = label_perm_matrix(lambda n: (n[2], n[0], n[1]))
    rows = [LAB[n] for n in L1]
    t3 = [m[np.ix_(rows, rows)] // 8 for m in t_lab]
    c3 = c_lab[np.ix_(rows, rows)] // 8
    chars = {tuple(int(m[i, i]) for m in t3) for i in range(3)}
    proj = []
    for i in range(3):
        p = np.eye(3, dtype=np.int64)
        for m in t3:
            p = p @ (np.eye(3, dtype=np.int64) + int(m[i, i]) * m)
        proj.append(p)  # 8 P_i
    units = all(any(np.array_equal(proj[i] @ np.linalg.matrix_power(c3, k) @ proj[j],
                                   64 * np.eye(3, dtype=np.int64)[:, [i]] @ np.eye(3, dtype=np.int64)[[j], :])
                    for k in range(3)) for i in range(3) for j in range(3))
    cyc3 = {i: int(np.nonzero(c3[:, i])[0][0]) for i in range(3)}
    no_sub = not [S for r in (1, 2) for S in combinations(range(3), r) if {cyc3[i] for i in S} == set(S)]
    ok = (np.array_equal(c_lab, 8 * cyc) and len(chars) == 3
          and all(np.array_equal(p, 8 * np.diag(np.eye(3, dtype=np.int64)[i])) for i, p in enumerate(proj))
          and units and no_sub)
    check("hw=1 labels: plain characters + bare cycle give all 9 matrix units, no proper invariant subset",
          ok, "M_3(C) on labels")
    return pc


def rotation_perm(r: np.ndarray) -> np.ndarray:
    """(P_R psi)(y) = psi(R^-1 y) on the 4^3 torus."""
    p = np.zeros((N, N), dtype=np.int64)
    rinv = r.T
    for i, y in enumerate(X):
        p[i, idx(rinv @ y)] = 1
    return p


def section_c3(d0, dc, pc):
    print("== The axis cycle C_3[111]: x -> (x3, x1, x2) ==")
    c_lab = label8(pc)
    ok = (commutes(pc, dc) and np.array_equal(np.linalg.matrix_power(pc, 3), I64)
          and np.array_equal(c_lab, 8 * label_perm_matrix(lambda n: (n[2], n[0], n[1]))))
    check("cyclic representative: P_C commutes with 2D, P_C^3 = 1, acts on labels as the bare cycle", ok)
    gc = (-1) ** (X[:, 0] * X[:, 1] + X[:, 0] * X[:, 2])
    wc = gc[:, None] * pc
    check("eta^0: P_C does not commute with 2D; W_C = (-1)^(y1 y2 + y1 y3) P_C does",
          (not commutes(pc, d0)) and commutes(wc, d0))
    lhs = 2 * (wc @ corner_vector((1, 0, 0)))
    rhs = (corner_vector((0, 1, 0)) + corner_vector((0, 0, 1))
           + corner_vector((1, 1, 0)) - corner_vector((1, 0, 1)))
    wl = label8(wc)
    check("eta^0: 2 W_C v_100 = v_010 + v_001 + v_110 - v_101; W_C does not preserve the hw=1 span",
          np.array_equal(lhs, rhs) and wl is not None and not span_invariant(wl, L1))


def section_rotations(d0):
    print("== Covering rotation symmetries of D in eta^0 ==")
    rots = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            r = np.zeros((3, 3), dtype=np.int64)
            for i, j in enumerate(perm):
                r[i, j] = signs[i]
            if round(np.linalg.det(r)) == 1:
                rots.append(r)
    w = {}
    ok = len(rots) == 24
    for r in rots:
        p = rotation_perm(r)
        g = solve_sign_field(d0, p @ d0 @ p.T)
        ok &= g is not None
        if g is not None:
            w[r.tobytes()] = (r, g, p)
    check("each of the 24 proper rotations has a covering sign field g_R, g_R(0) = 1", ok)
    y1, y2, y3 = X[:, 0], X[:, 1], X[:, 2]
    closed = [
        (np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]), (-1) ** (y1 * y2 + y1)),
        (np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]]), (-1) ** (y1 + y2)),
        (np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]), (-1) ** (y1 * y2 + y1 * y3)),
        (np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]]), (-1) ** (y1 * y2 + y3)),
    ]
    check("closed forms: C4z (-1)^(y1y2+y1), C2z (-1)^(y1+y2), C3 (-1)^(y1y2+y1y3), C2'(110) (-1)^(y1y2+y3)",
          all(np.array_equal(w[r.astype(np.int64).tobytes()][1], g) for r, g in closed))
    perms = {}
    for key, (r, g, p) in w.items():
        perms[key] = (np.array([idx(r.T @ y) for y in X]), g)
    law = True
    for (ka, (ra, _, _)), (kb, (rb, _, _)) in product(w.items(), repeat=2):
        pa, ga = perms[ka]
        pb, gb = perms[kb]
        pab, gab = perms[(ra @ rb).tobytes()]
        # (W_A W_B psi)(y) = g_A(y) g_B(A^-1 y) psi((AB)^-1 y)
        law &= np.array_equal(pb[pa], pab) and np.array_equal(ga * gb[pa], gab)
    check("group law W_R W_S = W_RS for all 576 pairs (no projective sign)", law)
    period = all(np.array_equal(g, g[[idx(y % 2) for y in X]]) for _, g, _ in w.values())
    check("every covering sign field g_R is 2-periodic (preserves the corner carrier)", period)
    classes = {"E": [], "8C3": [], "3C2": [], "6C4": [], "6C2'": []}
    for r, g, p in w.values():
        tr_r = int(np.trace(r))
        name = {3: "E", 0: "8C3", 1: "6C4"}.get(tr_r) or ("3C2" if np.count_nonzero(r - np.diag(np.diag(r))) == 0 else "6C2'")
        classes[name].append(int(np.trace(restrict(g[:, None] * p))))
    chi = tuple(sorted(set(v)) for v in classes.values())
    sizes = tuple(len(v) for v in classes.values())
    flat = tuple(v[0] for v in chi) if all(len(v) == 1 for v in chi) else None
    table = {"A1": (1, 1, 1, 1, 1), "A2": (1, 1, 1, -1, -1), "E": (2, -1, 2, 0, 0),
             "T1": (3, 0, -1, 1, -1), "T2": (3, 0, -1, -1, 1)}
    mult = {k: sum(s * c * v for s, c, v in zip(sizes, flat, row)) // 24 for k, row in table.items()} if flat else {}
    check("corner character by class (E, 8C3, 3C2, 6C4, 6C2') = (8, 2, 0, 4, 0) = 2 A1 + 2 T1",
          sizes == (1, 8, 3, 6, 6) and flat == (8, 2, 0, 4, 0)
          and mult == {"A1": 2, "A2": 0, "E": 0, "T1": 2, "T2": 0}, f"{flat}")


def section_hamming(d0):
    print("== Hamming labels relative to the representative ==")
    eps = corner_vector((1, 1, 1))
    ok = (np.array_equal(eps[:, None] * d0 * eps[None, :], -d0)
          and all(np.array_equal(eps * corner_vector(n), corner_vector(xor(n, (1, 1, 1)))) for n in LABELS)
          and {xor(n, (1, 1, 1)) for n in L1} == set(L2))
    check("epsilon 2D epsilon = -2D, epsilon v_n = v_(n xor 111): hw=1 labels -> hw=2 labels", ok)
    etas0 = [eta_field(z) for z in ZETA_ETA0]
    ok = True
    multisets = {}
    for c in LABELS:
        gc = corner_vector(c)
        etas_c = [(-1) ** c[mu] * etas0[mu] for mu in range(3)]
        ok &= np.array_equal(gc[:, None] * d0 * gc[None, :], two_d(etas_c))
        ok &= plaquettes_minus_one(etas_c)
        ok &= all(np.array_equal(gc * corner_vector(n), corner_vector(xor(n, c))) for n in LABELS)
        multisets[c] = tuple(sorted(sum(xor(n, c)) for n in L1))
    check("all 8 gauge transforms (-1)^(c.x): give eta^c = (-1)^(c_mu) eta^0, cocycle -1, v_n -> v_(n xor c)", ok)
    expect = {c: ((1, 1, 1) if sum(c) == 0 else (0, 2, 2) if sum(c) == 1
                  else (1, 1, 3) if sum(c) == 2 else (2, 2, 2)) for c in LABELS}
    check("hw multiset of the relabelled hw=1 set: 000 {1,1,1}; hw1 {0,2,2}; hw2 {1,1,3}; 111 {2,2,2}",
          multisets == expect)
    diffs = {c: {xor(xor(n, c), xor(m, c)) for n in L1 for m in L1} for c in LABELS}
    check("difference set {n xor n'} = {000, 011, 101, 110} is the same for every c",
          all(v == {(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)} for v in diffs.values()))


def section_cell_sectors(d0):
    print("== Cell-momentum sectors (two-site cells) in eta^0 ==")
    sq = [T[b] @ T[b] for b in range(3)]

    def p8(signs):
        p = I64.copy()
        for s, q in zip(signs, sq):
            p = p @ (I64 + s * q)
        return p  # 8 P_K

    p0 = p8((1, 1, 1))
    ok = np.array_equal(p0, J @ J.T) and not np.any(d0 @ p0)
    for signs in product((1, -1), repeat=3):
        p = p8(signs)
        ok &= np.array_equal(d0 @ d0 @ p, -4 * signs.count(-1) * p)
    check("K = 0 sector is the corner carrier (8 P_0 = J J^T); D^2 = -|K| on all 8 cell sectors, so ker D = carrier",
          ok)
    ok = all(commutes(q, d0) for q in sq)
    for a in range(3):
        signs = tuple(-1 if b == a else 1 for b in range(3))
        p = p8(signs)
        ok &= int(np.trace(p)) == 64 and np.array_equal(d0 @ d0 @ p, -4 * p)
        ok &= int(np.trace(d0 @ p)) == 0
        ok &= all(np.array_equal(sq[b] @ p, signs[b] * p) for b in range(3))
    check("K = pi e_a: 8-dim sectors with D^2 = -1 (iD = +-1, 4 + 4), two-site translations give the diagonal triple",
          ok)


REQUIRED_PHRASES = (
    "BZ-corner Hamming parity with the K-S",
    "parity-to-chirality identification is a separate bridge",
    "As a set they are not symmetries of the Block 03 Kawamoto-Smit operator",
    "Hamming weight is relative to a representative",
    "relabels n → n xor c",
    "anticommute pairwise and have no joint characters",
)
FORBIDDEN_PHRASES = (
    "decompose UNIQUELY",
    "There is no convention freedom in the Hamming-weight assignment",
    "is diagonalized in momentum space at the",
    "The three lattice translations `T_x, T_y, T_z` act on the hw=1 triplet",
    "If a quotient claims to preserve any exact retained operator",
    "Block 03 → unique K-S kinetic operator",
    "Sublattice A (chirality +)",
    "Sublattice B (chirality",
    "sublattice A: hw even",
    "sublattice B: hw odd",
    "Hamming-weight grading + sublattice parity",
)


def section_source_firewall() -> None:
    print("== Source firewall on the companion note ==")
    text = " ".join((ROOT / AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8").split())
    missing = [ph for ph in REQUIRED_PHRASES if ph not in text]
    present = [ph for ph in FORBIDDEN_PHRASES if ph in text]
    check("note keeps the epsilon fence and states the operator scope and gauge relabelling",
          not missing, f"missing {missing}" if missing else "")
    check("note carries none of the withdrawn uniqueness, diagonalization or parity wording",
          not present, f"present {present}" if present else "")


def main() -> int:
    d0, dc = section_construction()
    section_shift_symmetries(d0)
    pc = section_plain_translations(d0, dc)
    section_c3(d0, dc, pc)
    section_rotations(d0)
    section_hamming(d0)
    section_cell_sectors(d0)
    section_source_firewall()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
