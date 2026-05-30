#!/usr/bin/env python3
"""Source/measure P-cal cumulant/Mobius connected-response theorem runner.

Checks a second route to the P-cal/log generator:

  finite record moments + partition-lattice Mobius inversion
    -> connected responses are derivatives of log M
    -> raw Z^p or M^p does not generate unit connected responses unless p=1.

This is exact support for the claim that if "physical scalar response" means
connected response to local sources, the scalar generator is W=log Z.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = ROOT / "outputs" / "source_measure_pcal_cumulant_mobius_2026-05-30.json"

NOTE = DOCS / "SOURCE_MEASURE_PCAL_CUMULANT_MOBIUS_THEOREM_NOTE_2026-05-30.md"
RN_NOTE = DOCS / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
P1P2 = DOCS / "OBSERVABLE_PRINCIPLE_P1P2_TWO_STAGE_SYNTHESIS_NARROW_THEOREM_NOTE_2026-05-28.md"
SOURCE_ACTION = DOCS / "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def partitions(items: tuple[int, ...]) -> list[tuple[tuple[int, ...], ...]]:
    """All set partitions of a small tuple."""
    if not items:
        return [()]
    first, rest = items[0], items[1:]
    out = []
    for part in partitions(rest):
        out.append(((first,),) + part)
        for i in range(len(part)):
            block = tuple(sorted((first,) + part[i]))
            out.append(tuple(sorted(part[:i] + (block,) + part[i + 1 :])))
    # canonical unique
    uniq = []
    seen = set()
    for part in out:
        key = tuple(sorted(tuple(sorted(b)) for b in part))
        if key not in seen:
            seen.add(key)
            uniq.append(key)
    return uniq


def mobius_pi_to_one(num_blocks: int) -> int:
    """Mobius function mu(pi, top) on partition lattice."""
    return (-1) ** (num_blocks - 1) * sp.factorial(num_blocks - 1)


def part1_boundary() -> dict[str, Any]:
    print("\nPart 1: document/status boundary")
    for path in (NOTE, RN_NOTE, P1P2, SOURCE_ACTION):
        check(f"{path.relative_to(ROOT)} exists", path.exists())
    note = read(NOTE)
    for phrase in (
        "Theorem",
        "Mobius proof",
        "Scale test",
        "Connection to P-cal",
        "Status boundary",
        "Non-claims",
    ):
        check(f"note contains required phrase: {phrase}", phrase in note)
    check("note marks exact-support status", "actual_current_surface_status: exact-support" in note)
    check("note forbids retained overclaim", "bare_retained_allowed: false" in note)
    return {"actual_status": "exact-support"}


def part2_partition_lattice_mobius() -> dict[str, Any]:
    print("\nPart 2: partition-lattice Mobius inversion")
    # Three abstract variables with named moments.  The third cumulant is
    # m123 - m12 m3 - m13 m2 - m23 m1 + 2 m1 m2 m3.
    items = (1, 2, 3)
    parts = partitions(items)
    check("Bell number B3 is 5", len(parts) == 5, len(parts))

    m = {
        (1,): sp.Symbol("m1"),
        (2,): sp.Symbol("m2"),
        (3,): sp.Symbol("m3"),
        (1, 2): sp.Symbol("m12"),
        (1, 3): sp.Symbol("m13"),
        (2, 3): sp.Symbol("m23"),
        (1, 2, 3): sp.Symbol("m123"),
    }
    kappa3 = 0
    for pi in parts:
        prod = 1
        for block in pi:
            prod *= m[tuple(sorted(block))]
        kappa3 += mobius_pi_to_one(len(pi)) * prod
    expected = m[(1, 2, 3)] - m[(1, 2)] * m[(3,)] - m[(1, 3)] * m[(2,)] - m[(2, 3)] * m[(1,)] + 2 * m[(1,)] * m[(2,)] * m[(3,)]
    check("third cumulant Mobius formula is standard", sp.expand(kappa3 - expected) == 0, kappa3)

    # If variable 3 is independent from (1,2), moments factor and kappa3 is 0.
    independent = {
        m[(1, 3)]: m[(1,)] * m[(3,)],
        m[(2, 3)]: m[(2,)] * m[(3,)],
        m[(1, 2, 3)]: m[(1, 2)] * m[(3,)],
    }
    check("mixed cumulant vanishes under independence", sp.expand(kappa3.subs(independent)) == 0, sp.expand(kappa3.subs(independent)))
    return {"B3": 5, "kappa3": str(expected)}


def part3_log_generates_connected_responses() -> dict[str, Any]:
    print("\nPart 3: log moment generator gives connected responses")
    t, u = sp.symbols("t u", real=True)

    # Independent binary records with nonzero means a,b.  Use Bernoulli +/-1
    # parametrized by means a,b in (-1,1).
    a, b = sp.symbols("a b", real=True)
    Mx = sp.cosh(t) + a * sp.sinh(t)
    My = sp.cosh(u) + b * sp.sinh(u)
    M = sp.expand(Mx * My)
    K = sp.log(M)

    raw_mixed = sp.diff(M, t, u).subs({t: 0, u: 0})
    conn_mixed = sp.diff(K, t, u).subs({t: 0, u: 0})
    check("raw mixed moment includes disconnected product", is_zero(raw_mixed - a * b), raw_mixed)
    check("log generator mixed connected response vanishes for independent records", is_zero(conn_mixed), conn_mixed)

    # Same single variable: K''(0) gives variance, not raw second moment.
    Kx = sp.log(Mx)
    first = sp.diff(Kx, t).subs(t, 0)
    second = sp.diff(Kx, t, 2).subs(t, 0)
    check("first log derivative is mean", is_zero(first - a), first)
    check("second log derivative is variance", is_zero(second - (1 - a**2)), second)

    return {
        "raw_mixed": "a*b",
        "connected_mixed": "0 under independence",
        "second_connected": "variance",
    }


def part4_scale_test() -> dict[str, Any]:
    print("\nPart 4: scale test against F_p")
    t, p = sp.symbols("t p", positive=True)
    M = sp.cosh(t)  # centered signed record
    K = sp.log(M)
    Kp = p * K
    second = sp.diff(K, t, 2).subs(t, 0)
    second_p = sp.diff(Kp, t, 2).subs(t, 0)
    check("unit connected two-point response is one", is_zero(second - 1), second)
    check("p-scaled connected two-point response is p", is_zero(second_p - p), second_p)
    check("unit connected-response normalization selects p=1", sp.solve(sp.Eq(second_p, 1), p) == [1])

    # Raw M^p has the same origin second derivative p for centered records,
    # but higher disconnected structure is not the cumulant generator.
    Mp = M**p
    raw_second_p = sp.diff(Mp, t, 2).subs(t, 0)
    check("raw M^p second derivative also carries p at origin", is_zero(raw_second_p - p), raw_second_p)
    return {"scale_residual": "unit connected two-point normalization selects p=1"}


def part5_firewall() -> None:
    print("\nPart 5: firewall")
    note = read(NOTE)
    flat_note = " ".join(note.split())
    for phrase in ("H_unit", "yt_ward_identity", "y_t_bare", "PDG", "alpha_LM", "plaquette", "fitted selector"):
        check(f"forbidden import named in firewall: {phrase}", phrase in flat_note)
    for phrase in ("Status: retained", "unbounded retained Y_T closure is claimed", "audit-clean retained"):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 88)
    print("SOURCE/MEASURE P-CAL CUMULANT-MOBIUS THEOREM")
    print("=" * 88)
    result = {
        "boundary": part1_boundary(),
        "mobius": part2_partition_lattice_mobius(),
        "log_connected": part3_log_generates_connected_responses(),
        "scale": part4_scale_test(),
    }
    part5_firewall()
    result["summary"] = {
        "pass": PASS_COUNT,
        "fail": FAIL_COUNT,
        "actual_current_surface_status": "exact-support",
        "trace_class": "direct_blocker_closure_candidate",
        "proposal_allowed": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
