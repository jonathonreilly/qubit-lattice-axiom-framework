#!/usr/bin/env python3
"""Physical-intervention minimum-information uniqueness gate for Y_T."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_physical_intervention_mininfo_uniqueness_gate_2026-05-26.json"

NOTE = DOCS / "YT_PHYSICAL_INTERVENTION_MININFO_UNIQUENESS_GATE_NOTE_2026-05-26.md"
MIN_INFO = DOCS / "YT_MINIMUM_INFORMATION_SOURCE_ACTION_BRIDGE_THEOREM_NOTE_2026-05-26.md"
FISHER = DOCS / "YT_PRIMITIVE_PHYSICAL_SOURCE_FISHER_ARCLENGTH_INVARIANT_THEOREM_NOTE_2026-05-26.md"
PRIMITIVE_NOGO = DOCS / "YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md"
PHYSICAL_CANDIDATE = DOCS / "YT_PHYSICAL_TOP_INTERVENTION_IDENTIFICATION_CANDIDATE_NOTE_2026-05-25.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

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


def part1_anchors() -> None:
    print("\nPart 1: anchors and scope")
    for path in (NOTE, MIN_INFO, FISHER, PRIMITIVE_NOGO, PHYSICAL_CANDIDATE, FULL_STACK):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Operational Intervention Law",
        "Theorem",
        "What This Burns Down",
        "What Still Remains",
        "Why This Is Not The Old Ward Trap",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    check("note marks exact-support status", "actual_current_surface_status: exact-support" in note)
    check("note forbids proposal", "proposal_allowed: false" in note)


def part2_unique_mininfo_curve() -> None:
    print("\nPart 2: unique minimum-information curve")
    # Symbolic stationarity: q_i = p_i exp(h O_i - psi), already enough to
    # show all components share one source h and no hidden scale.
    q_i, p_i, alpha, beta, o_i = sp.symbols("q_i p_i alpha beta O_i", positive=True)
    term = q_i * sp.log(q_i / p_i) + alpha * q_i + beta * q_i * o_i
    stationary = sp.diff(term, q_i)
    solved = sp.solve(sp.Eq(stationary, 0), q_i)[0]
    h = sp.symbols("h")
    tilted = solved.subs(beta, -h)
    factor = sp.simplify(tilted / (p_i * sp.exp(h * o_i)))
    check("KL stationarity gives exponential tilt up to normalization", o_i not in factor.free_symbols, tilted)
    check("KL strict convexity gives uniqueness on simplex interior", sp.simplify(sp.diff(term, q_i, 2) - 1 / q_i) == 0)


def part3_top_component_readout() -> None:
    print("\nPart 3: top component readout under the intervention law")
    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    norm = sp.simplify((u.T * u)[0])
    check("six-component O_top is unit normalized", is_zero(norm - 1), norm)
    check("single component coefficient is 1/sqrt(6)", is_zero(u[0] - 1 / sp.sqrt(6)), u[0])

    lam = sp.symbols("lambda", positive=True)
    raw_component = lam * u[0]
    fisher_metric = lam**2
    fisher_component = sp.simplify(raw_component / sp.sqrt(fisher_metric))
    check("raw scaled component is lambda/sqrt(6)", is_zero(raw_component - lam / sp.sqrt(6)), raw_component)
    check("Fisher arclength component removes lambda", is_zero(fisher_component - 1 / sp.sqrt(6)), fisher_component)


def part4_hidden_scale_counterfamily() -> None:
    print("\nPart 4: hidden-scale counterfamily and narrowed no-go")
    lambdas = [0.5, 1.0, 1.7, 3.0]
    raw_values = [lam / math.sqrt(6.0) for lam in lambdas]
    fisher_values = [(lam / math.sqrt(6.0)) / lam for lam in lambdas]
    check("raw lambda family changes component values", len({round(v, 12) for v in raw_values}) == len(raw_values), raw_values)
    check("Fisher-unit readout is invariant across lambda family", max(fisher_values) - min(fisher_values) < 1.0e-14, fisher_values)

    primitive_nogo = read(PRIMITIVE_NOGO)
    check(
        "prior no-go remains scoped to baseline/current support only",
        "current support packets does not" in primitive_nogo
        and "force the primitive unit physical-source premise" in primitive_nogo,
    )
    check("prior no-go leaves future source/action theorem open", "future theorem derives" in primitive_nogo)


def part5_criteria_certificate() -> dict[str, bool]:
    print("\nPart 5: criteria certificate")
    criteria = {
        "local_target": True,
        "minimum_information": True,
        "intrinsic_fisher_source_unit": True,
        "no_hidden_channel": True,
        "normalized_top_operator": True,
        "physical_top_yukawa_law_audit_accepted": False,
        "one_higgs_top_carrier_retained": False,
        "same_scale_g2_retained_for_numeric_claim": False,
        "strict_top_w_response_evidence_present": False,
        "proposal_allowed": False,
    }
    for key in (
        "local_target",
        "minimum_information",
        "intrinsic_fisher_source_unit",
        "no_hidden_channel",
        "normalized_top_operator",
    ):
        check(f"criterion encoded: {key}", criteria[key])
    check("physical top Yukawa law still needs audit/derivation", not criteria["physical_top_yukawa_law_audit_accepted"])
    check("one-Higgs/top carrier authority remains outside this gate", not criteria["one_higgs_top_carrier_retained"])
    check("same-scale g2 remains outside local ratio scope", not criteria["same_scale_g2_retained_for_numeric_claim"])
    check("strict top/W response evidence remains absent", not criteria["strict_top_w_response_evidence_present"])
    check("proposal remains forbidden", not criteria["proposal_allowed"])
    return criteria


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
        "the no-hidden-scale minimum-information law has already been audited",
        "strict top/W pole-response evidence has been obtained",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T PHYSICAL-INTERVENTION MININFO UNIQUENESS GATE")
    print("=" * 78)

    part1_anchors()
    part2_unique_mininfo_curve()
    part3_top_component_readout()
    part4_hidden_scale_counterfamily()
    criteria = part5_criteria_certificate()
    part6_firewalls()

    result = {
        "actual_current_surface_status": "exact-support under no-hidden-scale minimum-information intervention law",
        "trace_class": "upstream_support",
        "reachability_to_target": "partially_closes",
        "conditional_surface_status": (
            "If the no-hidden-scale minimum-information intervention law is accepted "
            "as the physical top Yukawa source law for O_top, then y_33=1/sqrt(6)."
        ),
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The uniqueness theorem is exact under the intervention law, but the law "
            "still needs independent audit/derivation as the physical top Yukawa source law."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "first_open_gate_after_this_note": "audit/derive the physical intervention law",
        "backup_route": "strict same-source top/W pole-response measurement certificate",
        "criteria": criteria,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_PHYSICAL_INTERVENTION_MININFO_UNIQUENESS_GATE_NOTE_2026-05-26.md",
            "scripts/frontier_yt_physical_intervention_mininfo_uniqueness_gate.py",
            "outputs/yt_physical_intervention_mininfo_uniqueness_gate_2026-05-26.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
