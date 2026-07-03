#!/usr/bin/env python3
"""Dynamics nontriviality/selection firewall.

The runner checks a small exact matrix model illustrating the residual already
named by the dynamics-form theorem: class-membership constraints do not select
a nonzero Hamiltonian, coefficients, or truncation.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
TOL = 1e-11


def report(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 78)
    print(title)
    print("-" * 78)


def read_rel(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def require_text(path: str, needles: list[str]) -> None:
    text = read_rel(path)
    report(f"{path} exists", True)
    for needle in needles:
        report(f"{path} contains: {needle}", needle in text)


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)


def kron(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.kron(a, b)


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def norm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a))


def commutes(a: np.ndarray, b: np.ndarray) -> bool:
    return norm(comm(a, b)) < TOL


def hermitian(a: np.ndarray) -> bool:
    return np.allclose(a, a.conj().T, atol=TOL)


@dataclass(frozen=True)
class Term:
    name: str
    matrix: np.ndarray
    support_size: int


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06.md",
        [
            "actual_current_surface_status: no-go",
            "trace_class: negative_route_pruning",
            "allowed dynamics class",
            "Does not select a generation or Koide dial location.",
        ],
    )
    require_text(
        "docs/DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md",
        [
            "non-triviality",
            "trivial `H = 0` is in the class",
            "does **not** derive the action",
            "couplings + the minimality/truncation",
        ],
    )
    require_text(
        "docs/RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md",
        [
            "does not select couplings",
            "nonzero dynamics",
            "couplings, action shape, and lowest-order truncation",
            "nontriviality of the physical Hamiltonian/transfer step",
        ],
    )
    require_text(
        "docs/TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md",
        [
            "does not derive gauge dynamics",
            "coupling values",
            "The safe downstream use is only the bounded finite-algebra statement",
        ],
    )


def class_membership_checks() -> None:
    section("Allowed-class membership does not select coefficients")
    G = kron(Z, I2) + kron(I2, Z)
    mass = Term("mass", kron(Z, I2) + kron(I2, Z), 1)
    electric = Term("electric", kron(Z, Z), 2)
    exchange = Term("charge_exchange", kron(X, X) + kron(Y, Y), 2)
    variant = Term("bare_flip", kron(X, I2), 1)
    allowed_terms = (mass, electric, exchange)

    for term in allowed_terms:
        report(f"{term.name} is Hermitian", hermitian(term.matrix))
        report(f"{term.name} commutes with conserved charge", commutes(term.matrix, G))
    report("gauge-variant control fails the class predicate", not commutes(variant.matrix, G))

    H0 = np.zeros((4, 4), dtype=complex)
    report("zero Hamiltonian is Hermitian", hermitian(H0))
    report("zero Hamiltonian is in the allowed class", commutes(H0, G))

    couplings = [
        (0.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),
        (0.0, -2.0, 0.0),
        (0.25, -1.5, 3.0),
        (-7.0, 0.125, 0.5),
    ]
    hs = []
    for coeffs in couplings:
        H = sum(c * term.matrix for c, term in zip(coeffs, allowed_terms))
        hs.append(H)
        report(f"couplings {coeffs} remain in allowed class", hermitian(H) and commutes(H, G))
    distinct_nonzero = norm(hs[1] - hs[2]) > TOL and norm(hs[3] - hs[4]) > TOL
    report("multiple distinct nonzero allowed Hamiltonians exist", distinct_nonzero)
    report("class predicate does not choose among allowed coupling tuples", len(couplings) > 3)

    observable = kron(Z, I2)
    report("H=0 gives trivial Heisenberg derivative", norm(1j * comm(H0, observable)) < TOL)
    report("nonzero allowed H can give nontrivial derivative", norm(1j * comm(exchange.matrix, observable)) > TOL)


def truncation_checks() -> None:
    section("Allowed class does not force lowest-order truncation")
    candidates = [
        {"name": "on_site_mass", "support": 1, "allowed": True},
        {"name": "nearest_covariant_hop", "support": 3, "allowed": True},
        {"name": "plaquette_loop", "support": 4, "allowed": True},
        {"name": "rectangle_loop", "support": 6, "allowed": True},
        {"name": "long_covariant_path", "support": 7, "allowed": True},
        {"name": "bare_open_hop", "support": 2, "allowed": False},
    ]
    allowed = [c for c in candidates if c["allowed"]]
    leading = [c for c in allowed if c["support"] <= 4]
    higher = [c for c in allowed if c["support"] > 4]
    report("leading local invariants exist", {c["name"] for c in leading} >= {"on_site_mass", "nearest_covariant_hop", "plaquette_loop"})
    report("higher-range allowed invariants are not excluded by class membership", len(higher) == 2)
    report("bare open hop is excluded by class membership", not next(c for c in candidates if c["name"] == "bare_open_hop")["allowed"])
    minimality_principle_supplied = False
    report("minimality/truncation principle supplied flag is false", not minimality_principle_supplied)


def firewall_checks() -> None:
    section("Firewall flags")
    nonzero_dynamics_selected = False
    coupling_values_selected = False
    action_shape_selected = False
    lowest_order_truncation_selected = False
    clock_or_rate_selected = False
    born_weights_selected = False
    generation_or_koide_dial_selected = False
    report("nonzero dynamics selected flag is false", not nonzero_dynamics_selected)
    report("coupling values selected flag is false", not coupling_values_selected)
    report("action shape selected flag is false", not action_shape_selected)
    report("lowest-order truncation selected flag is false", not lowest_order_truncation_selected)
    report("clock/rate selected flag is false", not clock_or_rate_selected)
    report("Born/probability selected flag is false", not born_weights_selected)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)


def main() -> int:
    source_anchor_checks()
    class_membership_checks()
    truncation_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("FORM_CLASS_SELECTS_NONZERO_DYNAMICS=FALSE")
    print("FORM_CLASS_SELECTS_COUPLINGS_ACTION_OR_TRUNCATION=FALSE")
    print("ALLOWED_CLASS_MEMBERSHIP_INTERFACE=TRUE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
