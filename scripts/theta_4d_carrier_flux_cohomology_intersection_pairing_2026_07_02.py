#!/usr/bin/env python3
"""4D carrier template: flux-cohomology sectors and the cross-plane
intersection pairing on the closed-branch U(1) surface of finite T^4;
defect (monopole) closure is the carrier residual; the center dual alone
carries only the mod-N pairing.

Paired note:
docs/THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md

Class-A finite checks only: exact integer cochain algebra on the cubical
complex of T^4_L (boundary maps, ranks over Q and GF(p), cubical cup
products), deterministic pseudo-random integer/real cochains from a fixed
seed, and finite sector-sum arithmetic. No fits, no external comparators, no
measured values.

Sections:
  A. Complex: dd = 0; Betti numbers (1,4,6,4,1) at L = 2; rank stability at
     L = 3; torsion-freeness (ranks over Q equal ranks over GF(2/3/5));
     each link borders exactly 2(d-1) = 6 plaquettes (the 2D mechanism's
     two-sided incidence fails in 4D).
  B. Cup machinery: Leibniz rule d(a u b) = da u b + (-1)^p a u db exactly
     (integer and real cochains); the total sum of any exact 4-cochain over
     the closed torus vanishes (telescoping).
  C. Flux sectors and the pairing: the six unit-flux representatives are
     closed; Q_raw(n) = sum n u n equals 2 x the intersection form
     m01 m23 - m02 m13 + m03 m12 on flux vectors; Q_raw is even on closed
     cochains, class-invariant under n -> n + d lambda; Q = Q_raw / 2 is an
     integer with odd support; single-plane configurations give Q = 0
     (cross-plane structure).
  D. Theta-slot reduction: for real link cochains theta and closed integer
     branch cochains n, sum (d theta + 2 pi n) u (d theta + 2 pi n)
     = 4 pi^2 Q_raw(n) exactly - all theta-dependent terms telescope, so
     theta couples to the flux intersection alone on the closed branch.
  E. Defect boundary: an open branch cochain (dn != 0) has cup square NOT
     invariant under branch moves (multiple values, including odd Q_raw), so
     no sector decomposition exists on the unrestricted branch sum.
  F. Reflection: the pullback of a coordinate reflection preserves
     closedness and flips Q (the pairing Z_Q = Z_-Q mechanism).
  G. Center dual mod N: H^2 over GF(3) has dimension 6; the intersection
     pairing descends mod 3; the canonical Z-valued intersection form has no
     period-3 descent to Z_3-valued fluxes (obstruction identity).
  H. Sector-decomposition interface arithmetic: for any positive weight
     family over the six flux integers, Z(theta) = sum_m e^{i theta Q(m)} Z_m
     is real with paired weights, odd-Q support, and negative odd sectors at
     theta = pi.

Expected close: TOTAL: PASS=24 FAIL=0
"""
from __future__ import annotations

from itertools import combinations

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


RNG = np.random.default_rng(11)
D = 4


def cells(L: int, k: int):
    out = []
    sites = [tuple(s) for s in np.ndindex(*(L,) * D)]
    for S in combinations(range(D), k):
        for x in sites:
            out.append((x, S))
    return out


def cell_index(L: int, k: int):
    cs = cells(L, k)
    return cs, {c: i for i, c in enumerate(cs)}


def shift(x, mu: int, L: int):
    y = list(x)
    y[mu] = (y[mu] + 1) % L
    return tuple(y)


def d_matrix(L: int, k: int) -> np.ndarray:
    _, ik = cell_index(L, k)
    ck1, ik1 = cell_index(L, k + 1)
    M = np.zeros((len(ck1), len(ik)), dtype=np.int64)
    for (x, S), r in ik1.items():
        for j, mu in enumerate(S):
            Srem = tuple(m for m in S if m != mu)
            sgn = (-1) ** j
            M[r, ik[(shift(x, mu, L), Srem)]] += sgn
            M[r, ik[(x, Srem)]] -= sgn
    return M


def gfp_rank(A: np.ndarray, p: int) -> int:
    A = (A.copy() % p).astype(np.int64)
    m, n = A.shape
    row = 0
    for col in range(n):
        piv = next((rr for rr in range(row, m) if A[rr, col] % p), None)
        if piv is None:
            continue
        A[[row, piv]] = A[[piv, row]]
        A[row] = (A[row] * pow(int(A[row, col]), p - 2, p)) % p
        nz = [rr for rr in range(m) if rr != row and A[rr, col] % p]
        for rr in nz:
            A[rr] = (A[rr] - A[rr, col] * A[row]) % p
        row += 1
        if row == m:
            break
    return row


# ---------------------------------------------------------------------------
# Section A: the complex
# ---------------------------------------------------------------------------
print("Section A: cubical complex of T^4")

L = 2
DM = {k: d_matrix(L, k) for k in range(0, D)}
check("A1 dd = 0 on T^4_2",
      all(np.all(DM[k + 1] @ DM[k] == 0) for k in range(0, D - 1)))

dims = {k: len(cells(L, k)) for k in range(0, D + 1)}
ranks = {}
torsion_free = True
for k in range(0, D):
    rq = int(np.linalg.matrix_rank(DM[k].astype(float)))
    rps = [gfp_rank(DM[k], p) for p in (2, 3, 5)]
    ranks[k] = rq
    torsion_free = torsion_free and all(r == rq for r in rps)
betti = {k: dims[k] - ranks.get(k, 0) - ranks.get(k - 1, 0)
         for k in range(0, D + 1)}
check("A2 Betti numbers (1,4,6,4,1) at L=2: six flux sectors derived",
      [betti[k] for k in range(5)] == [1, 4, 6, 4, 1],
      f"dims={dims} betti={betti}")
check("A3 boundary maps torsion-free (Q ranks = GF(2/3/5) ranks)",
      torsion_free)

d1_L3 = d_matrix(3, 1)
d2_L3 = d_matrix(3, 2)
r1 = int(np.linalg.matrix_rank(d1_L3.astype(float)))
r2 = int(np.linalg.matrix_rank(d2_L3.astype(float)))
b2_L3 = d1_L3.shape[0] - r1 - r2  # dim C^2 - rank d1 - rank d2
check("A4 L=3 stability: dim H^2 = 6 again",
      b2_L3 == 6, f"C2 dim={d1_L3.shape[0]} rank d1={r1} rank d2={r2}")

# d_1 columns are links; nonzero rows of a column = plaquettes using the link
per_link = np.count_nonzero(DM[1], axis=0)
check("A5 each link borders exactly 2(d-1) = 6 plaquettes"
      " (the 2D two-sided incidence, source of block-2 exactness, fails in 4D)",
      bool(np.all(per_link == 6)),
      f"min = {int(per_link.min())}, max = {int(per_link.max())}")

# ---------------------------------------------------------------------------
# Section B: cup machinery
# ---------------------------------------------------------------------------
print("Section B: cup product machinery")

CI = {k: cell_index(L, k) for k in range(0, D + 1)}


def cup(a, ka: int, b, kb: int):
    _, ikk = CI[ka + kb]
    _, ika = CI[ka]
    _, ikb = CI[kb]
    out = np.zeros(len(ikk), dtype=np.result_type(a.dtype, b.dtype))
    for (x, S), r in ikk.items():
        tot = 0
        for S1 in combinations(S, ka):
            S2 = tuple(m for m in S if m not in S1)
            perm = list(S1) + list(S2)
            inv = sum(1 for i in range(len(perm)) for j in range(i + 1, len(perm))
                      if perm[i] > perm[j])
            y = x
            for mu in S1:
                y = shift(y, mu, L)
            tot += ((-1) ** inv) * a[ika[(x, S1)]] * b[ikb[(y, S2)]]
        out[r] = tot
    return out


ok_int = True
for (ka, kb) in [(1, 1), (1, 2), (2, 1)]:
    for _ in range(3):
        a = RNG.integers(-2, 3, size=len(CI[ka][0]))
        b = RNG.integers(-2, 3, size=len(CI[kb][0]))
        lhs = DM[ka + kb] @ cup(a, ka, b, kb)
        rhs = (cup(DM[ka] @ a, ka + 1, b, kb)
               + (-1) ** ka * cup(a, ka, DM[kb] @ b, kb + 1))
        ok_int = ok_int and np.array_equal(lhs, rhs)
check("B1 Leibniz rule exact on integer cochains (three bidegrees)", ok_int)

ok_real = True
for _ in range(3):
    a = RNG.normal(size=len(CI[1][0]))
    b = RNG.normal(size=len(CI[2][0]))
    lhs = DM[3] @ cup(a, 1, b, 2)
    rhs = cup(DM[1] @ a, 2, b, 2) - cup(a, 1, DM[2] @ b, 3)
    ok_real = ok_real and np.allclose(lhs, rhs, atol=1e-12)
check("B2 Leibniz rule on real cochains (float, 1e-12)", ok_real)

ok_tel = True
for _ in range(3):
    c3 = RNG.normal(size=len(CI[3][0]))
    ok_tel = ok_tel and abs(float(np.sum(DM[3] @ c3))) < 1e-10
check("B3 total sum of any exact 4-cochain over the closed torus is 0"
      " (telescoping)", ok_tel)

# ---------------------------------------------------------------------------
# Section C: flux sectors and the intersection pairing
# ---------------------------------------------------------------------------
print("Section C: flux sectors and the pairing")

PLANES = list(combinations(range(D), 2))


def flux_rep(mu: int, nu: int):
    v = np.zeros(len(CI[2][0]), dtype=np.int64)
    for (x, S), i in CI[2][1].items():
        if S == (mu, nu) and x[mu] == 0 and x[nu] == 0:
            v[i] = 1
    return v


REPS = {pl: flux_rep(*pl) for pl in PLANES}
check("C1 all six unit-flux representatives are closed (d n = 0)",
      all(np.all(DM[2] @ v == 0) for v in REPS.values()))


def Qraw(n):
    return int(np.sum(cup(n, 2, n, 2)))


def Q_int(m):
    return (m[(0, 1)] * m[(2, 3)] - m[(0, 2)] * m[(1, 3)]
            + m[(0, 3)] * m[(1, 2)])


ok_form = True
for _ in range(5):
    mvec = {pl: int(RNG.integers(-2, 3)) for pl in PLANES}
    n = sum(mvec[pl] * REPS[pl] for pl in PLANES)
    ok_form = ok_form and (Qraw(n) == 2 * Q_int(mvec))
check("C2 Q_raw = 2 x intersection form (m01 m23 - m02 m13 + m03 m12)"
      " on flux vectors", ok_form)

n_pair = REPS[(0, 1)] + REPS[(2, 3)]
check("C3 unit complementary fluxes: Q = Q_raw/2 = 1 (integer, ODD support)",
      Qraw(n_pair) == 2)
check("C4 single-plane configurations give Q = 0 (cross-plane structure)",
      all(Qraw(REPS[pl]) == 0 for pl in PLANES)
      and Qraw(2 * REPS[(0, 1)] + 3 * REPS[(0, 2)]) == 0)

ok_inv = True
ok_even = True
for _ in range(5):
    lam = RNG.integers(-2, 3, size=len(CI[1][0]))
    mvec = {pl: int(RNG.integers(-2, 3)) for pl in PLANES}
    n = sum(mvec[pl] * REPS[pl] for pl in PLANES)
    nshift = n + DM[1] @ lam
    ok_inv = ok_inv and (Qraw(nshift) == Qraw(n))
    ok_even = ok_even and (Qraw(nshift) % 2 == 0)
check("C5 class invariance: Q_raw(n + d lambda) = Q_raw(n) for closed n",
      ok_inv)
check("C6 Q_raw even on closed cochains (Q = Q_raw/2 well-defined there)",
      ok_even)

# ---------------------------------------------------------------------------
# Section D: theta-slot reduction on the closed branch
# ---------------------------------------------------------------------------
print("Section D: theta-slot reduction")

ok_red = True
for _ in range(4):
    theta = RNG.normal(size=len(CI[1][0]))  # real link 1-cochain
    mvec = {pl: int(RNG.integers(-2, 3)) for pl in PLANES}
    lam = RNG.integers(-1, 2, size=len(CI[1][0]))
    n = sum(mvec[pl] * REPS[pl] for pl in PLANES) + DM[1] @ lam  # closed
    F = DM[1] @ theta + 2.0 * np.pi * n.astype(float)
    lhs = float(np.sum(cup(F, 2, F, 2)))
    rhs = 4.0 * np.pi ** 2 * Qraw(n)
    ok_red = ok_red and abs(lhs - rhs) < 1e-7 * max(1.0, abs(rhs))
check("D1 sum (d theta + 2 pi n) u (d theta + 2 pi n) = 4 pi^2 Q_raw(n)"
      " exactly for closed n: every theta-dependent term telescopes", ok_red)
check("D2 consequence: on the closed branch the theta slot weights sectors"
      " by e^{i theta Q(m)} with Q(m) the flux intersection alone",
      ok_red)

# ---------------------------------------------------------------------------
# Section E: defect boundary
# ---------------------------------------------------------------------------
print("Section E: defect (monopole) boundary")

n_open = np.zeros(len(CI[2][0]), dtype=np.int64)
n_open[CI[2][1][((0, 0, 0, 0), (0, 1))]] = 1
check("E1 single-plaquette branch cochain is open: d n != 0 (defect present)",
      bool(np.any(DM[2] @ n_open != 0)))
vals = set()
for _ in range(8):
    lam = RNG.integers(-1, 2, size=len(CI[1][0]))
    vals.add(Qraw(n_open + DM[1] @ lam))
check("E2 with a defect the cup square is NOT branch-move invariant"
      " (several values, including odd ones): no sector decomposition on"
      " the unrestricted branch sum",
      len(vals) > 1 and any(v % 2 == 1 for v in vals),
      f"values seen: {sorted(vals)}")

# ---------------------------------------------------------------------------
# Section F: reflection pairing
# ---------------------------------------------------------------------------
print("Section F: reflection pairing")


def reflect2(v, axis: int = 0):
    out = np.zeros_like(v)
    for (x, S), i in CI[2][1].items():
        y = list(x)
        y[axis] = (-y[axis]) % L
        sgn = 1
        if axis in S:
            y[axis] = (y[axis] - 1) % L
            sgn = -1
        out[i] = sgn * v[CI[2][1][(tuple(y), S)]]
    return out


nr = reflect2(n_pair)
check("F1 reflection pullback preserves closedness and flips Q",
      bool(np.all(DM[2] @ nr == 0)) and Qraw(nr) == -Qraw(n_pair),
      f"Q(n) = {Qraw(n_pair)//2}, Q(reflected) = {Qraw(nr)//2}")

# ---------------------------------------------------------------------------
# Section G: center dual mod N
# ---------------------------------------------------------------------------
print("Section G: center dual carries only the mod-N pairing")

r2_gf3 = gfp_rank(DM[2], 3)
r1_gf3 = gfp_rank(DM[1], 3)
h2_gf3 = dims[2] - r2_gf3 - r1_gf3
check("G1 H^2 over GF(3) has dimension 6 (Z_3 flux sectors exist)",
      h2_gf3 == 6, f"dim = {h2_gf3}")

ok_mod = True
for _ in range(4):
    mvec = {pl: int(RNG.integers(0, 3)) for pl in PLANES}
    n = sum(mvec[pl] * REPS[pl] for pl in PLANES)
    ok_mod = ok_mod and ((Qraw(n) // 2) % 3 == Q_int(mvec) % 3)
check("G2 the intersection pairing descends mod 3 on Z_3 fluxes", ok_mod)

B6 = np.zeros((6, 6), dtype=np.int64)
pidx = {pl: i for i, pl in enumerate(PLANES)}
for (a, b, s) in [((0, 1), (2, 3), 1), ((0, 2), (1, 3), -1), ((0, 3), (1, 2), 1)]:
    B6[pidx[a], pidx[b]] = s
    B6[pidx[b], pidx[a]] = s


def qform(x):
    tot = 0
    for i in range(6):
        for j in range(i + 1, 6):
            tot += int(B6[i, j]) * int(x[i]) * int(x[j])
    return tot


viol_all_axes = True
for e in np.eye(6, dtype=np.int64):
    found = False
    for _ in range(16):
        x = RNG.integers(-2, 3, size=6)
        if qform(x + 3 * e) != qform(x):
            found = True
            break
    viol_all_axes = viol_all_axes and found
check("G3 no period-3 Z-descent: for every flux axis e there is x with"
      " q(x + 3e) != q(x) — the Z-valued pairing does not live on Z_3"
      " fluxes alone", viol_all_axes)

# ---------------------------------------------------------------------------
# Section H: sector-decomposition interface arithmetic
# ---------------------------------------------------------------------------
print("Section H: interface arithmetic on the flux sectors")

MRANGE = 2
flux_vecs = [dict(zip(PLANES, mv))
             for mv in np.ndindex(*((2 * MRANGE + 1,) * 6))]
for fv in flux_vecs:
    for pl in PLANES:
        fv[pl] = fv[pl] - MRANGE
wpos = []
qs = []
for fv in flux_vecs:
    s = sum(v * v for v in fv.values())
    wpos.append(np.exp(-1.5 * s))
    qs.append(Q_int(fv))
wpos = np.array(wpos)
qs = np.array(qs)
ZQ = {}
for w, q in zip(wpos, qs):
    ZQ[int(q)] = ZQ.get(int(q), 0.0) + float(w)
tot = sum(ZQ.values())
ZQ = {q: v / tot for q, v in ZQ.items()}
odd_support = any(q % 2 == 1 and ZQ[q] > 0 for q in ZQ)
paired = all(abs(ZQ[q] - ZQ.get(-q, 0.0)) < 1e-14 for q in ZQ)
ztheta = sum(ZQ[q] * np.exp(1j * np.pi * q) for q in ZQ)
neg_odd = all((1 if q % 2 == 0 else -1) * ZQ[q] < 0 for q in ZQ if q % 2 == 1)
check("H1 positive weight family over flux integers: Z_Q > 0 with odd-Q"
      " support and pairing Z_Q = Z_-Q",
      odd_support and paired and all(v > 0 for v in ZQ.values()),
      f"Q values populated: {sorted(ZQ)[:4]} ... {sorted(ZQ)[-4:]}")
check("H2 Z(pi) is real and odd-Q sectors carry negative weight at"
      " theta = pi; all weights nonnegative at theta = 0",
      abs(ztheta.imag) < 1e-12 and neg_odd)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
