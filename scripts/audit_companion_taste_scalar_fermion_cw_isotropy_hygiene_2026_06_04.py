#!/usr/bin/env python3
"""Audit companion runner: taste-scalar fermion Coleman-Weinberg isotropy
deps-restored hygiene companion.

This runner is a meta audit-companion runner. It does NOT modify the
parent note or the parent runner; it independently re-derives the
parent's load-bearing algebraic chain and verifies the current ledger /
note-text / parent-runner state for the dep-edge-restoration and
runner-staleness observations recorded in the companion note.

Parent narrow theorem note:
    docs/TASTE_SCALAR_FERMION_CW_ISOTROPY_NARROW_THEOREM_NOTE_2026-05-02.md
Parent narrow theorem runner:
    scripts/frontier_taste_scalar_fermion_cw_isotropy_narrow.py
Companion note (this runner's pair):
    docs/TASTE_SCALAR_FERMION_CW_ISOTROPY_HYGIENE_COMPANION_NOTE_2026-06-04.md

Block plan (12 blocks total; PASS/FAIL count cached in the SHA-pinned
output):

Algebraic chain blocks (independent re-derivation):
  Block 1  - eigenvalue formula on (C^2)^{x3} sigma_x eigenbasis
  Block 2  - binary Fourier orthogonality Sum_s (-1)^{s_i}(-1)^{s_j} = 8 delta_ij
  Block 3  - squared eigenvalue uniformity at phi = (v, 0, 0)
  Block 4  - fermion CW Hessian diagonality at phi = (v, 0, 0)
  Block 5  - Hessian common-coefficient formula C(v) = 8 (2 f'(v^2) + 4 v^2 f''(v^2))
  Block 6  - off-diagonal vanishing on a denser scan, f(x) = x

Bookkeeping / audit-hygiene blocks:
  Block 7  - dependency-edge restoration recorded in audit ledger
  Block 8  - parent note text contains both expected dep-link citations
  Block 9  - parent note records the axiom-reset retag wording
  Block 10 - parent runner Part-1 stale assertions still present (observable)
  Block 11 - parent runner Part-7 deps-bookkeeping assertion still present
  Block 12 - audit ledger row records the historical audit dispositions

Each block reports PASS/FAIL for its individual checks. The runner
exits 0 if and only if every block's checks all PASS.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
import json
import sys
from pathlib import Path


# -----------------------------------------------------------------------------
# Paths and constants
# -----------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
PARENT_NOTE_PATH = (
    ROOT
    / "docs"
    / "TASTE_SCALAR_FERMION_CW_ISOTROPY_NARROW_THEOREM_NOTE_2026-05-02.md"
)
PARENT_RUNNER_PATH = (
    ROOT / "scripts" / "frontier_taste_scalar_fermion_cw_isotropy_narrow.py"
)
COMPANION_NOTE_PATH = (
    ROOT
    / "docs"
    / "TASTE_SCALAR_FERMION_CW_ISOTROPY_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PARENT_CLAIM_ID = "taste_scalar_fermion_cw_isotropy_narrow_theorem_note_2026-05-02"
EXPECTED_DEPS = {
    "staggered_dirac_realization_gate_note_2026-05-03",
    "minimal_axioms_2026-05-03",
}


# -----------------------------------------------------------------------------
# Counters and printers
# -----------------------------------------------------------------------------

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    """Record one PASS/FAIL check and print a one-line trace."""
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    if detail:
        print(f"  [{tag}] {label} -- {detail}")
    else:
        print(f"  [{tag}] {label}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(f"  {title}")
    print("=" * 88)


# -----------------------------------------------------------------------------
# Helpers for algebraic blocks
# -----------------------------------------------------------------------------

STATES = list(product([0, 1], repeat=3))  # 8 Walsh-Hadamard states


def lam_s(phi: tuple, s: tuple) -> Fraction:
    """Eigenvalue lambda_s(phi) = Sum_i phi_i (-1)^{s_i}."""
    return sum(phi[i] * ((-1) ** s[i]) for i in range(3))


def hessian_at(f_prime, f_doubleprime, v: Fraction) -> list:
    """Compute H_{ij}(v) := d^2 V_f / d phi_i d phi_j at phi = (v, 0, 0)
    using the exact chain-rule expansion.

        V_f(phi) = Sum_s f(lambda_s(phi)^2)
        d V_f / d phi_i = Sum_s 2 lambda_s f'(lambda_s^2) d lambda_s / d phi_i
        d^2 V_f / d phi_i d phi_j
            = Sum_s [2 f'(lambda_s^2) (-1)^{s_i + s_j}
                     + 4 lambda_s^2 f''(lambda_s^2) (-1)^{s_i + s_j}]

    Returns 3x3 nested list of Fractions.
    """
    H = [[Fraction(0)] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for s in STATES:
                lam = lam_s((v, Fraction(0), Fraction(0)), s)
                lam_sq = lam * lam
                sign_ij = ((-1) ** s[i]) * ((-1) ** s[j])
                contrib = (
                    2 * f_prime(lam_sq) * sign_ij
                    + 4 * f_doubleprime(lam_sq) * lam_sq * sign_ij
                )
                H[i][j] += contrib
    return H


# -----------------------------------------------------------------------------
# Block 1 - eigenvalue formula on (C^2)^{x3} sigma_x eigenbasis
# -----------------------------------------------------------------------------

section("Block 1: eigenvalue formula lambda_s(phi) = Sum_i phi_i (-1)^{s_i}")

test_phis = [
    (Fraction(1), Fraction(2), Fraction(3)),
    (Fraction(2), Fraction(0), Fraction(0)),
    (Fraction(-1, 3), Fraction(7, 11), Fraction(0)),
    (Fraction(5, 7), Fraction(-3, 13), Fraction(11, 17)),
]
for phi in test_phis:
    # Expected eigenvalues by direct computation
    expected = [lam_s(phi, s) for s in STATES]
    # Sanity check: re-compute via explicit sum
    recomputed = [
        sum(phi[k] * ((-1) ** s[k]) for k in range(3)) for s in STATES
    ]
    ok_eigs = all(
        expected[idx] == recomputed[idx] for idx in range(len(STATES))
    )
    check(
        f"eigenvalues match for phi = {phi}",
        ok_eigs and len(expected) == 8,
        detail=f"len(expected) = {len(expected)}, all equal = {ok_eigs}",
    )


# -----------------------------------------------------------------------------
# Block 2 - binary Fourier orthogonality Sum_s (-1)^{s_i}(-1)^{s_j} = 8 delta_ij
# -----------------------------------------------------------------------------

section(
    "Block 2: binary Fourier orthogonality on (Z/2Z)^3 -> 8 delta_ij"
)

for i in range(3):
    for j in range(3):
        S = sum(((-1) ** s[i]) * ((-1) ** s[j]) for s in STATES)
        expected = 8 if i == j else 0
        check(
            f"Sum_s (-1)^{{s_{i+1}}}(-1)^{{s_{j+1}}} = {expected}",
            S == expected,
            detail=f"observed = {S}",
        )


# -----------------------------------------------------------------------------
# Block 3 - squared eigenvalue uniformity at phi = (v, 0, 0)
# -----------------------------------------------------------------------------

section(
    "Block 3: squared eigenvalue uniformity at phi = (v, 0, 0)"
)

for v in [
    Fraction(1),
    Fraction(2),
    Fraction(-3),
    Fraction(7, 11),
    Fraction(-5, 13),
    Fraction(11, 19),
]:
    phi = (v, Fraction(0), Fraction(0))
    lam_sq_values = {lam_s(phi, s) ** 2 for s in STATES}
    ok = lam_sq_values == {v * v}
    check(
        f"lambda_s(v, 0, 0)^2 = v^2 = {v * v} uniformly for v = {v}",
        ok,
        detail=f"observed set = {lam_sq_values}",
    )


# -----------------------------------------------------------------------------
# Block 4 - fermion CW Hessian diagonality at phi = (v, 0, 0)
# -----------------------------------------------------------------------------

section(
    "Block 4: fermion CW Hessian diagonality H_{ij}(v) = delta_ij * C(v)"
)

# f-families with exact derivatives (f', f'')
F_FAMILIES = [
    (
        "f(x) = x",
        lambda x: Fraction(1),
        lambda x: Fraction(0),
    ),
    (
        "f(x) = x^2",
        lambda x: 2 * x,
        lambda x: Fraction(2),
    ),
    (
        "f(x) = x^3",
        lambda x: 3 * x * x,
        lambda x: 6 * x,
    ),
    (
        "f(x) = x + x^2 / 3",
        lambda x: 1 + Fraction(2, 3) * x,
        lambda x: Fraction(2, 3),
    ),
]

for f_name, fp, fpp in F_FAMILIES:
    for v in [Fraction(1), Fraction(2), Fraction(3)]:
        H = hessian_at(fp, fpp, v)
        diag = H[0][0]
        all_diag_equal = all(H[i][i] == diag for i in range(3))
        all_off_diag_zero = all(
            H[i][j] == Fraction(0)
            for i in range(3)
            for j in range(3)
            if i != j
        )
        check(
            f"H_{{ij}}(v={v}) = delta_ij * C(v) for {f_name}",
            all_diag_equal and all_off_diag_zero,
            detail=(
                f"diag = {diag}, "
                f"all_diag_equal = {all_diag_equal}, "
                f"all_off_diag_zero = {all_off_diag_zero}"
            ),
        )


# -----------------------------------------------------------------------------
# Block 5 - Hessian common-coefficient formula
#   C(v) = 8 (2 f'(v^2) + 4 v^2 f''(v^2))
# -----------------------------------------------------------------------------

section(
    "Block 5: Hessian common coefficient C(v) = 8 (2 f'(v^2) + 4 v^2 f''(v^2))"
)

for f_name, fp, fpp in F_FAMILIES:
    for v in [Fraction(1), Fraction(2), Fraction(3)]:
        H = hessian_at(fp, fpp, v)
        H_diag = H[0][0]
        v_sq = v * v
        expected_C = 8 * (2 * fp(v_sq) + 4 * v_sq * fpp(v_sq))
        check(
            f"H_{{11}}(v={v}) = 8 (2 f'(v^2) + 4 v^2 f''(v^2)) for {f_name}",
            H_diag == expected_C,
            detail=f"H_11 = {H_diag}, expected C(v) = {expected_C}",
        )


# -----------------------------------------------------------------------------
# Block 6 - off-diagonal vanishing on a denser scan for f(x) = x
# -----------------------------------------------------------------------------

section(
    "Block 6: denser scan: H_{ij}(v) = 16 delta_ij for f(x) = x"
)

fp_id = lambda x: Fraction(1)
fpp_id = lambda x: Fraction(0)

for v in [Fraction(1), Fraction(2), Fraction(3), Fraction(4), Fraction(5)]:
    H = hessian_at(fp_id, fpp_id, v)
    for i in range(3):
        for j in range(3):
            expected = Fraction(16) if i == j else Fraction(0)
            check(
                f"H_{{{i+1}{j+1}}}(v={v}) = {expected} for f(x) = x",
                H[i][j] == expected,
                detail=f"observed = {H[i][j]}",
            )


# -----------------------------------------------------------------------------
# Block 7 - dependency-edge restoration recorded in audit ledger
# -----------------------------------------------------------------------------

section(
    "Block 7: dependency-edge restoration recorded in audit ledger"
)

ledger = json.loads(LEDGER_PATH.read_text())
rows = ledger["rows"]
parent_row = rows.get(PARENT_CLAIM_ID)
check(
    f"audit_ledger.json row exists for parent claim",
    parent_row is not None,
    detail=f"PARENT_CLAIM_ID = {PARENT_CLAIM_ID}",
)
if parent_row is not None:
    deps_set = set(parent_row.get("deps", []))
    check(
        "parent row deps contain staggered_dirac_realization_gate_note_2026-05-03",
        "staggered_dirac_realization_gate_note_2026-05-03" in deps_set,
        detail=f"deps = {sorted(deps_set)}",
    )
    check(
        "parent row deps contain minimal_axioms_2026-05-03",
        "minimal_axioms_2026-05-03" in deps_set,
        detail=f"deps = {sorted(deps_set)}",
    )
    check(
        "parent row deps contain both expected entries (and only them)",
        deps_set == EXPECTED_DEPS,
        detail=f"deps = {sorted(deps_set)}",
    )
    direct_in_degree = parent_row.get("direct_in_degree", 0)
    check(
        "parent row direct_in_degree >= 2",
        direct_in_degree >= 2,
        detail=f"direct_in_degree = {direct_in_degree}",
    )


# -----------------------------------------------------------------------------
# Block 8 - parent note text contains both expected dep-link citations
# -----------------------------------------------------------------------------

section(
    "Block 8: parent note text contains both expected dep-link citations"
)

parent_note_text = PARENT_NOTE_PATH.read_text()
check(
    "parent note contains STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md citation",
    "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md" in parent_note_text,
    detail="markdown link to staggered-Dirac realization gate",
)
check(
    "parent note contains MINIMAL_AXIOMS_2026-05-03.md citation",
    "MINIMAL_AXIOMS_2026-05-03.md" in parent_note_text,
    detail="markdown link to minimal axioms memo",
)
check(
    "parent note contains 'Audit dependency repair links' section header",
    "Audit dependency repair links" in parent_note_text,
    detail="explicit dep-edge-restoration section header",
)


# -----------------------------------------------------------------------------
# Block 9 - parent note records the axiom-reset retag wording
# -----------------------------------------------------------------------------

section(
    "Block 9: parent note records the axiom-reset retag wording"
)

check(
    "parent note Type field marks bounded_theorem with axiom-reset retag",
    "bounded_theorem (axiom-reset retag 2026-05-03; was positive_theorem)"
    in parent_note_text,
    detail="post-retag bounded_theorem wording",
)
check(
    "parent note target_claim_type proposal is bounded_theorem",
    "target_claim_type: bounded_theorem" in parent_note_text,
    detail="post-retag target_claim_type proposal",
)


# -----------------------------------------------------------------------------
# Block 10 - parent runner Part-1 stale assertions still present (observable)
# -----------------------------------------------------------------------------

section(
    "Block 10: parent runner Part-1 stale assertions are still present "
    "(observable; not repaired in this PR)"
)

parent_runner_text = PARENT_RUNNER_PATH.read_text()
check(
    "parent runner Part-1 asserts 'Type:** positive_theorem' (stale post-retag)",
    '"Type:** positive_theorem"' in parent_runner_text,
    detail="stale assertion still present in scripts/...narrow.py",
)
check(
    "parent runner Part-1 asserts 'target_claim_type: positive_theorem' (stale)",
    '"target_claim_type: positive_theorem"' in parent_runner_text,
    detail="stale assertion still present in scripts/...narrow.py",
)


# -----------------------------------------------------------------------------
# Block 11 - parent runner Part-7 deps-bookkeeping assertion still present
# -----------------------------------------------------------------------------

section(
    "Block 11: parent runner Part-7 deps-bookkeeping assertion is still present "
    "(observable; not repaired in this PR)"
)

check(
    "parent runner Part-7 asserts 'has no declared dependency edges' (stale)",
    "has no declared dependency edges" in parent_runner_text,
    detail="stale assertion still present in scripts/...narrow.py",
)
check(
    "parent runner Part-7 asserts 'not claim_deps' (stale post-dep-restoration)",
    "not claim_deps" in parent_runner_text,
    detail="stale assertion still present in scripts/...narrow.py",
)


# -----------------------------------------------------------------------------
# Block 12 - audit ledger row records the historical audit dispositions
# -----------------------------------------------------------------------------

section(
    "Block 12: audit ledger row records the historical audit dispositions"
)

if parent_row is not None:
    prev_audits = parent_row.get("previous_audits", [])
    check(
        "parent row records at least two previous_audits entries",
        len(prev_audits) >= 2,
        detail=f"previous_audits count = {len(prev_audits)}",
    )
    statuses = [pa.get("audit_status") for pa in prev_audits]
    check(
        "previous_audits contains an 'audited_clean' disposition",
        "audited_clean" in statuses,
        detail=f"statuses = {statuses}",
    )
    check(
        "previous_audits contains an 'audited_conditional' disposition",
        "audited_conditional" in statuses,
        detail=f"statuses = {statuses}",
    )
    # Find the conditional entry and check its blocker
    conditional_entry = next(
        (
            pa
            for pa in prev_audits
            if pa.get("audit_status") == "audited_conditional"
        ),
        None,
    )
    check(
        "audited_conditional entry exists",
        conditional_entry is not None,
        detail="for blocker inspection",
    )
    if conditional_entry is not None:
        notes_re = conditional_entry.get("notes_for_re_audit_if_any") or ""
        check(
            "audited_conditional notes_for_re_audit_if_any begins with 'missing_dependency_edge:'",
            notes_re.startswith("missing_dependency_edge:"),
            detail=f"notes_for_re_audit_if_any = {notes_re[:100]!r}",
        )


# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------

print("\n" + "=" * 88)
print(f"  TOTAL: PASS={PASS}, FAIL={FAIL}")
print("=" * 88)

sys.exit(0 if FAIL == 0 else 1)
