#!/usr/bin/env python3
"""No-go audit for retained APS/Wald/Gauss boundary source principles.

Target: derive the APS-locked source cross term

    S_int = - chi_eta M_phys <rho, Phi>

from retained boundary ingredients rather than adding it as a new premise.

The audit models the weak-field source derivative over the two APS sectors.
Within the retained separable class, the available source-current vectors are:

    positive Born/Gauss source:  [ +1, +1 ]
    APS eta spectator:          [  0,  0 ]
    positive Wald area carrier: [  0,  0 ]
    finite gap penalty:         [  0,  0 ]

The required signed source is [ +1, -1 ].  It appears only when the explicit
orientation-odd cross term chi_eta*rho*Phi is added.

This is not a physical signed-gravity claim.
"""

from __future__ import annotations

import math
import os
import sys
from dataclasses import dataclass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from scripts.numpy_replay_bootstrap import ensure_numpy_runtime

ensure_numpy_runtime(__file__, sys.argv)

import numpy as np

from scripts.signed_gravity_aps_boundary_index_probe import (  # noqa: E402
    boundary_model,
    chi_from_eta,
    eta_delta,
)


TOL = 1.0e-10
PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, passed: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    if passed:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    status = "PASS" if passed else "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"[{status}] {name}{suffix}")
    return passed


@dataclass(frozen=True)
class PrincipleTerm:
    name: str
    source_vector: np.ndarray
    retained: bool
    protects_gap: bool
    note: str


def retained_terms() -> list[PrincipleTerm]:
    z = np.array([0.0, 0.0])
    return [
        PrincipleTerm(
            "positive_born_gauss",
            np.array([1.0, 1.0]),
            True,
            False,
            "retained positive physical source scale",
        ),
        PrincipleTerm(
            "aps_eta_spectator",
            z,
            True,
            False,
            "topological label, Phi-source neutral on gapped sector",
        ),
        PrincipleTerm(
            "positive_wald_area",
            z,
            True,
            False,
            "positive area carrier, Phi-source neutral",
        ),
        PrincipleTerm(
            "finite_gap_penalty",
            z,
            False,
            False,
            "can discourage zero crossing but is not a hard superselection",
        ),
        PrincipleTerm(
            "hard_gap_constraint",
            z,
            False,
            True,
            "protects sector only by adding a new admissibility constraint",
        ),
        PrincipleTerm(
            "chi_rho_phi_cross_term",
            np.array([1.0, -1.0]),
            False,
            False,
            "exact proposed source term; new orientation-odd coupling",
        ),
    ]


def fit_source(terms: list[PrincipleTerm]) -> tuple[float, np.ndarray, np.ndarray]:
    target = np.array([1.0, -1.0])
    mat = np.column_stack([term.source_vector for term in terms])
    coeffs, *_ = np.linalg.lstsq(mat, target, rcond=None)
    fitted = mat @ coeffs
    return float(np.linalg.norm(fitted - target)), coeffs, fitted


def chi_path_across_zero() -> tuple[list[int], list[float]]:
    d0 = boundary_model(+1, gap=0.4)
    g0 = abs(float(np.real(d0[0, 0])))
    chis: list[int] = []
    gaps: list[float] = []
    for t in np.linspace(1.0, -1.0, 9):
        d = d0.copy()
        d[0, 0] = g0 * t
        eta, zero, _, vals = eta_delta(d, delta=1.0e-9)
        chis.append(chi_from_eta(eta, zero))
        gaps.append(float(np.min(np.abs(vals))))
    return chis, gaps


def finite_gap_barrier_values(epsilon: float = 1.0e-3) -> tuple[float, float, float]:
    _chis, gaps = chi_path_across_zero()
    vals = [1.0 / (gap * gap + epsilon * epsilon) for gap in gaps]
    return float(min(vals)), float(max(vals)), float(vals[len(vals) // 2])


def hard_gap_allowed(g_min: float = 0.1) -> tuple[bool, list[bool]]:
    _chis, gaps = chi_path_across_zero()
    allowed = [gap >= g_min for gap in gaps]
    return all(allowed), allowed


def orientation_symmetry_readout() -> tuple[bool, bool]:
    """Positive retained carrier is orientation-even; signed source is odd."""

    positive_source = np.array([1.0, 1.0])
    signed_source = np.array([1.0, -1.0])
    swap = np.array([[0.0, 1.0], [1.0, 0.0]])
    positive_even = np.allclose(swap @ positive_source, positive_source)
    signed_odd = np.allclose(swap @ signed_source, -signed_source)
    return bool(positive_even), bool(signed_odd)


def n5_execution_certificate() -> None:
    """Print-only record of what this runner resolves at each granularity.

    Adds no check and touches no counter.  No scan-derived value is quoted;
    grid size, range, tolerances and thresholds are named instead.
    """
    print()
    print("=" * 104)
    print("N5 execution certificate (print-only; adds no check and no counter)")
    print("=" * 104)
    print(
        "per_element: resolved as single-entry moves on a diagonal boundary operator -- the "
        "sector-crossing path is driven by rewriting exactly one entry, the [0,0] slot carrying the "
        "unpaired level, while all ten remaining diagonal entries stay pinned at their model values. "
        "The source side is decided component by component in the same spirit: each principle term "
        "contributes its own two-component column, and every verdict is the residual between the "
        "assembled column combination and the target components +1 and -1."
    )
    print(
        "per_site: checked and not executed -- the boundary operator is a toy spectral model, an "
        "eleven-by-eleven diagonal matrix of energy levels with no spatial index standing behind it, "
        "and the source objects are two-component sector amplitudes. No coordinate, neighbour "
        "relation, or site amplitude is built anywhere in the file, so there is no site-resolved "
        "quantity available to resolve and none is claimed."
    )
    print(
        "per_mode: resolved level by level -- the model carries eleven modes, one unpaired boundary "
        "level sitting at plus or minus the gap 0.4 and five symmetric pairs at 0.4 + 0.35*(j+1) for "
        "j from 0 through 4, whose positive and negative partners cancel out of eta by construction. "
        "eta_delta sorts each level individually into positive, negative, or zero against "
        "delta = 1e-9, so the invariant is assembled one mode at a time, and the gap recorded at "
        "every scan point is the minimum absolute level, again a per-mode reading."
    )
    print(
        "per_block: resolved as a paired-versus-unpaired spectral split, and separately as a "
        "retained-versus-added partition of the source basis -- the ten paired levels form a block "
        "contributing exactly nothing to eta while the single unpaired level is the entire eta "
        "carrier, which is precisely why moving that one level suffices to cross sectors. On the "
        "source side the six principle terms are partitioned three ways, into the retained block, "
        "that block extended by the two gap terms, and the retained block adjoined to the "
        "orientation-odd cross term, with least squares run separately on each partition."
    )
    print(
        "lattice_wide: checked and not executed -- no lattice, volume, box, or extent appears "
        "anywhere in this runner, the largest object being that eleven-by-eleven diagonal matrix. "
        "The blocking reason is the note's own finding: no retained boundary source principle is in "
        "hand, so there is no global theorem here whose lattice-scale content could be exercised, "
        "and this file asserts nothing about one."
    )
    print(
        "Determinism: no RNG, optimizer, root-finding, or Monte Carlo is used. The single sweep is a "
        "fixed grid of 9 evenly spaced values of t running from +1.0 down to -1.0, rescaling only the "
        "carrier level. Following the scan rule, this certificate names that grid size and range "
        "together with the tolerances delta = 1e-9 and TOL = 1e-10, the barrier regulator "
        "epsilon = 1e-3, and the hard-gap threshold g_min = 0.1, and it interpolates none of the "
        "scan-derived gap or barrier magnitudes. The sector labels along the path are exact integer "
        "classifications: four +1 readings, a single 0 exactly at the crossing, then four -1 readings."
    )


def main() -> int:
    print("=" * 104)
    print("RETAINED BOUNDARY SOURCE PRINCIPLE NO-GO AUDIT")
    print("  APS/Wald/Gauss retained class versus chi_eta rho Phi cross term")
    print("=" * 104)
    print()

    terms = retained_terms()

    print("SOURCE-CURRENT BASIS")
    print(f"  {'term':<26s} {'retained':>8s} {'gap':>6s} {'source +/-':>16s}  note")
    for term in terms:
        print(
            f"  {term.name:<26s} {'YES' if term.retained else 'NO':>8s} "
            f"{'YES' if term.protects_gap else 'NO':>6s} "
            f"[{term.source_vector[0]:+4.1f},{term.source_vector[1]:+4.1f}]  {term.note}"
        )
    print()

    retained_only = [term for term in terms if term.retained]
    residual_retained, coeffs_retained, fitted_retained = fit_source(retained_only)
    check(
        "retained APS/Wald/Gauss source basis cannot span signed source",
        residual_retained > 1.0,
        f"residual={residual_retained:.3e}, fitted={np.round(fitted_retained, 3)}",
    )

    retained_plus_gap = [
        term
        for term in terms
        if term.retained or term.name in {"finite_gap_penalty", "hard_gap_constraint"}
    ]
    residual_gap, _coeffs_gap, fitted_gap = fit_source(retained_plus_gap)
    check(
        "gap penalties/constraints alone do not create a Phi source",
        residual_gap > 1.0,
        f"residual={residual_gap:.3e}, fitted={np.round(fitted_gap, 3)}",
    )

    with_cross = retained_only + [term for term in terms if term.name == "chi_rho_phi_cross_term"]
    residual_cross, coeffs_cross, fitted_cross = fit_source(with_cross)
    check(
        "signed source appears exactly when the cross term is added",
        residual_cross < TOL and abs(coeffs_cross[-1] - 1.0) < TOL,
        f"residual={residual_cross:.3e}, fitted={np.round(fitted_cross, 3)}",
    )
    positive_even, signed_odd = orientation_symmetry_readout()
    check(
        "retained positive source is orientation-even while desired source is orientation-odd",
        positive_even and signed_odd,
    )
    print()

    print("APS GAP-PROTECTION CHECK")
    chi_path, gaps = chi_path_across_zero()
    check(
        "continuous path between eta sectors crosses zero",
        chi_path[:4] == [+1, +1, +1, +1] and chi_path[4] == 0 and chi_path[-4:] == [-1, -1, -1, -1],
        f"chi_path={chi_path}",
    )
    barrier_min, barrier_max, barrier_mid = finite_gap_barrier_values()
    check(
        "finite gap penalty is not a topological superselection rule",
        math.isfinite(barrier_mid) and math.isfinite(barrier_max),
        f"V_gap min={barrier_min:.2e}, midpoint={barrier_mid:.2e}, max={barrier_max:.2e}",
    )
    all_allowed, allowed = hard_gap_allowed()
    check(
        "hard gap protection works only as an added admissibility constraint",
        (not all_allowed) and allowed[:4] == [True, True, True, True] and not allowed[4],
        f"allowed_path={allowed}",
    )
    print()

    n5_execution_certificate()

    print("INTERPRETATION")
    print("  Retained positive source + APS spectator + positive Wald carrier cannot")
    print("  generate the orientation-odd signed source current.")
    print("  Gap protection is also not derived by eta itself: a finite path reaches")
    print("  the null crossing unless a hard gap constraint is added.")
    print("  Therefore a retained boundary source principle is not in hand.")
    print()
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("FINAL_TAG: RETAINED_BOUNDARY_SOURCE_PRINCIPLE_NO_GO")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
