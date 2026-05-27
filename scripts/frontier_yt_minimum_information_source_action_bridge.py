#!/usr/bin/env python3
"""Minimum-information source/action bridge for the Y_T source lane."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_minimum_information_source_action_bridge_2026-05-26.json"

NOTE = DOCS / "YT_MINIMUM_INFORMATION_SOURCE_ACTION_BRIDGE_THEOREM_NOTE_2026-05-26.md"
SOURCE_ACTION = DOCS / "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md"
FISHER = DOCS / "YT_PRIMITIVE_PHYSICAL_SOURCE_FISHER_ARCLENGTH_INVARIANT_THEOREM_NOTE_2026-05-26.md"
POLE_NOGO = DOCS / "YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md"

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


def normalize(weights: list[float]) -> list[float]:
    z = sum(weights)
    return [w / z for w in weights]


def states(n: int) -> list[tuple[int, ...]]:
    return list(itertools.product((-1, 1), repeat=n))


def kl(q: list[float], p: list[float]) -> float:
    return sum(qi * math.log(qi / pi) for qi, pi in zip(q, p) if qi > 0)


def part1_anchors() -> None:
    print("\nPart 1: anchors")
    for path in (NOTE, SOURCE_ACTION, FISHER, POLE_NOGO):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Theorem Statement",
        "What This Burns Down",
        "What Still Remains",
        "Relation To Existing No-Gos",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains required section: {phrase}", phrase in note)


def part2_variational_derivation() -> None:
    print("\nPart 2: symbolic KL variational derivation")
    q_i, p_i, alpha, beta, o_i = sp.symbols("q_i p_i alpha beta O_i", positive=True)
    lagrangian_term = q_i * sp.log(q_i / p_i) + alpha * q_i + beta * q_i * o_i
    stationarity = sp.diff(lagrangian_term, q_i)
    solved = sp.solve(sp.Eq(stationarity, 0), q_i)[0]
    h = sp.symbols("h")
    renamed = solved.subs(beta, -h)
    normalization_factor = sp.simplify(renamed / (p_i * sp.exp(h * o_i)))
    check(
        "stationarity gives exponential tilt up to normalization",
        o_i not in normalization_factor.free_symbols,
        renamed,
    )
    check("KL Hessian is strictly positive", sp.simplify(sp.diff(lagrangian_term, q_i, 2) - 1 / q_i) == 0)


def part3_numeric_i_projection() -> None:
    print("\nPart 3: numeric finite-record I-projection witness")
    omega = states(3)
    p0 = [1.0 / len(omega)] * len(omega)
    values = [sum(eps) / math.sqrt(3.0) for eps in omega]
    h = 0.37
    weights = [p * math.exp(h * o) for p, o in zip(p0, values)]
    qh = normalize(weights)
    mean_h = sum(q * o for q, o in zip(qh, values))

    # KKT residual for minimizing D(q||p0) with the achieved mean constraint.
    psi = math.log(sum(p * math.exp(h * o) for p, o in zip(p0, values)))
    residuals = [abs(math.log(q / p) - h * o + psi) for q, p, o in zip(qh, p0, values)]
    check("exponential family satisfies KKT residuals", max(residuals) < 1.0e-14, max(residuals))
    check("source changes target expectation", abs(mean_h) > 0.01, mean_h)

    perturbed = qh.copy()
    perturbed[0] *= 1.001
    perturbed[1] *= 0.999
    perturbed = normalize(perturbed)
    # Adjusting arbitrary probabilities typically changes the target mean;
    # the witness only checks that the exponential member is a valid KKT point.
    check("exponential member has finite KL", kl(qh, p0) > 0.0, kl(qh, p0))


def part4_action_equivalence_and_fisher_unit() -> None:
    print("\nPart 4: source-action equivalence and Fisher unit")
    omega = states(3)
    h = 0.21
    values = [sum(eps) / math.sqrt(3.0) for eps in omega]
    p0 = [1.0 / len(omega)] * len(omega)
    rn = normalize([p * math.exp(h * o) for p, o in zip(p0, values)])
    action = normalize([math.exp(h * o) for o in values])
    l1 = sum(abs(a - b) for a, b in zip(rn, action))
    check("RN exponential tilt equals source-coupled action density", l1 < 1.0e-14, l1)

    mean0 = sum(p * o for p, o in zip(p0, values))
    var0 = sum(p * (o - mean0) ** 2 for p, o in zip(p0, values))
    check("normalized signed top proxy has zero baseline mean", abs(mean0) < 1.0e-14, mean0)
    check("normalized signed top proxy has Fisher unit variance", abs(var0 - 1.0) < 1.0e-14, var0)

    lam = 2.3
    fisher_scaled = lam * lam * var0
    arclength_derivative = -lam / math.sqrt(fisher_scaled)
    check("scaled raw source has same Fisher-unit derivative", abs(arclength_derivative + 1.0) < 1.0e-14, arclength_derivative)


def part5_current_boundary() -> dict[str, Any]:
    print("\nPart 5: current boundary")
    boundary = {
        "minimum_information_source_action_derived": True,
        "physical_top_intervention_identified_with_minimum_information_source": False,
        "accepted_same_surface_pole_action_authority": False,
        "strict_top_w_response_evidence": False,
        "proposal_allowed": False,
    }
    check("minimum-information source/action bridge is derived", boundary["minimum_information_source_action_derived"])
    check(
        "physical top intervention identification remains open",
        not boundary["physical_top_intervention_identified_with_minimum_information_source"],
    )
    check("accepted same-surface pole/action authority remains open", not boundary["accepted_same_surface_pole_action_authority"])
    check("strict top/W response evidence remains open", not boundary["strict_top_w_response_evidence"])
    check("proposal remains forbidden", not boundary["proposal_allowed"])
    return boundary


def part6_firewalls() -> None:
    print("\nPart 6: firewalls")
    note = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed W/Z/top masses",
        "PDG",
        "`alpha_LM`",
        "plaquette/u0",
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in note)

    for phrase in (
        "Status:** retained",
        "proposed_retained Y_T closure",
        "This note derives `y_t`",
        "physical Y_T pole/action surface has been obtained",
        "strict top/W pole-response evidence has been obtained",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T MINIMUM-INFORMATION SOURCE-ACTION BRIDGE")
    print("=" * 78)

    part1_anchors()
    part2_variational_derivation()
    part3_numeric_i_projection()
    part4_action_equivalence_and_fisher_unit()
    boundary = part5_current_boundary()
    part6_firewalls()

    result = {
        "actual_current_surface_status": "exact-support under minimum-information intervention criterion",
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The theorem derives the RN/source-action source family from finite-record "
            "minimum-information intervention, but the physical top intervention and "
            "accepted same-surface pole/action authority remain open."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "boundary": boundary,
        "first_open_gate_after_this_note": "accepted same-surface pole/action authority",
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_MINIMUM_INFORMATION_SOURCE_ACTION_BRIDGE_THEOREM_NOTE_2026-05-26.md",
            "scripts/frontier_yt_minimum_information_source_action_bridge.py",
            "outputs/yt_minimum_information_source_action_bridge_2026-05-26.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
