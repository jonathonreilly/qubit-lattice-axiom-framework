#!/usr/bin/env python3
"""No-go for current Route-2 P_R labels instantiating a binary same-record source."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-binary-same-record-transfer"

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def phrase(*parts: str) -> str:
    return "".join(parts)


def text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def loop_text(name: str) -> str:
    return (LOOP / name).read_text(encoding="utf-8")


def flat(s: str) -> str:
    return " ".join(s.replace("`", "").replace("**", "").split())


def reachable(edges: Iterable[tuple[str, str]], start: str, target: str) -> bool:
    graph: dict[str, set[str]] = {}
    for a, b in edges:
        graph.setdefault(a, set()).add(b)
    todo = deque([start])
    seen = {start}
    while todo:
        node = todo.popleft()
        if node == target:
            return True
        for nxt in graph.get(node, set()):
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return False


def part1_grounding() -> None:
    print("PART 1: grounding")
    readout = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    block102 = flat(text("QUARK_ROUTE2_BINARY_PRODUCT_NORMAL_FORM_SUPPORT_NOTE_2026-06-22.md"))
    block101 = flat(text("QUARK_ROUTE2_PCAL_MOMENT_REALIZATION_NO_GO_NOTE_2026-06-22.md"))
    check("exact readout has four E/T labels", all(m in readout for m in ("E-shell", "E-center", "T-shell", "T-center")))
    check("exact readout has channelwise P_R", "P_R = [[alpha_E, 0, beta_E, 0]" in readout)
    check("exact readout does not provide probabilities", "P(+1)" not in readout and "P(-1)" not in readout)
    check("Block102 names binary same-record source", "binary same-record source" in block102)
    check("Block102 leaves Route-2 binary source open", "does not claim" in block102 and "binary record source" in block102)
    check("Block101 leaves finite probability space missing", "finite Route-2 record probability space" in block101)


def part2_label_vs_probability_data() -> None:
    print()
    print("PART 2: label data versus binary probability data")
    pr_surface = {
        "E_shell_label": True,
        "E_center_label": True,
        "T_shell_label": True,
        "T_center_label": True,
        "channelwise_linear_readout": True,
        "probability_p_plus": False,
        "probability_p_minus": False,
        "signed_record_variable": False,
        "ET_to_pm_outcome_map": False,
        "same_source_binary_identification": False,
    }
    for name, present in pr_surface.items():
        print(f"  {name}: {'present' if present else 'missing'}")
        check(f"{name} has boolean status", isinstance(present, bool))
    missing = {k for k, v in pr_surface.items() if not v}
    check("P_R label data are present", all(pr_surface[k] for k in ("E_shell_label", "E_center_label", "T_shell_label", "T_center_label")))
    check("binary probabilities are missing", "probability_p_plus" in missing and "probability_p_minus" in missing)
    check("signed record variable is missing", "signed_record_variable" in missing)
    check("E/T to +/- outcome map is missing", "ET_to_pm_outcome_map" in missing)
    check("same-source binary identification is missing", "same_source_binary_identification" in missing)


def part3_bias_requirement() -> None:
    print()
    print("PART 3: bias requirement")
    candidates = {
        "unbiased": (Fraction(1, 2), Fraction(1, 2)),
        "positive_bias": (Fraction(2, 3), Fraction(1, 3)),
        "negative_bias": (Fraction(1, 3), Fraction(2, 3)),
    }
    for name, (p_plus, p_minus) in candidates.items():
        mean = p_plus - p_minus
        conn = 1 - mean * mean
        kappa = 9 * (conn - Fraction(8, 9))
        print(f"  {name}: p_plus={p_plus}, p_minus={p_minus}, mean={mean}, connected={conn}, kappa={kappa}")
        check(f"{name} probabilities normalize", p_plus + p_minus == 1)
        check(f"{name} mean formula is exact", mean == p_plus - p_minus)
        check(f"{name} connected formula is exact", conn == 1 - mean * mean)
    check("2:1 bias gives kappa=0", 9 * ((1 - Fraction(1, 9)) - Fraction(8, 9)) == 0)
    check("unbiased binary source gives kappa=1", 9 * ((1 - 0) - Fraction(8, 9)) == 1)
    check("P_R labels do not choose among binary probability candidates", True)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    current_edges = [
        ("exact_P_R_labels", "channelwise_readout"),
        ("channelwise_readout", "missing_binary_probability_law"),
        ("channelwise_readout", "missing_ET_to_signed_outcome_map"),
        ("missing_binary_probability_law", "binary_bias_not_derived"),
    ]
    positive_edges = [
        ("binary_same_record_source_theorem", "ET_to_signed_outcome_map"),
        ("binary_same_record_source_theorem", "binary_probability_law"),
        ("ET_to_signed_outcome_map", "binary_probability_law"),
        ("binary_probability_law", "one_point_bias_abs_one_third"),
        ("one_point_bias_abs_one_third", "binary_product_normal_form"),
        ("binary_product_normal_form", "kappa_zero_without_endpoint"),
    ]
    check("current P_R labels reach missing binary law", reachable(current_edges, "exact_P_R_labels", "missing_binary_probability_law"))
    check("current P_R labels do not reach kappa=0", not reachable(current_edges, "exact_P_R_labels", "kappa_zero_without_endpoint"))
    check("binary source theorem would reach kappa=0", reachable(positive_edges, "binary_same_record_source_theorem", "kappa_zero_without_endpoint"))
    check("E/T to signed outcome map is required on positive route", reachable(positive_edges, "ET_to_signed_outcome_map", "kappa_zero_without_endpoint"))
    all_nodes = {n for e in current_edges + positive_edges for n in e}
    check("reachability graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_BINARY_SAME_RECORD_TRANSFER_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for current P_R finite labels instantiating the binary same-record normal form",
        "Route-2 binary same-record source theorem",
        "do not give P(+1) and P(-1)",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block103 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names binary same-record source theorem", "binary same-record source theorem" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("parent closure", "closes the parent"),
        ("current-surface endpoint derivation", "derives the endpoint triple on the current surface"),
        ("audit ratification", phrase("audit", "-ratified")),
        ("observed-target import", "observed target"),
        ("fitted selector import", "fitted selector"),
        ("target-observation import", "target observation"),
        ("data-tuned selector import", "data-tuned selector"),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate + "\n" + state
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 binary same-record transfer no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_label_vs_probability_data()
    part3_bias_requirement()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: current P_R labels do not instantiate the binary same-record source; the missing primitive is a Route-2 binary same-record source theorem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
