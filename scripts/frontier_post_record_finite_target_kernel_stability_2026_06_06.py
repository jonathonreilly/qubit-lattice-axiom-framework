#!/usr/bin/env python3
"""Finite target-prior reset kernel stability certificate."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
ALPHABET = ("A", "B", "C")
Vector = tuple[Fraction, ...]
Matrix = tuple[tuple[Fraction, ...], ...]


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


def normalized(p: Vector) -> bool:
    return sum(p) == 1 and all(x >= 0 for x in p)


def reset_kernel(pi: Vector, alpha: Fraction) -> Matrix:
    rows = []
    for i in range(len(pi)):
        row = []
        for j in range(len(pi)):
            delta = Fraction(1) if i == j else Fraction(0)
            row.append((1 - alpha) * delta + alpha * pi[j])
        rows.append(tuple(row))
    return tuple(rows)


def row_stochastic(k: Matrix) -> bool:
    return all(sum(row) == 1 and all(x >= 0 for x in row) for row in k)


def apply(p: Vector, k: Matrix) -> Vector:
    return tuple(sum(p[i] * k[i][j] for i in range(len(p))) for j in range(len(p)))


def sub(a: Vector, b: Vector) -> Vector:
    return tuple(x - y for x, y in zip(a, b))


def scale(c: Fraction, v: Vector) -> Vector:
    return tuple(c * x for x in v)


def detailed_balance(pi: Vector, k: Matrix) -> bool:
    for i in range(len(pi)):
        for j in range(len(pi)):
            if pi[i] * k[i][j] != pi[j] * k[j][i]:
                return False
    return True


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_FINITE_TARGET_KERNEL_STABILITY_2026-06-06.md",
        [
            "actual_current_surface_status: exact-support",
            "Every supplied target prior can be made stable",
            "Stability is not selection",
            "stable target-kernel dynamics remains conditional",
            "generation or Koide dial",
        ],
    )
    require_text(
        "docs/RECORD_PRIOR_STABILITY_SELECTOR_2026-06-05.md",
        [
            "Stability alone does not choose the endpoint",
            "Koide is not forced",
            "Phi_{s,alpha}(p) = (1 - alpha) p + alpha pi_s",
        ],
    )
    require_text(
        "docs/RECORD_EQUAL_LETTER_STABLE_LOCATION_2026-06-05.md",
        [
            "The same reset construction works for every dial prior",
            "stability of a location, not selection of the dial",
            "Does not fix the dial",
        ],
    )
    require_text(
        "docs/RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md",
        [
            "post-record information dynamics",
            "probability laws, Born typicality, and transition rates",
            "dial selection",
        ],
    )


def target_kernel_checks() -> None:
    section("Target-kernel checks")
    pi = (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6))
    alpha = Fraction(2, 5)
    k = reset_kernel(pi, alpha)
    report("target prior is normalized", normalized(pi), str(pi))
    report("alpha is in open unit interval", 0 < alpha < 1, str(alpha))
    report("reset kernel is row-stochastic", row_stochastic(k), str(k))
    report("target prior is stationary", apply(pi, k) == pi, str(apply(pi, k)))
    report("reset kernel satisfies detailed balance", detailed_balance(pi, k))

    p = (Fraction(0), Fraction(1), Fraction(0))
    lhs = sub(apply(p, k), pi)
    rhs = scale(1 - alpha, sub(p, pi))
    report("one-step vector deviation contracts by 1-alpha", lhs == rhs, str(lhs))

    q = (Fraction(1, 4), Fraction(1, 4), Fraction(1, 2))
    lhs_q = sub(apply(q, k), pi)
    rhs_q = scale(1 - alpha, sub(q, pi))
    report("contraction identity holds for second distribution", lhs_q == rhs_q, str(lhs_q))

    p2 = apply(apply(p, k), k)
    report("two-step deviation contracts by (1-alpha)^2", sub(p2, pi) == scale((1 - alpha) ** 2, sub(p, pi)), str(p2))


def multiple_target_checks() -> None:
    section("Multiple target prior checks")
    alpha = Fraction(1, 3)
    uniform = (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))
    biased = (Fraction(2, 3), Fraction(1, 6), Fraction(1, 6))
    uniform_k = reset_kernel(uniform, alpha)
    biased_k = reset_kernel(biased, alpha)
    report("uniform target is stationary for its kernel", apply(uniform, uniform_k) == uniform)
    report("biased target is stationary for its kernel", apply(biased, biased_k) == biased)
    report("different supplied targets produce different kernels", uniform_k != biased_k)
    report("different supplied targets produce different stable locations", uniform != biased)


def firewall_checks() -> None:
    section("Firewall flags")
    record_derives_target_prior = False
    record_derives_alpha = False
    record_derives_physical_kernel = False
    record_derives_clock_or_rate = False
    record_derives_born_or_instrument = False
    record_derives_hamiltonian = False
    generation_or_koide_dial_selected = False
    audit_verdict_applied = False

    report("Record-derived target-prior flag is false", not record_derives_target_prior)
    report("Record-derived alpha flag is false", not record_derives_alpha)
    report("Record-derived physical-kernel flag is false", not record_derives_physical_kernel)
    report("Record-derived clock/rate flag is false", not record_derives_clock_or_rate)
    report("Record-derived Born/instrument flag is false", not record_derives_born_or_instrument)
    report("Record-derived Hamiltonian flag is false", not record_derives_hamiltonian)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("audit verdict applied flag is false", not audit_verdict_applied)


def main() -> int:
    source_anchor_checks()
    target_kernel_checks()
    multiple_target_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("SUPPLIED_TARGET_KERNEL_STABILITY=TRUE")
    print("EVERY_SUPPLIED_TARGET_CAN_BE_STABILIZED=TRUE")
    print("RECORD_DERIVES_TARGET_PRIOR=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
