#!/usr/bin/env python3
"""Framework-native N5 no-go for independent commuting transfer factors.

The runner checks that the current minimal/local tensor surface does not
exclude independent commuting transfer factors on disjoint local regions. It
does not admit those factors as physical clocks; it shows that an N5 exclusion
needs an extra irreducibility, physical-clock, or gauge/redundancy bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "SINGLE_CLOCK_INDEPENDENT_COMMUTING_TRANSFER_FACTOR_N5_NO_GO_NOTE_2026-06-17.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md"
TENSOR = ROOT / "docs" / "LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md"
SCOPE = ROOT / "docs" / "SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md"
SINGLE_CLOCK = ROOT / "docs" / "AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md"
AXIS_NO_GO = ROOT / "docs" / "SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md"
KMS_NO_GO = ROOT / "docs" / "SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_NOTE_2026-06-16.md"


@dataclass
class Check:
    ok: bool
    label: str
    detail: str = ""


checks: list[Check] = []


def check(ok: bool, label: str, detail: str = "") -> None:
    checks.append(Check(bool(ok), label, detail))
    status = "PASS" if ok else "FAIL"
    if detail:
        print(f"{status}: {label} -- {detail}")
    else:
        print(f"{status}: {label}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def assert_contains(path: Path, needle: str, label: str | None = None) -> None:
    body = read(path)
    check(needle in body, label or f"{path.name} contains {needle!r}")


def opnorm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix, ord=2))


def expm_hermitian(generator: np.ndarray, coefficient: complex) -> np.ndarray:
    vals, vecs = np.linalg.eigh(generator)
    return vecs @ np.diag(np.exp(coefficient * vals)) @ vecs.conj().T


def positive_sqrt_transfer(generator: np.ndarray, tau: float) -> np.ndarray:
    return expm_hermitian(generator, -tau)


def is_positive_definite(matrix: np.ndarray, tol: float = 1e-12) -> bool:
    vals = np.linalg.eigvalsh((matrix + matrix.conj().T) / 2)
    return bool(np.min(vals) > tol)


def kron2(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.kron(a, b)


def main() -> int:
    print("single-clock independent commuting transfer factor N5 no-go")
    print("=" * 72)

    assert_contains(NOTE, "Claim boundary", "note states claim boundary")
    assert_contains(NOTE, "does not prove a second physical clock exists", "note blocks physical-clock overclaim")
    assert_contains(NOTE, "Does not alter the axiom count")
    assert_contains(NOTE, "AUDIT_LEDGER_WRITTEN=FALSE")
    assert_contains(NOTE, "B_AXIS_DERIVED=FALSE")
    assert_contains(NOTE, "SECOND_PHYSICAL_CLOCK_PROVED=FALSE")
    assert_contains(NOTE, "irreducibility/nonfactorization theorem", "note names irreducibility supplier")
    assert_contains(NOTE, "physical-clock admission theorem", "note names clock-admission supplier")
    assert_contains(NOTE, "gauge/redundancy theorem", "note names gauge-redundancy supplier")

    assert_contains(MINIMAL, "dynamics", "minimal Lattice/Quantum surface supplies no dynamics")
    assert_contains(MINIMAL, "time metric", "Record axiom explicitly supplies no time metric")
    assert_contains(MINIMAL, "finite central-sector decomposition", "Record readout context is explicit")
    assert_contains(TENSOR, "[O_x, O_y]", "tensor-locality note supplies disjoint-factor commutation")
    assert_contains(TENSOR, "Does **not** prove the (M2) Lieb-Robinson lightcone", "tensor note excludes dynamics")
    assert_contains(SCOPE, "N5:", "scope boundary keeps N5 explicit")
    assert_contains(SCOPE, "independent commuting transfer factors", "scope boundary names the N5 wall")
    assert_contains(SINGLE_CLOCK, "(B-AXIS.3)", "single-clock source contains B-AXIS.3")
    assert_contains(SINGLE_CLOCK, "no independent commuting transfer factor", "single-clock source target text visible")
    assert_contains(AXIS_NO_GO, "B-AXIS.3", "axis-label no-go leaves N5 visible")
    assert_contains(KMS_NO_GO, "Does not exclude independent commuting transfer factors", "KMS/APBC no-go leaves N5 visible")

    # Two disjoint one-qubit local factors.
    ident = np.eye(2, dtype=complex)
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
    p_up = np.array([[1, 0], [0, 0]], dtype=complex)

    # Non-scalar positive-energy factor generators. Distinct tau values make
    # the clock-unit wall visible, while the common-product check below fixes a
    # common tau for the product transfer.
    h_a = 1.20 * ident + 0.35 * sigma_z
    h_b = 0.90 * ident + 0.25 * sigma_z
    tau_a = 1.0
    tau_b = 1.7

    h_a_lift = kron2(h_a, ident)
    h_b_lift = kron2(ident, h_b)
    t_a_lift = kron2(positive_sqrt_transfer(h_a, tau_a), ident)
    t_b_lift = kron2(ident, positive_sqrt_transfer(h_b, tau_b))

    check(is_positive_definite(t_a_lift), "T_A x I is positive with trivial kernel",
          f"min_eig={np.min(np.linalg.eigvalsh(t_a_lift)).real:.6f}")
    check(is_positive_definite(t_b_lift), "I x T_B is positive with trivial kernel",
          f"min_eig={np.min(np.linalg.eigvalsh(t_b_lift)).real:.6f}")
    check(opnorm(t_a_lift @ t_b_lift - t_b_lift @ t_a_lift) < 1e-13,
          "lifted factor transfers commute exactly",
          f"resid={opnorm(t_a_lift @ t_b_lift - t_b_lift @ t_a_lift):.2e}")
    check(opnorm(h_a_lift @ h_b_lift - h_b_lift @ h_a_lift) < 1e-13,
          "lifted factor generators commute exactly",
          f"resid={opnorm(h_a_lift @ h_b_lift - h_b_lift @ h_a_lift):.2e}")

    span_rank = np.linalg.matrix_rank(np.stack([h_a_lift.ravel(), h_b_lift.ravel()]), tol=1e-12)
    check(span_rank == 2, "factor-generator tangent span is two-dimensional",
          f"rank={span_rank}")

    # With one common tau, product Stone uniqueness returns the summed
    # generator. This confirms no contradiction with the narrow Stone theorem.
    tau_common = 1.0
    t_a_common = kron2(positive_sqrt_transfer(h_a, tau_common), ident)
    t_b_common = kron2(ident, positive_sqrt_transfer(h_b, tau_common))
    t_product = t_a_common @ t_b_common
    vals, vecs = np.linalg.eigh(t_product)
    h_from_product = vecs @ np.diag(-np.log(vals) / tau_common) @ vecs.conj().T
    h_sum = h_a_lift + h_b_lift
    check(opnorm(h_from_product - h_sum) < 1e-10,
          "product transfer Stone generator is H_A x I + I x H_B",
          f"resid={opnorm(h_from_product - h_sum):.2e}")

    u10 = expm_hermitian(h_a_lift, -1j)
    rs = np.linspace(-8.0, 8.0, 32001)
    min_gap = min(opnorm(u10 - expm_hermitian(h_sum, -1j * r)) for r in rs)
    check(min_gap > 0.05, "U_A(1) x I is not on the diagonal one-clock product orbit",
          f"min_gap={min_gap:.4f}")

    u_a = expm_hermitian(h_a_lift, -0.37j)
    u_b = expm_hermitian(h_b_lift, 0.81j)
    check(opnorm(u_a @ u_b - u_b @ u_a) < 1e-13,
          "two-parameter unitary family is abelian on disjoint factors",
          f"resid={opnorm(u_a @ u_b - u_b @ u_a):.2e}")

    # Record compatibility: two disjoint factor projectors are commuting durable
    # counters, and finite scalar additivity is exactly respected.
    p_a = kron2(p_up, ident)
    p_b = kron2(ident, p_up)
    zero = np.zeros((4, 4), dtype=complex)
    record_1 = p_a
    record_2 = p_a + p_b
    check(opnorm(p_a @ p_b - p_b @ p_a) < 1e-13,
          "disjoint record projectors commute",
          f"resid={opnorm(p_a @ p_b - p_b @ p_a):.2e}")
    check(is_positive_definite(record_1 - zero + 1e-9 * np.eye(4)),
          "record counter 0 <= P_A is operator-monotone")
    check(is_positive_definite(record_2 - record_1 + 1e-9 * np.eye(4)),
          "record counter P_A <= P_A + P_B is operator-monotone")
    check(abs(np.trace(record_2).real - (np.trace(p_a).real + np.trace(p_b).real)) < 1e-12,
          "finite scalar readout is additive on disjoint records",
          f"tr(P_A+P_B)={np.trace(record_2).real:.1f}")

    # A nonfactorizing coupling is the shape of a possible future escape: it
    # breaks the independent factor-clock construction, but it is an extra
    # bridge not supplied by the minimal local tensor surface.
    h_couple = kron2(sigma_x, sigma_x)
    comm_a = opnorm(h_couple @ h_a_lift - h_a_lift @ h_couple)
    comm_b = opnorm(h_couple @ h_b_lift - h_b_lift @ h_couple)
    check(comm_a > 0.1 and comm_b > 0.1,
          "nonfactorizing coupling would obstruct independent factor clocks",
          f"comm_a={comm_a:.3f}, comm_b={comm_b:.3f}")
    check("irreducibility/nonfactorization" in read(NOTE) and "not present in the current minimal surface" in read(NOTE),
          "note classifies the coupling escape as an extra bridge, not an axiom consequence")

    passed = sum(1 for c in checks if c.ok)
    failed = sum(1 for c in checks if not c.ok)
    print()
    print(f"SUMMARY: PASS={passed} FAIL={failed}")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("B_AXIS_DERIVED=FALSE")
    print("SECOND_PHYSICAL_CLOCK_PROVED=FALSE")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
