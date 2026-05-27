#!/usr/bin/env python3
"""Guard runner for the Y_T physical source-law research synthesis."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_physical_source_law_research_panel_synthesis_2026-05-26.json"

NOTE = DOCS / "YT_PHYSICAL_SOURCE_LAW_RESEARCH_PANEL_SYNTHESIS_NOTE_2026-05-26.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
MININFO_GATE = DOCS / "YT_PHYSICAL_INTERVENTION_MININFO_UNIQUENESS_GATE_NOTE_2026-05-26.md"
FISHER = DOCS / "YT_PRIMITIVE_PHYSICAL_SOURCE_FISHER_ARCLENGTH_INVARIANT_THEOREM_NOTE_2026-05-26.md"
FISHER_LSZ = DOCS / "YT_FISHER_LSZ_SOURCE_NORMALIZATION_BRIDGE_THEOREM_NOTE_2026-05-26.md"
TOP_CARRIER = DOCS / "YT_ONE_HIGGS_TOP_CARRIER_SELECTION_SUPPORT_NOTE_2026-05-26.md"

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
    print("\nPart 1: anchors")
    for path in (NOTE, FULL_STACK, MININFO_GATE, FISHER, FISHER_LSZ, TOP_CARRIER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Narrow Problem",
        "Five-Agent Exercise",
        "Convergence Synthesis",
        "Literature Scan",
        "Assumptions Audit",
        "First-Principles Reframe",
        "Attack Vector Selection",
        "Multi-Block Track",
        "Current Decision",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)


def part2_panel_convergence() -> dict[str, Any]:
    print("\nPart 2: panel convergence")
    note = read(NOTE)
    probes = (
        "Literature 2020+",
        "Math tools",
        "20-physicist panel",
        "Framework-native bottom-up",
        "Assumptions audit",
    )
    for probe in probes:
        check(f"probe recorded: {probe}", probe in note)

    check("panel records conditional acceptance count", "`20/20` accept the conditional theorem" in note)
    check("panel records zero retained acceptance now", "`0/20` accept retained physical-source closure now" in note)
    check(
        "all probes converge on physical source law",
        "primitive physical source intervention law" in note,
    )
    check("strict top/W fallback remains live", "strict same-source top/W response evidence" in note)
    return {
        "agent_count": 5,
        "conditional_theorem_acceptance": "20/20",
        "retained_physical_source_acceptance_now": "0/20",
        "selected_primitive": "LSP-compatible primitive physical intervention law",
        "backup_route": "strict same-source top/W response evidence",
    }


def part3_math_kernel() -> None:
    print("\nPart 3: math kernel for selected primitive")
    q_i, p_i, alpha, beta, o_i = sp.symbols("q_i p_i alpha beta O_i", positive=True)
    term = q_i * sp.log(q_i / p_i) + alpha * q_i + beta * q_i * o_i
    stationary = sp.diff(term, q_i)
    solved = sp.solve(sp.Eq(stationary, 0), q_i)[0]
    h = sp.symbols("h")
    tilted = solved.subs(beta, -h)
    normalization_factor = sp.simplify(tilted / (p_i * sp.exp(h * o_i)))
    check("KL stationarity gives RN exponential tilt up to normalization", o_i not in normalization_factor.free_symbols, tilted)
    check("KL objective is strictly convex on simplex interior", sp.simplify(sp.diff(term, q_i, 2) - 1 / q_i) == 0)

    lam = sp.symbols("lambda", positive=True)
    fisher_metric_raw_h = lam**2
    intrinsic_derivative = sp.simplify((-lam) / sp.sqrt(fisher_metric_raw_h))
    check("Fisher arclength removes positive raw lambda", is_zero(intrinsic_derivative + 1), intrinsic_derivative)

    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    check("six-component top vector is unit normalized", is_zero((u.T * u)[0] - 1), (u.T * u)[0])
    check("component readout is 1/sqrt(6)", is_zero(u[0] - 1 / sp.sqrt(6)), u[0])


def part4_literature_and_import_firewall() -> None:
    print("\nPart 4: literature scan and import firewall")
    note = read(NOTE)
    references = (
        "Functional information geometry of Euclidean quantum",
        "Exact flow equation for the divergence functional",
        "Erdmenger",
        "Chentsov",
        "Markov-kernel information geometry",
        "Markov categories with entropy",
        "Lattice Feynman-Hellmann",
        "modular flavor symmetries",
        "warped",
    )
    for ref in references:
        check(f"literature/topic recorded: {ref}", ref in note)

    check("literature is not used as proof authority", "not imported" in note or "not acceptable proof inputs" in note)
    check("hierarchy models demoted to context", "Context Only" in note and "not provide framework-native closure" in note)


def part5_track_and_status_firewalls() -> list[str]:
    print("\nPart 5: multi-block track and status firewalls")
    note = read(NOTE)
    blocks = (
        "Block 1: Primitive Record Intervention Law",
        "Block 2: Chentsov/Fisher Source Unit",
        "Block 3: Top Source Direction And Carrier",
        "Block 4: Local Coefficient Closure",
        "Block 5: LSZ/Pole Compatibility",
        "Block 6: Strict Top/W Response Fallback Or Cross-Check",
    )
    for block in blocks:
        check(f"track contains {block}", block in note)

    check("current decision is Block 1 first", "Proceed with Block 1 first" in note)
    check("actual current status is exact-support", "actual_current_surface_status: exact-support" in note)
    check("proposal remains forbidden", "proposal_allowed: false" in note)
    check("bare retained remains forbidden", "bare_retained_allowed: false" in note)

    forbidden_overclaims = (
        "Status:** retained",
        "Status:** proposed_retained",
        "This synthesis derives y_t",
        "This note claims retained physical-source closure now",
        "strict top/W response rows are proved",
        "The no-hidden-scale minimum-information law is already derived as the physical top Yukawa source law.",
    )
    for phrase in forbidden_overclaims:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    forbidden_inputs = (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed W/Z/top masses",
        "PDG",
        "`alpha_LM`",
        "plaquette/u0",
        "Planck",
        "alpha_s",
        "fitted selector",
    )
    for phrase in forbidden_inputs:
        check(f"firewall input recorded: {phrase}", phrase in note)

    return list(blocks)


def part6_trace_reachability() -> None:
    print("\nPart 6: trace reachability")
    full_stack = read(FULL_STACK)
    mininfo = read(MININFO_GATE)
    note = read(NOTE)
    check(
        "synthesis targets the full-stack first open gate",
        "audit/derive that the no-hidden-scale minimum-information law" in full_stack
        and "derive/audit the no-hidden-scale minimum-information intervention law" in note,
    )
    check(
        "synthesis preserves mininfo gate status",
        "actual_current_surface_status: exact-support" in mininfo
        and "actual_current_surface_status: exact-support" in note,
    )
    check(
        "synthesis names fallback when law is not accepted",
        "If Block 1 fails" in note and "pivot to Block 6" in note,
    )


def main() -> int:
    print("=" * 78)
    print("Y_T PHYSICAL SOURCE-LAW RESEARCH PANEL SYNTHESIS")
    print("=" * 78)

    part1_anchors()
    panel = part2_panel_convergence()
    part3_math_kernel()
    part4_literature_and_import_firewall()
    blocks = part5_track_and_status_firewalls()
    part6_trace_reachability()

    result = {
        "actual_current_surface_status": "exact-support",
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The research panel selects the next primitive but does not derive "
            "the physical intervention law."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "panel": panel,
        "selected_next_primitive": "LSP-compatible primitive physical intervention law",
        "multi_block_track": blocks,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_PHYSICAL_SOURCE_LAW_RESEARCH_PANEL_SYNTHESIS_NOTE_2026-05-26.md",
            "scripts/frontier_yt_physical_source_law_research_panel_synthesis.py",
            "outputs/yt_physical_source_law_research_panel_synthesis_2026-05-26.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
