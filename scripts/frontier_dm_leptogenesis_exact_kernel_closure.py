#!/usr/bin/env python3
"""Exact source-package identifiability boundary for DM leptogenesis.

This runner no longer assigns ``gamma``, ``E1``, ``E2``, and ``K00`` and
then treats their downstream arithmetic as a derivation.  It tests the
load-bearing question directly:

    Does the current minimal framework axiom surface fix those four numbers?

It constructs two exact expansions of the same minimal-axiom reduct.  The
expansions differ only in a downstream Hermitian source carrier ``H -> lam H``.
The minimal axioms do not mention that carrier, a source/action map, a
readout-context selector, or a physical-observable identification, so the
reduct is unchanged.  Both expansions obey the same exact extraction and
coherent-kernel formulas, but their source packages and epsilon/DI ratios
differ.  This is a finite symbolic countermodel to axiom-only identifiability,
not a claim that future retained bridge structure cannot select one member.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
MINIMAL_AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_COUNTS: dict[str, int] = {}


def check(name: str, condition: bool, detail: str = "", cls: str = "C") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    CLASS_COUNTS[cls] = CLASS_COUNTS.get(cls, 0) + 1
    message = f"  [{cls}] {status}: {name}"
    if detail:
        message += f"  ({detail})"
    print(message)
    return condition


@dataclass(frozen=True)
class SourcePackage:
    gamma: sp.Expr
    e1: sp.Expr
    e2: sp.Expr
    k00: sp.Expr
    cp1: sp.Expr
    cp2: sp.Expr


def hermitian_carrier(
    a: sp.Expr,
    b: sp.Expr,
    c: sp.Expr,
    d: sp.Expr,
    delta: sp.Expr,
    rho: sp.Expr,
    gamma: sp.Expr,
) -> sp.Matrix:
    """Breaking-triplet carrier used by the restricted source packet."""

    return sp.Matrix(
        [
            [a, b + rho, b - rho - sp.I * gamma],
            [b + rho, c + delta, d],
            [b - rho + sp.I * gamma, d, c - delta],
        ]
    )


def extract_package(h: sp.Matrix) -> SourcePackage:
    """Extract the packet's exact coordinates from a Hermitian carrier."""

    a = sp.re(h[0, 0])
    b = sp.simplify((sp.re(h[0, 1]) + sp.re(h[0, 2])) / 2)
    c = sp.simplify((sp.re(h[1, 1]) + sp.re(h[2, 2])) / 2)
    d = sp.re(h[1, 2])
    delta = sp.simplify((sp.re(h[1, 1]) - sp.re(h[2, 2])) / 2)
    rho = sp.simplify((sp.re(h[0, 1]) - sp.re(h[0, 2])) / 2)
    gamma = sp.simplify(-sp.im(h[0, 2]))

    e1 = sp.simplify(delta + rho)
    e2 = sp.simplify(a + b - c - d)

    uniform = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    k00 = sp.simplify((sp.conjugate(uniform).T * h * uniform)[0])
    cp1 = sp.simplify(-2 * gamma * e1 / 3)
    cp2 = sp.simplify(2 * gamma * e2 / 3)
    return SourcePackage(gamma, e1, e2, k00, cp1, cp2)


def reference_carrier() -> sp.Matrix:
    """One exact positive-definite completion of the reference package."""

    e1 = sp.sqrt(sp.Rational(8, 3))
    a = 2 + 4 * sp.sqrt(2) / 9
    b = 0
    c = 2 - sp.sqrt(2) / 9
    d = -sp.sqrt(2) / 9
    delta = sp.Rational(1, 2)
    rho = e1 - delta
    return hermitian_carrier(a, b, c, d, delta, rho, sp.Rational(1, 2))


def leading_principal_minors(h: sp.Matrix) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    minors = [sp.simplify(h[:size, :size].det()) for size in (1, 2, 3)]
    return minors[0], minors[1], minors[2]


def part1_exact_reference_witness() -> tuple[sp.Matrix, SourcePackage]:
    print("\n" + "=" * 88)
    print("PART 1: ONE EXACT DOWNSTREAM COMPLETION REPRODUCES THE REFERENCE PACKAGE")
    print("=" * 88)

    h = reference_carrier()
    package = extract_package(h)

    check(
        "The constructed carrier is exactly Hermitian",
        h == sp.conjugate(h).T,
        cls="A",
    )
    d1, d2, d3 = leading_principal_minors(h)
    expected_d1 = 2 + 4 * sp.sqrt(2) / 9
    expected_d2 = sp.Rational(643, 324) + 2 * sp.sqrt(6) / 3 + 8 * sp.sqrt(2) / 9
    expected_d3 = (
        -sp.Rational(3361, 648)
        - 16 * sp.sqrt(3) / 27
        + 227 * sp.sqrt(2) / 108
        + 8 * sp.sqrt(6) / 3
    )
    check(
        "Sylvester's criterion places H_ref in the positive-polar carrier domain",
        sp.simplify(d1 - expected_d1) == 0
        and sp.simplify(d2 - expected_d2) == 0
        and sp.simplify(d3 - expected_d3) == 0
        and sp.Rational(7, 5) ** 2 < 2
        and sp.Rational(12, 5) ** 2 < 6
        and sp.Rational(7, 4) ** 2 > 3
        and -sp.Rational(3361, 648)
        - 16 * sp.Rational(7, 4) / 27
        + 227 * sp.Rational(7, 5) / 108
        + 8 * sp.Rational(12, 5) / 3
        == sp.Rational(2021, 648)
        and sp.Rational(2021, 648) > 0,
        f"(D1,D2,D3)=({d1},{d2},{d3})",
        cls="A",
    )
    check(
        "The carrier extraction gives gamma = 1/2",
        sp.simplify(package.gamma - sp.Rational(1, 2)) == 0,
        f"gamma={package.gamma}",
        cls="A",
    )
    check(
        "The carrier extraction gives E1 = sqrt(8/3) and E2 = sqrt(8)/3",
        sp.simplify(package.e1 - sp.sqrt(sp.Rational(8, 3))) == 0
        and sp.simplify(package.e2 - sp.sqrt(8) / 3) == 0,
        f"(E1,E2)=({package.e1},{package.e2})",
        cls="A",
    )
    check(
        "The uniform heavy-basis projection gives K00 = 2",
        sp.simplify(package.k00 - 2) == 0,
        f"K00={package.k00}",
        cls="A",
    )
    check(
        "The CP channels are extracted rather than independently assigned",
        sp.simplify(package.cp1 + sp.sqrt(sp.Rational(8, 3)) / 3) == 0
        and sp.simplify(package.cp2 - sp.sqrt(8) / 9) == 0,
        f"(cp1,cp2)=({package.cp1},{package.cp2})",
        cls="A",
    )
    return h, package


def part2_same_axiom_reduct_has_a_distinct_exact_completion(
    h_reference: sp.Matrix,
    reference: SourcePackage,
) -> tuple[SourcePackage, sp.Expr]:
    print("\n" + "=" * 88)
    print("PART 2: A SOURCE-CARRIER RESCALING PRESERVES THE AXIOM REDUCT")
    print("=" * 88)

    axiom_text = MINIMAL_AXIOMS.read_text(encoding="utf-8")
    required_absences = (
        "source/action and physical-observable identification",
        "source/action and physical-observable identification;",
    )
    check(
        "The current axiom memo explicitly leaves source/action and observable identification outside A_min",
        any(needle in axiom_text for needle in required_absences),
        cls="B",
    )
    check(
        "The current axiom memo leaves readout-context and log-determinant selection outside A_min",
        "readout-context selection" in axiom_text and "log-det readout theorem" in axiom_text,
        cls="B",
    )

    lam = sp.symbols("lambda", positive=True)
    h_scaled = sp.simplify(lam * h_reference)
    scaled = extract_package(h_scaled)
    ref_minors = leading_principal_minors(h_reference)
    scaled_minors = leading_principal_minors(h_scaled)

    check(
        "For every positive lambda, H_lambda stays Hermitian and positive definite",
        all(sp.simplify(entry) == 0 for entry in h_scaled - sp.conjugate(h_scaled).T)
        and all(
            sp.simplify(scaled_minors[index] - lam ** (index + 1) * ref_minors[index]) == 0
            for index in range(3)
        ),
        cls="A",
    )
    check(
        "All four extracted source-package coordinates scale by lambda",
        all(
            sp.simplify(getattr(scaled, field) - lam * getattr(reference, field)) == 0
            for field in ("gamma", "e1", "e2", "k00")
        ),
        f"lambda={lam}; scaled=(gamma={scaled.gamma},E1={scaled.e1},E2={scaled.e2},K00={scaled.k00})",
        cls="A",
    )
    check(
        "The CP channels scale quadratically while the diagonal scales linearly",
        sp.simplify(scaled.cp1 - lam**2 * reference.cp1) == 0
        and sp.simplify(scaled.cp2 - lam**2 * reference.cp2) == 0
        and sp.simplify(scaled.k00 - lam * reference.k00) == 0,
        cls="A",
    )
    check(
        "The two completions disagree on every claimed absolute package value",
        all(
            sp.simplify(getattr(scaled, field).subs(lam, 2) - getattr(reference, field)) != 0
            for field in ("gamma", "e1", "e2", "k00")
        ),
        "the explicit second completion uses lambda=2",
        cls="A",
    )
    return scaled, lam


def part3_coherent_kernel_is_not_invariant(
    reference: SourcePackage,
    scaled: SourcePackage,
    lam: sp.Expr,
) -> None:
    print("\n" + "=" * 88)
    print("PART 3: THE COHERENT KERNEL DOES NOT REMOVE THE COMPLETION FREEDOM")
    print("=" * 88)

    f23, f3, prefactor, epsilon_di = sp.symbols(
        "f23 f3 prefactor epsilon_DI", nonzero=True, real=True
    )
    source_reference = sp.simplify(
        prefactor * (reference.cp1 * f23 + reference.cp2 * f3) / reference.k00
    )
    source_scaled = sp.simplify(
        prefactor * (scaled.cp1 * f23 + scaled.cp2 * f3) / scaled.k00
    )

    check(
        "At fixed benchmark loop functions, epsilon_1 scales by lambda",
        sp.simplify(source_scaled - lam * source_reference) == 0,
        cls="A",
    )
    ratio_reference = sp.simplify(source_reference / epsilon_di)
    ratio_scaled = sp.simplify(source_scaled / epsilon_di)
    check(
        "At fixed Davidson-Ibarra comparator, epsilon_1/epsilon_DI also scales by lambda",
        sp.simplify(ratio_scaled - lam * ratio_reference) == 0,
        cls="A",
    )


def part4_record_additivity_has_the_same_scale_freedom() -> None:
    print("\n" + "=" * 88)
    print("PART 4: RECORD ADDITIVITY DOES NOT FIX AN ABSOLUTE READOUT SCALE")
    print("=" * 88)

    # A finite record readout is a sum of content values.  Multiplying every
    # content value by a nonzero scalar preserves content determination,
    # I(empty)=0, and finite additivity exactly.
    content_values = {"r0": sp.Rational(1, 2), "r1": sp.sqrt(2)}
    lam = sp.Integer(3)

    def readout(records: tuple[str, ...], scale: sp.Expr = sp.Integer(1)) -> sp.Expr:
        return sp.simplify(scale * sum((content_values[r] for r in records), sp.Integer(0)))

    left = ("r0",)
    right = ("r1",)
    union = left + right
    check(
        "The reference readout is finitely additive on disjoint record collections",
        sp.simplify(readout(union) - readout(left) - readout(right)) == 0,
        cls="A",
    )
    check(
        "A nontrivially rescaled readout is also finitely additive",
        sp.simplify(readout(union, lam) - readout(left, lam) - readout(right, lam)) == 0,
        cls="A",
    )
    check(
        "Both readouts obey I(empty)=0 but disagree on nonempty record content",
        readout(()) == 0
        and readout((), lam) == 0
        and sp.simplify(readout(left, lam) - readout(left)) != 0,
        cls="A",
    )


def part5_conditional_benchmark_replay(reference: SourcePackage) -> None:
    print("\n" + "=" * 88)
    print("PART 5: CONDITIONAL BENCHMARK REPLAY (NOT AN AXIOM DERIVATION)")
    print("=" * 88)

    # This deliberately consumes the existing conditional package only to
    # preserve the old downstream arithmetic. It is not used by Parts 1-4.
    from dm_leptogenesis_exact_common import exact_package

    package = exact_package()
    check(
        "The imported conditional package matches the independently extracted reference tuple",
        abs(package.gamma - float(reference.gamma)) < 1e-15
        and abs(package.E1 - float(reference.e1)) < 1e-15
        and abs(package.E2 - float(reference.e2)) < 1e-15
        and abs(package.K00 - float(reference.k00)) < 1e-15,
        cls="B",
    )
    check(
        "The conditional coherent kernel gives epsilon_1/epsilon_DI = 0.9276209209",
        abs(package.epsilon_ratio - 0.9276209209197268) < 1e-12,
        f"epsilon_1/epsilon_DI={package.epsilon_ratio:.12f}",
        cls="D",
    )
    check(
        "The consistent conditional benchmark still gives eta/eta_obs = 0.5578749661",
        abs(package.eta_ratio_fit_bench_exact_bookkeeping - 0.557874966110017) < 1e-12,
        f"eta/eta_obs={package.eta_ratio_fit_bench_exact_bookkeeping:.12f}",
        cls="D",
    )


def main() -> int:
    print("=" * 88)
    print("DM LEPTOGENESIS SOURCE-PACKAGE IDENTIFIABILITY BOUNDARY")
    print("=" * 88)

    h_reference, reference = part1_exact_reference_witness()
    scaled, lam = part2_same_axiom_reduct_has_a_distinct_exact_completion(h_reference, reference)
    part3_coherent_kernel_is_not_invariant(reference, scaled, lam)
    part4_record_additivity_has_the_same_scale_freedom()
    part5_conditional_benchmark_replay(reference)

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    breakdown = ", ".join(f"class {key}: {value}" for key, value in sorted(CLASS_COUNTS.items()))
    print(f"CLASS BREAKDOWN: {breakdown}")
    print(
        "BOUNDARY: the current A_min surface does not identify a unique nonzero\n"
        "(gamma,E1,E2,K00) package or epsilon_1/epsilon_DI value.  The reference\n"
        "numbers remain a conditional completion.  A normalized carrier theorem\n"
        "or a scale-invariant kernel bypass remains open."
    )
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
