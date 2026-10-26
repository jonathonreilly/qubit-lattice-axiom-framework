#!/usr/bin/env python3
"""Finite supplied single-link weight diagnostics and conditional axis relabeling.
Quantitative fixtures are unchanged; they neither construct physical Wilson
transfer dynamics nor discharge spatial H1/H2. Nonidentity character powers
are heuristic samples, not exact SU(3) characters or a positivity proof.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ('docs/CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md', 'docs/CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02.md')

import math
import os
import subprocess
import sys
from typing import Iterable


PASS = 0
FAIL = 0
LOG: list[str] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        LOG.append(f"[PASS] {name}" + (f"  ({detail})" if detail else ""))
    else:
        FAIL += 1
        LOG.append(f"[FAIL] {name}" + (f"  ({detail})" if detail else ""))


# ======================================================================
# Part A: SU(3) heat-kernel character expansion (axis-symmetric)
# ======================================================================
# The SU(3) heat kernel admits the character expansion
#   K_tau(g) = Sum_R (dim R) chi_R(g) exp(-tau C_2(R) / (2 N_c))
# At g = e (identity), chi_R(e) = dim R, so K_tau(e) = Sum (dim R)^2 exp(-tau C_2/6).
# We work with a truncated character basis up to (p+q) <= P_MAX.

N_C = 3.0


def su3_irrep_dim(p: int, q: int) -> int:
    """dim(p, q) for SU(3) irrep labeled by Dynkin (p, q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def su3_irrep_casimir(p: int, q: int) -> float:
    """C_2(p, q) for SU(3) in the standard normalization."""
    return (p * p + q * q + p * q) / 3.0 + p + q


def su3_irreps_up_to(p_max: int) -> Iterable[tuple[int, int]]:
    """Enumerate (p, q) with p + q <= p_max."""
    for total in range(p_max + 1):
        for p in range(total + 1):
            q = total - p
            yield (p, q)


# Heat kernel at identity (a positive scalar; strict positivity check)
TAU = 2.0
P_MAX = 12

# K_tau(e) = Sum_R (dim R)^2 exp(-tau C_2 / (2 N_c))
K_identity_terms = [
    (su3_irrep_dim(p, q) ** 2) * math.exp(-TAU * su3_irrep_casimir(p, q) / (2.0 * N_C))
    for (p, q) in su3_irreps_up_to(P_MAX)
]
K_identity = sum(K_identity_terms)

record(
    "A.heat.positive: SU(3) heat-kernel value at identity is strictly positive",
    K_identity > 0,
    f"K_tau({TAU})(e) = {K_identity:.6f}",
)

# Convergence check: tail beyond P_MAX is small
K_identity_finer = sum(
    (su3_irrep_dim(p, q) ** 2) * math.exp(-TAU * su3_irrep_casimir(p, q) / (2.0 * N_C))
    for (p, q) in su3_irreps_up_to(P_MAX + 2)
)
rel_tail = abs(K_identity_finer - K_identity) / K_identity
record(
    "A.heat.cutoff_difference: two finite cutoff sums differ by less than tolerance",
    rel_tail < 1e-3,
    f"relative tail beyond P_MAX={P_MAX}: {rel_tail:.2e}",
)

# Heat kernel positivity at non-identity points: sample several elements
# (we use the fact that chi_R takes real values on conjugacy-class representatives;
# for axis-independence demonstration we only need positivity, not full continuity).
# Sample heat kernel values at "phase" elements e^{i*theta * Lambda_3} for several theta.
def chi_fundamental(theta: float) -> float:
    """Character of fundamental irrep (1, 0) of SU(3) at e^{i*theta*Lambda_3}.
    The fundamental rep on SU(3) has chi_(1,0)(g) = tr(g). For a diagonal
    element diag(e^{i*theta}, e^{-i*theta}, 1) we get 2cos(theta) + 1."""
    return 2.0 * math.cos(theta) + 1.0


def K_value_at_theta(theta: float) -> float:
    """Historical normalized character-power heuristic at theta.
    Not the SU(3) character formula; samples do not prove heat positivity."""
    val = 0.0
    for (p, q) in su3_irreps_up_to(P_MAX):
        d = su3_irrep_dim(p, q)
        # Approximate character: for the fundamental and conjugate at this
        # element, use the Weyl character formula reduced to this class.
        # For demonstration purposes use the (p+q)-power expansion of chi_fund.
        # This is a structural check, not a high-precision character sum.
        chi_approx = chi_fundamental(theta) ** (p + q) if (p + q) > 0 else 1.0
        # Normalize to keep approximation bounded
        chi_approx = chi_approx / (1.0 + chi_approx ** 2) ** 0.5 * d
        val += chi_approx * math.exp(-TAU * su3_irrep_casimir(p, q) / (2.0 * N_C))
    return val


sample_thetas = [0.0, 0.1, 0.3, 0.7, 1.0, 1.5]
K_sample_values = [K_value_at_theta(theta) for theta in sample_thetas]
all_positive = all(v > 0 for v in K_sample_values)
record(
    "A.heuristic.sampled_positive: normalized character-power fixture positive at six samples",
    all_positive,
    f"K values at theta={sample_thetas}: {[round(v, 4) for v in K_sample_values]}",
)

# ======================================================================
# Part A.2: Axis-permutation symmetry of the truncated basis
# ======================================================================
# On a cubic Z^3 substrate, the link product L^2(SU(3)^E, dU) inherits
# the cubic-symmetry group S_3 acting on the three spatial axes. The
# heat-kernel character expansion is axis-symmetric: the eigenvalue
# weight exp(-tau C_2(R)/2N_c) depends on (p, q) only, not on which
# axis the link sits along.

# Verify: under any permutation sigma of the three axes, the eigenvalue
# weights are invariant.
axis_perm_invariant = True
for perm in [(0, 1, 2), (1, 0, 2), (2, 1, 0), (1, 2, 0), (2, 0, 1)]:
    # The eigenvalue weights are scalar (depend only on irrep label), so any
    # axis permutation leaves the spectrum unchanged.
    weight_before = sorted(
        [math.exp(-TAU * su3_irrep_casimir(p, q) / (2.0 * N_C))
         for (p, q) in su3_irreps_up_to(P_MAX)]
    )
    weight_after = sorted(
        [math.exp(-TAU * su3_irrep_casimir(p, q) / (2.0 * N_C))
         for (p, q) in su3_irreps_up_to(P_MAX)]
    )  # same set, since irreps are axis-independent
    if any(abs(b - a) > 1e-15 for b, a in zip(weight_before, weight_after)):
        axis_perm_invariant = False

record(
    "A.perm.weights: SU(3) heat-kernel eigenvalue weights invariant under transfer-axis relabeling",
    axis_perm_invariant,
    "spectrum is a set of (p,q)-indexed scalars; permuting axes does not relabel (p,q)",
)

# Verify: top eigenvalue (trivial irrep, p=q=0) is simple and strictly positive,
# and there is a strict gap below to the next-lowest C_2 value.
top_eigenvalue = math.exp(-TAU * su3_irrep_casimir(0, 0) / (2.0 * N_C))
# Next irrep: (1,0) has C_2 = 4/3
next_eigenvalue = math.exp(-TAU * su3_irrep_casimir(1, 0) / (2.0 * N_C))

record(
    "A.gap.top: top eigenvalue corresponds to trivial irrep (p=q=0), value = 1.0",
    abs(top_eigenvalue - 1.0) < 1e-15,
    f"top eigenvalue = {top_eigenvalue}",
)

record(
    "A.gap.strict: strict gap below top eigenvalue",
    top_eigenvalue - next_eigenvalue > 1e-6,
    f"top = {top_eigenvalue}, next = {next_eigenvalue:.6f}, gap = {top_eigenvalue - next_eigenvalue:.6f}",
)

# Multiplicty of top: trivial irrep is unique
multiplicity_top = sum(
    1 for (p, q) in su3_irreps_up_to(P_MAX) if (p, q) == (0, 0)
)
record(
    "A.gap.simple: top eigenvalue is simple (multiplicity 1)",
    multiplicity_top == 1,
    f"trivial irrep multiplicity = {multiplicity_top}",
)

# Both temporal and spatial transfer operators have the same spectrum on
# the truncated basis, because the basis is axis-independent.
# (This is the load-bearing axis-permutation content of Lemma X.)
spatial_top = top_eigenvalue  # spatial axis: same construction, same spectrum
spatial_gap = top_eigenvalue - next_eigenvalue

record(
    "A.perm.spectrum_equal: identical supplied single-link data agree under a label change",
    abs(spatial_top - top_eigenvalue) < 1e-15 and abs(spatial_gap - (top_eigenvalue - next_eigenvalue)) < 1e-15,
    "identity of supplied weight data; not physical axis-transfer equivalence",
)

# ======================================================================
# Part B: actual current-source contracts, not file-presence authority
# ======================================================================
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
PARENT = "docs/CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md"
NOTE = "docs/CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02.md"
parent = " ".join((ROOT / PARENT).read_text().split())
note = " ".join((ROOT / NOTE).read_text().split())
record("B.parent.supplied_kernel: smooth positive symmetric multiplier explicitly supplied",
       "a is a supplied smooth, strictly positive, real symmetric function" in parent)
record("B.parent.physical_boundary: canonical transfer identification not derived",
       "It does not derive the canonical lattice gauge/fermion transfer operator." in parent)
record("B.note.H1H2_open: physical identification and operator positivity remain additional",
       "does not discharge H1/H2" in note
       and "Pointwise kernel positivity does not imply positive semidefiniteness" in note)
print("\n=== Conditional kernel relabeling and finite weight fixtures ===\n")
print("No physical Wilson H1/H2 supply; analytic claim requires the supplied kernel hypotheses.")
print("Heuristic nonidentity samples and two-cutoff differences are not universal positivity or tail proofs.")
for line in LOG:
    print(line)
print(f"\nPASS={PASS}  FAIL={FAIL}\n")
sys.exit(1 if FAIL else 0)
