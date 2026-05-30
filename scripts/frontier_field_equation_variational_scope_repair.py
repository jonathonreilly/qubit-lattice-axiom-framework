#!/usr/bin/env python3
"""Exact variational-scope runner for FIELD_EQUATION_DERIVATION_NOTE.

The repaired row proves only that the displayed finite graph action has
Euler-Lagrange equation

    (L + mu^2 I) Phi = G_c rho.

It does not prove that this action is uniquely selected.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


NOTE = Path("docs/FIELD_EQUATION_DERIVATION_NOTE.md")


class Gate:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.pass_count += 1
            status = "PASS"
        else:
            self.fail_count += 1
            status = "FAIL"
        suffix = f" ({detail})" if detail else ""
        print(f"[{status}] {label}{suffix}")

    def summary(self) -> int:
        print(f"SUMMARY: PASS={self.pass_count} FAIL={self.fail_count}")
        return 0 if self.fail_count == 0 else 1


def laplacian(n: int, edges: list[tuple[int, int, Fraction]]) -> list[list[Fraction]]:
    L = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i, j, w in edges:
        L[i][i] += w
        L[j][j] += w
        L[i][j] -= w
        L[j][i] -= w
    return L


def mat_vec(A: list[list[Fraction]], x: list[Fraction]) -> list[Fraction]:
    return [sum(aij * xj for aij, xj in zip(row, x)) for row in A]


def dot(x: list[Fraction], y: list[Fraction]) -> Fraction:
    return sum(xi * yi for xi, yi in zip(x, y))


def action(
    L: list[list[Fraction]],
    phi: list[Fraction],
    rho: list[Fraction],
    mu2: Fraction,
    coupling: Fraction,
) -> Fraction:
    Lphi = mat_vec(L, phi)
    return Fraction(1, 2) * dot(phi, Lphi) + Fraction(1, 2) * mu2 * dot(phi, phi) - coupling * dot(rho, phi)


def grad(
    L: list[list[Fraction]],
    phi: list[Fraction],
    rho: list[Fraction],
    mu2: Fraction,
    coupling: Fraction,
) -> list[Fraction]:
    Lphi = mat_vec(L, phi)
    return [lp + mu2 * p - coupling * r for lp, p, r in zip(Lphi, phi, rho)]


def finite_difference_component(
    L: list[list[Fraction]],
    phi: list[Fraction],
    rho: list[Fraction],
    mu2: Fraction,
    coupling: Fraction,
    idx: int,
) -> Fraction:
    # For a quadratic action, central difference with step 1 is exact.
    plus = list(phi)
    minus = list(phi)
    plus[idx] += 1
    minus[idx] -= 1
    return (action(L, plus, rho, mu2, coupling) - action(L, minus, rho, mu2, coupling)) / 2


def all_row_sums_zero(L: list[list[Fraction]]) -> bool:
    return all(sum(row) == 0 for row in L)


def quadratic_form(L: list[list[Fraction]], x: list[Fraction]) -> Fraction:
    return dot(x, mat_vec(L, x))


def main() -> int:
    gate = Gate()
    print("Field-equation variational scope-repair certificate")
    print("=" * 72)

    edges = [
        (0, 1, Fraction(2)),
        (1, 2, Fraction(3, 2)),
        (2, 3, Fraction(5, 3)),
        (0, 3, Fraction(7, 4)),
        (1, 3, Fraction(4, 5)),
    ]
    n = 4
    L = laplacian(n, edges)
    phi = [Fraction(1, 3), Fraction(-2, 5), Fraction(3, 7), Fraction(5, 11)]
    rho = [Fraction(2, 3), Fraction(1, 5), Fraction(-3, 4), Fraction(4, 9)]
    mu2 = Fraction(7, 6)
    coupling = Fraction(5, 4)

    gate.check("weighted graph Laplacian is symmetric", L == [list(row) for row in zip(*L)])
    gate.check("weighted graph Laplacian has constant-mode row sums zero", all_row_sums_zero(L))
    gate.check(
        "graph-gradient quadratic form is nonnegative on test vector",
        quadratic_form(L, phi) > 0,
        f"phi^T L phi={quadratic_form(L, phi)}",
    )

    g = grad(L, phi, rho, mu2, coupling)
    fd = [
        finite_difference_component(L, phi, rho, mu2, coupling, idx)
        for idx in range(n)
    ]
    gate.check("central finite difference equals analytic gradient", fd == g)

    # Stationary solution generated from an arbitrary phi by defining rho =
    # (L+mu^2 I) phi / coupling.
    Lphi = mat_vec(L, phi)
    stationary_rho = [(lp + mu2 * p) / coupling for lp, p in zip(Lphi, phi)]
    gate.check(
        "constructed source makes chosen phi stationary",
        grad(L, phi, stationary_rho, mu2, coupling) == [0] * n,
    )

    constant = [Fraction(1) for _ in range(n)]
    gate.check("mu2=0 Laplacian kills constant mode", mat_vec(L, constant) == [0] * n)
    gate.check(
        "mu2>0 removes constant-mode kernel",
        [lp + mu2 * c for lp, c in zip(mat_vec(L, constant), constant)] != [0] * n,
    )
    gate.check(
        "positive mu2 gives positive quadratic form on constant mode",
        quadratic_form(L, constant) + mu2 * dot(constant, constant) > 0,
    )

    # Sample several nonzero vectors to check positive definiteness on the
    # finite rational witness set.
    witnesses = [
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(1), Fraction(-1), Fraction(0), Fraction(0)],
        [Fraction(2), Fraction(-3), Fraction(5), Fraction(-7)],
        [Fraction(1, 2), Fraction(1, 3), Fraction(-1, 5), Fraction(1, 7)],
    ]
    for idx, x in enumerate(witnesses, start=1):
        q = quadratic_form(L, x) + mu2 * dot(x, x)
        gate.check(f"witness {idx}: L+mu2 I positive", q > 0, f"q={q}")

    text = NOTE.read_text(encoding="utf-8")
    required = [
        "not derive or uniquely select that action",
        "does not derive the quadratic action from axioms",
        "does not prove that the mass term is selected rather than supplied",
        "does not prove uniqueness among all local, nonlocal, higher-derivative",
        "Selecting that action remains a separate science target.",
    ]
    for needle in required:
        gate.check(f"source note contains required firewall: {needle}", needle in text)

    forbidden = [
        "The field equation is NOT purely \"chosen by convention.\"",
        "Within this restricted class, the screened Poisson equation is the unique",
        "Einstein's equation reduces",
        "massive gravity",
    ]
    for needle in forbidden:
        gate.check(f"source note omits old overclaim: {needle}", needle not in text)

    return gate.summary()


if __name__ == "__main__":
    raise SystemExit(main())
