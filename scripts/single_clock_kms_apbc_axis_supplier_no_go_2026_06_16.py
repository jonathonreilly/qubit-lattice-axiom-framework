#!/usr/bin/env python3
"""KMS/APBC cannot supply the single-clock axis.

This runner is intentionally finite and deterministic. It checks that
fermionic antiperiodic boundary conditions are covariant with the already
chosen evolution circle: APBC on tau transports to APBC on x1 under the
same W exchange used in the single-clock axis-selection notes. The
axis-selecting datum is the asymmetry between axes, not KMS/APBC itself.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_NOTE_2026-06-16.md"
KMS_NOTE = ROOT / "docs" / "AXIOM_FIRST_KMS_CONDITION_THEOREM_NOTE_2026-05-01.md"
AXIS_NOTE = ROOT / "docs" / "SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md"
SCOPE_NOTE = ROOT / "docs" / "SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md"
SPIN_NOTE = ROOT / "docs" / "SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md"


@dataclass
class Check:
    ok: bool
    label: str
    detail: str = ""


checks: list[Check] = []


def check(ok: bool, label: str, detail: str = "") -> None:
    checks.append(Check(ok, label, detail))
    status = "PASS" if ok else "FAIL"
    if detail:
        print(f"{status}: {label} -- {detail}")
    else:
        print(f"{status}: {label}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def assert_contains(path: Path, needle: str, label: str | None = None) -> None:
    text = read(path)
    check(needle in text, label or f"{path.name} contains {needle!r}")


L = (4, 4, 2, 2)
COORDS = [(a, b, c, d) for a in range(L[0]) for b in range(L[1]) for c in range(L[2]) for d in range(L[3])]
INDEX = {x: i for i, x in enumerate(COORDS)}
N = len(COORDS)


def eta(x: tuple[int, int, int, int], mu: int) -> int:
    if mu == 0:
        return 1
    return -1 if sum(x[:mu]) % 2 else 1


def staggered_hop(anti_axes: set[int]) -> np.ndarray:
    """Real antisymmetric staggered hop with optional APBC wrap signs."""

    matrix = np.zeros((N, N), dtype=float)
    for x in COORDS:
        i = INDEX[x]
        for mu in range(4):
            y = list(x)
            wraps = y[mu] == L[mu] - 1
            y[mu] = (y[mu] + 1) % L[mu]
            y_t = tuple(y)
            sign = eta(x, mu)
            if wraps and mu in anti_axes:
                sign *= -1
            j = INDEX[y_t]
            matrix[i, j] += sign
            matrix[j, i] -= sign
    return matrix


def exchange_w() -> np.ndarray:
    """W = P_{tau<->x1} diag((-1)^(x_tau*x_1))."""

    matrix = np.zeros((N, N), dtype=float)
    for x in COORDS:
        tau, x1, x2, x3 = x
        y = (x1, tau, x2, x3)
        sign = -1 if (tau * x1) % 2 else 1
        matrix[INDEX[y], INDEX[x]] = sign
    return matrix


def norm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a))


def cyclic_shift(length: int, antiperiodic: bool) -> np.ndarray:
    matrix = np.zeros((length, length), dtype=float)
    for i in range(length):
        j = (i + 1) % length
        matrix[j, i] = -1.0 if antiperiodic and i == length - 1 else 1.0
    return matrix


def main() -> int:
    print("single-clock KMS/APBC axis-supplier no-go")
    print("=" * 72)

    assert_contains(NOTE, "KMS/APBC cannot discharge B-AXIS")
    assert_contains(NOTE, "APBC on a supplied circle is axis-covariant")
    assert_contains(NOTE, "Does not alter the axiom count")
    assert_contains(NOTE, "actual_current_surface_status: no-go")
    assert_contains(NOTE, "Five scoped routes were checked")
    assert_contains(NOTE, "context only, not as a proof dependency")

    assert_contains(KMS_NOTE, "RP-reconstructed two-step transfer-matrix", "KMS note starts from supplied RP transfer")
    assert_contains(KMS_NOTE, "Euclidean-time block", "KMS note names a supplied Euclidean time block")
    assert_contains(KMS_NOTE, "anti-periodic-in-time, periodic-in-space", "KMS note APBC is already time-labelled")
    assert_contains(SCOPE_NOTE, "N2:", "scope note keeps N2 explicit")
    assert_contains(SCOPE_NOTE, "N4:", "scope note keeps N4 explicit")
    assert_contains(SCOPE_NOTE, "N5:", "scope note keeps N5 explicit")
    assert_contains(AXIS_NOTE, "boundary-condition asymmetry", "prior axis no-go identifies BC-asymmetry pin")
    assert_contains(SPIN_NOTE, "Grassmann generators", "spin/Berezin note is algebraic after generators are supplied")

    w = exchange_w()
    ident = np.eye(N)
    check(norm(w @ w.T - ident) < 1e-12, "W is orthogonal", f"resid={norm(w @ w.T - ident):.2e}")

    pbc = staggered_hop(set())
    ap_tau = staggered_hop({0})
    ap_x1 = staggered_hop({1})
    ap_both = staggered_hop({0, 1})

    check(norm(w @ pbc @ w.T - pbc) < 1e-12, "periodic staggered surface is W-invariant", f"resid={norm(w @ pbc @ w.T - pbc):.2e}")
    check(norm(w @ ap_tau @ w.T - ap_x1) < 1e-12, "APBC on supplied tau transports exactly to APBC on supplied x1", f"resid={norm(w @ ap_tau @ w.T - ap_x1):.2e}")
    check(norm(w @ ap_tau @ w.T - ap_tau) > 1.0, "APBC(tau)/PBC(x1) breaks W only as a supplied asymmetric datum", f"resid={norm(w @ ap_tau @ w.T - ap_tau):.6g}")
    check(norm(w @ ap_both @ w.T - ap_both) < 1e-12, "APBC on both exchanged axes restores W", f"resid={norm(w @ ap_both @ w.T - ap_both):.2e}")

    rank_tau = int(np.linalg.matrix_rank(ap_tau, tol=1e-9))
    rank_pbc = int(np.linalg.matrix_rank(pbc, tol=1e-9))
    check(N - rank_tau == 0, "tau-APBC removes the periodic zero-kernel witness on this block", f"kernel_dim={N-rank_tau}")
    check(N - rank_pbc > 0, "PBC surface keeps a zero-kernel witness on this block", f"kernel_dim={N-rank_pbc}")

    for length in (4, 6):
        cap = cyclic_shift(length, antiperiodic=True)
        cp = cyclic_shift(length, antiperiodic=False)
        check(norm(np.linalg.matrix_power(cap, length) + np.eye(length)) < 1e-12, f"APBC cyclic shift has C^{length}=-I on a supplied circle")
        check(norm(np.linalg.matrix_power(cp, length) - np.eye(length)) < 1e-12, f"PBC cyclic shift has C^{length}=I on a supplied circle")

    passed = sum(1 for c in checks if c.ok)
    failed = sum(1 for c in checks if not c.ok)
    print()
    print(f"SUMMARY: PASS={passed} FAIL={failed}")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print("B_AXIS_DERIVED=FALSE")
    print("BC_ASYMMETRY_SUPPLIED_BY_KMS_APBC=FALSE")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
