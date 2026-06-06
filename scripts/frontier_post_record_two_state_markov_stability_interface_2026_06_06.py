#!/usr/bin/env python3
"""Exact stability interface for supplied two-state post-record kernels."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0


Vector = tuple[Fraction, Fraction]
Kernel = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


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


def kernel(a: Fraction, b: Fraction) -> Kernel:
    return ((1 - a, a), (b, 1 - b))


def row_stochastic(k: Kernel) -> bool:
    return all(sum(row) == 1 and all(x >= 0 for x in row) for row in k)


def stationary(a: Fraction, b: Fraction) -> Vector:
    return (b / (a + b), a / (a + b))


def apply(p: Vector, k: Kernel) -> Vector:
    return (
        p[0] * k[0][0] + p[1] * k[1][0],
        p[0] * k[0][1] + p[1] * k[1][1],
    )


def iterate(p: Vector, k: Kernel, steps: int) -> Vector:
    out = p
    for _ in range(steps):
        out = apply(out, k)
    return out


def deviation0(p: Vector, pi: Vector) -> Fraction:
    return p[0] - pi[0]


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_TWO_STATE_MARKOV_STABILITY_INTERFACE_2026-06-06.md",
        [
            "actual_current_surface_status: exact-support",
            "stable post-record location",
            "This is a stability interface, not a dial-selection theorem",
            "different supplied kernels",
            "generation or Koide dial",
        ],
    )
    require_text(
        "docs/RECORD_EQUAL_LETTER_STABLE_LOCATION_2026-06-05.md",
        [
            "The equal-letter point is a stable location",
            "This is not a physical dial-selection theorem",
            "Does not force Koide",
        ],
    )
    require_text(
        "docs/RECORD_PRIOR_STABILITY_SELECTOR_2026-06-05.md",
        [
            "Stability alone does not choose the endpoint",
            "Koide is not forced",
            "post-record label/count dynamics",
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


def general_kernel_checks() -> None:
    section("General two-state kernel checks")
    a = Fraction(1, 5)
    b = Fraction(2, 5)
    k = kernel(a, b)
    pi = stationary(a, b)
    lam = 1 - a - b
    report("kernel is row-stochastic", row_stochastic(k), str(k))
    report("stationary vector is normalized", sum(pi) == 1 and all(x > 0 for x in pi), str(pi))
    report("stationary vector is exact", pi == (Fraction(2, 3), Fraction(1, 3)), str(pi))
    report("pi is stationary", apply(pi, k) == pi, str(apply(pi, k)))
    report("contraction eigenvalue is exact", lam == Fraction(2, 5), str(lam))
    report("kernel is attracting", abs(lam) < 1)

    p0 = (Fraction(0), Fraction(1))
    p1 = apply(p0, k)
    report("one-step deviation contracts by lambda", deviation0(p1, pi) == lam * deviation0(p0, pi), str(p1))
    p4 = iterate(p0, k, 4)
    report("four-step deviation contracts by lambda^4", deviation0(p4, pi) == (lam ** 4) * deviation0(p0, pi), str(p4))


def equal_letter_and_biased_checks() -> None:
    section("Equal-letter and biased-location checks")
    alpha = Fraction(3, 5)
    equal_k = kernel(alpha / 2, alpha / 2)
    equal_pi = stationary(alpha / 2, alpha / 2)
    equal_lam = 1 - alpha
    report("equal-letter reset kernel is row-stochastic", row_stochastic(equal_k))
    report("equal-letter stationary point is uniform", equal_pi == (Fraction(1, 2), Fraction(1, 2)), str(equal_pi))
    report("equal-letter contraction factor is 1-alpha", 1 - alpha == equal_lam, str(equal_lam))

    biased_k = kernel(Fraction(1, 10), Fraction(1, 2))
    biased_pi = stationary(Fraction(1, 10), Fraction(1, 2))
    report("biased supplied kernel is row-stochastic", row_stochastic(biased_k))
    report("biased supplied kernel has different stable point", biased_pi == (Fraction(5, 6), Fraction(1, 6)), str(biased_pi))
    report("same alphabet admits different supplied stable locations", biased_pi != equal_pi)


def firewall_checks() -> None:
    section("Firewall flags")
    record_derives_kernel = False
    record_derives_physical_bridge = False
    record_derives_clock_or_rate = False
    record_derives_born_or_instrument = False
    record_derives_hamiltonian = False
    record_selects_kernel_family = False
    generation_or_koide_dial_selected = False
    audit_verdict_applied = False

    report("Record-derived kernel flag is false", not record_derives_kernel)
    report("Record-derived physical-bridge flag is false", not record_derives_physical_bridge)
    report("Record-derived clock/rate flag is false", not record_derives_clock_or_rate)
    report("Record-derived Born/instrument flag is false", not record_derives_born_or_instrument)
    report("Record-derived Hamiltonian flag is false", not record_derives_hamiltonian)
    report("Record-selected kernel-family flag is false", not record_selects_kernel_family)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("audit verdict applied flag is false", not audit_verdict_applied)


def main() -> int:
    source_anchor_checks()
    general_kernel_checks()
    equal_letter_and_biased_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("SUPPLIED_TWO_STATE_MARKOV_STABILITY_INTERFACE=TRUE")
    print("STATIONARY_LOCATION_EXACT=TRUE")
    print("RECORD_DERIVES_KERNEL=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
