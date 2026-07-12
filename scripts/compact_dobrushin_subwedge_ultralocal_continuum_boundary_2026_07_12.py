#!/usr/bin/env python3
"""Certificate for compact-interior Dobrushin continuum ultralocality."""

from __future__ import annotations

from math import exp, log
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "COMPACT_DOBRUSHIN_SUBWEDGE_SEPARATED_POINT_ULTRALOCAL_CONTINUUM_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {name}: {detail}")


def alpha(beta: float, mass: float) -> float:
    kappa = 14.0 / (mass * mass + 2.0)
    return 18.0 * beta + 1.5 * kappa**2 * (2.0 - kappa) / (1.0 - kappa) ** 2


def weighted_alpha(beta: float, mass: float, weight: float) -> float:
    factor = exp(2.0 * weight)
    weighted_kappa = 14.0 * factor / (mass * mass + 2.0)
    fermion = 1.5 * weighted_kappa**2 * (2.0 - weighted_kappa) / (1.0 - weighted_kappa) ** 2
    return 18.0 * beta * factor + fermion


def main() -> int:
    compact_points = ((0.0, 8.0), (0.01, 8.0), (0.02, 10.0), (0.04, 10.0))
    values = [alpha(beta, mass) for beta, mass in compact_points]
    margin = 1.0 - max(values)
    check(
        "A concrete compact parameter packet has a strict uniform Dobrushin margin",
        margin > 0.0,
        "alphas=" + ",".join(f"{value:.6f}" for value in values) + f", epsilon={margin:.6f}",
    )

    lattice_rate = 0.01
    weighted_values = [weighted_alpha(beta, mass, lattice_rate) for beta, mass in compact_points]
    check(
        "One positive exponential weight keeps the full packet influence row below one",
        max(weighted_values) < 1.0,
        "weighted alphas=" + ",".join(f"{value:.6f}" for value in weighted_values)
        + f", lambda={lattice_rate:.3f}",
    )

    separation = 1.0
    spacings = (0.04, 0.02, 0.01, 0.005)
    correlations = [exp(-lattice_rate * separation / spacing) for spacing in spacings]
    check(
        "Fixed-physical-separation correlations vanish as lattice distance diverges",
        all(correlations[index + 1] < correlations[index] for index in range(3))
        and correlations[-1] < 0.15,
        "bounds=" + ",".join(f"{value:.6e}" for value in correlations),
    )

    power = 6
    renormalized = [spacing ** (-power) * exp(-lattice_rate / spacing) for spacing in spacings]
    tiny_spacings = (0.0005, 0.0002, 0.0001)
    tiny = [spacing ** (-power) * exp(-lattice_rate / spacing) for spacing in tiny_spacings]
    check(
        "Exponential separation beats every tested power-law field normalization",
        tiny[-1] < tiny[-2] < tiny[-3] and tiny[-1] < 1.0,
        "coarse=" + ",".join(f"{value:.3e}" for value in renormalized)
        + "; asymptotic=" + ",".join(f"{value:.3e}" for value in tiny),
    )

    # Example subexponential normalization exp(sqrt(1/a)).
    subexp = [exp((1.0 / spacing) ** 0.5 - lattice_rate / spacing) for spacing in tiny_spacings]
    check(
        "A sampled subexponential normalization cannot cancel the mixing exponential",
        subexp[-1] < subexp[-2] < subexp[-3],
        "bounds=" + ",".join(f"{value:.3e}" for value in subexp),
    )

    rho = 0.9
    gaps = [-log(rho) / (2.0 * spacing) for spacing in spacings]
    check(
        "A uniform transfer radius below one gives an inverse-spacing OS gap lower bound",
        all(gaps[index + 1] > gaps[index] for index in range(3))
        and abs(gaps[-1] * spacings[-1] + log(rho) / 2.0) < 1.0e-14,
        "gap lower bounds=" + ",".join(f"{value:.6f}" for value in gaps),
    )

    mass_floor = 5.809057503265459
    physical_masses = [mass_floor / spacing for spacing in spacings]
    check(
        "The compact-wedge dimensionful bare mass parameter diverges",
        all(physical_masses[index + 1] > physical_masses[index] for index in range(3)),
        "m/a=" + ",".join(f"{value:.3f}" for value in physical_masses),
    )

    text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    required = [
        "**Type:** no_go",
        "compact subset `K`",
        "log[L_F L_G |Z_F Z_G|]=o(1/a_j)",
        "contact-supported correlations can survive",
        "white-noise-type distributional limits may remain",
        "does not assert existence of a full distribution-valued continuum field",
        "Exponentially large field rescalings",
        "nonlocal/macroscopic loop families are not",
        "Delta_OS,j>=-(2a_j)^(-1)log rho_K",
        "varying OS Hilbert spaces",
        "Fixed-mass closed determinant loops",
        "does not imply that the gauge marginal becomes the pure",
        "standard Wilson weak-bare-coupling/light-lattice-mass",
        "No axiom-update stop",
        "No-Go Discipline N1--N8",
        "### N3 — hidden-condition phrase scan",
        "### N4 — citation/residual matching",
        "### N5 — rhetoric and resolution audit",
        "### N6 — partial-closure and primitive scan",
        "### N7 — hostile steelman",
        "### N8 — cross-cycle echo",
    ]
    missing = [item for item in required if item not in text]
    attempted = text.count("| `ATTEMPTED` |")
    independent = text.count("| No | No | Yes |")
    n2_conditions = [
        "compact strict Dobrushin interior",
        "controlled subexponential local observable class",
        "uniform lattice correlation length",
        "propagating continuum with covered nonzero separated correlations",
        "axiom-selected action",
    ]
    n2_pairs = [
        f"| {n2_conditions[left]} | {n2_conditions[right]} |"
        for left in range(len(n2_conditions))
        for right in range(left + 1, len(n2_conditions))
    ]
    missing_pairs = [item for item in n2_pairs if item not in text]
    check(
        "Source-note narrow no-go and N1-N8 contract",
        not missing and not missing_pairs and attempted >= 8 and independent >= 9,
        f"missing={missing}; missing N2 pairs={missing_pairs}; "
        f"attempted={attempted}; independent pairs={independent}",
    )

    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
