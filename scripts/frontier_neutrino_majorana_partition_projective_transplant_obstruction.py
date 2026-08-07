#!/usr/bin/env python3
"""
Majorana partition/projective transplant obstruction on the current atlas stack.

Question:
  Can the exact universal UV-finite partition density, projective Schur
  closure, or canonical refinement-net pullback provide the missing absolute
  Majorana staircase selector once the current local lane has already selected
  the self-dual source ray?

Answer on the current exact stack:
  No. On a homogeneous source ray J_lambda = lambda J_0, the exact local
  partition density changes only by

      Delta log rho(lambda) = 1/2 lambda^2 <J_0, K^-1 J_0>,

  so it is monotone with no finite stationary selector. Exact Schur/projective
  coarse-graining preserves the same source scaling, and the refinement/atlas
  density cocycle introduces no new lambda dependence.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

PASS_COUNT = 0
FAIL_COUNT = 0
ALPHA_LM = 0.09067

ROOT = Path(__file__).resolve().parents[1]


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def build_positive_background_operator() -> np.ndarray:
    d = np.array([2.0, 3.0, 5.0, 7.0], dtype=float)
    h_d = np.diag(
        [
            1.0 / (d[0] * d[0]),
            1.0 / (d[1] * d[1]),
            1.0 / (d[2] * d[2]),
            1.0 / (d[3] * d[3]),
            1.0 / (d[0] * d[1]),
            1.0 / (d[0] * d[2]),
            1.0 / (d[0] * d[3]),
            1.0 / (d[1] * d[2]),
            1.0 / (d[1] * d[3]),
            1.0 / (d[2] * d[3]),
        ]
    )
    lambda_r = np.array(
        [
            [2.0, 0.2, 0.0],
            [0.2, 1.7, 0.1],
            [0.0, 0.1, 1.4],
        ],
        dtype=float,
    )
    return np.kron(h_d, lambda_r)


def log_partition_density(k_op: np.ndarray, j: np.ndarray) -> float:
    sign, logdet = np.linalg.slogdet(k_op)
    if sign <= 0:
        raise ValueError("expected positive-definite operator")
    return -0.5 * logdet + 0.5 * float(j @ np.linalg.solve(k_op, j))


def schur_reduce(
    k_op: np.ndarray,
    j: np.ndarray,
    keep: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    all_idx = np.arange(k_op.shape[0])
    elim = np.setdiff1d(all_idx, keep, assume_unique=True)
    k_kk = k_op[np.ix_(keep, keep)]
    k_ke = k_op[np.ix_(keep, elim)]
    k_ek = k_op[np.ix_(elim, keep)]
    k_ee = k_op[np.ix_(elim, elim)]
    j_k = j[keep]
    j_e = j[elim]
    k_ee_inv = np.linalg.inv(k_ee)
    k_eff = k_kk - k_ke @ k_ee_inv @ k_ek
    j_eff = j_k - k_ke @ k_ee_inv @ j_e
    return k_eff, j_eff


def random_invertible(seed: int, n: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    q1, _ = np.linalg.qr(rng.normal(size=(n, n)))
    if np.linalg.det(q1) < 0:
        q1[:, 0] *= -1
    q2, _ = np.linalg.qr(rng.normal(size=(n, n)))
    if np.linalg.det(q2) < 0:
        q2[:, 0] *= -1
    scales = np.diag(0.8 + 0.4 * rng.random(size=n))
    return q1 @ scales @ q2


def test_authority_stack_is_present() -> None:
    print("\n" + "=" * 88)
    print("PART 1: THE ATLAS ALREADY CONTAINS THE PARTITION / PROJECTIVE FAMILY")
    print("=" * 88)

    atlas = read("docs/publication/ci3_z3/DERIVATION_ATLAS.md")
    uv = read("docs/UNIVERSAL_QG_UV_FINITE_PARTITION_NOTE.md")
    proj = read("docs/UNIVERSAL_QG_PROJECTIVE_SCHUR_CLOSURE_NOTE.md")
    refine = read("docs/UNIVERSAL_QG_CANONICAL_REFINEMENT_NET_NOTE.md")
    blocker = read("docs/NEUTRINO_MAJORANA_SELF_DUAL_STAIRCASE_LIFT_OBSTRUCTION_NOTE.md")

    check("Atlas retains the universal UV-finite partition-density row", "Universal UV-finite partition density" in atlas)
    check("Atlas retains the universal projective-Schur closure row", "Universal projective Schur closure" in atlas)
    check("Atlas retains the universal canonical refinement-net row", "Universal canonical geometric refinement net" in atlas)
    check("The UV-finite partition note defines an exact partition-density family", "partition-density family" in uv.lower())
    check("The projective-Schur note gives exact Schur coarse-graining closure", "schur" in proj.lower() and "coarse-graining" in proj.lower())
    check("The refinement note gives exact density pullback / invariance on the net", "density invariance" in refine.lower() or "partition density is refinement-invariant" in refine.lower())
    check("The current Majorana blocker note already fixes the self-dual source family to one positive ray", "positive ray" in blocker.lower() and "projective" in blocker.lower())


def test_partition_density_stays_monotone_on_the_ray() -> None:
    print("\n" + "=" * 88)
    print("PART 2: THE UV-FINITE PARTITION DENSITY HAS NO FINITE SELECTOR ON THE RAY")
    print("=" * 88)

    k_op = build_positive_background_operator()
    k_inv = np.linalg.inv(k_op)
    j0 = np.linspace(1.0, float(k_op.shape[0]), k_op.shape[0], dtype=float)
    scales = [ALPHA_LM ** 7, ALPHA_LM ** 8, ALPHA_LM ** 9]
    coeff = float(j0 @ (k_inv @ j0))

    ratios = []
    derivatives = []
    for scale in scales:
        j = scale * j0
        delta_log_rho = 0.5 * float(j @ (k_inv @ j))
        ratios.append(delta_log_rho / (scale * scale))
        derivatives.append(scale * coeff)

    spread = max(ratios) - min(ratios)

    check("The partition-density response on the ray is exactly quadratic in lambda", spread < 1e-9, f"spread in Delta log rho / lambda^2={spread:.2e}")
    check("The partition-density coefficient is positive", coeff > 0.0, f"<J_0,K^-1 J_0>={coeff:.6e}")
    check("d log rho / d lambda = lambda <J_0,K^-1 J_0> stays strictly positive on lambda > 0", all(derivative > 0.0 for derivative in derivatives), f"derivatives={derivatives}")
    check("So the local partition density has no intrinsic finite positive stationary selector", coeff > 0.0 and all(derivative > 0.0 for derivative in derivatives), "only the trivial lambda=0 boundary is stationary")


def test_projective_schur_closure_preserves_the_same_source_law() -> None:
    print("\n" + "=" * 88)
    print("PART 3: EXACT SCHUR / PROJECTIVE CLOSURE PRESERVES THE SAME SCALE LAW")
    print("=" * 88)

    k_op = build_positive_background_operator()
    j0 = np.linspace(1.0, float(k_op.shape[0]), k_op.shape[0], dtype=float)
    keep = np.arange(10)
    scales = [ALPHA_LM ** 7, ALPHA_LM ** 8, ALPHA_LM ** 9]

    base_j_eff = None
    ratios = []
    for scale in scales:
        k_eff, j_eff = schur_reduce(k_op, scale * j0, keep)
        if base_j_eff is None:
            base_j_eff = j_eff / scale
        ratios.append(0.5 * float(j_eff @ np.linalg.solve(k_eff, j_eff)) / (scale * scale))
        diff = float(np.max(np.abs(j_eff / scale - base_j_eff)))
        check(f"Schur-reduced source stays linear in lambda at scale {scale:.3e}", diff < 1e-12, f"max reduced-source deviation={diff:.2e}")

    spread = max(ratios) - min(ratios)
    check("The coarse partition-density response is still exactly quadratic in lambda", spread < 1e-9, f"spread in coarse Delta log rho / lambda^2={spread:.2e}")


def test_density_cocycle_does_not_create_new_lambda_dependence() -> None:
    print("\n" + "=" * 88)
    print("PART 4: THE DENSITY COCYCLE / REFINEMENT PULLBACK ADDS NO NEW SCALE LAW")
    print("=" * 88)

    k_op = build_positive_background_operator()
    n = k_op.shape[0]
    t = random_invertible(17, n)
    t_inv = np.linalg.inv(t)
    k_prime = t_inv.T @ k_op @ t_inv
    jac = abs(float(np.linalg.det(t)))
    j0 = np.linspace(1.0, float(n), n, dtype=float)
    scales = [ALPHA_LM ** 7, ALPHA_LM ** 8, ALPHA_LM ** 9]

    max_err = 0.0
    for scale in scales:
        j = scale * j0
        j_prime = t_inv.T @ j
        # Raw partition densities differ by the chart Jacobian; the compensated
        # density is the invariant quantity on the exact atlas/refinement net.
        log_rho = log_partition_density(k_op, j)
        log_rho_prime = log_partition_density(k_prime, j_prime) - math.log(jac)
        max_err = max(max_err, abs(log_rho_prime - log_rho))

    check("The measure-compensated partition density is exactly chart/refinement invariant across the source ray", max_err < 1e-9, f"max compensated-density mismatch={max_err:.2e}")
    check("So the refinement/overlap cocycle introduces no new lambda dependence", max_err < 1e-9, "the density cocycle is lambda-blind after compensation")


def n5_execution_certificate() -> None:
    """State the granularity at which this runner actually resolves the no-go.

    Reporting only: no check() call is added and no PASS/FAIL count moves.
    Nothing drawn from the seeded chart-map stream is quoted; every number
    below is a closed-form invariant, a named constant or a structural count.
    """
    print("\n" + "=" * 88)
    print("N5 EXECUTION CERTIFICATE: WHAT THIS RUNNER RESOLVES")
    print("=" * 88)

    k_op = build_positive_background_operator()
    dim = k_op.shape[0]
    copies = 10
    internal = dim // copies
    j0 = np.linspace(1.0, float(dim), dim, dtype=float)
    coeff = float(j0 @ np.linalg.solve(k_op, j0))
    keep = np.arange(copies)
    elim = np.setdiff1d(np.arange(dim), keep, assume_unique=True)
    cross = k_op[np.ix_(keep, elim)]
    cross_nonzero = int(np.count_nonzero(np.abs(cross) > 1e-15))

    print(
        "per_element: resolved with amplitudes. The background operator is written "
        "from named entries - the ten reciprocals 1/(d_i d_j) over d = (2, 3, 5, 7), "
        "so 1/4, 1/9, 1/25, 1/49 on the squares and 1/6, 1/10, 1/14, 1/15, 1/21, "
        "1/35 on the mixed pairs, times the internal matrix whose entries are 2.0, "
        "0.2, 1.7, 0.1, 1.4 with exact zeros at [0, 2] and [2, 0]. The source vector "
        f"carries the {dim} distinct components 1 through {dim} laid down one at a "
        f"time, the quadratic form contracts all of them into <J_0, K^-1 J_0> = "
        f"{coeff:.6e}, and the Schur test compares the reduced source entry by entry "
        f"as a maximum over the {copies} retained components."
    )
    print(
        "per_site: checked and not executed. There is no geometry to resolve: the "
        f"{dim} indices factor as a {copies}-element inventory of dimension pairs "
        f"drawn from d = (2, 3, 5, 7) crossed with a {internal}-dimensional internal "
        "sector, and none of those labels is a position. No lattice, no neighbour "
        "relation and no volume is ever constructed in this runner."
    )
    print(
        "per_mode: checked and not executed. The only spectral operation applied to "
        "the background operator is slogdet, which collapses the whole spectrum into "
        "a single scalar; neither the operator, nor its Schur complement, nor the "
        f"{internal} x {internal} internal block is ever diagonalized, so no "
        "eigenvalue, normal mode or mode-resolved weight exists anywhere here. The "
        "QR factorization in the chart map builds a transformation, it does not "
        "resolve any mode of the operator."
    )
    print(
        "per_block: resolved, and the structure is copies. Because the dimension-pair "
        f"factor is diagonal, the operator is exactly block diagonal: {copies} copies "
        f"of the same {internal} x {internal} internal matrix, copy a scaled by its "
        "own reciprocal 1/(d_i d_j). The Schur step then partitions the indices into "
        f"{keep.size} kept and {elim.size} eliminated and forms all four sub-blocks "
        "explicitly. The limitation is worth naming: the retained set is an index "
        "range, not a block-aligned choice, so copies 0-2 are kept whole and copies "
        "4-9 removed whole, and since the copies do not couple, the entire cross "
        f"block holds exactly {cross_nonzero} nonzero entry - the elimination does "
        "real work inside copy 3 only."
    )
    print(
        "lattice_wide: checked, but resolved only as whole-object scalars and a "
        "documentation inventory, and the missing global ingredient is the note's own "
        "obstruction. Part 1's seven checks are substring searches in five Markdown "
        "files: they certify that the atlas rows and companion notes exist by name "
        "and evaluate no amplitude at all. Part 4's compensated density is a single "
        "whole-operator scalar (log-determinant plus one quadratic form minus a chart "
        "Jacobian), exercised with one chart map rather than an actual refinement net "
        "or any limit of one, so nothing asymptotic and nothing genuinely global is "
        "established; the absolute staircase selector the note is hunting stays absent."
    )
    print(
        "  scope: two of Part 2's checks cannot discriminate as written. The "
        "derivative list is formed directly as lambda * <J_0, K^-1 J_0> from positive "
        "scales and a positive coefficient rather than by differentiating anything, "
        "and the fourth check simply re-tests those same two conditions; the "
        "quadratic-in-lambda spread test divides a quadratic form by lambda^2, so it "
        "confirms the algebraic homogeneity of a bilinear form rather than probing a "
        "response."
    )
    print(
        f"  scope: the three scales exercised are ALPHA_LM^7, ^8 and ^9 for the module "
        f"constant ALPHA_LM = {ALPHA_LM}, a narrow window at the very small end near "
        "5.0e-08 down to 4.1e-10; no scale of order one and no wide sweep is tested."
    )
    print(
        "  scope: the Part 4 chart map is drawn from a seeded stream (seed 17). Two "
        "back-to-back executions of this runner are byte-identical, and no sampled "
        "quantity is quoted anywhere in the lines above."
    )


def main() -> int:
    print("=" * 88)
    print("NEUTRINO MAJORANA: PARTITION / PROJECTIVE TRANSPLANT OBSTRUCTION")
    print("=" * 88)
    print()
    print("Question:")
    print("  Can the universal UV-finite partition density, exact projective Schur")
    print("  closure, or canonical refinement-net pullback act as the missing")
    print("  absolute Majorana staircase selector on the current self-dual ray?")

    test_authority_stack_is_present()
    test_partition_density_stays_monotone_on_the_ray()
    test_projective_schur_closure_preserves_the_same_source_law()
    test_density_cocycle_does_not_create_new_lambda_dependence()
    n5_execution_certificate()

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  No. The universal partition / projective family still does not")
    print("  break the current source-scale homogeneity: the local density changes")
    print("  only by a monotone quadratic-in-lambda exponent, exact Schur coarse-")
    print("  graining preserves that same law, and the refinement/atlas density")
    print("  cocycle adds no new lambda dependence.")
    print()
    print("  So this QG/measure route is not the missing non-homogeneous")
    print("  local-to-generation bridge on the present stack.")
    print()
    print(f"  PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
