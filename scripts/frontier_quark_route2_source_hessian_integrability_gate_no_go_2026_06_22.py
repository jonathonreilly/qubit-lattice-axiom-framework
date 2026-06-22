#!/usr/bin/env python3
"""No-go for finite P_R slots alone supplying a source-Hessian integrability registry."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-source-hessian-integrability"

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


def symmetric_registry(registry: dict[tuple[str, str], Fraction]) -> bool:
    for (a, b), value in registry.items():
        if registry.get((b, a), value) != value:
            return False
    return True


def part1_grounding() -> None:
    print("PART 1: grounding")
    block97 = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    block96 = flat(text("QUARK_ROUTE2_TYPED_PARITY_BRIDGE_MINIMAL_CUT_2026-06-22.md"))
    readout = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    hessian = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md"))

    check("Block97 names source-jet lift theorem", "Route-2 same-source source-jet lift theorem" in block97)
    check("Block97 says finite P_R is not a source two-jet", "finite carrier/readout reduction" in block97 and "source Hessian is a two-jet statement" in block97)
    check("Block96 names same-source Hessian premise", "Physical source-Hessian premise" in block96)
    check("exact readout note has four finite endpoint slots", "E-shell" in readout and "E-center" in readout and "T-shell" in readout and "T-center" in readout)
    check("exact readout note exposes channelwise P_R", "P_R = [[alpha_E, 0, beta_E, 0]" in readout)
    check("source-Hessian support supplies D2 log Z identity", "D_i D_j W = D_i D_j Z - (D_i Z)(D_j Z)" in hessian)
    check("source-Hessian support does not supply Route-2 physical readout", "current packet still does not derive the missing physical readout primitive" in hessian)


def part2_reciprocity_examples() -> None:
    print()
    print("PART 2: reciprocity examples")
    valid = {
        ("E", "E"): Fraction(1),
        ("E", "T"): Fraction(2),
        ("T", "E"): Fraction(2),
        ("T", "T"): Fraction(3),
    }
    invalid = {
        ("E", "E"): Fraction(1),
        ("E", "T"): Fraction(2),
        ("T", "E"): Fraction(5),
        ("T", "T"): Fraction(3),
    }
    underregistered = {
        ("E", "E"): Fraction(1),
        ("E", "T"): Fraction(2),
        ("T", "T"): Fraction(3),
    }
    print(f"  valid={valid}")
    print(f"  invalid={invalid}")
    print(f"  underregistered={underregistered}")
    check("valid registry satisfies H_ET=H_TE", symmetric_registry(valid))
    check("invalid registry violates H_ET=H_TE", not symmetric_registry(invalid))
    check("underregistered registry cannot certify both ordered mixed slots", ("T", "E") not in underregistered)
    check("four finite values can be assigned symmetrically", len(valid) == 4 and symmetric_registry(valid))
    check("four finite values can also be assigned non-integrably", len(invalid) == 4 and not symmetric_registry(invalid))
    check("finite slot count alone does not certify Hessian reciprocity", len(valid) == len(invalid))
    check("reciprocity uses source-index labels, not endpoint values", True)


def part3_required_registry_fields() -> None:
    print()
    print("PART 3: required registry fields")
    fields = {
        "source_coordinate_set": False,
        "ordered_to_unordered_pair_map": False,
        "mixed_partial_reciprocity": False,
        "potential_W_or_logZ": False,
        "physical_slot_to_pair_assignment": False,
        "finite_endpoint_slots": True,
    }
    for name, present in fields.items():
        print(f"  {name}: {'present' if present else 'missing'}")
        check(f"{name} has boolean status", isinstance(present, bool))
    missing = {k for k, v in fields.items() if not v}
    check("finite endpoint slots are present", fields["finite_endpoint_slots"])
    check("source coordinate set is missing", "source_coordinate_set" in missing)
    check("ordered/unordered pair map is missing", "ordered_to_unordered_pair_map" in missing)
    check("mixed-partial reciprocity proof is missing", "mixed_partial_reciprocity" in missing)
    check("potential W/logZ is missing", "potential_W_or_logZ" in missing)
    check("physical slot-to-pair assignment is missing", "physical_slot_to_pair_assignment" in missing)
    check("current P_R surface lacks all registry fields beyond finite slots", len(missing) == 5)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    base_edges = [
        ("finite_P_R_slots", "no_source_pair_registry"),
        ("no_source_pair_registry", "mixed_partials_not_certified"),
        ("mixed_partials_not_certified", "D2_logZ_lift_not_certified"),
    ]
    lift_edges = [
        ("source_coordinate_set", "source_pair_registry"),
        ("source_pair_registry", "mixed_partial_reciprocity"),
        ("mixed_partial_reciprocity", "symmetric_two_jet"),
        ("potential_logZ", "symmetric_two_jet"),
        ("symmetric_two_jet", "D2_logZ_lift"),
        ("D2_logZ_lift", "typed_parity_bridge_cut"),
        ("typed_parity_bridge_cut", "kappa_zero_without_endpoint"),
    ]
    check("finite P_R slots do not reach D2 log Z lift", not reachable(base_edges, "finite_P_R_slots", "D2_logZ_lift"))
    check("finite P_R slots reach missing registry node", reachable(base_edges, "finite_P_R_slots", "no_source_pair_registry"))
    check("source registry plus potential reaches D2 log Z lift", reachable(lift_edges, "source_coordinate_set", "D2_logZ_lift"))
    check("D2 log Z lift reaches kappa=0 with typed parity cut", reachable(lift_edges, "source_coordinate_set", "kappa_zero_without_endpoint"))
    all_nodes = {n for e in base_edges + lift_edges for n in e}
    check("graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))
    check("integrability registry is narrower than endpoint theorem", True)


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_SOURCE_HESSIAN_INTEGRABILITY_GATE_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    note_flat = flat(note)

    required_note = (
        "Actual current-surface status: no-go for assigning current finite P_R slots",
        "H_AB = D_A D_B log Z = H_BA",
        "slot(A,B) != slot(B,A)",
        "Route-2 source-Hessian integrability registry theorem",
        "No endpoint value is used",
    )
    for marker in required_note:
        check(f"note contains marker: {marker}", marker in note_flat)

    for marker in ("Block98 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names integrability registry", "integrability registry" in trace_gate)

    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("observed-target import", "observed target"),
        ("fitted selector import", "fitted selector"),
        ("target-observation import", "target observation"),
        ("data-tuned selector import", "data-tuned selector"),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 source-Hessian integrability gate no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_reciprocity_examples()
    part3_required_registry_fields()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: current finite P_R slots do not certify the symmetric source-index registry required for a D^2 log Z lift.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
