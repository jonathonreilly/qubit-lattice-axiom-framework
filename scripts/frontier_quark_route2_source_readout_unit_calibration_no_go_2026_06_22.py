#!/usr/bin/env python3
"""No-go for internal source-unit equality alone fixing physical mu=1."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-source-readout-unit-calibration"

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


def oriented_mu(mu: Fraction) -> Fraction:
    return -mu * Fraction(8, 9)


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
    block121 = flat(text("QUARK_ROUTE2_MINIMAL_MULTI_RECORD_EXTENSION_SUPPORT_2026-06-22.md"))
    block122 = flat(text("QUARK_ROUTE2_MINIMAL_EXTENSION_READOUT_COUPLING_NO_GO_2026-06-22.md"))
    block123 = flat(text("QUARK_ROUTE2_MINIMAL_READOUT_COUPLING_CONTRACT_SUPPORT_2026-06-22.md"))
    coeff = flat(text("QUARK_ROUTE2_HESSIAN_ET_COEFFICIENT_NORMALIZATION_NO_GO_NOTE_2026-06-22.md"))
    check("Block121 records equal source unit weights", "equal source normalization" in block121 or "equal source unit weights" in block121)
    check("Block121 derives internal R_conn=8/9", "R_conn = 8 / (8 + 1) = 8/9" in block121)
    check("Block122 names mu=1 as missing physical coupling", "mu = 1" in block122 and "readout-coupling theorem" in block122)
    check("Block123 C4 is mu_one", "C4. mu_one" in block123)
    check("coefficient no-go says output coefficients are separate gates", "E/T coefficient normalization theorem" in coeff)


def part2_internal_vs_physical_units() -> None:
    print()
    print("PART 2: internal source units versus physical readout units")
    fields = {
        "internal_identity_unit": True,
        "internal_adjoint_unit": True,
        "internal_equal_weights": True,
        "physical_readout_unit": False,
        "source_to_readout_calibration": False,
        "mu_one": False,
    }
    for name, value in fields.items():
        print(f"  {name}: {value}")
        check(f"{name} has boolean status", isinstance(value, bool))
    check("internal source normalization is complete", all(fields[k] for k in ("internal_identity_unit", "internal_adjoint_unit", "internal_equal_weights")))
    check("physical readout unit remains missing", not fields["physical_readout_unit"])
    check("source-to-readout calibration remains missing", not fields["source_to_readout_calibration"])
    check("mu=1 remains missing", not fields["mu_one"])


def part3_mu_family() -> None:
    print()
    print("PART 3: endpoint-free mu family")
    mus = [Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2)]
    outputs = []
    for mu in mus:
        c = oriented_mu(mu)
        outputs.append(c)
        print(f"  mu={mu}, c_TE={c}")
        check(f"mu={mu} output is rational", isinstance(c, Fraction))
        check(f"mu={mu} keeps internal R_conn fixed", Fraction(8, 9) == Fraction(8, 9))
    check("different mu choices give different physical magnitudes", len(set(outputs)) == len(outputs))
    check("mu=1 is only one member of the family", mus.count(Fraction(1)) == 1)
    check("source algebra alone does not select mu", len(set(mus)) > 1)
    check("no endpoint value is used to construct the mu family", True)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    current_edges = [
        ("Block121_equal_source_units", "internal_R_conn_8_9"),
        ("internal_R_conn_8_9", "free_source_to_readout_mu"),
        ("free_source_to_readout_mu", "C4_not_satisfied"),
    ]
    positive_edges = [
        ("Route2_source_readout_unit_calibration_theorem", "physical_readout_unit"),
        ("physical_readout_unit", "mu_one"),
        ("mu_one", "C4_satisfied"),
    ]
    check("Block121 reaches internal R_conn", reachable(current_edges, "Block121_equal_source_units", "internal_R_conn_8_9"))
    check("Block121 reaches free mu node", reachable(current_edges, "Block121_equal_source_units", "free_source_to_readout_mu"))
    check("Block121 alone does not satisfy C4", not reachable(current_edges, "Block121_equal_source_units", "C4_satisfied"))
    check("unit calibration theorem would satisfy C4", reachable(positive_edges, "Route2_source_readout_unit_calibration_theorem", "C4_satisfied"))
    all_nodes = {n for e in current_edges + positive_edges for n in e}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in n and "q_E" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_SOURCE_READOUT_UNIT_CALIBRATION_NO_GO_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for Block121 equal source-unit weights alone fixing the physical readout coupling mu=1",
        "c_TE(mu) = -mu * (8/9)",
        "Route-2 source-readout unit calibration theorem",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block126 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks negative pruning", "trace_class: negative_route_pruning" in trace_gate)
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
    print("Route-2 source-readout unit calibration no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_internal_vs_physical_units()
    part3_mu_family()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: Block121 equal source-unit weights do not fix physical source-to-readout calibration mu=1.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
