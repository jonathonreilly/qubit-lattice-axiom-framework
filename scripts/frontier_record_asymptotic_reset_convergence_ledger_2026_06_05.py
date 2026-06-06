#!/usr/bin/env python3
"""Asymptotic reset convergence ledger for record sink dynamics."""

from __future__ import annotations

from math import ceil, log
from pathlib import Path


PASS = 0
FAIL = 0


def emit(line: str = "") -> None:
    print(line)


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    emit(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    emit()
    emit("-" * 78)
    emit(title)
    emit("-" * 78)


def residual(p: float, steps: int) -> float:
    return (1.0 - p) ** steps


def steps_for_epsilon(p: float, epsilon: float) -> int:
    return ceil(log(epsilon) / log(1.0 - p))


def main() -> int:
    emit("=" * 78)
    emit("RECORD ASYMPTOTIC RESET CONVERGENCE LEDGER")
    emit("bounded-support / epsilon-reset residual runner")
    emit("=" * 78)

    section("1. One-bit residual ledger")
    for p in (0.1, 0.25, 0.5):
        vals = [residual(p, n) for n in range(0, 7)]
        check(f"p={p}: residual starts at one", vals[0] == 1.0)
        check(f"p={p}: residual strictly decreases", all(vals[i + 1] < vals[i] for i in range(len(vals) - 1)))
        check(f"p={p}: finite-step residual remains positive", vals[-1] > 0.0, f"{vals[-1]:.6f}")
        check(f"p={p}: composition gives q^n", abs(vals[6] - (1.0 - p) ** 6) < 1e-15)
        check(f"p={p}: longer run improves residual", residual(p, 100) < residual(p, 10))

    section("2. Epsilon threshold arithmetic")
    p = 0.2
    for epsilon in (1e-1, 1e-3):
        n = steps_for_epsilon(p, epsilon)
        check(f"epsilon={epsilon}: chosen n reaches threshold", residual(p, n) <= epsilon, f"n={n}")
        check(f"epsilon={epsilon}: previous n misses threshold", residual(p, n - 1) > epsilon, f"n-1={n - 1}")

    section("3. Multi-bit union-bound ledger")
    k = 3
    epsilon = 1e-2
    n = steps_for_epsilon(0.2, epsilon / k)
    union_bound = k * residual(0.2, n)
    check("k=3 union bound reaches requested epsilon", union_bound <= epsilon, f"{union_bound:.6e}")
    check("k=3 threshold depends on k", n > steps_for_epsilon(0.2, epsilon), f"n={n}")

    section("4. Exact endpoint remains separate")
    check("finite p<1 finite n is not exact reset", residual(0.5, 20) > 0.0, f"{residual(0.5, 20):.6e}")
    check("p=1 endpoint is exact in one supplied step", residual(1.0, 1) == 0.0)

    section("5. Source note sanity")
    doc = Path("docs/RECORD_ASYMPTOTIC_RESET_CONVERGENCE_LEDGER_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "actual_current_surface_status: bounded-support",
        "trace_class: upstream_support",
        "epsilon-reset convergence ledger",
        "Does not derive exact finite-time reset",
        "step counts, not physical time",
        "audit_required_before_effective_retained: true",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("exact closure", "exact finite-time reset is " + "derived"),
        ("rate closure", "finite-time rate is " + "derived"),
        ("clock closure", "clock is " + "derived"),
        ("cost closure", "thermodynamic cost is " + "derived"),
        ("dial closure", "dial location is " + "selected"),
        ("audit verdict", "promoted to " + "retained"),
    ]
    for label, phrase in forbidden_wording:
        check(f"forbidden wording absent: {label}", phrase not in text)

    section("SCORECARD")
    emit(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
