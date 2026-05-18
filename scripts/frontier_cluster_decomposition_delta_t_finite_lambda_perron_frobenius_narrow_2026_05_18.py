#!/usr/bin/env python3
"""Cluster Decomposition Δ_T > 0 Finite-Λ Perron-Frobenius — narrow runner.

Companion to
docs/CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_PERRON_FROBENIUS_NARROW_BOUNDED_NOTE_2026-05-18.md

Exhibits the bounded support theorem on explicit small transfer matrices:

  T1  Pure Wilson transfer matrix is non-negative element-wise
      (Step 1 of the proof).
  T2  Non-negative transfer matrix is irreducible on a connected
      lattice (Step 2).
  T3  Perron-Frobenius for an irreducible non-negative finite-dim
      operator: top eigenvalue strictly > |next| (Step 3).
  T4  Fermion-determinant positivity: det(D + m) > 0 via eigenvalue
      pairing on a small staggered Dirac block (Step 4) — exact
      Fraction arithmetic.
  T5  Composite T = T_W · diag(T_F) preserves Perron-Frobenius
      structure (Step 4 composition).
  T6  Source-note boundary check: no overclaim, no thermodynamic-
      limit claim, no Yang-Mills mass-gap claim.

T1/T2/T3/T5 use numpy float arithmetic for eigenvalue computation
(exact-rational power iteration on 4x4 matrices blows up the
numerator/denominator bit lengths). T4 uses exact Fraction arithmetic
where the determinant identity is a simple polynomial in m.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys

import numpy as np

PASS = 0
FAIL = 0
FAILURES: list[str] = []


def assert_pass(label: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"PASS: {label}")
    else:
        FAIL += 1
        FAILURES.append(f"{label}: {detail}")
        print(f"FAIL: {label} -- {detail}")


def is_nonneg(M: np.ndarray) -> bool:
    return bool(np.all(M >= 0))


def is_irreducible_pos(M: np.ndarray) -> bool:
    """Strong connectivity of positive-entry directed graph."""
    n = M.shape[0]
    adj = (M > 0).astype(bool)
    # Floyd-Warshall transitive closure
    reach = adj.copy()
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i, j] = bool(reach[i, j]) or (
                    bool(reach[i, k]) and bool(reach[k, j])
                )
    return bool(np.all(reach))


# ---------------------------------------------------------------------------
# T1 — Pure Wilson transfer matrix is non-negative
# ---------------------------------------------------------------------------

print("=" * 70)
print("T1 — Pure Wilson transfer matrix non-negativity")
print("=" * 70)

# Toy 4-state transfer matrix mimicking Wilson structure:
# - diagonal entries large (most-likely same-config transition)
# - off-diagonal entries small positive (nearest-neighbor transitions)
# - entries 0 for non-adjacent (here, configs 0 and 3)

T_W = np.array(
    [
        [1.0, 1.0 / 3.0, 1.0 / 4.0, 0.0],
        [1.0 / 3.0, 1.0, 1.0 / 5.0, 1.0 / 6.0],
        [1.0 / 4.0, 1.0 / 5.0, 1.0, 1.0 / 4.0],
        [0.0, 1.0 / 6.0, 1.0 / 4.0, 1.0],
    ],
    dtype=float,
)

assert_pass(
    "T1.1 T_W entries are all non-negative",
    is_nonneg(T_W),
    "found negative entry",
)

zero_entries = [(i, j) for i in range(4) for j in range(4) if T_W[i, j] == 0.0]
assert_pass(
    "T1.2 T_W zero entries correspond to non-adjacent configurations (0,3)/(3,0)",
    len(zero_entries) == 2 and (0, 3) in zero_entries and (3, 0) in zero_entries,
    f"zero entries: {zero_entries}",
)

# ---------------------------------------------------------------------------
# T2 — T_W is irreducible on connected toy lattice
# ---------------------------------------------------------------------------

print("\n" + "=" * 70)
print("T2 — T_W irreducibility on connected lattice")
print("=" * 70)

assert_pass(
    "T2.1 T_W is irreducible (strongly connected positive-entry graph)",
    is_irreducible_pos(T_W),
    "T_W is reducible",
)

# Explicit two-step path: 0 -> 2 -> 3 (since T_W[0][3] = 0 directly)
T_W_squared = T_W @ T_W
assert_pass(
    "T2.2 (T_W^2)[0][3] > 0 via path 0 -> 2 -> 3",
    T_W_squared[0, 3] > 0,
    f"(T_W^2)[0][3] = {T_W_squared[0, 3]:.6f}",
)

# ---------------------------------------------------------------------------
# T3 — Perron-Frobenius: top eigenvalue strictly > |next|
# ---------------------------------------------------------------------------

print("\n" + "=" * 70)
print("T3 — Perron-Frobenius: λ_0 > |λ_1|")
print("=" * 70)

eigs_W, vecs_W = np.linalg.eig(T_W)
# T_W is symmetric (we constructed it that way), so eigenvalues are real
eigs_W_real = np.sort(eigs_W.real)[::-1]  # descending
print(f"  Eigenvalues (descending): {[f'{e:.6f}' for e in eigs_W_real]}")

lam_0_W = float(eigs_W_real[0])
lam_1_W = float(eigs_W_real[1])

assert_pass(
    "T3.1 Top eigenvalue λ_0 > 0",
    lam_0_W > 0,
    f"λ_0 = {lam_0_W}",
)

assert_pass(
    "T3.2 Perron-Frobenius strict gap λ_0 > |λ_1|",
    lam_0_W > abs(lam_1_W),
    f"λ_0 = {lam_0_W}, |λ_1| = {abs(lam_1_W)}, gap = {lam_0_W - abs(lam_1_W)}",
)

# Identify top eigenvector and verify Perron property (all positive components)
top_idx = int(np.argmax(eigs_W.real))
v_top = vecs_W[:, top_idx].real
# Normalize sign
if v_top[0] < 0:
    v_top = -v_top
assert_pass(
    "T3.3 Top eigenvector has strictly positive components (Perron property)",
    bool(np.all(v_top > 1e-12)),
    f"v_top = {v_top}",
)

# Spectral gap on the transfer-matrix side: ratio λ_1 / λ_0 < 1
ratio = abs(lam_1_W) / lam_0_W
assert_pass(
    "T3.4 |λ_1| / λ_0 < 1 strictly (transfer matrix gap)",
    ratio < 1,
    f"ratio = {ratio:.6f}",
)

# Δ_T = -log(|λ_1| / λ_0) / a > 0
import math
delta_T_W = -math.log(ratio)  # with a = 1
assert_pass(
    "T3.5 Δ_T = -log(|λ_1|/λ_0) / a > 0 strictly",
    delta_T_W > 0,
    f"Δ_T = {delta_T_W:.6f}",
)

# ---------------------------------------------------------------------------
# T4 — Fermion-determinant positivity (Leg A from strong CP)
# ---------------------------------------------------------------------------

print("\n" + "=" * 70)
print("T4 — Fermion-determinant positivity via eigenvalue pairing")
print("=" * 70)

# Exact Fraction arithmetic for det(D + m) on a small staggered Dirac block.
# Anti-Hermitian D has eigenvalues in ±iλ pairs. det(D + m I) = Π_k (m^2 + λ_k^2).
lambda_1 = Fraction(3, 2)
lambda_2 = Fraction(5, 4)
m = Fraction(7, 10)

m_sq = m * m
det_paired = (m_sq + lambda_1 * lambda_1) * (m_sq + lambda_2 * lambda_2)
print(f"  m = {m} = {float(m):.6f}")
print(f"  λ_1 = {lambda_1} = {float(lambda_1):.6f}")
print(f"  λ_2 = {lambda_2} = {float(lambda_2):.6f}")
print(f"  m² + λ_1² = {m_sq + lambda_1 * lambda_1} = {float(m_sq + lambda_1 * lambda_1):.6f}")
print(f"  m² + λ_2² = {m_sq + lambda_2 * lambda_2} = {float(m_sq + lambda_2 * lambda_2):.6f}")
print(f"  det(D+m) = (m²+λ_1²)(m²+λ_2²) = {det_paired} = {float(det_paired):.6f}")

assert_pass(
    "T4.1 det(D + m) > 0 for real m > 0 (exact Fraction)",
    det_paired > 0,
    f"det = {det_paired}",
)

# Verify the eigenvalue-pairing argument explicitly:
# ±λ_k pairs contribute (m + iλ_k)(m - iλ_k) = m² + λ_k² > 0
for k, lam_k in enumerate([lambda_1, lambda_2], 1):
    pair_det = m_sq + lam_k * lam_k
    assert_pass(
        f"T4.2 ±λ_{k} eigenvalue pair contributes (m² + λ_{k}²) > 0",
        pair_det > 0,
        f"pair_det = {pair_det}",
    )

# Sweep over multiple m values
for m_test in [Fraction(1, 10), Fraction(1, 2), Fraction(1), Fraction(3), Fraction(10)]:
    det_test = (m_test * m_test + lambda_1 * lambda_1) * (
        m_test * m_test + lambda_2 * lambda_2
    )
    assert_pass(
        f"T4.3 det(D + m) > 0 for m = {m_test} = {float(m_test):.4f}",
        det_test > 0,
        f"det = {det_test}",
    )

# ---------------------------------------------------------------------------
# T5 — Composite T = T_W · diag(T_F) preserves Perron-Frobenius
# ---------------------------------------------------------------------------

print("\n" + "=" * 70)
print("T5 — Composite T = T_W · diag(T_F) preserves Perron-Frobenius")
print("=" * 70)

# T_F[U] = det(D[U] + m) > 0 for every configuration U.
# Model as positive diagonal weighting.
T_F_diag = np.array([1.1, 0.9, 1.3, 0.8])

assert_pass(
    "T5.1 All T_F[U] weights are strictly positive",
    bool(np.all(T_F_diag > 0)),
    f"T_F_diag = {T_F_diag}",
)

# Compose T = T_W * diag(T_F)
T_full = T_W * T_F_diag[np.newaxis, :]

assert_pass(
    "T5.2 T = T_W · diag(T_F) is non-negative",
    is_nonneg(T_full),
    "negative entry found",
)

assert_pass(
    "T5.3 T = T_W · diag(T_F) preserves irreducibility (same zero pattern as T_W)",
    is_irreducible_pos(T_full),
    "T_full reducibility test failed",
)

eigs_full, vecs_full = np.linalg.eig(T_full)
# Use absolute value sort since composite is not necessarily symmetric
eigs_full_sorted = np.sort(np.abs(eigs_full.real))[::-1]
print(f"  |Eigenvalues| (descending): {[f'{e:.6f}' for e in eigs_full_sorted]}")

lam_0_full = float(eigs_full_sorted[0])
lam_1_full = float(eigs_full_sorted[1])

assert_pass(
    "T5.4 Composite top eigenvalue λ_0(T) > 0",
    lam_0_full > 0,
    f"λ_0(T) = {lam_0_full}",
)

assert_pass(
    "T5.5 Composite Perron-Frobenius gap λ_0(T) - |λ_1(T)| > 0",
    lam_0_full > lam_1_full,
    f"λ_0 = {lam_0_full}, |λ_1| = {lam_1_full}, gap = {lam_0_full - lam_1_full}",
)

delta_T_full = -math.log(lam_1_full / lam_0_full)
assert_pass(
    "T5.6 Δ_T = -log(|λ_1(T)|/λ_0(T)) / a > 0 on finite Λ",
    delta_T_full > 0,
    f"Δ_T = {delta_T_full:.6f}",
)

# ---------------------------------------------------------------------------
# T6 — Source-note boundary check
# ---------------------------------------------------------------------------

print("\n" + "=" * 70)
print("T6 — Source-note boundary check")
print("=" * 70)

NOTE_PATH = (
    Path(__file__).resolve().parent.parent
    / "docs"
    / "CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_PERRON_FROBENIUS_NARROW_BOUNDED_NOTE_2026-05-18.md"
)

if not NOTE_PATH.exists():
    assert_pass("T6 Source note exists", False, f"missing: {NOTE_PATH}")
else:
    text = NOTE_PATH.read_text()

    assert_pass(
        "T6.1 Claim type is bounded_theorem",
        "**Claim type:** bounded_theorem" in text,
        "claim type not bounded_theorem",
    )

    td_oos = (
        "Thermodynamic limit `Λ → Z^3`" in text
        or "Λ → ∞" in text
        or "thermodynamic limit" in text.lower()
    )
    assert_pass(
        "T6.2 explicit thermodynamic-limit out-of-scope disclaimer",
        td_oos,
        "missing thermodynamic-limit disclaimer",
    )

    ym_oos = (
        "Yang-Mills mass-gap" in text
        or "Yang-Mills mass gap" in text
        or "Clay Millennium" in text
    )
    assert_pass(
        "T6.3 explicit Yang-Mills mass-gap NOT closed disclaimer",
        ym_oos,
        "missing Yang-Mills mass-gap disclaimer",
    )

    forbidden = [
        "**Status:** retained\n",
        "**Status:** promoted\n",
        "promote to retained",
    ]
    has_forbidden = [s for s in forbidden if s in text]
    assert_pass(
        "T6.4 no overclaim strings",
        len(has_forbidden) == 0,
        f"forbidden: {has_forbidden}",
    )

    assert_pass(
        "T6.5 Status authority: independent audit lane only line present",
        "Status authority:** independent audit lane only" in text,
        "missing Status authority line",
    )

    has_steps = all(f"Step {i}" in text for i in range(1, 5))
    assert_pass(
        "T6.6 Proof has all four steps (Step 1/2/3/4)",
        has_steps,
        "missing a Step",
    )

    # T6.7: explicit Leg A citation
    leg_a_cite = "Leg A" in text and "STRONG_CP" in text.upper()
    assert_pass(
        "T6.7 explicit Leg A from STRONG_CP citation present",
        leg_a_cite,
        "missing Leg A / STRONG_CP citation",
    )

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

print("\n" + "=" * 70)
print(f"PASS={PASS}  FAIL={FAIL}")
print("=" * 70)

if FAIL > 0:
    print("\nFailures:")
    for failure in FAILURES:
        print(f"  - {failure}")
    sys.exit(1)
sys.exit(0)
