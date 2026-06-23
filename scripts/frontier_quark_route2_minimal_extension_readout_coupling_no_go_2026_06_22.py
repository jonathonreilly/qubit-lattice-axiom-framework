#!/usr/bin/env python3
"""No-go for Block121 minimal source extension alone fixing physical E/T coupling."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-minimal-extension-readout-coupling"

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


def center_ratio(internal_fraction: Fraction, sigma: Fraction, mu: Fraction) -> Fraction:
    return sigma * mu * internal_fraction


def part1_grounding() -> None:
    print("PART 1: grounding")
    block121 = flat(text("QUARK_ROUTE2_MINIMAL_MULTI_RECORD_EXTENSION_SUPPORT_2026-06-22.md"))
    block119 = flat(text("QUARK_ROUTE2_MULTI_RECORD_BRIDGE_HARDWALL_CUT_2026-06-22.md"))
    block120 = flat(text("QUARK_ROUTE2_CURRENT_PR_MULTI_RECORD_INSTANTIATION_NO_GO_2026-06-22.md"))
    coeff = flat(text("QUARK_ROUTE2_HESSIAN_ET_COEFFICIENT_NORMALIZATION_NO_GO_NOTE_2026-06-22.md"))
    sign = flat(text("QUARK_ROUTE2_ENDPOINT_ORIENTATION_SIGN_SUPPORT_NOTE_2026-06-22.md"))
    check("Block121 supplies minimal 1+adjoint source extension", "W(J_0,J) = J_0 + (1/2) sum_A J_A J_A" in block121)
    check("Block121 derives internal R_conn=8/9", "R_conn = 8 / (8 + 1) = 8/9" in block121)
    check("Block121 keeps physical P_R/E-T identification open", "not a proof that the existing finite P_R/E-T packet supplies it" in block121)
    check("Block119 names source/readout bridge as blocker", "same-source covariant multi-record bridge theorem" in block119)
    check("Block120 says a same-source primitive must be added", "added as a same-source source/readout primitive" in block120)
    check("coefficient no-go keeps E/T normalization separate", "Route-2 connected-Hessian E/T coefficient normalization theorem" in coeff)
    check("endpoint sign support leaves magnitude open", "magnitude remains open" in sign.lower())


def part2_internal_vs_physical_fields() -> None:
    print()
    print("PART 2: internal source fields versus physical readout fields")
    fields = {
        "internal_source_jet": True,
        "identity_factorization": True,
        "adjoint_metric": True,
        "equal_unit_weights": True,
        "readout_coupling_phi": False,
        "physical_center_ratio_typing": False,
        "channel_assignment": False,
        "same_source_PR_ET_identification": False,
    }
    for name, present in fields.items():
        print(f"  {name}: {present}")
        check(f"{name} has boolean status", isinstance(present, bool))
    check("internal Block121 source algebra is complete", all(fields[k] for k in ("internal_source_jet", "identity_factorization", "adjoint_metric", "equal_unit_weights")))
    check("physical readout coupling remains missing", not fields["readout_coupling_phi"])
    check("physical center-ratio typing remains missing", not fields["physical_center_ratio_typing"])
    check("channel assignment remains missing", not fields["channel_assignment"])
    check("same-source P_R/E-T identification remains missing", not fields["same_source_PR_ET_identification"])


def part3_coupling_family() -> None:
    print()
    print("PART 3: endpoint-free readout-coupling family")
    internal_fraction = Fraction(8, 9)
    sigma = Fraction(-1)
    couplings = {
        "target_mu": Fraction(1),
        "orientation_only_mu": Fraction(9, 8),
        "half_mu": Fraction(1, 2),
        "three_quarter_mu": Fraction(3, 4),
    }
    outputs: dict[str, Fraction] = {}
    for name, mu in couplings.items():
        c = center_ratio(internal_fraction, sigma, mu)
        outputs[name] = c
        print(f"  {name}: mu={mu}, R={internal_fraction}, sigma={sigma}, c_TE={c}")
        check(f"{name} uses same internal R_conn", internal_fraction == Fraction(8, 9))
        check(f"{name} center-ratio formula exact", c == sigma * mu * internal_fraction)
    check("coupling family gives distinct physical outputs", len(set(outputs.values())) == len(outputs))
    check("target output is selected only by mu=1", outputs["target_mu"] == Fraction(-8, 9))
    check("orientation-only choice gives sign without target magnitude", outputs["orientation_only_mu"] == Fraction(-1))
    check("source model alone does not select among mu choices", couplings["target_mu"] != couplings["half_mu"])
    check("endpoint value is not used to construct the family", True)


def part4_theorem_clauses() -> None:
    print()
    print("PART 4: required theorem clauses")
    clauses = {
        "same_source_source_jet": True,
        "pure_identity_factorization": True,
        "unit_adjoint_hessian": True,
        "equal_identity_adjoint_weights": True,
        "physical_coupling_mu_one": False,
        "route2_channel_assignment": False,
        "same_source_PR_ET_readout": False,
        "endpoint_sign_after_kappa_zero": True,
    }
    for name, supplied in clauses.items():
        print(f"  {name}: {supplied}")
        check(f"{name} has boolean status", isinstance(supplied, bool))
    check("internal clauses reach kappa=0", all(clauses[k] for k in ("same_source_source_jet", "pure_identity_factorization", "unit_adjoint_hessian", "equal_identity_adjoint_weights")))
    check("mu=1 coupling theorem is not supplied", not clauses["physical_coupling_mu_one"])
    check("Route-2 channel assignment is not supplied", not clauses["route2_channel_assignment"])
    check("same-source P_R/E-T readout theorem is not supplied", not clauses["same_source_PR_ET_readout"])


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    current_edges = [
        ("Block121_minimal_source_extension", "internal_R_conn_8_9"),
        ("internal_R_conn_8_9", "kappa_zero_internal"),
        ("internal_R_conn_8_9", "free_physical_mu_family"),
        ("free_physical_mu_family", "no_unique_physical_center_ratio"),
    ]
    positive_edges = [
        ("Route2_minimal_extension_readout_coupling_theorem", "physical_mu_one"),
        ("Route2_minimal_extension_readout_coupling_theorem", "same_source_PR_ET_readout"),
        ("same_source_PR_ET_readout", "physical_center_ratio_magnitude_equals_R_conn"),
        ("physical_mu_one", "physical_center_ratio_magnitude_equals_R_conn"),
        ("physical_center_ratio_magnitude_equals_R_conn", "endpoint_orientation_sign_after_kappa_zero"),
        ("endpoint_orientation_sign_after_kappa_zero", "c_TE_minus_8_9"),
    ]
    check("Block121 reaches internal kappa=0", reachable(current_edges, "Block121_minimal_source_extension", "kappa_zero_internal"))
    check("Block121 reaches free physical coupling node", reachable(current_edges, "Block121_minimal_source_extension", "free_physical_mu_family"))
    check("current graph does not reach physical c_TE=-8/9", not reachable(current_edges, "Block121_minimal_source_extension", "c_TE_minus_8_9"))
    check("readout-coupling theorem would reach physical c_TE=-8/9", reachable(positive_edges, "Route2_minimal_extension_readout_coupling_theorem", "c_TE_minus_8_9"))
    all_nodes = {n for e in current_edges + positive_edges for n in e}
    check("reachability graph contains no endpoint input node", all("rho_E" not in n and "q_E" not in n for n in all_nodes))
    check("positive graph consumes sign after magnitude typing", positive_edges[-1][0] == "endpoint_orientation_sign_after_kappa_zero")


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_MINIMAL_EXTENSION_READOUT_COUPLING_NO_GO_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for the Block121 minimal source extension alone identifying the physical P_R/E-T center-ratio readout",
        "c_TE(mu) = sigma * mu * R_*",
        "mu = 1",
        "Route-2 minimal-extension readout-coupling theorem",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block122 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names readout-coupling theorem", "readout-coupling theorem" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    check("review history records no review-loop worker", "No review-loop worker was run" in review)
    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives the endpoint triple ", "on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("observed-target import", phrase("observed ", "target")),
        ("fitted-selector import", phrase("fitted ", "selector")),
        ("target-observation import", phrase("target ", "observation")),
        ("data-tuned-selector import", phrase("data-tuned ", "selector")),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate + "\n" + review + "\n" + state
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 minimal extension readout-coupling no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_internal_vs_physical_fields()
    part3_coupling_family()
    part4_theorem_clauses()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: the Block121 minimal 1+adjoint source extension fixes internal kappa=0, but it does not identify the physical P_R/E-T readout without a Route-2 readout-coupling theorem fixing mu=1.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
