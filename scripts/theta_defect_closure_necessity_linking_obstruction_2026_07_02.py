#!/usr/bin/env python3
"""Defect-closure NECESSITY on T^4 for the tested single-plaquette family.

The change of the cup-square Q_raw under exact 1-cochain shifts is EXACTLY a
linking pairing with the defect current. On the tested single-plaquette
family, a well-defined sector structure therefore REQUIRES the branch cochain
to be closed.

Self-contained class-A runner (numpy only, fixed seed). Reimplements the
cubical-complex machinery of the reference runner
  scripts/theta_4d_carrier_flux_cohomology_intersection_pairing_2026_07_02.py
(cells, coboundary d with the alternating-sign convention, cubical cup
product of two 2-cochains via (2,2)-shuffles with shuffle signs, second
factor evaluated at the shifted vertex). Nothing is imported from it.

Setup: T^4, L = 2 (16 sites). For an integer 2-cochain n with defect current
J = d n, and an exact shift n -> n + d lambda (lambda in C^1),
  Delta(lambda) := Q_raw(n + d lambda) - Q_raw(n).
Derivation sketch (VERIFIED here, not assumed):
  Q_raw(n + dl) - Q_raw(n) = sum(n u dl) + sum(dl u n) + sum(dl u dl);
  Leibniz d(a u b) = da u b + (-1)^p a u db pins the signs of the cross
  terms, and sum(dl u dl) = sum d(l u dl) = 0 on the closed torus.
The resulting identity is a linking pairing between J and lambda; the winning
sign pattern is DERIVED (both candidates tested; exactly one holds).

Sections:
  A. Machinery ground: dd = 0; Leibniz spot-check pinning the sign convention.
  B. The linking identity: Delta(lambda) matches exactly one signed pairing
     of J and lambda across all trials (open n); vanishes for closed n.
  C. Necessity: every tested nonzero single-plaquette defect current admits a
     lambda with Delta != 0 (sector structure requires d n = 0 on this
     family); the obstruction is defect-supported (locality witness).
  D. Consequence arithmetic: on the closed subfamily Q = Q_raw/2 equals the
     intersection form m01 m23 - m02 m13 + m03 m12.

Expected close: TOTAL: PASS=7 FAIL=0
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


RNG = np.random.default_rng(7)
D = 4
L = 2


# ---------------------------------------------------------------------------
# Cubical complex machinery (reimplemented from the reference conventions)
# ---------------------------------------------------------------------------
def cells(k: int):
    out = []
    sites = [tuple(s) for s in np.ndindex(*(L,) * D)]
    for S in combinations(range(D), k):
        for x in sites:
            out.append((x, S))
    return out


def cell_index(k: int):
    cs = cells(k)
    return cs, {c: i for i, c in enumerate(cs)}


def shift(x, mu: int):
    y = list(x)
    y[mu] = (y[mu] + 1) % L
    return tuple(y)


def d_matrix(k: int) -> np.ndarray:
    _, ik = cell_index(k)
    _, ik1 = cell_index(k + 1)
    M = np.zeros((len(ik1), len(ik)), dtype=np.int64)
    for (x, S), r in ik1.items():
        for j, mu in enumerate(S):
            Srem = tuple(m for m in S if m != mu)
            sgn = (-1) ** j
            M[r, ik[(shift(x, mu), Srem)]] += sgn
            M[r, ik[(x, Srem)]] -= sgn
    return M


CI = {k: cell_index(k) for k in range(0, D + 1)}
DM = {k: d_matrix(k) for k in range(0, D)}


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
                y = shift(y, mu)
            tot += ((-1) ** inv) * a[ika[(x, S1)]] * b[ikb[(y, S2)]]
        out[r] = tot
    return out


def Qraw(n):
    return int(np.sum(cup(n, 2, n, 2)))


def sum_cup(a, ka, b, kb):
    return int(np.sum(cup(a, ka, b, kb)))


PLANES = list(combinations(range(D), 2))


def flux_rep(mu: int, nu: int):
    v = np.zeros(len(CI[2][0]), dtype=np.int64)
    for (x, S), i in CI[2][1].items():
        if S == (mu, nu) and x[mu] == 0 and x[nu] == 0:
            v[i] = 1
    return v


REPS = {pl: flux_rep(*pl) for pl in PLANES}


# ---------------------------------------------------------------------------
# Section A: machinery ground
# ---------------------------------------------------------------------------
print("Section A: machinery ground")

check("A1 dd = 0 for d1 (C^1->C^2) and d2 (C^2->C^3)",
      bool(np.all(DM[2] @ DM[1] == 0)) and bool(np.all(DM[3] @ DM[2] == 0)))

# Leibniz spot-check with a in C^1 (p = 1), b in C^2. This pins the sign
# convention the derivation uses. Determine which sign holds and report it.
minus_ok = True
plus_ok = True
for _ in range(6):
    a = RNG.integers(-2, 3, size=len(CI[1][0]))
    b = RNG.integers(-2, 3, size=len(CI[2][0]))
    lhs = DM[3] @ cup(a, 1, b, 2)
    rhs_minus = cup(DM[1] @ a, 2, b, 2) - cup(a, 1, DM[2] @ b, 3)
    rhs_plus = cup(DM[1] @ a, 2, b, 2) + cup(a, 1, DM[2] @ b, 3)
    minus_ok = minus_ok and np.array_equal(lhs, rhs_minus)
    plus_ok = plus_ok and np.array_equal(lhs, rhs_plus)
# Exactly one of the two forms must hold (they differ whenever a u db != 0).
convention = "minus" if minus_ok else ("plus" if plus_ok else "none")
check("A2 Leibniz d(a u b) = da u b + (-1)^p a u db exact (a in C^1, p=1)",
      minus_ok and not plus_ok,
      f"convention that holds: d(a u b) = da u b - a u db ({convention})")

# ---------------------------------------------------------------------------
# Section B: the linking identity (the core)
# ---------------------------------------------------------------------------
print("Section B: the linking identity")

# With the convention pinned in A2 (d(a u b) = da u b + (-1)^p a u db):
# for a = n (p = 2): sum d(n u l) = 0 = sum(J u l) + sum(n u dl)
#   => sum(n u dl) = -sum(J u lambda);
# for a = l (p = 1): sum d(l u n) = 0 = sum(dl u n) - sum(l u J)
#   => sum(dl u n) = +sum(lambda u J);
# so the derived identity is Delta = -sum(J u lambda) + sum(lambda u J),
# i.e. the (-,+) pattern. The sign pattern is nonetheless DERIVED from the
# data: all four candidates are tested and exactly one must hold across all
# 36 (n, lambda) trials.
sign_patterns = {
    "(+,-)": (+1, -1),
    "(+,+)": (+1, +1),
    "(-,+)": (-1, +1),
    "(-,-)": (-1, -1),
}
pattern_ok = {name: True for name in sign_patterns}
n_trials = 0
telescope_ok = True
for _ in range(6):
    # draw an open n (dn != 0)
    while True:
        n = RNG.integers(-2, 3, size=len(CI[2][0]))
        J = DM[2] @ n
        if np.any(J != 0):
            break
    for _ in range(6):
        lam = RNG.integers(-2, 3, size=len(CI[1][0]))
        dl = DM[1] @ lam
        delta = Qraw(n + dl) - Qraw(n)
        JuL = sum_cup(J, 3, lam, 1)  # sum(J u lambda), J in C^3? no: J in C^3
        LuJ = sum_cup(lam, 1, J, 3)  # sum(lambda u J)
        # cross-check the telescoping term sum(dl u dl) = 0
        telescope_ok = telescope_ok and (sum_cup(dl, 2, dl, 2) == 0)
        for name, (s1, s2) in sign_patterns.items():
            pattern_ok[name] = pattern_ok[name] and (
                delta == s1 * JuL + s2 * LuJ)
        n_trials += 1
winners = [name for name, ok in pattern_ok.items() if ok]
check("B1 Delta(lambda) is a linking pairing of J and lambda: exactly one"
      " signed candidate matches ALL trials (sign DERIVED, not fitted)",
      len(winners) == 1 and telescope_ok,
      f"winner: {winners[0] if len(winners)==1 else winners}"
      f" over {n_trials} trials; sum(dl u dl)=0 held: {telescope_ok}")

# B2 closed contrast: for closed n (flux combinations, dn = 0), Delta = 0.
closed_zero = True
closed_had_nonzero_contrast = False
for _ in range(6):
    mvec = {pl: int(RNG.integers(-2, 3)) for pl in PLANES}
    n = sum(mvec[pl] * REPS[pl] for pl in PLANES)
    assert np.all(DM[2] @ n == 0)
    lam = RNG.integers(-2, 3, size=len(CI[1][0]))
    delta = Qraw(n + DM[1] @ lam) - Qraw(n)
    closed_zero = closed_zero and (delta == 0)
    # discriminating contrast: the same lambda on an OPEN n gives Delta != 0
    while True:
        n_open = RNG.integers(-2, 3, size=len(CI[2][0]))
        if np.any(DM[2] @ n_open != 0):
            break
    if Qraw(n_open + DM[1] @ lam) - Qraw(n_open) != 0:
        closed_had_nonzero_contrast = True
check("B2 closed contrast: Delta(lambda) = 0 for closed n (invariance"
      " re-earned) while the same shift moves an open n (discriminating)",
      closed_zero and closed_had_nonzero_contrast)

# ---------------------------------------------------------------------------
# Section C: necessity
# ---------------------------------------------------------------------------
print("Section C: necessity")

# For each of the six single-plaquette branch cochains (one per plane), the
# defect current J = dn is nonzero, and there is a lambda with Delta != 0.
links = list(CI[1][1].keys())


def single_plaquette(mu, nu):
    n = np.zeros(len(CI[2][0]), dtype=np.int64)
    n[CI[2][1][((0, 0, 0, 0), (mu, nu))]] = 1
    return n


necessity_all = True
min_mag = None
found_details = []
for pl in PLANES:
    n = single_plaquette(*pl)
    assert np.any(DM[2] @ n != 0)  # nonzero defect current
    best = 0
    best_link = None
    # scan the 64 unit-link lambdas first
    for li, link in enumerate(links):
        lam = np.zeros(len(CI[1][0]), dtype=np.int64)
        lam[li] = 1
        delta = Qraw(n + DM[1] @ lam) - Qraw(n)
        if abs(delta) > best:
            best = abs(delta)
            best_link = link
    if best == 0:
        # fall back to random integer lambdas
        for _ in range(200):
            lam = RNG.integers(-2, 3, size=len(CI[1][0]))
            delta = Qraw(n + DM[1] @ lam) - Qraw(n)
            if abs(delta) > best:
                best = abs(delta)
    necessity_all = necessity_all and (best >= 1)
    min_mag = best if min_mag is None else min(min_mag, best)
    found_details.append((pl, best, best_link))
check("C1 necessity: every tested nonzero single-plaquette defect current"
      " admits a lambda with |Delta| >= 1 (sector structure REQUIRES dn = 0"
      " on this family)",
      necessity_all and (min_mag is not None and min_mag >= 1),
      f"min |Delta| over the six planes: {min_mag}")

# C2 locality witness: for a fixed single-plaquette n, some near unit-link
# lambda gives Delta != 0 while a far unit-link lambda (max torus distance)
# gives Delta = 0.
n = single_plaquette(0, 1)


def torus_dist(x, y):
    return sum(min((x[i] - y[i]) % L, (y[i] - x[i]) % L) for i in range(D))


defect_site = (0, 0, 0, 0)
near_link = None
near_delta = 0
far_link = None
far_delta = None
# find a near unit link giving Delta != 0
for li, (lx, lS) in enumerate(links):
    lam = np.zeros(len(CI[1][0]), dtype=np.int64)
    lam[li] = 1
    delta = Qraw(n + DM[1] @ lam) - Qraw(n)
    if delta != 0 and torus_dist(lx, defect_site) <= 1:
        near_link = (lx, lS)
        near_delta = delta
        break
# find a far unit link giving Delta = 0
for li, (lx, lS) in enumerate(links):
    lam = np.zeros(len(CI[1][0]), dtype=np.int64)
    lam[li] = 1
    delta = Qraw(n + DM[1] @ lam) - Qraw(n)
    dist = torus_dist(lx, defect_site)
    if delta == 0 and dist == max(torus_dist(x, defect_site)
                                  for x, _ in [(l[0], l[1]) for l in links]):
        far_link = (lx, lS)
        far_delta = delta
        break
check("C2 obstruction is defect-supported: a near lambda gives Delta != 0"
      " while a far lambda gives Delta = 0 (locality witness)",
      near_link is not None and near_delta != 0
      and far_link is not None and far_delta == 0,
      f"near link {near_link} -> Delta={near_delta};"
      f" far link {far_link} -> Delta={far_delta}")

# ---------------------------------------------------------------------------
# Section D: consequence arithmetic
# ---------------------------------------------------------------------------
print("Section D: consequence arithmetic")


def Q_int(m):
    return (m[(0, 1)] * m[(2, 3)] - m[(0, 2)] * m[(1, 3)]
            + m[(0, 3)] * m[(1, 2)])


d_ok = True
d_detail = []
for _ in range(3):
    mvec = {pl: int(RNG.integers(-2, 3)) for pl in PLANES}
    n = sum(mvec[pl] * REPS[pl] for pl in PLANES)
    q_raw = Qraw(n)
    ok = (q_raw % 2 == 0) and (q_raw // 2 == Q_int(mvec))
    d_ok = d_ok and ok
    d_detail.append((q_raw // 2, Q_int(mvec)))
check("D1 on the closed subfamily Q = Q_raw/2 equals the intersection form"
      " m01 m23 - m02 m13 + m03 m12",
      d_ok, f"(Q, form) pairs: {d_detail}")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
