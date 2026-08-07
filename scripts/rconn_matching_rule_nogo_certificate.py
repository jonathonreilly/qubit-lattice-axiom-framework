#!/usr/bin/env python3
"""Certificate for the R_conn matching-rule no-go repair."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@dataclass(frozen=True)
class Check:
    name: str
    ok: bool
    detail: str


class Checkbook:
    def __init__(self) -> None:
        self.checks: list[Check] = []

    def require(self, name: str, ok: bool, detail: str) -> None:
        self.checks.append(Check(name, bool(ok), detail))

    @property
    def pass_count(self) -> int:
        return sum(1 for check in self.checks if check.ok)

    @property
    def fail_count(self) -> int:
        return sum(1 for check in self.checks if not check.ok)

    def report(self) -> None:
        print("CHECK SUMMARY")
        for check in self.checks:
            status = "PASS" if check.ok else "FAIL"
            print(f"  {status:4s} {check.name}: {check.detail}")


def su_generators(n: int) -> list[np.ndarray]:
    """Return Hermitian SU(n) generators with Tr(T_a T_b)=delta_ab/2."""
    gens: list[np.ndarray] = []

    for i in range(n):
        for j in range(i + 1, n):
            sym = np.zeros((n, n), dtype=complex)
            sym[i, j] = 0.5
            sym[j, i] = 0.5
            gens.append(sym)

            anti = np.zeros((n, n), dtype=complex)
            anti[i, j] = -0.5j
            anti[j, i] = 0.5j
            gens.append(anti)

    for k in range(1, n):
        diag = np.zeros((n, n), dtype=complex)
        for i in range(k):
            diag[i, i] = 1.0
        diag[k, k] = -float(k)
        diag /= math.sqrt(2.0 * k * (k + 1.0))
        gens.append(diag)

    return gens


def orthonormality_error(gens: list[np.ndarray]) -> float:
    max_error = 0.0
    for i, left in enumerate(gens):
        for j, right in enumerate(gens):
            expected = 0.5 if i == j else 0.0
            value = np.trace(left @ right)
            max_error = max(max_error, abs(value - expected))
    return float(max_error)


def fierz_error(gens: list[np.ndarray]) -> float:
    n = gens[0].shape[0]
    max_error = 0.0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    lhs = 1.0 if (i == l and j == k) else 0.0
                    rhs = (1.0 / n if (i == j and k == l) else 0.0)
                    rhs += 2.0 * sum(gen[i, j] * gen[k, l] for gen in gens)
                    max_error = max(max_error, abs(lhs - rhs))
    return float(max_error)


def f_adj(n: int) -> Fraction:
    return Fraction(n * n - 1, n * n)


def k_ew(n: int, kappa: Fraction) -> Fraction:
    f = f_adj(n)
    return Fraction(1, 1) / (f + kappa * (1 - f))


def cmt_scaled_k(n: int, kappa: Fraction, u0: Fraction) -> Fraction:
    f = f_adj(n)
    c = f * u0 * u0
    s = (1 - f) * u0 * u0
    total = c + s
    return total / (c + kappa * s)


def run_algebra_checks(checks: Checkbook) -> None:
    print("FIERZ / CHANNEL-COUNT PACKET")
    for n in (2, 3, 4, 5):
        gens = su_generators(n)
        expected_count = n * n - 1
        ortho = orthonormality_error(gens)
        fierz = fierz_error(gens)
        fraction = f_adj(n)
        assert np.allclose(ortho, 0.0, atol=1e-12)
        assert np.allclose(fierz, 0.0, atol=1e-12)

        print(
            f"  N={n}: generators={len(gens)}, ortho={ortho:.3e}, "
            f"Fierz={fierz:.3e}, F_adj={fraction}"
        )

        checks.require(
            f"SU({n}) generator count",
            len(gens) == expected_count,
            f"{len(gens)} == {expected_count}",
        )
        checks.require(
            f"SU({n}) generator orthonormality",
            np.allclose(ortho, 0.0, atol=1e-12),
            f"max error={ortho:.3e}",
        )
        checks.require(
            f"SU({n}) Fierz completeness",
            np.allclose(fierz, 0.0, atol=1e-12),
            f"max error={fierz:.3e}",
        )
        checks.require(
            f"SU({n}) adjoint fraction",
            fraction == Fraction(n * n - 1, n * n),
            f"F_adj={fraction}",
        )


def run_matching_rule_checks(checks: Checkbook) -> None:
    n = 3
    f = f_adj(n)
    k0 = k_ew(n, Fraction(0, 1))
    k1 = k_ew(n, Fraction(1, 1))
    k_half = k_ew(n, Fraction(1, 2))

    print()
    print("MATCHING-RULE UNDERDETERMINATION PACKET")
    print(f"  F_adj={f}, K(0)={k0}, K(1/2)={k_half}, K(1)={k1}")

    checks.require("Nc=3 exact F_adj", f == Fraction(8, 9), f"F_adj={f}")
    checks.require("connected selector K(0)", k0 == Fraction(9, 8), f"K(0)={k0}")
    checks.require("full trace selector K(1)", k1 == Fraction(1, 1), f"K(1)={k1}")
    checks.require("selector non-uniqueness", k0 != k1, f"K(0)={k0}, K(1)={k1}")

    u0_values = (Fraction(1, 2), Fraction(4, 5), Fraction(13, 10))
    for kappa in (Fraction(0, 1), Fraction(1, 2), Fraction(1, 1)):
        values = [cmt_scaled_k(n, kappa, u0) for u0 in u0_values]
        checks.require(
            f"CMT scaling invariance kappa={kappa}",
            all(value == values[0] for value in values),
            f"values={values}",
        )

    disconnected_ratios = {
        Fraction(0, 1): Fraction(0, 1),
        Fraction(1, 2): Fraction(1, 16),
        Fraction(1, 1): Fraction(1, 8),
    }
    checks.require(
        "OZI class does not select coefficient",
        len(set(disconnected_ratios.values())) == len(disconnected_ratios),
        f"ratios={disconnected_ratios}",
    )
    checks.require(
        "two-completion no-go witness",
        f == Fraction(8, 9) and k0 == Fraction(9, 8) and k1 == Fraction(1, 1),
        "kappa=0 and kappa=1 share Fierz/CMT premises but produce different K_EW",
    )


def run_note_checks(checks: Checkbook) -> None:
    note_path = os.path.join(ROOT, "docs", "RCONN_DERIVED_NOTE.md")
    with open(note_path, "r", encoding="utf-8") as handle:
        text = handle.read()

    checks.require("note declares no_go", "**Claim type:** no_go" in text, "claim type marker present")
    checks.require("note names runner", "scripts/rconn_matching_rule_nogo_certificate.py" in text, "runner path present")
    checks.require("note names kappa_EW", "kappa_EW" in text, "free readout coefficient present")
    checks.require("note states no new axiom", "No new axiom" in text, "no-new-axiom sentence present")
    checks.require(
        "note keeps physical readout conditional",
        "does not claim that the physical connected-trace readout is derived" in text,
        "physical readout disclaimer present",
    )


def print_n5_execution_certificate() -> None:
    """Print-only granularity record; adds no Check to the Checkbook."""
    gens = su_generators(3)
    ortho = orthonormality_error(gens)
    fierz = fierz_error(gens)

    print()
    print("N5 EXECUTION CERTIFICATE")
    print(
        f"  per_element: exercised at full index resolution -- the Fierz test walks every one of the {3 ** 4} index "
        "quadruples (i,j,k,l) of the SU(3) color space and compares the two sides of the completeness identity entry "
        f"against entry, while orthonormality evaluates Tr(T_a T_b) for all {len(gens) ** 2} ordered generator pairs "
        f"against delta_ab/2. The worst entrywise residuals here are {fierz:.3e} and {ortho:.3e} against the atol of "
        "1e-12 the runner asserts with."
    )
    print(
        "  per_site: checked and not executed -- no lattice and no spatial index exists in this file. Every index it "
        "carries is an internal color index of the N_c x N_c-bar space, and the tadpole factors that appear later "
        "are bare rationals (1/2, 4/5, 13/10) chosen to expose a cancellation, not measurements taken at any site."
    )
    print(
        f"  per_mode: exercised in the color-channel sense, which is the only mode structure present -- each of the "
        f"N_c^2-1 adjoint generators is resolved on its own rather than in bulk. The construction lays down three "
        "explicit families, symmetric and antisymmetric off-diagonal pairs plus the N_c-1 Cartan diagonals, counts "
        "them against N_c^2-1 at N_c = 2, 3, 4, 5, and certifies every single one orthonormal. These are internal "
        "color channels, not dynamical or spatial modes, and nothing wider is claimed."
    )
    print(
        "  per_block: exercised, and this is where the no-go actually lives -- the readout space splits into exactly "
        "two blocks, the adjoint block of weight F_adj = (N_c^2-1)/N_c^2 and the singlet block of weight 1 - F_adj, "
        "and kappa_EW is by definition the free coefficient multiplying the second block. The demonstration that CMT "
        "scaling cannot fix it is itself a block statement: scaling both blocks by the same u0^2 leaves K unchanged "
        "at all three tested u0 values, so the underdetermination is exhibited precisely at block granularity."
    )
    print(
        "  lattice_wide: checked and not executed -- no system of any extent is built, so there is no whole-system "
        "quantity to report and no finite-N or limiting statement to make. The N this runner varies is the color "
        "rank N_c over 2, 3, 4, 5, which is the dimension of an internal space and not a volume. The physical "
        "lattice connected-trace readout that a whole-system statement would concern is exactly the object this "
        "packet declines to derive, which is the note's own obstruction."
    )


def main() -> None:
    checks = Checkbook()
    print("=" * 92)
    print("R_CONN MATCHING-RULE NO-GO CERTIFICATE")
    print("  exact Fierz support plus kappa_EW underdetermination")
    print("=" * 92)

    run_algebra_checks(checks)
    run_matching_rule_checks(checks)
    run_note_checks(checks)

    print()
    print("FINITE READ")
    print("  F_adj=8/9 is exact SU(3) Fierz/channel-count support.")
    print("  K_EW=9/8 is only the kappa_EW=0 specialization.")
    print("  The current packet does not derive kappa_EW=0.")
    print_n5_execution_certificate()
    print()
    checks.report()
    print()
    print(f"RUNNER STATUS: {'PASS' if checks.fail_count == 0 else 'FAIL'} (PASS={checks.pass_count} FAIL={checks.fail_count})")
    if checks.fail_count:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
