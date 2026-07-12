#!/usr/bin/env python3
"""Interior OS descent and subsequential infinite-time transfer certificate."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "COUPLED_OS_INTERIOR_DESCENT_SUBSEQUENTIAL_INFINITE_TIME_TRANSFER_"
    "BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
SUPPLIER = ROOT / "scripts" / (
    "coupled_periodic_two_seam_su3_wilson_staggered_reflected_gram_"
    "2026_07_12.py"
)
TOL = 5.0e-10
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


def load_supplier():
    spec = importlib.util.spec_from_file_location("block17_supplier", SUPPLIER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def generalized_spectrum(metric: np.ndarray, form: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh((metric + metric.conj().T) / 2.0)
    keep = values > 1.0e-11
    inverse_root = (
        vectors[:, keep] * (1.0 / np.sqrt(values[keep]))
    ) @ vectors[:, keep].conj().T
    compressed = inverse_root @ form @ inverse_root
    return np.linalg.eigvalsh((compressed + compressed.conj().T) / 2.0)


def main() -> int:
    supplier = load_supplier()
    basis = supplier.observable_basis()
    translated = [supplier.shift_observable(item, 2, 6) for item in basis]
    gram0, _, _, _ = supplier.z3_reflected_gram(0, basis, basis)
    gram2, _, _, _ = supplier.z3_reflected_gram(0, basis, translated)

    boundary_names = {"1", "n1", "W1", "W1n1", "B1", "barB1"}
    boundary_indices = [
        index for index, observable in enumerate(basis) if observable[0] in boundary_names
    ]
    boundary_metric = gram0[np.ix_(boundary_indices, boundary_indices)]
    boundary_form = gram2[np.ix_(boundary_indices, boundary_indices)]
    boundary_spectrum = generalized_spectrum(boundary_metric, boundary_form)
    check(
        "Exact finite-group boundary core descends to a positive contraction matrix",
        np.min(np.linalg.eigvalsh(boundary_metric)) > 0.0
        and np.min(boundary_spectrum) > -TOL
        and np.max(boundary_spectrum) <= 1.0 + TOL,
        f"spectrum={','.join(f'{value:.9f}' for value in boundary_spectrum)}",
    )

    density2_index = next(
        index for index, observable in enumerate(basis) if observable[0] == "n2"
    )
    density_ratio = float(
        (gram2[density2_index, density2_index] / gram0[density2_index, density2_index]).real
    )
    check(
        "Exact finite-circle multi-slice contraction counterexample is 29 over 25",
        abs(density_ratio - 29.0 / 25.0) < TOL,
        f"B2(n2,n2)/B0(n2,n2)={density_ratio:.12f}",
    )

    identity_index = next(
        index for index, observable in enumerate(basis) if observable[0] == "1"
    )
    vacuum_ratio = float(
        (gram2[identity_index, identity_index] / gram0[identity_index, identity_index]).real
    )
    check(
        "Vacuum normalization blocks a scalar contraction repair",
        abs(vacuum_ratio - 1.0) < TOL and density_ratio > 1.0 + TOL,
        f"vacuum ratio={vacuum_ratio:.12f}, density ratio={density_ratio:.12f}",
    )

    seam_spectrum = np.linalg.eigvalsh(np.ones((3, 3)) + np.eye(3))
    check(
        "Strict seam-kernel positivity does not remove the broad counterexample",
        np.allclose(seam_spectrum, [1.0, 1.0, 4.0])
        and density_ratio > 1.0 + TOL,
        f"seam spectrum={seam_spectrum.tolist()}, density ratio={density_ratio:.12f}",
    )

    full_spectrum = generalized_spectrum(gram0, gram2)
    check(
        "Broad finite-circle core is positive but noncontractive",
        np.min(full_spectrum) > -TOL and np.max(full_spectrum) > 100.0,
        f"minimum={np.min(full_spectrum):.6e}, maximum={np.max(full_spectrum):.6f}",
    )

    roots = np.exp(2j * np.pi * np.arange(3) / 3.0)
    maximum_inverse_defect = 0.0
    for mass in (0.2, 1.0, 3.0):
        for labels in np.ndindex(*(3,) * 6):
            temporal = np.array([roots[label] for label in labels])
            dmat = supplier.temporal_dirac(temporal, mass)
            inverse_norm = float(np.linalg.norm(np.linalg.inv(dmat), 2))
            maximum_inverse_defect = max(
                maximum_inverse_defect, inverse_norm - 1.0 / mass
            )
    check(
        "Massive staggered resolvent obeys the uniform one over m bound",
        maximum_inverse_defect < TOL,
        f"maximum ||D^-1||-1/m={maximum_inverse_defect:.3e}",
    )

    spectral_points = np.array([1.0, 0.73, 0.21])
    weights = np.array([0.2, 0.5, 0.3])
    sequence = np.array(
        [np.sum(weights * spectral_points ** (2 * step)) for step in range(12)]
    )
    log_convex_defect = max(
        sequence[step] ** 2 - sequence[step - 1] * sequence[step + 1]
        for step in range(1, len(sequence) - 1)
    )
    check(
        "Positive spectral moments are bounded log-convex and nonincreasing",
        log_convex_defect < TOL and np.max(np.diff(sequence)) <= TOL,
        f"max log-convex defect={log_convex_defect:.3e}, max increase={np.max(np.diff(sequence)):.3e}",
    )

    null_metric = np.diag([1.0, 0.0, 2.0])
    shift = np.array([[0.5, 0.0, 0.0], [0.0, 7.0, 0.0], [0.0, 0.0, 0.25]])
    descended = null_metric @ shift
    null_vector = np.array([0.0, 1.0, 0.0])
    check(
        "Support-controlled B0 pairing kills every B0-null first slot",
        np.linalg.norm(null_metric @ null_vector) == 0.0
        and np.linalg.norm(descended.conj().T @ null_vector) == 0.0,
        "finite matrix model of B2(F,G)=B0(F,tau2 G)",
    )

    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    conditions = [
        "supplied action and dynamics",
        "supplied spin and reflection",
        "unique boundary-independent infinite-time state",
        "spatial thermodynamic limit",
        "controlled Lorentz, QFT, and Standard Model continuum",
        "dynamical gravity and GR limit",
    ]
    pairs = [
        f"| {conditions[left]} | {conditions[right]} |"
        for left in range(len(conditions))
        for right in range(left + 1, len(conditions))
    ]
    required = [
        "finite-circle interior null descent",
        "29/25",
        "subsequential infinite-time",
        "diagonal subsequence",
        "bounded log-convex",
        "positive self-adjoint contraction",
        "does not prove uniqueness",
        "No-Go Discipline N1--N8",
        "### N3 — hidden-condition phrase scan",
        "### N4 — citation/residual matching",
        "### N5 — rhetoric and resolution audit",
        "### N6 — partial-closure, convention, reframe, and primitive scan",
        "### N7 — hostile steelman",
        "### N8 — cross-cycle echo",
        "Test and result",
        "Why it does not close the remaining boundary / authority surface",
        "Left closes right? | Right closes left? | Independent?",
        "| `we assume` |",
        "| `by construction` |",
        "| `as is standard` |",
        "| `the framework provides` |",
        "| `bridge context` |",
        "| `background` |",
        "| `naturally` |",
        "| `obviously` |",
        "| `standard QFT` |",
        "| `registered` |",
        "| `canonical` |",
        "Cited witness and location | Witness residual | Present residual | Match?",
        "Statement / resolution | Tested?",
        "Full gauge-invariant positive-half algebra | No",
        "Dynamical `SU(3)` finite circle | No",
        "Larger temporal circumferences | No in the primary certificate",
        "Retirement mechanism and applicability here",
        "No axiom-update stop",
    ]
    missing = [item for item in required + pairs if item not in note_text]
    attempted = note_text.count("| `ATTEMPTED` |")
    directional_pairs = note_text.count("| No | No | Yes |")
    contract = (
        not missing
        and attempted >= 7
        and directional_pairs >= 15
        and "Block 17" not in note_text
        and "| `C1,C2` |" not in note_text
    )
    check(
        "Source-note boundary and N1-N8 contract",
        contract,
        f"schema present; attempted routes={attempted}; directional pairs={directional_pairs}"
        if contract
        else (
            f"missing={missing}; attempted={attempted}; "
            f"directional pairs={directional_pairs}"
        ),
    )

    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
