#!/usr/bin/env python3
"""Finite evaluation of a stipulated SU(3) character integral at x = 2.

For supplied data

  c_(p,q)(x) = int_SU(3) chi_(p,q)(U) exp(x Re tr U) dmu_Haar(U),
  rho_(p,q)(x) = c_(p,q)(x) / (d_(p,q) c_(0,0)(x)),

this runner evaluates x = 6/3 = 2 on 0 <= p,q <= 4.  The label beta=6,
the factor 1/3, the group, the Haar probability measure, and the finite box
are stipulated inputs.  No physical-environment, local-factor, plaquette
readout, framework-selection, or canonicity identification is made here.

Two separately implemented numerical routes evaluate the same integral:

* the absolutely convergent Bessel-determinant series obtained from the
  Fourier expansion of exp(x cos(theta)), truncated to modes -80..80;
* direct periodic quadrature of the Weyl-torus formula, using the stable
  product det(numerator) conjugate(det(denominator)) so Weyl walls never
  require a 0/0 character evaluation.

Mode-cutoff and grid-refinement ladders provide convergence checks.  Hostile
mutations exercise sign, rho normalization, torus domain, Haar density/Weyl
factor, and determinant-index conventions.  Those mutation checks measure
sensitivity; they are not substitutes for the two evaluations.

The historical public function names at the bottom are retained because two
finite-packet runners import them.  They denote only the stipulated integral
defined above.
"""

from __future__ import annotations

import platform
import sys

import numpy as np
import scipy
from scipy.special import iv


THEOREM_PASS = 0
SUPPORT_PASS = 0
FAIL = 0

NMAX = 4
BETA_LABEL = 6.0
ARG = BETA_LABEL / 3.0
MODE_MAX = 80
MODE_CHECK = 12
WEYL_GRID = 64
WEYL_GRID_LADDER = (24, 32, 40, WEYL_GRID)

CROSS_ABS_TOL = 1.0e-12
CROSS_REL_TOL = 1.0e-10
CONVERGENCE_TOL = 1.0e-12
SYMMETRY_TOL = 1.0e-13


def check(name: str, condition: bool, detail: str = "", bucket: str = "THEOREM") -> None:
    global THEOREM_PASS, SUPPORT_PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        if bucket == "SUPPORT":
            SUPPORT_PASS += 1
        else:
            THEOREM_PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] [{bucket}] {name}")
    if detail:
        print(f"         {detail}")


def dim_su3(p: int, q: int) -> int:
    """Dimension of the SU(3) irrep with Dynkin labels (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def highest_weight_triple(p: int, q: int) -> tuple[int, int, int]:
    return (p + q, q, 0)


def weights_box(nmax: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


def coefficient_matrix_bessel(
    mode: int,
    lam: tuple[int, int, int],
    *,
    arg: float = ARG,
    row_weight_mutation: bool = False,
) -> np.ndarray:
    """Bessel matrix; row_weight_mutation implements a hostile index error."""
    return np.array(
        [
            [
                iv(
                    mode
                    + (lam[i] if row_weight_mutation else lam[j])
                    + i
                    - j,
                    arg,
                )
                for j in range(3)
            ]
            for i in range(3)
        ],
        dtype=float,
    )


def stipulated_character_coefficient_bessel(
    p: int,
    q: int,
    *,
    mode_max: int = MODE_MAX,
    arg: float = ARG,
    row_weight_mutation: bool = False,
) -> float:
    """Truncated Bessel-determinant evaluation of c_(p,q)(x)."""
    lam = highest_weight_triple(p, q)
    return float(
        sum(
            np.linalg.det(
                coefficient_matrix_bessel(
                    mode,
                    lam,
                    arg=arg,
                    row_weight_mutation=row_weight_mutation,
                )
            )
            for mode in range(-mode_max, mode_max + 1)
        )
    )


def bessel_coefficient_vector(
    weights: list[tuple[int, int]],
    *,
    mode_max: int = MODE_MAX,
    arg: float = ARG,
    row_weight_mutation: bool = False,
) -> np.ndarray:
    return np.array(
        [
            stipulated_character_coefficient_bessel(
                p,
                q,
                mode_max=mode_max,
                arg=arg,
                row_weight_mutation=row_weight_mutation,
            )
            for p, q in weights
        ],
        dtype=float,
    )


def torus_eigenvalues(
    n_grid: int,
    *,
    domain: float = 2.0 * np.pi,
    offset1: float = 0.0,
    offset2: float = 0.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    theta1 = (np.arange(n_grid, dtype=float) + offset1) * domain / n_grid
    theta2 = (np.arange(n_grid, dtype=float) + offset2) * domain / n_grid
    t1, t2 = np.meshgrid(theta1, theta2, indexing="ij")
    z = np.stack(
        (np.exp(1j * t1), np.exp(1j * t2), np.exp(-1j * (t1 + t2))),
        axis=-1,
    )
    return t1, t2, z


def alternant_determinant(z: np.ndarray, exponents: tuple[int, int, int]) -> np.ndarray:
    matrix = z[..., :, np.newaxis] ** np.asarray(exponents, dtype=int)
    return np.linalg.det(matrix)


def stipulated_character_coefficient_weyl_complex(
    p: int,
    q: int,
    *,
    n_grid: int = WEYL_GRID,
    arg: float = ARG,
    domain: float = 2.0 * np.pi,
) -> complex:
    """Direct Weyl-torus quadrature with Haar probability normalization.

    For theta_3 = -theta_1-theta_2 and both independent angles in [0,2pi),

      dmu_Haar = |Delta|^2 dtheta_1 dtheta_2 / (6 (2pi)^2).

    Since chi = det_num/det_den and |Delta|^2 = |det_den|^2, the product
    chi |Delta|^2 is evaluated as det_num conjugate(det_den).  This equality
    removes the removable 0/0 singularity on Weyl walls.
    """
    t1, t2, z = torus_eigenvalues(n_grid, domain=domain)
    den = alternant_determinant(z, (2, 1, 0))
    lam = highest_weight_triple(p, q)
    num = alternant_determinant(z, (lam[0] + 2, lam[1] + 1, lam[2]))
    weight = np.exp(arg * (np.cos(t1) + np.cos(t2) + np.cos(t1 + t2)))
    domain_fraction = (domain / (2.0 * np.pi)) ** 2
    return complex(np.mean(num * np.conjugate(den) * weight) * domain_fraction / 6.0)


def weyl_coefficient_vector_complex(
    weights: list[tuple[int, int]],
    *,
    n_grid: int = WEYL_GRID,
    arg: float = ARG,
    domain: float = 2.0 * np.pi,
) -> np.ndarray:
    return np.array(
        [
            stipulated_character_coefficient_weyl_complex(
                p,
                q,
                n_grid=n_grid,
                arg=arg,
                domain=domain,
            )
            for p, q in weights
        ],
        dtype=complex,
    )


def flat_torus_measure_mutation(
    weights: list[tuple[int, int]], *, n_grid: int = WEYL_GRID, arg: float = ARG
) -> np.ndarray:
    """Hostile mutation: replace SU(3) Haar density by flat torus measure.

    Unequal deterministic offsets avoid sampling Weyl walls, where the
    character quotient has a removable 0/0 singularity.
    """
    t1, t2, z = torus_eigenvalues(n_grid, offset1=0.371, offset2=0.137)
    den = alternant_determinant(z, (2, 1, 0))
    if float(np.min(np.abs(den))) <= 1.0e-8:
        raise RuntimeError("flat-measure mutation grid approached a Weyl wall")
    weight = np.exp(arg * (np.cos(t1) + np.cos(t2) + np.cos(t1 + t2)))
    values = []
    for p, q in weights:
        lam = highest_weight_triple(p, q)
        num = alternant_determinant(z, (lam[0] + 2, lam[1] + 1, lam[2]))
        values.append(complex(np.mean((num / den) * weight)))
    return np.asarray(values, dtype=complex)


def normalized_rho(coefficients: np.ndarray, weights: list[tuple[int, int]]) -> np.ndarray:
    dims = np.asarray([dim_su3(p, q) for p, q in weights], dtype=float)
    return coefficients / (dims * coefficients[0])


def max_abs_rel(left: np.ndarray, right: np.ndarray) -> tuple[float, float]:
    delta = np.abs(left - right)
    relative = delta / np.maximum(np.abs(left), 1.0e-30)
    return float(np.max(delta)), float(np.max(relative))


# Historical compatibility API.  The names describe the original file path,
# not a physical-environment identification.
def wilson_character_coefficient_bessel(p: int, q: int) -> float:
    return stipulated_character_coefficient_bessel(p, q)


def wilson_character_coefficient_weyl(p: int, q: int, n_grid: int = WEYL_GRID) -> float:
    value = stipulated_character_coefficient_weyl_complex(p, q, n_grid=n_grid)
    return float(value.real)


def rho_pq(p: int, q: int, c00: float, method: str = "bessel") -> float:
    if method == "bessel":
        coefficient = stipulated_character_coefficient_bessel(p, q)
    elif method == "weyl":
        coefficient = wilson_character_coefficient_weyl(p, q)
    else:
        raise ValueError("method must be 'bessel' or 'weyl'")
    return coefficient / (dim_su3(p, q) * c00)


def main() -> int:
    weights = weights_box(NMAX)
    index = {weight: i for i, weight in enumerate(weights)}

    # Route A and its mode-cutoff convergence check.
    c_bessel = bessel_coefficient_vector(weights)
    c_bessel_check = bessel_coefficient_vector(weights, mode_max=MODE_CHECK)
    rho_bessel = normalized_rho(c_bessel, weights)
    rho_bessel_check = normalized_rho(c_bessel_check, weights)
    mode_drift = float(np.max(np.abs(rho_bessel - rho_bessel_check)))

    # Route B and its grid-refinement ladder.  Each grid recomputes the
    # integral from the definitions; no Route-A table is imported.
    weyl_by_grid = {
        grid: weyl_coefficient_vector_complex(weights, n_grid=grid)
        for grid in WEYL_GRID_LADDER
    }
    c_weyl_complex = weyl_by_grid[WEYL_GRID]
    c_weyl = c_weyl_complex.real
    rho_weyl_by_grid = {
        grid: normalized_rho(values.real, weights) for grid, values in weyl_by_grid.items()
    }
    rho_weyl = rho_weyl_by_grid[WEYL_GRID]
    grid_drifts = {
        (left, right): float(
            np.max(np.abs(rho_weyl_by_grid[left] - rho_weyl_by_grid[right]))
        )
        for left, right in zip(WEYL_GRID_LADDER[:-1], WEYL_GRID_LADDER[1:])
    }
    final_grid_drift = grid_drifts[(WEYL_GRID_LADDER[-2], WEYL_GRID_LADDER[-1])]
    weyl_imag_residual = float(np.max(np.abs(c_weyl_complex.imag)))

    cross_c_abs, cross_c_rel = max_abs_rel(c_bessel, c_weyl)
    cross_rho_abs, cross_rho_rel = max_abs_rel(rho_bessel, rho_weyl)
    rho_cross_delta = np.abs(rho_bessel - rho_weyl)
    rho_cross_abs_weight = weights[int(np.argmax(rho_cross_delta))]
    rho_cross_rel_weight = weights[
        int(np.argmax(rho_cross_delta / np.maximum(np.abs(rho_bessel), 1.0e-30)))
    ]

    swap_error = float(
        max(
            abs(rho_bessel[index[(p, q)]] - rho_bessel[index[(q, p)]])
            for p, q in weights
        )
    )
    rho_min = float(np.min(rho_bessel))

    # Exact Haar/character orthogonality sanity check at x=0.  With this
    # finite Fourier polynomial, the 16x16 periodic grid resolves all modes.
    haar_zero = weyl_coefficient_vector_complex(weights, n_grid=16, arg=0.0)
    haar_unit_error = float(abs(haar_zero[0] - 1.0))
    haar_nontrivial_error = float(np.max(np.abs(haar_zero[1:])))

    # Hostile mutations.  Each recomputes from formulas rather than comparing
    # strings or importing an expected result table.
    sign_mutation = weyl_coefficient_vector_complex(weights, arg=-ARG).real
    rho_sign_mutation = normalized_rho(sign_mutation, weights)
    sign_mutation_gap = float(np.max(np.abs(rho_sign_mutation - rho_weyl)))

    rho_no_dimension = c_bessel / c_bessel[0]
    normalization_mutation_gap = float(np.max(np.abs(rho_no_dimension - rho_bessel)))

    half_domain = weyl_coefficient_vector_complex(weights, domain=np.pi).real
    rho_half_domain = normalized_rho(half_domain, weights)
    domain_mutation_gap = float(np.max(np.abs(rho_half_domain - rho_weyl)))

    flat_measure = flat_torus_measure_mutation(weights).real
    rho_flat_measure = normalized_rho(flat_measure, weights)
    measure_mutation_gap = float(np.max(np.abs(rho_flat_measure - rho_weyl)))

    weyl_factor_mutation_gap = float(np.max(np.abs(6.0 * c_weyl - c_bessel)))

    index_mutation = bessel_coefficient_vector(weights, row_weight_mutation=True)
    rho_index_mutation = normalized_rho(index_mutation, weights)
    index_mutation_gap = float(np.max(np.abs(rho_index_mutation - rho_bessel)))

    print("=" * 78)
    print("STIPULATED SU(3) CHARACTER INTEGRAL: FINITE EVALUATION AT x=2")
    print("=" * 78)
    print()
    print("Supplied mathematical inputs")
    print(f"  group=SU(3), Haar measure=probability measure, beta label={BETA_LABEL:.1f}")
    print(f"  x=beta/3={ARG:.1f}, finite box=0<=p,q<={NMAX}")
    print("  Weyl domain: theta1,theta2 in [0,2pi), theta3=-theta1-theta2")
    print("  Haar density: |Delta|^2 / (6 (2pi)^2)")
    print(f"  Bessel modes=-{MODE_MAX}..{MODE_MAX}; cutoff check=-{MODE_CHECK}..{MODE_CHECK}")
    print(f"  Weyl grid ladder={' -> '.join(str(grid) for grid in WEYL_GRID_LADDER)}")
    print(
        f"  arithmetic=float64, Python={platform.python_version()}, "
        f"NumPy={np.__version__}, SciPy={scipy.__version__}"
    )
    print(f"  platform={platform.platform()}, mantissa bits={sys.float_info.mant_dig}")
    print()
    print("Normalized finite values rho_(p,q)=c_(p,q)/(d_(p,q)c_(0,0))")
    for p, q in [
        (0, 0),
        (1, 0),
        (0, 1),
        (1, 1),
        (2, 0),
        (0, 2),
        (2, 1),
        (1, 2),
        (3, 0),
        (0, 3),
        (2, 2),
        (4, 4),
    ]:
        i = index[(p, q)]
        print(
            f"  rho_({p},{q}) = {rho_bessel[i]:.12e}   "
            f"(direct Weyl: {rho_weyl[i]:.12e})"
        )
    print()
    print("Convergence and independent cross-check")
    print(f"  Bessel normalized drift M={MODE_CHECK} -> M={MODE_MAX} = {mode_drift:.3e}")
    for (left, right), drift in grid_drifts.items():
        print(f"  Weyl normalized drift N={left} -> N={right:<2}       = {drift:.3e}")
    print(f"  max Weyl coefficient imaginary residual          = {weyl_imag_residual:.3e}")
    print(f"  max raw-coefficient absolute cross-error          = {cross_c_abs:.3e}")
    print(f"  max raw-coefficient relative cross-error          = {cross_c_rel:.3e}")
    print(
        f"  max normalized absolute cross-error               = {cross_rho_abs:.3e} "
        f"at {rho_cross_abs_weight}"
    )
    print(
        f"  max normalized relative cross-error               = {cross_rho_rel:.3e} "
        f"at {rho_cross_rel_weight}"
    )
    print(f"  c_(0,0)(x=2)                                      = {c_bessel[0]:.12f}")
    print(f"  finite-box rho min/max                            = {rho_min:.12e}, {float(np.max(rho_bessel)):.12f}")
    print()
    print("Hostile-mutation separations from the unmutated evaluation")
    print(f"  sign x -> -x                                      = {sign_mutation_gap:.3e}")
    print(f"  omit d_(p,q) in rho normalization                 = {normalization_mutation_gap:.3e}")
    print(f"  replace [0,2pi)^2 by [0,pi)^2                    = {domain_mutation_gap:.3e}")
    print(f"  replace Haar density by flat torus measure        = {measure_mutation_gap:.3e}")
    print(f"  omit Weyl factor 1/6 in raw coefficients          = {weyl_factor_mutation_gap:.3e}")
    print(f"  attach highest-weight index to determinant row    = {index_mutation_gap:.3e}")
    print()

    check(
        "the Weyl formula has Haar probability normalization and character orthogonality at x=0",
        haar_unit_error < 1.0e-14 and haar_nontrivial_error < 1.0e-14,
        detail=(
            f"|c_(0,0)(0)-1|={haar_unit_error:.3e}; "
            f"max nontrivial |c_(p,q)(0)|={haar_nontrivial_error:.3e}"
        ),
    )
    check(
        "the Bessel-determinant evaluation is stable under the disclosed mode-cutoff refinement",
        mode_drift < CONVERGENCE_TOL,
        detail=f"max normalized drift from M={MODE_CHECK} to M={MODE_MAX}: {mode_drift:.3e}",
    )
    check(
        "the direct Weyl evaluation is stable on the final disclosed periodic-grid refinement",
        final_grid_drift < CONVERGENCE_TOL,
        detail=(
            f"max normalized drift from N={WEYL_GRID_LADDER[-2]} to "
            f"N={WEYL_GRID_LADDER[-1]}: {final_grid_drift:.3e}"
        ),
    )
    check(
        "the Bessel series and wall-stable direct Weyl quadrature agree on all 25 supplied weights",
        cross_c_abs < CROSS_ABS_TOL
        and cross_c_rel < CROSS_REL_TOL
        and cross_rho_abs < CROSS_ABS_TOL
        and cross_rho_rel < CROSS_REL_TOL
        and weyl_imag_residual < CROSS_ABS_TOL,
        detail=(
            f"raw max abs={cross_c_abs:.3e}, raw max rel={cross_c_rel:.3e}; "
            f"rho max abs={cross_rho_abs:.3e}, rho max rel={cross_rho_rel:.3e}"
        ),
    )
    check(
        "the definition gives rho_(0,0)=1 and the finite values obey conjugation symmetry",
        abs(rho_bessel[0] - 1.0) < 1.0e-15 and swap_error < SYMMETRY_TOL,
        detail=f"|rho_(0,0)-1|={abs(rho_bessel[0]-1.0):.3e}; swap error={swap_error:.3e}",
    )
    check(
        "all 25 numerically evaluated normalized coefficients are strictly positive",
        rho_min > 0.0,
        detail=f"minimum finite-box value={rho_min:.12e}",
    )

    for name, gap in [
        ("hostile sign mutation x -> -x is detected", sign_mutation_gap),
        ("hostile omission of d_(p,q) from rho is detected", normalization_mutation_gap),
        ("hostile half-domain torus integration is detected", domain_mutation_gap),
        ("hostile flat-torus replacement of Haar density is detected", measure_mutation_gap),
        ("hostile omission of the Weyl factor 1/6 is detected in raw coefficients", weyl_factor_mutation_gap),
        ("hostile determinant highest-weight row/column index swap is detected", index_mutation_gap),
    ]:
        check(name, gap > 1.0e-6, detail=f"max separation={gap:.3e}", bucket="SUPPORT")

    print()
    print("Scope boundary: this certificate evaluates only the stipulated integral/data.")
    print("It supplies no canonical or physical environment identification and no plaquette readout.")
    print()
    print("=" * 78)
    print(f"SUMMARY: THEOREM PASS={THEOREM_PASS} SUPPORT={SUPPORT_PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
