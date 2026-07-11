#!/usr/bin/env python3
"""Center sector-record context on the retained character surface, and the
integer-grading obstruction that localizes the theta Q-context wall.

Paired note:
docs/GAUGE_CENTER_SECTOR_RECORD_CONTEXT_AND_THETA_Q_CHARACTER_GRADING_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-01.md

Class-A finite checks only: exact Weyl-character identities at fixed torus
points, exact integer fusion matrices from the retained recurrence, exact
finite linear algebra over Q / GF(2) / GF(3), and truncation-stable
transfer-vector sector weights. Deterministic; no fits, no external
comparators, no measured values.

Sections:
  A. Center action is diagonal on characters (SU(3): omega^(p-q); SU(2): (-1)^n).
  B. Retained recurrence ground: product rules verified at Weyl level;
     fusion matrices shift the center label by exactly +/-1; projector algebra.
  C. Transfer-vector sector weights: strictly positive on every sector,
     conjugation-paired, truncation-stable; exact nonnegativity structure.
  D. Grading obstruction: fusion-additive labels solve a homogeneous linear
     system; nullity over Q is 0 (no Z-valued label), over GF(2) is 0 for
     SU(3) (no parity) and 1 for SU(2) (center parity), over GF(3) is 1 for
     SU(3) with kernel exactly the triality line.
  E. Record-interface arithmetic: disjoint-region label additivity mod N;
     sector-sharp products compose with additive labels.
  F. Source-note discipline: canonical metadata, graph links, fail-closed
     hygiene.

Expected close: TOTAL: PASS=56 FAIL=0
"""
from __future__ import annotations

import cmath
from pathlib import Path

import numpy as np
from scipy.linalg import expm

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


# ---------------------------------------------------------------------------
# Weyl characters at maximal-torus points
# ---------------------------------------------------------------------------

def torus3(t1: float, t2: float) -> np.ndarray:
    return np.array([cmath.exp(1j * t1), cmath.exp(1j * t2),
                     cmath.exp(-1j * (t1 + t2))], dtype=complex)


def su3_char(p: int, q: int, z: np.ndarray) -> complex:
    lam = [p + q, q, 0]
    num = np.array([[z[i] ** (lam[j] + 2 - j) for j in range(3)]
                    for i in range(3)], dtype=complex)
    den = np.array([[z[i] ** (2 - j) for j in range(3)]
                    for i in range(3)], dtype=complex)
    return complex(np.linalg.det(num) / np.linalg.det(den))


def su2_char(n: int, th: float) -> float:
    return float(np.sin((n + 1) * th) / np.sin(th))


TORUS_SAMPLES = [(0.37, -0.91), (1.11, 0.43), (-0.64, 1.27), (0.82, -1.44)]
OMEGA = cmath.exp(2j * cmath.pi / 3)

# ---------------------------------------------------------------------------
# Section A: center action diagonal on characters
# ---------------------------------------------------------------------------
print("Section A: center action is diagonal on characters")

for (p, q) in [(1, 0), (0, 1), (1, 1), (2, 0), (3, 1), (2, 2)]:
    ok = True
    for (t1, t2) in TORUS_SAMPLES:
        z = torus3(t1, t2)
        lhs = su3_char(p, q, OMEGA * z)
        rhs = (OMEGA ** ((p - q) % 3)) * su3_char(p, q, z)
        ok = ok and abs(lhs - rhs) < 1e-9
    check(f"A1 SU(3) chi_({p},{q})(omega U) = omega^((p-q) mod 3) chi(U)", ok)

for n in range(5):
    ok = all(abs(su2_char(n, th + np.pi) - ((-1) ** n) * su2_char(n, th)) < 1e-9
             for th in [0.3, 0.7, 1.1])
    check(f"A2 SU(2) chi_{n}(-U) = (-1)^{n} chi_{n}(U)", ok)

# ---------------------------------------------------------------------------
# Section B: retained recurrence ground + grading shift
# ---------------------------------------------------------------------------
print("Section B: retained recurrence and center-grading shift")


def rule_F(p: int, q: int):
    return [(a, b) for (a, b) in [(p + 1, q), (p - 1, q + 1), (p, q - 1)]
            if a >= 0 and b >= 0]


def rule_Fb(p: int, q: int):
    return [(a, b) for (a, b) in [(p, q + 1), (p + 1, q - 1), (p - 1, q)]
            if a >= 0 and b >= 0]


for (p, q) in [(0, 0), (1, 0), (0, 1), (1, 1), (2, 1), (3, 2)]:
    ok = True
    for (t1, t2) in TORUS_SAMPLES:
        z = torus3(t1, t2)
        lhs = su3_char(1, 0, z) * su3_char(p, q, z)
        rhs = sum(su3_char(a, b, z) for (a, b) in rule_F(p, q))
        ok = ok and abs(lhs - rhs) < 1e-8
    check(f"B1 retained rule chi_(1,0) chi_({p},{q}) = sum of channels", ok)

for (p, q) in [(0, 0), (1, 0), (1, 1)]:
    ok = True
    for (t1, t2) in TORUS_SAMPLES:
        z = torus3(t1, t2)
        lhs = su3_char(0, 1, z) * su3_char(p, q, z)
        rhs = sum(su3_char(a, b, z) for (a, b) in rule_Fb(p, q))
        ok = ok and abs(lhs - rhs) < 1e-8
    check(f"B1 retained rule chi_(0,1) chi_({p},{q}) = sum of channels", ok)

PMAX = 30
IRREPS = [(p, q) for p in range(PMAX + 1) for q in range(PMAX + 1)
          if p + q <= PMAX]
IDX = {pq: i for i, pq in enumerate(IRREPS)}
N3 = len(IRREPS)
TRI = np.array([(p - q) % 3 for (p, q) in IRREPS])


def fusion_matrix(rule) -> np.ndarray:
    M = np.zeros((N3, N3))
    for (p, q), i in IDX.items():
        for (a, b) in rule(p, q):
            if (a, b) in IDX:
                M[IDX[(a, b)], i] += 1.0
    return M


MF = fusion_matrix(rule_F)
MFb = fusion_matrix(rule_Fb)

r, c = np.nonzero(MF)
check("B2 multiplication by chi_(1,0) shifts triality by exactly +1",
      bool(np.all(TRI[r] == (TRI[c] + 1) % 3)))
r, c = np.nonzero(MFb)
check("B2 multiplication by chi_(0,1) shifts triality by exactly -1",
      bool(np.all(TRI[r] == (TRI[c] - 1) % 3)))

J6 = MF + MFb  # 6*J in the retained normalization J = X-multiplication
check("B3 J6 = MF + MFb is symmetric on the truncation cone",
      bool(np.allclose(J6, J6.T)))

P_SEC = [np.diag((TRI == k).astype(float)) for k in range(3)]
check("B3 projectors: orthogonal, idempotent, complete",
      all(np.allclose(P_SEC[a] @ P_SEC[b],
                      P_SEC[a] if a == b else np.zeros_like(P_SEC[a]))
          for a in range(3) for b in range(3))
      and np.allclose(sum(P_SEC), np.eye(N3)))

D_CENTER = [np.diag(np.exp(2j * np.pi * j * TRI / 3)) for j in range(3)]
check("B3 spectral construction P_k = (1/3) sum_j omega^(-jk) Delta_(omega^j)",
      all(np.allclose(sum((OMEGA ** (-j * k)) * D_CENTER[j]
                          for j in range(3)) / 3, P_SEC[k])
          for k in range(3)))

check("B3 P_k' J6 P_k = 0 unless k' = k +- 1 (mod 3); no diagonal block",
      all(np.allclose(P_SEC[a] @ J6 @ P_SEC[b], 0)
          for a in range(3) for b in range(3)
          if a != (b + 1) % 3 and a != (b - 1) % 3)
      and all(not np.allclose(P_SEC[(b + s) % 3] @ J6 @ P_SEC[b], 0)
              for b in range(3) for s in (1, -1)))

word_ok = True
for word in [(1,), (1, 1), (1, -1), (1, 1, 1), (-1, 1, 1, -1), (1, 1, -1, 1, 1, 1)]:
    W = np.eye(N3)
    for s in word:
        W = (MF if s == 1 else MFb) @ W
    shift = sum(word) % 3
    rr, cc = np.nonzero(W)
    word_ok = word_ok and np.all(TRI[rr] == (TRI[cc] + shift) % 3)
check("B4 word rule: an (F,Fb)-insertion word shifts the sector by"
      " (#F - #Fb) mod 3", bool(word_ok))

# ---------------------------------------------------------------------------
# Section C: transfer-vector sector weights
# ---------------------------------------------------------------------------
print("Section C: transfer-vector sector weights")

E0 = np.zeros(N3)
E0[IDX[(0, 0)]] = 1.0
KEEP = [i for i, (p, q) in enumerate(IRREPS) if p + q <= PMAX - 6]
KEEP_POS = {i: s for s, i in enumerate(KEEP)}

for beta in [1.0, 6.0, 12.0]:
    v = expm((beta / 2.0) * (J6 / 6.0)) @ E0
    Z = np.array([float(v @ P_SEC[k] @ v) for k in range(3)])
    Z = Z / Z.sum()
    Js = (J6 / 6.0)[np.ix_(KEEP, KEEP)]
    e0s = np.zeros(len(KEEP))
    e0s[KEEP_POS[IDX[(0, 0)]]] = 1.0
    vs = expm((beta / 2.0) * Js) @ e0s
    tris = TRI[KEEP]
    Zs = np.array([float(np.sum(vs[tris == k] ** 2)) for k in range(3)])
    Zs = Zs / Zs.sum()
    drift = float(np.max(np.abs(Z - Zs)))
    check(f"C1 beta={beta:g}: Z_k > 0 on every center sector",
          bool(np.all(Z > 0)), f"Z = {np.round(Z, 6).tolist()}")
    check(f"C1 beta={beta:g}: conjugation pairing Z_1 = Z_2 exactly",
          abs(Z[1] - Z[2]) < 1e-14)
    check(f"C1 beta={beta:g}: truncation-stable (cone {PMAX} vs {PMAX-6})",
          drift < 1e-8, f"max drift = {drift:.2e}")

NMAX2 = 20
M2 = np.zeros((NMAX2 + 1, NMAX2 + 1))
for m in range(NMAX2 + 1):
    for x in (m - 1, m + 1):
        if 0 <= x <= NMAX2:
            M2[x, m] += 1.0
PAR2 = np.array([m % 2 for m in range(NMAX2 + 1)])
for beta in [1.0, 6.0]:
    e0 = np.zeros(NMAX2 + 1)
    e0[0] = 1.0
    v2 = expm((beta / 2.0) * (M2 / 2.0)) @ e0
    z_odd = float(np.sum(v2[PAR2 == 1] ** 2) / np.sum(v2 ** 2))
    check(f"C2 SU(2) beta={beta:g}: odd-parity sector weight Z_odd > 0",
          z_odd > 0, f"Z_odd = {z_odd:.6f}")

pow_ok_nonneg = True
pow_ok_cover = True
Wm = np.eye(N3)
for m in range(1, 5):
    Wm = J6 @ Wm
    col = Wm @ E0
    pow_ok_nonneg = pow_ok_nonneg and bool(np.all(col >= 0))
    if m >= 2:
        pow_ok_cover = pow_ok_cover and all(
            float(col @ P_SEC[k] @ col) > 0 or
            bool(np.any(col[TRI == k] > 0)) for k in range(3))
check("C3 (chi_F + chi_Fb)^m e_0 has nonnegative coefficients (m <= 4)",
      pow_ok_nonneg)
check("C3 (chi_F + chi_Fb)^m e_0 supports every triality for m in {2,3,4}",
      pow_ok_cover)

# ---------------------------------------------------------------------------
# Section D: grading obstruction over Q, GF(2), GF(3)
# ---------------------------------------------------------------------------
print("Section D: grading obstruction")


def modp_nullspace(A: np.ndarray, p: int):
    """Nullity and one reduced row-echelon copy of A over GF(p)."""
    A = (A.copy() % p).astype(np.int64)
    m, n = A.shape
    row = 0
    lead_cols = []
    for col in range(n):
        piv = next((rr for rr in range(row, m) if A[rr, col] % p != 0), None)
        if piv is None:
            continue
        A[[row, piv]] = A[[piv, row]]
        inv = pow(int(A[row, col]), p - 2, p)
        A[row] = (A[row] * inv) % p
        for rr in range(m):
            if rr != row and A[rr, col] % p:
                A[rr] = (A[rr] - A[rr, col] * A[row]) % p
        lead_cols.append(col)
        row += 1
        if row == m:
            break
    nullity = n - len(lead_cols)
    return nullity, A, lead_cols


def grading_system_su3(cone_max: int):
    uni = [(p, q) for p in range(cone_max + 1) for q in range(cone_max + 1)
           if p + q <= cone_max]
    ui = {u: i for i, u in enumerate(uni)}
    rows = []
    for gen, rule in [((1, 0), rule_F), ((0, 1), rule_Fb)]:
        for b in uni:
            for ch in rule(*b):
                if ch in ui:
                    rvec = np.zeros(len(uni), dtype=np.int64)
                    rvec[ui[ch]] += 1
                    rvec[ui[gen]] -= 1
                    rvec[ui[b]] -= 1
                    rows.append(rvec)
    return np.array(rows), uni


R3, UNI3 = grading_system_su3(8)
null_q3 = R3.shape[1] - int(np.linalg.matrix_rank(R3.astype(float)))
check("D1 SU(3): fusion-additive labels over Q have nullity 0"
      " (no nontrivial Z-valued label)", null_q3 == 0)

null_2, _, _ = modp_nullspace(R3, 2)
check("D1 SU(3): nullity over GF(2) is 0 (no parity label (-1)^Q exists)",
      null_2 == 0)

null_3, A3, lead3 = modp_nullspace(R3, 3)
check("D1 SU(3): nullity over GF(3) is 1 (center grading, and only it)",
      null_3 == 1)

kernel_is_triality = False
if null_3 == 1:
    free_cols = [cc for cc in range(R3.shape[1]) if cc not in lead3]
    g = np.zeros(R3.shape[1], dtype=np.int64)
    g[free_cols[0]] = 1
    for rvec in A3[::-1]:
        nz = np.nonzero(rvec % 3)[0]
        if len(nz) == 0:
            continue
        piv = nz[0]
        if piv in lead3:
            g[piv] = (-sum(int(rvec[cc]) * int(g[cc]) for cc in nz[1:])) % 3
    tvec = np.array([(p - q) % 3 for (p, q) in UNI3])
    kernel_is_triality = (np.array_equal(g % 3, tvec % 3)
                          or np.array_equal(g % 3, (2 * tvec) % 3))
check("D1 SU(3): the GF(3) kernel is exactly the triality line",
      kernel_is_triality)

uni2 = list(range(NMAX2 + 1))
rows2 = []
for b in uni2:
    for ch in (b - 1, b + 1):
        if 0 <= ch <= NMAX2:
            rvec = np.zeros(len(uni2), dtype=np.int64)
            rvec[ch] += 1
            rvec[1] -= 1
            rvec[b] -= 1
            rows2.append(rvec)
R2 = np.array(rows2)
null_q2 = R2.shape[1] - int(np.linalg.matrix_rank(R2.astype(float)))
check("D2 SU(2): nullity over Q is 0 (no nontrivial Z-valued label)",
      null_q2 == 0)
null_22, A22, lead2 = modp_nullspace(R2, 2)
kernel2_is_parity = False
if null_22 == 1:
    free_cols = [cc for cc in range(R2.shape[1]) if cc not in lead2]
    g2 = np.zeros(R2.shape[1], dtype=np.int64)
    g2[free_cols[0]] = 1
    for rvec in A22[::-1]:
        nz = np.nonzero(rvec % 2)[0]
        if len(nz) == 0:
            continue
        piv = nz[0]
        if piv in lead2:
            g2[piv] = (-sum(int(rvec[cc]) * int(g2[cc]) for cc in nz[1:])) % 2
    kernel2_is_parity = np.array_equal(g2 % 2, np.array(uni2) % 2)
check("D2 SU(2): nullity over GF(2) is 1 and the kernel is n mod 2",
      null_22 == 1 and kernel2_is_parity)

# replay of the named hand relations, as pure integer forcing
# g(0,0)=0 from F.(0,0)=(1,0); g(2,0)=g(0,1)=2a from F.(1,0);
# 3a=0 from F.(0,1) containing (0,0); then g(p,q)=(p-q)a.
hand_ok = True
# relation 1: g(1,0) = a + g(0,0) with g(1,0)=a  => g(0,0)=0
# relation 2: channels of F.(1,0): {(2,0),(0,1)} => both labels 2a
# relation 3: channels of F.(0,1): {(1,1),(0,0)} => 0 = a + 2a = 3a
hand_ok = hand_ok and rule_F(0, 0) == [(1, 0)]
hand_ok = hand_ok and set(rule_F(1, 0)) == {(2, 0), (0, 1)}
hand_ok = hand_ok and set(rule_F(0, 1)) == {(1, 1), (0, 0)}
# over Z: 3a = 0 forces a = 0; over GF(3): a free -> label (p-q)a
check("D3 hand-proof relation replay: F.(0,0)={(1,0)}, F.(1,0)={(2,0),(0,1)},"
      " F.(0,1) contains (0,0) => 3a = 0", hand_ok)

ch_ff = rule_F(1, 0)
int_labels = [(a - b) for (a, b) in ch_ff]
check("D4 raw integer label p-q is not additive: fund x fund channels"
      " carry {2, -1}; only the mod-3 shadow is sharp",
      len(set(int_labels)) > 1
      and len(set((a - b) % 3 for (a, b) in ch_ff)) == 1)

# ---------------------------------------------------------------------------
# Section E: record-interface arithmetic
# ---------------------------------------------------------------------------
print("Section E: record-interface arithmetic")

tA = np.array([0, 1, 2])
tAB = (tA[:, None] + tA[None, :]) % 3
DA = np.diag(np.exp(2j * np.pi * tA / 3))
check("E1 disjoint regions: center acts as Delta x Delta; labels add mod 3",
      bool(np.allclose(np.kron(DA, DA),
                       np.diag(np.exp(2j * np.pi * tAB.flatten() / 3)))))

prod_ok = True
for (t1, t2) in TORUS_SAMPLES[:2]:
    z = torus3(t1, t2)
    f1 = su3_char(1, 0, z)          # sector 1
    f2 = su3_char(0, 2, z)          # sector (0-2) mod 3 = 1
    lhs = f1 * f2                   # expected sector 2
    z_om = OMEGA * z
    lhs_om = su3_char(1, 0, z_om) * su3_char(0, 2, z_om)
    prod_ok = prod_ok and abs(lhs_om - (OMEGA ** 2) * lhs) < 1e-8
check("E2 sector-sharp product: (sector 1)x(sector 1) is sharp in sector 2",
      prod_ok)

born_ok = True
for beta in [6.0]:
    v = expm((beta / 2.0) * (J6 / 6.0)) @ E0
    Z = np.array([float(v @ P_SEC[k] @ v) for k in range(3)])
    Z = Z / Z.sum()
    born_ok = born_ok and bool(np.all(Z >= 0)) and abs(Z.sum() - 1.0) < 1e-12
check("E3 interface shape: Z_k = ||P_k psi||^2 / ||psi||^2 nonnegative,"
      " normalized, finite (3 sectors)", born_ok)

# ---------------------------------------------------------------------------
# Section F: source-note discipline
# ---------------------------------------------------------------------------
print("Section F: source-note discipline")

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/GAUGE_CENTER_SECTOR_RECORD_CONTEXT_AND_THETA_Q_CHARACTER_GRADING_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-01.md"
).read_text(encoding="utf-8")
check("F1 note declares canonical bounded_theorem claim type",
      "**Claim type:** bounded_theorem" in NOTE)
check("F1 note does not use runner PASS as source status",
      "**Status:** PASS" not in NOTE)
check("F1 note keeps decision history as non-linked provenance",
      "`docs/audit/data/premise_decision_history.json`" in NOTE
      and "(audit/data/premise_decision_history.json)" not in NOTE)
check("F1 note graph-links the retained RP-half no-go row",
      "(STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md)" in NOTE)
check("F1 unaudited no-winding-carrier note is non-load-bearing context",
      "non-load-bearing context here and is not consumed as a premise" in NOTE)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
raise SystemExit(0)
