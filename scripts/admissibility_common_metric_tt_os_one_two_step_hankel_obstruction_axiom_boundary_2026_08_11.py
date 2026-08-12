#!/usr/bin/env python3
"""Test the Block-48 common-metric candidate at the physical OS gate.

The test uses the gauge-invariant spatial cross-polarization coordinate at a
declared axis momentum, obtains its covariance from the full six-dimensional
gauge quotient, and checks the first one- and two-step Hankel Grams.  It does
not infer a no-go for other constraint projections, boundary terms, field
coordinates, blocking depths, or gravity laws.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import null_space


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_COMMON_METRIC_TT_OS_ONE_TWO_STEP_HANKEL_OBSTRUCTION_"
    "AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
COMMON_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_"
    "GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
CURVATURE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_"
    "INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
IR_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_"
    "CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
TWO_STEP_PATH = (
    ROOT / "docs" / "AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md"
)
PREMISE_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_COMMON_METRIC_TT_OS_ONE_TWO_STEP_HANKEL_OBSTRUCTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py",
    "scripts/admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11 as block48  # noqa: E402


WAVE_NUMBER = 0.4
TIME_SIZES = (128, 256, 512, 1024, 2048, 4096)
HCOMPS = tuple(block48.HCOMPS)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 132 else detail[:129] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)


@dataclass(frozen=True)
class CarrierDatum:
    size: int
    moments: np.ndarray
    one_step_determinant: float
    one_step_minimum: float
    two_step_determinant: float
    two_step_minimum: float
    gauge_overlap: float
    ward_error: float
    hermiticity_error: float
    quotient_inertias: tuple[tuple[int, int, int], ...]


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def cross_coordinate() -> np.ndarray:
    vector = np.zeros(len(HCOMPS), dtype=complex)
    vector[HCOMPS.index((1, 2))] = 1.0
    return vector


def quotient_covariance(
    momentum: np.ndarray, observable: np.ndarray
) -> tuple[complex, tuple[int, int, int], float, float, float]:
    operator = -block48.common_metric_operator(momentum)
    gauge = block48.metric_gauge_map(momentum)
    quotient = null_space(gauge.conj().T, rcond=1.0e-11)
    reduced = quotient.conj().T @ operator @ quotient
    reduced = 0.5 * (reduced + reduced.conj().T)
    eigenvalues = np.linalg.eigvalsh(reduced)
    projected = quotient.conj().T @ observable
    covariance = projected.conj() @ np.linalg.solve(reduced, projected)
    inertia = (
        int(np.sum(eigenvalues < -1.0e-9)),
        int(np.sum(eigenvalues > 1.0e-9)),
        int(np.sum(np.abs(eigenvalues) <= 1.0e-9)),
    )
    return (
        covariance,
        inertia,
        float(np.linalg.norm(gauge.conj().T @ observable)),
        float(np.linalg.norm(operator @ gauge)),
        float(np.linalg.norm(operator - operator.conj().T)),
    )


def bordered_covariance(momentum: np.ndarray, observable: np.ndarray) -> complex:
    operator = -block48.common_metric_operator(momentum)
    gauge = block48.metric_gauge_map(momentum)
    border = np.block(
        [
            [operator, gauge],
            [gauge.conj().T, np.zeros((4, 4), dtype=complex)],
        ]
    )
    inverse = np.linalg.inv(border)[: len(HCOMPS), : len(HCOMPS)]
    return observable.conj() @ inverse @ observable


def carrier(size: int, observable: np.ndarray) -> CarrierDatum:
    frequencies = -np.pi + np.arange(size) * (2.0 * np.pi / size)
    covariance = np.empty(size, dtype=complex)
    inertias: set[tuple[int, int, int]] = set()
    gauge_overlap = 0.0
    ward_error = 0.0
    hermiticity_error = 0.0
    for index, frequency in enumerate(frequencies):
        momentum = np.asarray(
            (WAVE_NUMBER, 0.0, 0.0, frequency), dtype=complex
        )
        value, inertia, gauge, ward, hermiticity = quotient_covariance(
            momentum, observable
        )
        covariance[index] = value
        inertias.add(inertia)
        gauge_overlap = max(gauge_overlap, gauge)
        ward_error = max(ward_error, ward)
        hermiticity_error = max(hermiticity_error, hermiticity)

    moments = np.asarray(
        [
            np.mean(np.exp(1j * frequencies * time) * covariance).real
            for time in range(19)
        ]
    )
    one_step = np.asarray(
        ((moments[0], moments[1]), (moments[1], moments[2])), dtype=float
    )
    two_step = np.asarray(
        ((moments[0], moments[2]), (moments[2], moments[4])), dtype=float
    )
    return CarrierDatum(
        size=size,
        moments=moments,
        one_step_determinant=float(np.linalg.det(one_step)),
        one_step_minimum=float(np.linalg.eigvalsh(one_step)[0]),
        two_step_determinant=float(np.linalg.det(two_step)),
        two_step_minimum=float(np.linalg.eigvalsh(two_step)[0]),
        gauge_overlap=gauge_overlap,
        ward_error=ward_error,
        hermiticity_error=hermiticity_error,
        quotient_inertias=tuple(sorted(inertias)),
    )


def positive_atom_control(block: int) -> tuple[float, float]:
    weights = np.asarray((0.7, 0.3), dtype=float)
    eigenvalues = np.asarray((0.8, 0.3), dtype=float)
    moments = np.asarray(
        [np.sum(weights * eigenvalues**time) for time in range(2 * block + 1)]
    )
    gram = np.asarray(
        ((moments[0], moments[block]), (moments[block], moments[2 * block]))
    )
    return float(np.linalg.det(gram)), float(np.linalg.eigvalsh(gram)[0])


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axioms = flat(AXIOM_PATH)
    common = flat(COMMON_PATH)
    curvature = flat(CURVATURE_PATH)
    infrared = flat(IR_PATH)
    two_step = flat(TWO_STEP_PATH)

    checks.check(
        "source-and-scope-bindings",
        "the current axioms and exact gravity/transfer parents are read without importing a selected law",
        all(Path(ROOT / path).exists() for path in AUDIT_INPUT_PATHS)
        and "does not choose a hamiltonian or transfer operator" in axioms
        and "positive conditional decaying two-step spectral kernel" in common
        and "missing joint law is therefore a sourced connection/curvature propagation" in curvature
        and "two transverse-traceless polarizations" in infrared
        and "action-to-physical-car/os transfer identification" in two_step,
    )

    observable = cross_coordinate()
    data = tuple(carrier(size, observable) for size in TIME_SIZES)
    finest = data[-1]

    checks.check(
        "gauge-invariant-cross-coordinate",
        "the axis-momentum h_yz coordinate is orthogonal to every displacement-gauge column on every declared time carrier",
        max(item.gauge_overlap for item in data) < 5.0e-13,
        f"maximum gauge overlap={max(item.gauge_overlap for item in data):.3e}",
    )
    checks.check(
        "common-operator-ward-and-hermiticity",
        "the sign-fixed common-metric operator remains Hermitian and Ward-null on all tested Euclidean modes",
        max(item.ward_error for item in data) < 2.0e-12
        and max(item.hermiticity_error for item in data) < 2.0e-13,
        f"Ward={max(item.ward_error for item in data):.3e}; Hermiticity={max(item.hermiticity_error for item in data):.3e}",
    )
    checks.check(
        "six-dimensional-quotient-signature",
        "the full gauge quotient, not a scalar pole projection, is inverted and has one conformal-sign direction plus five positive directions",
        all(item.quotient_inertias == ((1, 5, 0),) for item in data),
        f"inertias={sorted(set(item.quotient_inertias for item in data))}",
    )

    method_error = 0.0
    for frequency in (-np.pi, -2.1, -1.0, 0.0, 0.7, 2.4, np.pi - 0.01):
        momentum = np.asarray(
            (WAVE_NUMBER, 0.0, 0.0, frequency), dtype=complex
        )
        quotient_value = quotient_covariance(momentum, observable)[0]
        border_value = bordered_covariance(momentum, observable)
        method_error = max(method_error, abs(quotient_value - border_value))
    checks.check(
        "quotient-bordered-crosscheck",
        "null-basis quotient inversion and an independent Lagrange-bordered inverse give the same TT covariance",
        method_error < 2.0e-13,
        f"maximum method difference={method_error:.3e}",
    )

    convergence = float(np.max(np.abs(data[-1].moments[:5] - data[-2].moments[:5])))
    checks.check(
        "finite-carrier-convergence",
        "the first five covariance moments stabilize across the two finest periodic-time carriers",
        convergence < 1.0e-6,
        "N=4096 moments=" + ",".join(f"{value:.9f}" for value in finest.moments[:5]),
    )

    checks.check(
        "one-step-os-hankel-obstruction",
        "the first h_yz moment Gram is indefinite on every declared carrier, excluding this covariance from a self-adjoint one-step transfer",
        max(item.one_step_determinant for item in data) < -0.15
        and max(item.one_step_minimum for item in data) < -0.043,
        f"det range={min(item.one_step_determinant for item in data):.9f}..{max(item.one_step_determinant for item in data):.9f}; finest min={finest.one_step_minimum:.9f}",
    )
    checks.check(
        "two-step-os-hankel-obstruction",
        "even-slice blocking leaves the first h_yz moment Gram indefinite, so the positive pole branches are not an action-derived two-step transfer",
        max(item.two_step_determinant for item in data) < -0.059
        and max(item.two_step_minimum for item in data) < -0.020,
        f"det range={min(item.two_step_determinant for item in data):.9f}..{max(item.two_step_determinant for item in data):.9f}; finest min={finest.two_step_minimum:.9f}",
    )

    controls = tuple(positive_atom_control(block) for block in (1, 2))
    checks.check(
        "positive-transfer-moment-control",
        "the identical Gram engine is positive on an explicit two-atom positive self-adjoint transfer measure",
        all(determinant > 0.05 and minimum > 0.03 for determinant, minimum in controls),
        f"controls={controls}",
    )

    poles = tuple(
        block48.solve_common_pole(WAVE_NUMBER, sector)
        for sector in block48.metric_sectors()
    )
    checks.check(
        "positive-poles-do-not-supply-positive-residues",
        "both Block-48 tensor poles remain real and give positive decaying numbers while the full TT covariance Gram is negative",
        all(pole.success for pole in poles)
        and max(abs(pole.frequency.imag) for pole in poles) < 1.0e-10
        and all(np.exp(-2.0 * pole.frequency.real) > 0.0 for pole in poles)
        and finest.two_step_determinant < 0.0,
        "poles=" + ",".join(f"{pole.frequency.real:.9f}" for pole in poles),
    )

    block_nine = np.asarray(
        (
            (finest.moments[0], finest.moments[9]),
            (finest.moments[9], finest.moments[18]),
        )
    )
    checks.check(
        "longer-block-and-boundary-routes-preserved",
        "a nine-slice first Gram is positive, so the result does not become a no-blocking, no-boundary, or gravity no-go",
        np.linalg.det(block_nine) > 1.0e-4
        and "longer blocking" in note
        and "boundary term" in note,
        f"nine-slice determinant={np.linalg.det(block_nine):.9f}",
    )

    checks.check(
        "exact-law-and-axiom-boundary",
        "the obstruction removes the advertised one/two-step common-metric repair but does not invent the dynamics excluded by the axioms",
        "retype admissibility" in note
        and "no canonical axiom is edited" in note
        and "zero toe percentage points" in note,
    )
    checks.check(
        "fresh-no-go-discipline-packet",
        "the bounded transfer obstruction passes N1 through N8 while retaining distinct constructive routes",
        all(f"n{index} —" in note for index in range(1, 9))
        and all(
            phrase in note
            for phrase in (
                "local edge observable",
                "canonical constraint reduction",
                "longer blocking",
                "boundary term",
                "nonlinear connection",
            )
        ),
    )

    print(
        "N5_CERTIFICATE: one complete ten-coordinate common metric, four gauge columns, six quotient directions, the h_yz TT coordinate, all 8,064 temporal modes on six carriers, one-step and two-step first Hankel blocks, two positive-control atoms, two tensor poles, and one nine-slice escape control are resolved"
    )
    print(
        "per_element: checked all ten metric coordinates through the full quotient operator and all four displacement-gauge columns before reading h_yz"
    )
    print(
        "per_site: checked the local common-metric cross-polarization coordinate and its independent quotient/bordered covariance constructions"
    )
    print(
        "per_mode: checked every Euclidean time mode on N=128,256,512,1024,2048,4096 at the declared k=0.4 axis momentum"
    )
    print(
        "per_block: checked one-step, even-slice two-step, positive-transfer atom controls, both common tensor poles, and a nine-slice non-no-go control"
    )
    print(
        "lattice_wide: no alternative field coordinate, boundary normalization, canonical constraint transfer, nonlinear connection, full-Z3 phase, or Record clock is excluded or inferred"
    )
    print(
        "scope_boundary: finite-carrier h_yz one/two-step OS obstruction for the Block-48 common-metric stationary-Schur candidate; not gravity failure, all-blocking failure, selected law, axiom adoption, or TOE closure"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
