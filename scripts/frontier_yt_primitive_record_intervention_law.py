#!/usr/bin/env python3
"""Primitive no-hidden-record intervention law for the Y_T source lane."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_primitive_record_intervention_law_2026-05-27.json"

NOTE = DOCS / "YT_PRIMITIVE_RECORD_INTERVENTION_LAW_THEOREM_NOTE_2026-05-27.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-05-20.md"
LSP = DOCS / "LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md"
LSP_SOURCE = DOCS / "YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md"
MIN_INFO = DOCS / "YT_MINIMUM_INFORMATION_SOURCE_ACTION_BRIDGE_THEOREM_NOTE_2026-05-26.md"
MININFO_GATE = DOCS / "YT_PHYSICAL_INTERVENTION_MININFO_UNIQUENESS_GATE_NOTE_2026-05-26.md"
SOURCE_UNIT_NOGO = DOCS / "YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md"
SOURCE_SCALE = DOCS / "YT_LSP_SOURCE_SCALE_BOUNDARY_AND_STRICT_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
PANEL = DOCS / "YT_PHYSICAL_SOURCE_LAW_RESEARCH_PANEL_SYNTHESIS_NOTE_2026-05-26.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

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


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(read(path))


def ledger_status(claim_id: str) -> str | None:
    rows = load_json(LEDGER)["rows"]
    iterable = rows.values() if isinstance(rows, dict) else rows
    for row in iterable:
        if row.get("claim_id") == claim_id:
            return row.get("effective_status")
    return None


def states(n: int) -> list[tuple[int, ...]]:
    return list(itertools.product((-1, 1), repeat=n))


def normalize(xs: list[float]) -> list[float]:
    z = sum(xs)
    return [x / z for x in xs]


def kl(q: list[float], p: list[float]) -> float:
    return sum(qi * math.log(qi / pi) for qi, pi in zip(q, p) if qi > 0.0)


def mean(q: list[float], vals: list[float]) -> float:
    return sum(qi * vi for qi, vi in zip(q, vals))


def variance(q: list[float], vals: list[float]) -> float:
    m = mean(q, vals)
    return sum(qi * (vi - m) ** 2 for qi, vi in zip(q, vals))


def part1_anchors() -> dict[str, str | None]:
    print("\nPart 1: anchors and current authority")
    paths = (
        NOTE,
        AXIOMS,
        LSP,
        LSP_SOURCE,
        MIN_INFO,
        MININFO_GATE,
        SOURCE_UNIT_NOGO,
        SOURCE_SCALE,
        FULL_STACK,
        PANEL,
        LEDGER,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Definitions",
        "Theorem",
        "Proof",
        "Y_T Consequence",
        "What This Burns Down",
        "Remaining Gate",
        "Relation To Existing No-Gos",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    statuses = {
        "lsp_projective": ledger_status("lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22"),
        "lsp_signed_record": ledger_status("yt_lsp_signed_record_source_readout_support_note_2026-05-24"),
        "source_action": ledger_status("yt_source_action_support_packet_note_2026-05-22"),
        "powers_tracial": ledger_status("powers_uhf_tracial_uniqueness_on_qubit_lattice_narrow_theorem_note_2026-05-20"),
        "busch_povm": ledger_status("busch_povm_extension_on_qubit_lattice_narrow_theorem_note_2026-05-20"),
    }
    check("LSP projective row is retained_bounded", statuses["lsp_projective"] == "retained_bounded", statuses["lsp_projective"])
    check("Y_T LSP signed-record row is retained_bounded", statuses["lsp_signed_record"] == "retained_bounded", statuses["lsp_signed_record"])
    check("source/action support row is retained_bounded", statuses["source_action"] == "retained_bounded", statuses["source_action"])
    check("Powers tracial theorem is retained", statuses["powers_tracial"] == "retained", statuses["powers_tracial"])
    check("Busch POVM theorem is retained", statuses["busch_povm"] == "retained", statuses["busch_povm"])
    return statuses


def part2_lsp_record_space() -> dict[str, Any]:
    print("\nPart 2: finite LSP record space")
    omega = states(3)
    p0 = [1.0 / len(omega)] * len(omega)
    vals = [sum(eps) / math.sqrt(3.0) for eps in omega]
    check("finite signed record block has 2^3 states", len(omega) == 8)
    check("baseline law has full support", all(p > 0 for p in p0))
    check("normalized signed statistic has zero mean", abs(mean(p0, vals)) < 1.0e-14, mean(p0, vals))
    check("normalized signed statistic has unit variance", abs(variance(p0, vals) - 1.0) < 1.0e-14, variance(p0, vals))

    identity = sp.eye(2)
    sigma_z = sp.Matrix([[1, 0], [0, -1]])
    p_plus = (identity + sigma_z) / 2
    p_minus = (identity - sigma_z) / 2
    check("P_plus is projection", p_plus * p_plus == p_plus)
    check("P_minus is projection", p_minus * p_minus == p_minus)
    check("signed readout equals sigma_z", p_plus - p_minus == sigma_z)
    check("signed readout spectrum is {-1,+1}", sorted(sigma_z.eigenvals().keys()) == [-1, 1])
    return {"state_count": len(omega), "mean": mean(p0, vals), "variance": variance(p0, vals)}


def part3_kl_projection_symbolic() -> None:
    print("\nPart 3: symbolic KL/I-projection")
    q_i, p_i, alpha, beta, o_i = sp.symbols("q_i p_i alpha beta O_i", positive=True)
    term = q_i * sp.log(q_i / p_i) + alpha * q_i + beta * q_i * o_i
    stationarity = sp.diff(term, q_i)
    solved = sp.solve(sp.Eq(stationarity, 0), q_i)[0]
    ell = sp.symbols("ell")
    tilted = solved.subs(beta, -ell)
    factor = sp.simplify(tilted / (p_i * sp.exp(ell * o_i)))
    check("stationarity gives exponential tilt up to normalization", o_i not in factor.free_symbols, tilted)
    check("KL Hessian is 1/q_i", sp.simplify(sp.diff(term, q_i, 2) - 1 / q_i) == 0)
    check("KL Hessian is positive on simplex interior", sp.diff(term, q_i, 2) == 1 / q_i)


def part4_no_hidden_fiber_witness() -> dict[str, float]:
    print("\nPart 4: no-hidden-record fiber witness")
    # Four records (a,b), target O=a. Hidden changes alter b conditionals
    # while preserving the target expectation.
    omega = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    p0 = [0.25] * 4
    target_m = 0.3
    q_min = [
        (1 - target_m) / 4,
        (1 - target_m) / 4,
        (1 + target_m) / 4,
        (1 + target_m) / 4,
    ]
    q_hidden = [
        (1 - target_m) * 0.15,
        (1 - target_m) * 0.35,
        (1 + target_m) * 0.40,
        (1 + target_m) * 0.10,
    ]
    vals = [a for a, _b in omega]
    check("minimum law has target expectation", abs(mean(q_min, vals) - target_m) < 1.0e-14, mean(q_min, vals))
    check("hidden law has same target expectation", abs(mean(q_hidden, vals) - target_m) < 1.0e-14, mean(q_hidden, vals))
    kl_min = kl(q_min, p0)
    kl_hidden = kl(q_hidden, p0)
    check("hidden fiber change has larger KL distinguishability", kl_hidden > kl_min, (kl_min, kl_hidden))
    check("minimum law preserves b conditional in a=-1 fiber", abs(q_min[0] / (q_min[0] + q_min[1]) - 0.5) < 1.0e-14)
    check("minimum law preserves b conditional in a=+1 fiber", abs(q_min[2] / (q_min[2] + q_min[3]) - 0.5) < 1.0e-14)
    check("hidden law changes b conditional in a=-1 fiber", abs(q_hidden[0] / (q_hidden[0] + q_hidden[1]) - 0.5) > 0.1)
    check("hidden law changes b conditional in a=+1 fiber", abs(q_hidden[2] / (q_hidden[2] + q_hidden[3]) - 0.5) > 0.1)
    return {"kl_minimum": kl_min, "kl_hidden": kl_hidden}


def part5_markov_naturality() -> dict[str, float]:
    print("\nPart 5: Markov sufficiency and coarse-graining")
    omega = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    p0 = [0.10, 0.20, 0.30, 0.40]
    ell = 0.47
    vals = [a for a, _b in omega]
    weights = [p * math.exp(ell * v) for p, v in zip(p0, vals)]
    q = normalize(weights)
    p0_marg = {-1: p0[0] + p0[1], 1: p0[2] + p0[3]}
    q_marg = {-1: q[0] + q[1], 1: q[2] + q[3]}
    marginal_tilt = {
        a: p0_marg[a] * math.exp(ell * a)
        for a in (-1, 1)
    }
    z = sum(marginal_tilt.values())
    marginal_tilt = {a: v / z for a, v in marginal_tilt.items()}
    check("tilt commutes with sufficient coarse-graining for a=-1", abs(q_marg[-1] - marginal_tilt[-1]) < 1.0e-14)
    check("tilt commutes with sufficient coarse-graining for a=+1", abs(q_marg[1] - marginal_tilt[1]) < 1.0e-14)
    check("conditional b|-1 remains baseline", abs(q[0] / q_marg[-1] - p0[0] / p0_marg[-1]) < 1.0e-14)
    check("conditional b|+1 remains baseline", abs(q[2] / q_marg[1] - p0[2] / p0_marg[1]) < 1.0e-14)
    return {"q_marg_minus": q_marg[-1], "q_marg_plus": q_marg[1]}


def part6_fisher_lambda_and_top_component() -> dict[str, str]:
    print("\nPart 6: Fisher unit, lambda, and top component")
    lam = sp.symbols("lambda", positive=True)
    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    norm = sp.simplify((u.T * u)[0])
    check("six-component top statistic is unit normalized", sp.simplify(norm - 1) == 0, norm)
    check("top component is 1/sqrt(6)", sp.simplify(u[0] - 1 / sp.sqrt(6)) == 0, u[0])
    raw_component = lam * u[0]
    fisher_metric = lam**2
    intrinsic_component = sp.simplify(raw_component / sp.sqrt(fisher_metric))
    check("raw lambda changes raw component", sp.simplify(raw_component - lam / sp.sqrt(6)) == 0, raw_component)
    check("Fisher arclength removes positive lambda", sp.simplify(intrinsic_component - 1 / sp.sqrt(6)) == 0, intrinsic_component)
    return {"top_component": "1/sqrt(6)", "lambda_status": "raw coordinate scale under Fisher unit"}


def part7_boundary_and_firewalls() -> dict[str, Any]:
    print("\nPart 7: boundary and firewalls")
    note = read(NOTE)
    boundary = {
        "primitive_record_intervention_law_derived": True,
        "physical_top_yukawa_identified_as_primitive_intervention": False,
        "strict_top_w_response_evidence_present": False,
        "proposal_allowed_for_full_y_t": False,
        "actual_current_surface_status": "exact-support",
    }
    check("primitive record law is marked derived", boundary["primitive_record_intervention_law_derived"])
    check("physical top-source identification remains open", not boundary["physical_top_yukawa_identified_as_primitive_intervention"])
    check("strict top/W response remains absent", not boundary["strict_top_w_response_evidence_present"])
    check("full Y_T proposal remains forbidden", not boundary["proposal_allowed_for_full_y_t"])
    check("actual current status is exact-support", "actual_current_surface_status: exact-support" in note)
    check("proposal remains false", "proposal_allowed: false" in note)
    check("first open gate is top-source identification", "first_open_gate_after_this_note: physical top-source identification" in note)

    for phrase in (
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
    ):
        check(f"firewall input recorded: {phrase}", phrase in note)

    for phrase in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "strict top/W response rows are proved",
        "This note proves that the physical top Yukawa deformation has already been accepted",
        "This note claims full Y_T retained closure",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)
    return boundary


def main() -> int:
    print("=" * 78)
    print("Y_T PRIMITIVE RECORD INTERVENTION LAW")
    print("=" * 78)

    statuses = part1_anchors()
    record_space = part2_lsp_record_space()
    part3_kl_projection_symbolic()
    hidden = part4_no_hidden_fiber_witness()
    markov = part5_markov_naturality()
    top = part6_fisher_lambda_and_top_component()
    boundary = part7_boundary_and_firewalls()

    result = {
        "actual_current_surface_status": "exact-support",
        "trace_class": "upstream_support",
        "reachability_to_target": "partially_closes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The primitive no-hidden-record intervention law is derived, but "
            "full Y_T closure still needs top-source identification or strict "
            "same-source top/W response evidence."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "statuses": statuses,
        "record_space": record_space,
        "no_hidden_fiber_witness": hidden,
        "markov_naturality": markov,
        "top_component": top,
        "boundary": boundary,
        "first_open_gate_after_this_note": "physical top-source identification",
        "backup_route": "strict same-source top/W response evidence",
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_PRIMITIVE_RECORD_INTERVENTION_LAW_THEOREM_NOTE_2026-05-27.md",
            "scripts/frontier_yt_primitive_record_intervention_law.py",
            "outputs/yt_primitive_record_intervention_law_2026-05-27.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
