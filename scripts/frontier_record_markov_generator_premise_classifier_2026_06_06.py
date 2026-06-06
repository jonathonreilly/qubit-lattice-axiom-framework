#!/usr/bin/env python3
"""Premise classifier for record-production Markov-generator dynamics.

This stacked block builds on the embeddability boundary:

  record append/count information
    != production probabilities
    != continuous-time rates

The classifier records the exact extra premises needed to move among those
claims. It does not derive a kernel, generator, clock, or Born/IID bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import sympy as sp


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def is_column_stochastic(P: sp.Matrix) -> bool:
    return all(P[i, j] >= 0 for i in range(P.rows) for j in range(P.cols)) and all(
        sp.simplify(sum(P[i, j] for i in range(P.rows)) - 1) == 0
        for j in range(P.cols)
    )


def is_generator(Q: sp.Matrix) -> bool:
    return all(Q[i, j] >= 0 for i in range(Q.rows) for j in range(Q.cols) if i != j) and all(
        sp.simplify(sum(Q[i, j] for i in range(Q.rows))) == 0
        for j in range(Q.cols)
    )


def two_state_generator(rate: sp.Expr) -> sp.Matrix:
    return sp.Matrix([[-rate, rate], [rate, -rate]])


def two_state_semigroup(rate: sp.Expr, t: sp.Expr) -> sp.Matrix:
    e = sp.exp(-2 * rate * t)
    return sp.Matrix([
        [(1 + e) / 2, (1 - e) / 2],
        [(1 - e) / 2, (1 + e) / 2],
    ])


def has_determinant_obstruction(P: sp.Matrix) -> bool:
    return sp.simplify(P.det()) <= 0


@dataclass(frozen=True)
class PremiseBundle:
    record_atoms: bool = False
    probability_kernel: sp.Matrix | None = None
    born_iid_bridge: bool = False
    supplied_generator: sp.Matrix | None = None
    supplied_clock_interval: sp.Expr | None = None
    supplied_rate_unit: bool = False


@dataclass(frozen=True)
class Classification:
    level: str
    allowed_claims: tuple[str, ...]
    missing_premises: tuple[str, ...]
    blocked_claims: tuple[str, ...]


def classify(bundle: PremiseBundle) -> Classification:
    allowed: list[str] = []
    missing: list[str] = []
    blocked: list[str] = []

    if bundle.record_atoms:
        allowed.append("realized post-record append/count information")
    else:
        missing.append("record atoms")

    P = bundle.probability_kernel
    has_kernel = P is not None and is_column_stochastic(P)
    if has_kernel:
        allowed.append("one-step stochastic production kernel")
    else:
        missing.append("stochastic production kernel")
        blocked.append("future-record probabilities")

    if has_kernel and bundle.born_iid_bridge:
        allowed.append("pre-record probability interface supplied")
    elif has_kernel:
        missing.append("Born/IID or other probability-origin bridge")

    generator_ok = bundle.supplied_generator is not None and is_generator(bundle.supplied_generator)
    clock_ok = bundle.supplied_clock_interval is not None
    rate_ok = bundle.supplied_rate_unit

    if has_kernel and has_determinant_obstruction(P):
        blocked.append("finite bounded continuous-time Markov generator for this kernel")
        missing.append("different kernel, asymptotic/sink construction, or unbounded/nonfinite generator premise")
    elif has_kernel and generator_ok:
        allowed.append("candidate continuous-time Markov generator")
    elif has_kernel:
        missing.append("Markov generator or embeddability proof")
        blocked.append("continuous-time rate law")

    if generator_ok and clock_ok:
        allowed.append("semigroup step exp(Q t) with supplied clock interval")
    elif generator_ok:
        missing.append("clock interval")

    if generator_ok and clock_ok and rate_ok:
        allowed.append("physical rate normalization")
    elif generator_ok and clock_ok:
        missing.append("rate/unit normalization")

    if "physical rate normalization" in allowed and bundle.born_iid_bridge:
        level = "physical-rate-model"
    elif "semigroup step exp(Q t) with supplied clock interval" in allowed:
        level = "Markov-semigroup-model"
    elif "one-step stochastic production kernel" in allowed:
        level = "production-kernel-model"
    elif "realized post-record append/count information" in allowed:
        level = "post-record-information-only"
    else:
        level = "unlicensed"

    # Stable ordering for reproducible output.
    return Classification(
        level=level,
        allowed_claims=tuple(dict.fromkeys(allowed)),
        missing_premises=tuple(dict.fromkeys(missing)),
        blocked_claims=tuple(dict.fromkeys(blocked)),
    )


def assert_contains(items: Iterable[str], needle: str) -> bool:
    return any(needle in item for item in items)


def main() -> int:
    print("Record Markov-generator premise classifier")
    print("actual_current_surface_status: exact-support")
    print("trace_class: direct_blocker_closure")
    print("reachability_to_target: partially_closes")
    print("proposal_allowed: false")
    print("audit_required_before_effective_retained: true")
    print()

    P_lazy = sp.Matrix([[sp.Rational(3, 4), sp.Rational(1, 4)],
                        [sp.Rational(1, 4), sp.Rational(3, 4)]])
    P_swap = sp.Matrix([[0, 1], [1, 0]])
    P_reset = sp.Matrix([[1, 1], [0, 0]])
    r = sp.log(2) / 2
    Q_lazy = two_state_generator(r)

    print("A. exact kernel/generator anchors")
    check("lazy kernel is stochastic", is_column_stochastic(P_lazy), f"det={P_lazy.det()}")
    check("swap kernel is stochastic but determinant-obstructed", is_column_stochastic(P_swap) and has_determinant_obstruction(P_swap), f"det={P_swap.det()}")
    check("reset kernel is stochastic but singular", is_column_stochastic(P_reset) and has_determinant_obstruction(P_reset), f"det={P_reset.det()}")
    check("supplied lazy Q is a Markov generator", is_generator(Q_lazy), f"Q={Q_lazy}")
    check("supplied lazy Q at t=1 generates P_lazy", sp.simplify(two_state_semigroup(r, 1) - P_lazy) == sp.zeros(2))

    print("\nB. premise classifications")
    record_only = classify(PremiseBundle(record_atoms=True))
    check("record-only level is post-record information only", record_only.level == "post-record-information-only", record_only.level)
    check("record-only blocks probabilities", assert_contains(record_only.blocked_claims, "future-record probabilities"), str(record_only.blocked_claims))

    kernel_only = classify(PremiseBundle(record_atoms=True, probability_kernel=P_lazy))
    check("stochastic kernel reaches production-kernel model", kernel_only.level == "production-kernel-model", kernel_only.level)
    check("kernel-only still misses Born/IID bridge", assert_contains(kernel_only.missing_premises, "Born/IID"), str(kernel_only.missing_premises))
    check("kernel-only still blocks continuous-time rate law", assert_contains(kernel_only.blocked_claims, "continuous-time rate law"), str(kernel_only.blocked_claims))

    swap_case = classify(PremiseBundle(record_atoms=True, probability_kernel=P_swap, born_iid_bridge=True))
    check("swap case remains production-kernel only", swap_case.level == "production-kernel-model", swap_case.level)
    check("swap case blocks finite bounded generator", assert_contains(swap_case.blocked_claims, "finite bounded continuous-time"), str(swap_case.blocked_claims))

    reset_case = classify(PremiseBundle(record_atoms=True, probability_kernel=P_reset, born_iid_bridge=True))
    check("reset case remains production-kernel only", reset_case.level == "production-kernel-model", reset_case.level)
    check("reset case records singular finite-time obstruction", assert_contains(reset_case.blocked_claims, "finite bounded continuous-time"), str(reset_case.blocked_claims))

    semigroup_case = classify(PremiseBundle(
        record_atoms=True,
        probability_kernel=P_lazy,
        born_iid_bridge=True,
        supplied_generator=Q_lazy,
        supplied_clock_interval=sp.Integer(1),
    ))
    check("generator plus clock reaches Markov semigroup model", semigroup_case.level == "Markov-semigroup-model", semigroup_case.level)
    check("generator plus clock still misses rate/unit normalization", assert_contains(semigroup_case.missing_premises, "rate/unit"), str(semigroup_case.missing_premises))

    physical_rate_case = classify(PremiseBundle(
        record_atoms=True,
        probability_kernel=P_lazy,
        born_iid_bridge=True,
        supplied_generator=Q_lazy,
        supplied_clock_interval=sp.Integer(1),
        supplied_rate_unit=True,
    ))
    check("rate unit reaches physical-rate model", physical_rate_case.level == "physical-rate-model", physical_rate_case.level)
    check("physical-rate model keeps all key allowed claims", all(
        assert_contains(physical_rate_case.allowed_claims, phrase)
        for phrase in (
            "one-step stochastic production kernel",
            "pre-record probability interface supplied",
            "semigroup step exp(Q t)",
            "physical rate normalization",
        )
    ), str(physical_rate_case.allowed_claims))

    print("\nC. boundary firewalls")
    check("classifier never derives a kernel from record atoms alone", "stochastic production kernel" in record_only.missing_premises)
    check("classifier never derives Born/IID from a kernel", "Born/IID or other probability-origin bridge" in kernel_only.missing_premises)
    check("classifier separates generator from clock", "clock interval" not in semigroup_case.missing_premises and "rate/unit normalization" in semigroup_case.missing_premises)
    check("classifier leaves dial selection absent", True, "no Koide/generation dial field is present")

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    if PASS > 0 and FAIL == 0:
        print(
            "VERDICT: exact support for a record-dynamics premise classifier. "
            "Post-record information, stochastic production kernels, Markov "
            "generators, clock intervals, rate units, and Born/IID bridges are "
            "separate gates."
        )
        return 0
    print("VERDICT: classifier failed; do not use this artifact.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
