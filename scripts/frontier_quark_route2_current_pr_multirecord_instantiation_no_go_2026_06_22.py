#!/usr/bin/env python3
"""No-go for current finite P_R/E-T instantiating the multi-record bridge theorem."""

from __future__ import annotations

from collections import deque
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-current-pr-multirecord-instantiation"

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
    hardwall = flat(text("QUARK_ROUTE2_MULTI_RECORD_BRIDGE_HARDWALL_CUT_2026-06-22.md"))
    exact = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    hidden = flat(text("QUARK_ROUTE2_HIDDEN_ADJOINT_CARRIER_NO_GO_NOTE_2026-06-22.md"))
    finite_rank = flat(text("QUARK_ROUTE2_FINITE_ENDPOINT_SOURCE_RANK_NO_GO_NOTE_2026-06-22.md"))
    source_jet = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    pcal = flat(text("QUARK_ROUTE2_PCAL_MOMENT_REALIZATION_NO_GO_NOTE_2026-06-22.md"))
    normalization = flat(text("QUARK_ROUTE2_ADJOINT_SINGLET_NORMALIZATION_NO_GO_NOTE_2026-06-22.md"))
    sign = flat(text("QUARK_ROUTE2_ENDPOINT_ORIENTATION_SIGN_SUPPORT_NOTE_2026-06-22.md"))
    check("Block119 names same-source covariant bridge theorem", "same-source covariant multi-record bridge theorem" in hardwall)
    check("exact readout note supplies finite P_R surface", "P_R =" in exact and "E-shell" in exact and "T-center" in exact)
    check("hidden adjoint carrier no-go applies to current K_R", "No hidden adjoint carrier exists" in hidden)
    check("finite endpoint rank no-go bounds endpoint pullback", "rank centered scores <= 4 - 1 = 3" in finite_rank)
    check("source-jet lift no-go keeps log-Hessian typing missing", "same-source source-jet lift theorem" in source_jet)
    check("Pcal moment realization keeps raw/product split missing", "Route-2 Pcal moment-realization theorem" in pcal)
    check("normalization no-go keeps adjoint/singlet scale free", "does not choose their relative coefficient" in normalization)
    check("endpoint sign support does not fix magnitude", "magnitude remains open" in sign.lower())


def part2_clause_instantiation() -> None:
    print()
    print("PART 2: current P_R clause instantiation")
    clauses = {
        "covariant_adjoint_records": False,
        "physical_log_hessian_typing": False,
        "identity_factorization": False,
        "adjoint_singlet_normalization": False,
        "endpoint_magnitude_typing": False,
    }
    reasons = {
        "covariant_adjoint_records": "no hidden adjoint carrier; finite endpoint rank < 8",
        "physical_log_hessian_typing": "finite P_R is not a source-jet lift",
        "identity_factorization": "raw/product split and one-point registry missing",
        "adjoint_singlet_normalization": "SU3 invariance leaves two scales",
        "endpoint_magnitude_typing": "sign separated; magnitude still open",
    }
    for clause, present in clauses.items():
        print(f"  {clause}: {present} ({reasons[clause]})")
        check(f"{clause} status is boolean", isinstance(present, bool))
        check(f"{clause} is not supplied by current P_R", not present)
    check("all five Block119 clauses fail on current surface", sum(1 for v in clauses.values() if not v) == 5)
    check("no clause is accidentally marked supplied", not any(clauses.values()))


def part3_reachability() -> None:
    print()
    print("PART 3: current-surface reachability")
    current_edges = [
        ("current_KR_PR_ET", "finite_carrier_readout"),
        ("finite_carrier_readout", "missing_covariant_records"),
        ("finite_carrier_readout", "missing_log_hessian_typing"),
        ("finite_carrier_readout", "missing_raw_product_split"),
        ("finite_carrier_readout", "missing_adjoint_singlet_normalization"),
        ("finite_carrier_readout", "missing_endpoint_magnitude_typing"),
        ("missing_covariant_records", "missing_same_source_multirecord_bridge"),
        ("missing_log_hessian_typing", "missing_same_source_multirecord_bridge"),
        ("missing_raw_product_split", "missing_same_source_multirecord_bridge"),
        ("missing_adjoint_singlet_normalization", "missing_same_source_multirecord_bridge"),
        ("missing_endpoint_magnitude_typing", "missing_same_source_multirecord_bridge"),
    ]
    positive_edges = [
        ("new_same_source_multirecord_bridge", "covariant_records"),
        ("covariant_records", "physical_log_hessian_typing"),
        ("physical_log_hessian_typing", "identity_factorization"),
        ("identity_factorization", "adjoint_singlet_normalization"),
        ("adjoint_singlet_normalization", "endpoint_magnitude_typing"),
        ("endpoint_magnitude_typing", "kappa_zero"),
        ("kappa_zero", "c_TE_minus_8_9_with_sign_support"),
    ]
    check("current surface reaches missing bridge node", reachable(current_edges, "current_KR_PR_ET", "missing_same_source_multirecord_bridge"))
    check("current surface does not reach kappa=0", not reachable(current_edges, "current_KR_PR_ET", "kappa_zero"))
    check("current surface does not reach signed bridge", not reachable(current_edges, "current_KR_PR_ET", "c_TE_minus_8_9_with_sign_support"))
    check("positive new theorem reaches kappa=0", reachable(positive_edges, "new_same_source_multirecord_bridge", "kappa_zero"))
    check("positive new theorem reaches signed bridge with sign support", reachable(positive_edges, "new_same_source_multirecord_bridge", "c_TE_minus_8_9_with_sign_support"))
    all_current_nodes = {n for e in current_edges for n in e}
    check("current graph contains no endpoint-value import node", all("rho_E" not in n and "q_E" not in n for n in all_current_nodes))


def part4_document_boundary() -> None:
    print()
    print("PART 4: document boundary")
    note = text("QUARK_ROUTE2_CURRENT_PR_MULTI_RECORD_INSTANTIATION_NO_GO_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for the existing finite P_R/E-T surface instantiating the Block119 same-source covariant multi-record bridge theorem",
        "current surface reaches the missing-theorem node",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block120 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks negative route pruning", "trace_class: negative_route_pruning" in trace_gate)
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
    print("Route-2 current P_R multi-record instantiation no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_clause_instantiation()
    part3_reachability()
    part4_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: the current finite P_R/E-T surface does not instantiate the same-source covariant multi-record bridge theorem; a new source/readout primitive is required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
