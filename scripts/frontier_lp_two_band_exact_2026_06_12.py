#!/usr/bin/env python3
"""Finite-dimensional two-band Peierls-response verifier.

Companion draft:
    docs/LP_TWO_BAND_EXACT_COMPLETION_BOUNDED_THEOREM_NOTE_2026-06-12.md

This runner mirrors the landed LP-failure Harper cell first, then checks the
native second-order Peierls response on that finite magnetic cell.  The
second-order calculation uses the matrix expansion

    H(B) = H0 + B H1 + B^2 H2 + O(B^3)

obtained directly from the Peierls phase exp(i B x) on the y-links.  The
grand-potential curvature is evaluated by the standard finite-dimensional
Rayleigh-Schrodinger/divided-difference formula, including the interband
H1 matrix elements.

Run:
    python3 scripts/frontier_lp_two_band_exact_2026_06_12.py

Short smoke:
    python3 scripts/frontier_lp_two_band_exact_2026_06_12.py --smoke
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
from dataclasses import dataclass

import numpy as np
from numpy.polynomial.legendre import leggauss


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "LP_TWO_BAND_EXACT_COMPLETION_BOUNDED_THEOREM_NOTE_2026-06-12.md"


# Landed Harper/LP predecessor constants (commit 811953e76).
T_HOP = 1.0
Q_HARPER = 24
LX = Q_HARPER
LY = 2
N_SITE = LX * LY
B_FIELD_LANDED = 2.0 * np.pi / Q_HARPER

# Native small-B coefficient reference.  This is fixed before any result gate.
REFERENCE_B = 1.0e-3
TEMPERATURE = 0.2
DEFAULT_GL_ORDER = 12
SMOKE_GL_ORDER = 4
CHI_PROBE_MU = 1.7086

MASSES = (0.0, 0.2, 0.3, 0.5)

# Fixed gates.
HERMITICITY_TOL = 1.0e-12
B0_FOLDING_TOL = 1.0e-10
PT_CHI_REL_TOL = 2.0e-2
ANTI_FAB_INTERBAND_MIN = 1.0e-6

# Landed off-m0 intraband-LP boundary deviations from the predecessor runner,
# printed as provenance context only (the LP curvature-form split is a different
# decomposition from the velocity-gauge PT split below; they are not gated
# against each other).
LANDED_DEV_PROVENANCE = (
    ("m=0.2 T=0.2", 0.0424013805),
    ("m=0.2 T=0.4", 0.0461600062),
    ("m=0.5 T=0.2", 0.2010378416),
    ("m=0.5 T=0.4", 0.1994054030),
)

# Computed-anchor controls.  The landed small-B second-difference estimator uses
# a non-flux-quantized field on the finite torus, so it carries a finite-B floor;
# the B-vs-B/2 drift is measured and gated below 1e-2 (measured ~5.6e-3, directed
# TOWARD the PT value), an order of magnitude under the landed intraband
# failures (0.04-0.20).  A flux-quantized reference is named follow-on work: at
# accessible sizes (LX <= 240) the quantized estimator is Landau-reorganization
# dominated and unconverged, so it cannot serve as a gate here.
HALF_B_DRIFT_DISCLOSURE_TOL = 1.0e-2
CANCELLATION_FACTOR_MIN = 5.0

SITE_SIGNS = np.array(
    [1.0 if (x + y) % 2 == 0 else -1.0 for x in range(LX) for y in range(LY)]
)


PASS_COUNT = 0
FAIL_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    """Gate a computed quantity against a fixed labeled tolerance or constant."""

    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def site_index(x: int, y: int) -> int:
    return (x % LX) * LY + (y % LY)


def gl_average_nodes_weights(n: int) -> tuple[np.ndarray, np.ndarray]:
    x, w = leggauss(n)
    return np.pi * x, 0.5 * w


def grand_kernel(energy: np.ndarray, mu: float, temp: float) -> np.ndarray:
    return -temp * np.logaddexp(0.0, -(energy - mu) / temp)


def fermi_occupation(energy: np.ndarray, mu: float, temp: float) -> np.ndarray:
    z = np.clip((energy - mu) / temp, -60.0, 60.0)
    return 1.0 / (1.0 + np.exp(z))


def grand_kernel_second_derivative(
    energy: np.ndarray, mu: float, temp: float
) -> np.ndarray:
    f = fermi_occupation(energy, mu, temp)
    return -f * (1.0 - f) / temp


def harper_matrix(kx: float, ky: float, b_field: float, mass: float) -> np.ndarray:
    h = np.zeros((N_SITE, N_SITE), dtype=np.complex128)
    h[np.diag_indices(N_SITE)] = mass * SITE_SIGNS
    exp_kx = np.exp(1j * kx)
    exp_ky = np.exp(1j * ky)

    for x in range(LX):
        for y in range(LY):
            i = site_index(x, y)

            xp = (x + 1) % LX
            x_phase = exp_kx if x + 1 == LX else 1.0 + 0.0j
            j = site_index(xp, y)
            amp = -T_HOP * x_phase
            h[i, j] += amp
            h[j, i] += np.conjugate(amp)

            yp = (y + 1) % LY
            y_phase = np.exp(1j * b_field * x)
            if y + 1 == LY:
                y_phase *= exp_ky
            j = site_index(x, yp)
            amp = -T_HOP * y_phase
            h[i, j] += amp
            h[j, i] += np.conjugate(amp)

    return h


def harper_h0_h1_h2(kx: float, ky: float, mass: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    h0 = harper_matrix(kx, ky, 0.0, mass)
    h1 = np.zeros_like(h0)
    h2 = np.zeros_like(h0)
    exp_ky = np.exp(1j * ky)

    for x in range(LX):
        for y in range(LY):
            i = site_index(x, y)
            yp = (y + 1) % LY
            j = site_index(x, yp)
            y_boundary_phase = exp_ky if y + 1 == LY else 1.0 + 0.0j

            # -t exp(i B x) = -t [1 + iBx - (B^2 x^2)/2 + O(B^3)].
            amp1 = -T_HOP * (1j * x) * y_boundary_phase
            amp2 = T_HOP * (x * x / 2.0) * y_boundary_phase
            h1[i, j] += amp1
            h1[j, i] += np.conjugate(amp1)
            h2[i, j] += amp2
            h2[j, i] += np.conjugate(amp2)

    return h0, h1, h2


def folded_zero_spectrum(kx: float, ky: float, mass: float) -> np.ndarray:
    vals: list[float] = []
    py = ky / LY
    for nx in range(Q_HARPER):
        px = (kx + 2.0 * np.pi * nx) / Q_HARPER
        eps = -2.0 * T_HOP * (np.cos(px) + np.cos(py))
        radius = float(np.sqrt(mass * mass + eps * eps))
        vals.extend((-radius, radius))
    return np.sort(np.array(vals, dtype=np.float64))


@dataclass(frozen=True)
class ExactPoint:
    weight_per_site: float
    eig_plus: np.ndarray
    eig_zero: np.ndarray
    eig_minus: np.ndarray


@dataclass(frozen=True)
class PTPoint:
    weight_per_site: float
    eig: np.ndarray
    h2_diag: np.ndarray
    h1_abs2: np.ndarray
    interband_mask: np.ndarray


@dataclass(frozen=True)
class MassTables:
    mass: float
    exact_points: tuple[ExactPoint, ...]
    pt_points: tuple[PTPoint, ...]


def build_mass_tables(mass: float, gl_order: int) -> MassTables:
    nodes, weights = gl_average_nodes_weights(gl_order)
    exact_points: list[ExactPoint] = []
    pt_points: list[PTPoint] = []

    for ix, kx in enumerate(nodes):
        for iy, ky in enumerate(nodes):
            weight_per_site = float(weights[ix] * weights[iy] / N_SITE)
            eig_plus = np.linalg.eigvalsh(harper_matrix(kx, ky, REFERENCE_B, mass))
            eig_zero = np.linalg.eigvalsh(harper_matrix(kx, ky, 0.0, mass))
            eig_minus = np.linalg.eigvalsh(harper_matrix(kx, ky, -REFERENCE_B, mass))
            exact_points.append(
                ExactPoint(
                    weight_per_site=weight_per_site,
                    eig_plus=eig_plus,
                    eig_zero=eig_zero,
                    eig_minus=eig_minus,
                )
            )

            h0, h1, h2 = harper_h0_h1_h2(kx, ky, mass)
            eig, vec = np.linalg.eigh(h0)
            h1_eig = vec.conjugate().T @ h1 @ vec
            h2_eig = vec.conjugate().T @ h2 @ vec
            signs = np.sign(eig)
            interband_mask = (signs[:, None] * signs[None, :]) < 0.0
            pt_points.append(
                PTPoint(
                    weight_per_site=weight_per_site,
                    eig=eig,
                    h2_diag=np.real(np.diag(h2_eig)),
                    h1_abs2=np.abs(h1_eig) ** 2,
                    interband_mask=interband_mask,
                )
            )

    return MassTables(mass=mass, exact_points=tuple(exact_points), pt_points=tuple(pt_points))


def exact_chi_reference(mu: float, temp: float, points: tuple[ExactPoint, ...]) -> float:
    total = 0.0
    inv_b2 = 1.0 / (REFERENCE_B * REFERENCE_B)
    for point in points:
        total += point.weight_per_site * inv_b2 * float(
            np.sum(
                grand_kernel(point.eig_plus, mu, temp)
                + grand_kernel(point.eig_minus, mu, temp)
                - 2.0 * grand_kernel(point.eig_zero, mu, temp)
            )
        )
    return total


@dataclass(frozen=True)
class PTValue:
    full: float
    intraband: float
    interband: float


def pt_chi(mu: float, temp: float, points: tuple[PTPoint, ...]) -> PTValue:
    full_total = 0.0
    intra_total = 0.0
    inter_total = 0.0

    for point in points:
        eig = point.eig
        fp = fermi_occupation(eig, mu, temp)
        fpp = grand_kernel_second_derivative(eig, mu, temp)
        diff = eig[:, None] - eig[None, :]
        fp_diff = fp[:, None] - fp[None, :]

        kernel = np.empty_like(diff)
        offdiag = np.abs(diff) > 1.0e-10
        kernel[offdiag] = fp_diff[offdiag] / diff[offdiag]
        degenerate_limit = 0.5 * (fpp[:, None] + fpp[None, :])
        kernel[~offdiag] = degenerate_limit[~offdiag]

        h1_term_matrix = kernel * point.h1_abs2
        h1_term = float(np.sum(h1_term_matrix))
        inter_term = float(np.sum(h1_term_matrix[point.interband_mask]))
        seagull = float(2.0 * np.sum(fp * point.h2_diag))

        full = seagull + h1_term
        full_total += point.weight_per_site * full
        inter_total += point.weight_per_site * inter_term
        intra_total += point.weight_per_site * (full - inter_term)

    return PTValue(full=full_total, intraband=intra_total, interband=inter_total)


def exact_chi_at_b(mass: float, gl_order: int, b_field: float) -> float:
    nodes, weights = gl_average_nodes_weights(gl_order)
    inv_b2 = 1.0 / (b_field * b_field)
    total = 0.0
    for ix, kx in enumerate(nodes):
        for iy, ky in enumerate(nodes):
            weight_per_site = float(weights[ix] * weights[iy] / N_SITE)
            eig_plus = np.linalg.eigvalsh(harper_matrix(kx, ky, b_field, mass))
            eig_zero = np.linalg.eigvalsh(harper_matrix(kx, ky, 0.0, mass))
            eig_minus = np.linalg.eigvalsh(harper_matrix(kx, ky, -b_field, mass))
            total += weight_per_site * inv_b2 * float(
                np.sum(
                    grand_kernel(eig_plus, CHI_PROBE_MU, TEMPERATURE)
                    + grand_kernel(eig_minus, CHI_PROBE_MU, TEMPERATURE)
                    - 2.0 * grand_kernel(eig_zero, CHI_PROBE_MU, TEMPERATURE)
                )
            )
    return total


@dataclass(frozen=True)
class MassResult:
    mass: float
    exact_chi: float
    pt_chi: PTValue
    chi_rel_dev: float


def analyze_mass(table: MassTables) -> MassResult:
    exact_value = exact_chi_reference(CHI_PROBE_MU, TEMPERATURE, table.exact_points)
    pt_value = pt_chi(CHI_PROBE_MU, TEMPERATURE, table.pt_points)
    chi_rel_dev = abs(pt_value.full - exact_value) / max(1.0e-12, abs(exact_value))

    return MassResult(
        mass=table.mass,
        exact_chi=exact_value,
        pt_chi=pt_value,
        chi_rel_dev=chi_rel_dev,
    )


def anchor_gates(gl_order: int) -> None:
    print("\nS0 ANCHORS: provenance + computed discretization control")
    print("landed intraband-LP curvature-form deviations (provenance, not gated against")
    print("the velocity-gauge PT split below — different decompositions):")
    for label, value in LANDED_DEV_PROVENANCE:
        print(f"  {label}: {value:.10f}")

    chi_b = exact_chi_at_b(0.2, gl_order, REFERENCE_B)
    chi_half = exact_chi_at_b(0.2, gl_order, 0.5 * REFERENCE_B)
    half_b_rel = abs(chi_b - chi_half) / max(1.0e-12, abs(chi_half))
    check(
        "computed anchor: landed estimator finite-B drift at m=0.2 is below the "
        "disclosed 1e-2 floor (B vs B/2; drift direction printed)",
        half_b_rel <= HALF_B_DRIFT_DISCLOSURE_TOL,
        f"chi(B)={chi_b:.10e}, chi(B/2)={chi_half:.10e}, rel_drift={half_b_rel:.3e}, "
        f"floor={HALF_B_DRIFT_DISCLOSURE_TOL:.1e}",
    )


def structural_gates() -> None:
    print("\nS1 STRUCTURE: Harper cell controls")
    probe_kx = 0.37
    probe_ky = -0.91
    probe_mass = 0.2
    h_probe = harper_matrix(probe_kx, probe_ky, B_FIELD_LANDED, probe_mass)
    hermiticity = float(np.max(np.abs(h_probe - h_probe.conjugate().T)))

    h0_probe = harper_matrix(probe_kx, probe_ky, 0.0, probe_mass)
    folded = folded_zero_spectrum(probe_kx, probe_ky, probe_mass)
    b0_folding = float(np.max(np.abs(np.sort(np.linalg.eigvalsh(h0_probe)) - folded)))

    print(f"cell convention: Q={Q_HARPER} (even, contains the staggered period), Ly={LY}")
    check(
        "Harper matrix Hermiticity",
        hermiticity <= HERMITICITY_TOL,
        f"max |H-H^dag|={hermiticity:.3e}, tol={HERMITICITY_TOL:.1e}",
    )
    check(
        "B=0 folded two-band spectrum",
        b0_folding <= B0_FOLDING_TOL,
        f"max folded-spectrum error={b0_folding:.3e}, tol={B0_FOLDING_TOL:.1e}",
    )


def run(gl_order: int, smoke: bool) -> int:
    print("Two-band exact Peierls response verifier")
    print(
        f"cell: Q={Q_HARPER}, Ly={LY}, N={N_SITE}, t={T_HOP}, "
        f"T={TEMPERATURE}, GL={gl_order}, small_B={REFERENCE_B}"
    )

    anchor_gates(gl_order)
    structural_gates()

    print("\nS2/S3: native second-order PT vs small-B Hofstadter second difference")
    print(f"fixed chi probe: mu={CHI_PROBE_MU}, T={TEMPERATURE}")
    results: list[MassResult] = []
    for mass in MASSES:
        table = build_mass_tables(mass, gl_order)
        result = analyze_mass(table)
        results.append(result)
        print(
            "mass={:.3g}  chi_exact={:.10e}  chi_PT={:.10e}  rel_dev={:.3e}  "
            "PT(intra,inter)=({:.3e},{:.3e})".format(
                mass,
                result.exact_chi,
                result.pt_chi.full,
                result.chi_rel_dev,
                result.pt_chi.intraband,
                result.pt_chi.interband,
            )
        )

    for result in results:
        check(
            f"full two-band PT matches exact chi m={result.mass}",
            result.chi_rel_dev <= PT_CHI_REL_TOL,
            f"rel_dev={result.chi_rel_dev:.3e}, tol={PT_CHI_REL_TOL:.3e}",
        )

    max_interband_m05 = max(
        abs(result.pt_chi.interband) for result in results if result.mass == 0.5
    )
    check(
        "anti-fabrication: m=0.5 interband contribution is nontrivial",
        max_interband_m05 > ANTI_FAB_INTERBAND_MIN,
        f"max |interband|={max_interband_m05:.3e}, min={ANTI_FAB_INTERBAND_MIN:.1e}",
    )

    print("\nS4: computed near-cancellation structure of the PT split")
    min_cancellation = min(
        min(abs(result.pt_chi.intraband), abs(result.pt_chi.interband))
        / max(1.0e-12, abs(result.pt_chi.full))
        for result in results
    )
    check(
        "near-cancellation: both PT terms exceed 5x the net response at every mass",
        min_cancellation >= CANCELLATION_FACTOR_MIN,
        f"min term/net ratio={min_cancellation:.3f}, factor_min={CANCELLATION_FACTOR_MIN:.1f}",
    )
    interband_mags = [abs(result.pt_chi.interband) for result in results]
    check(
        "interband magnitude is strictly increasing with mass on the fixed grid",
        all(b > a for a, b in zip(interband_mags, interband_mags[1:])),
        "interband magnitudes=" + ", ".join(f"{v:.6e}" for v in interband_mags),
    )

    print("\nS5: note hygiene")
    note = NOTE.read_text(encoding="utf-8")
    check(
        "canonical claim type is present and noncanonical Type front matter is absent",
        "**Claim type:** bounded_theorem" in note and "**Type:**" not in note,
        "bounded_theorem with single claim-type field",
    )
    check(
        "status authority and no-promotion statements are present",
        "**Status authority:** independent audit lane" in note
        and "**No-promotion statement:**" in note,
        "audit status remains independent",
    )
    check(
        "landed LP off-m0 predecessor is linked as the comparison-context dependency",
        "[`LP_IDENTIFICATION_FAILS_OFF_M0_BOUNDED_THEOREM_NOTE_2026-06-12.md`]"
        "(LP_IDENTIFICATION_FAILS_OFF_M0_BOUNDED_THEOREM_NOTE_2026-06-12.md)" in note,
        "dependency graph receives the predecessor edge",
    )

    print(f"\nTOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--smoke",
        action="store_true",
        help="Use the fixed small quadrature for a sub-30-second smoke test.",
    )
    parser.add_argument(
        "--gl-order",
        type=int,
        default=None,
        help="Override the fixed Gauss-Legendre order for local reruns.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    gl_order = args.gl_order
    if gl_order is None:
        gl_order = SMOKE_GL_ORDER if args.smoke else DEFAULT_GL_ORDER
    return run(gl_order=gl_order, smoke=args.smoke)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
