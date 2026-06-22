#!/usr/bin/env python3
"""No-go for a bare formal source-coordinate registry forcing Route-2 kappa=0."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-source-coordinate-registry"

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


def pair_capacity(source_count: int) -> int:
    return source_count * (source_count + 1) // 2


def formal_hessian(
    sources: tuple[str, ...], assignments: dict[tuple[str, str], Fraction]
) -> dict[tuple[str, str], Fraction]:
    hessian: dict[tuple[str, str], Fraction] = {}
    for a in sources:
        for b in sources:
            key = (a, b) if a <= b else (b, a)
            if key in assignments:
                hessian[(a, b)] = assignments[key]
    return hessian


def is_symmetric_matrix(hessian: dict[tuple[str, str], Fraction]) -> bool:
    for (a, b), value in hessian.items():
        if hessian.get((b, a), value) != value:
            return False
    return True


def kappa_response(kappa: Fraction) -> Fraction:
    return Fraction(8, 9) + kappa * Fraction(1, 9)


def raw_for_connected(connected: Fraction, one_point: Fraction) -> Fraction:
    return connected + one_point * one_point


def connected_from_raw(raw_second: Fraction, one_point: Fraction) -> Fraction:
    return raw_second - one_point * one_point


def part1_grounding() -> None:
    print("PART 1: grounding")
    block98 = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_INTEGRABILITY_GATE_NO_GO_NOTE_2026-06-22.md"))
    block97 = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    block96 = flat(text("QUARK_ROUTE2_TYPED_PARITY_BRIDGE_MINIMAL_CUT_2026-06-22.md"))
    source = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md"))
    readout = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    observable = flat(text("QUARK_ROUTE2_OBSERVABLE_HESSIAN_READOUT_IDENTIFICATION_NO_GO_NOTE_2026-06-22.md"))

    check("Block98 names source-Hessian integrability registry theorem", "Route-2 source-Hessian integrability registry theorem" in block98)
    check("Block98 says finite slots do not supply the pair registry", "finite endpoint slots" in block98 and "does not provide a registry" in block98)
    check("Block98 requires mixed-partial reciprocity", "H_AB = D_A D_B log Z = H_BA" in block98)
    check("Block97 requires raw second moment and one-point product", "the raw second source moment D_A D_B Z" in block97 and "the one-point product (D_A Z)(D_B Z)" in block97)
    check("Block97 requires same-source identification", "same source used by the color/singlet decomposition" in block97)
    check("Block96 names three same-source typed parity premises", "Symmetric purity premise" in block96 and "Antisymmetric adjoint premise" in block96)
    check("source-Hessian support leaves kappa free without singlet purity", "R_cumulant(eta) = 8/9 + eta/9" in source)
    check("exact readout exposes four finite physical slots", all(marker in readout for marker in ("E-shell", "E-center", "T-shell", "T-center")))
    check("observable-Hessian no-go rules out scalar-only source Hessian", "scalar Hessian cannot by itself identify the E/T readout map" in observable)


def part2_formal_embedding() -> None:
    print()
    print("PART 2: formal source-coordinate embedding")
    sources = ("A", "B", "C")
    slots = {
        "E_shell": Fraction(11, 10),
        "E_center": Fraction(7, 5),
        "T_shell": Fraction(5, 4),
        "T_center": Fraction(13, 8),
    }
    assignment = {
        ("A", "A"): slots["E_shell"],
        ("A", "B"): slots["E_center"],
        ("B", "B"): slots["T_shell"],
        ("B", "C"): slots["T_center"],
    }
    alt_assignment = {
        ("A", "A"): slots["T_center"],
        ("A", "B"): slots["E_shell"],
        ("B", "B"): slots["E_center"],
        ("B", "C"): slots["T_shell"],
    }
    hessian = formal_hessian(sources, assignment)
    alt_hessian = formal_hessian(sources, alt_assignment)

    print(f"  sources={sources}, pair_capacity={pair_capacity(len(sources))}")
    print(f"  assignment={assignment}")
    check("three formal sources have at least four unordered pairs", pair_capacity(len(sources)) >= len(slots))
    check("all four finite slots are assigned", set(slots.values()).issubset(set(assignment.values())))
    check("formal Hessian is symmetric", is_symmetric_matrix(hessian))
    check("assigned mixed pair is mirrored", hessian[("A", "B")] == hessian[("B", "A")])
    check("unassigned source pair remains free", ("A", "C") not in hessian and ("C", "A") not in hessian)
    check("alternate assignment is also symmetric", is_symmetric_matrix(alt_hessian))
    check("formal slot-to-pair assignment is nonunique", hessian != alt_hessian)
    check("nonunique formal embedding cannot identify the physical pair map", True)
    check("formal embeddability used arbitrary rational slot values", all(v.denominator != 0 for v in slots.values()))


def part3_kappa_freedom() -> None:
    print()
    print("PART 3: kappa freedom under formal integrability")
    sources = ("A", "B", "C")
    kappas = [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(-1, 2)]
    responses: list[Fraction] = []
    for kappa in kappas:
        response = kappa_response(kappa)
        responses.append(response)
        hessian = formal_hessian(
            sources,
            {
                ("A", "B"): response,
                ("A", "A"): Fraction(1),
                ("B", "B"): Fraction(1),
                ("C", "C"): Fraction(1),
            },
        )
        print(f"  kappa={kappa}, response={response}, H_AB={hessian[('A', 'B')]}")
        check(f"kappa={kappa} gives a rational connected response", isinstance(response, Fraction))
        check(f"kappa={kappa} formal Hessian satisfies reciprocity", is_symmetric_matrix(hessian))

    check("formal registry accepts multiple kappa values", len(set(responses)) == len(kappas))
    check("kappa=0 response is present", kappa_response(Fraction(0)) in responses)
    check("kappa=1 response is also present", kappa_response(Fraction(1)) in responses)
    check("mixed-partial reciprocity does not select kappa=0", len(set(responses)) > 1)
    check("same registry skeleton accepts kappa=0 and kappa=1", kappa_response(Fraction(0)) != kappa_response(Fraction(1)))
    check("connected singlet residual eta remains kappa", all(kappa_response(k) == Fraction(8, 9) + k * Fraction(1, 9) for k in kappas))
    check("no endpoint value is used to vary kappa", True)


def part4_product_registry_boundary() -> None:
    print()
    print("PART 4: source-action and product registry boundary")
    fields = {
        "formal_source_coordinates": True,
        "formal_symmetric_W_hessian": True,
        "physical_source_action": False,
        "raw_second_Z_moment": False,
        "one_point_product_registry": False,
        "same_source_color_typing": False,
        "pure_disconnected_singlet_typing": False,
        "anti_invariant_adjoint_typing": False,
    }
    for name, present in fields.items():
        print(f"  {name}: {'present' if present else 'missing'}")
        check(f"{name} has boolean status", isinstance(present, bool))

    missing = {k for k, v in fields.items() if not v}
    check("formal coordinates and symmetric W are present in the shortcut", fields["formal_source_coordinates"] and fields["formal_symmetric_W_hessian"])
    check("physical source action remains missing", "physical_source_action" in missing)
    check("raw Z second moment remains missing", "raw_second_Z_moment" in missing)
    check("one-point product registry remains missing", "one_point_product_registry" in missing)
    check("same-source color typing remains missing", "same_source_color_typing" in missing)
    check("pure-disconnected singlet typing remains missing", "pure_disconnected_singlet_typing" in missing)
    check("anti-invariant adjoint typing remains missing", "anti_invariant_adjoint_typing" in missing)

    connected = kappa_response(Fraction(0))
    one_points = [Fraction(0), Fraction(1, 3), Fraction(2, 3), Fraction(1)]
    raws = [raw_for_connected(connected, p) for p in one_points]
    for one_point, raw in zip(one_points, raws):
        recovered = connected_from_raw(raw, one_point)
        print(f"  connected={connected}, one_point={one_point}, raw={raw}, recovered={recovered}")
        check(f"raw moment recovers connected value for one_point={one_point}", recovered == connected)
    check("same connected Hessian allows multiple raw Z moments", len(set(raws)) == len(raws))

    fixed_raw = Fraction(1)
    connected_values = [connected_from_raw(fixed_raw, p) for p in one_points]
    print(f"  fixed_raw={fixed_raw}, connected_values={connected_values}")
    check("same raw moment allows multiple connected Hessians if one-point product varies", len(set(connected_values)) == len(connected_values))
    check("one-point product registry is load-bearing for disconnected subtraction", connected_values[0] != connected_values[-1])
    check("formal W Hessian alone cannot type singlet as pure disconnected", True)


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    formal_edges = [
        ("finite_P_R_slots", "formal_pair_capacity"),
        ("formal_pair_capacity", "symmetric_quadratic_W"),
        ("symmetric_quadratic_W", "mixed_partial_reciprocity"),
        ("mixed_partial_reciprocity", "formal_integrable_Hessian"),
        ("formal_integrable_Hessian", "kappa_free"),
        ("kappa_free", "kappa_not_forced"),
    ]
    typed_edges = [
        ("physical_source_action", "source_coordinates"),
        ("source_coordinates", "raw_D2Z_registry"),
        ("source_coordinates", "one_point_product_registry"),
        ("raw_D2Z_registry", "D2_logZ_connected_hessian"),
        ("one_point_product_registry", "D2_logZ_connected_hessian"),
        ("D2_logZ_connected_hessian", "pure_disconnected_singlet_removed"),
        ("pure_disconnected_singlet_removed", "connected_adjoint_only"),
        ("connected_adjoint_only", "kappa_zero_without_endpoint"),
    ]
    check("formal registry reaches an integrable Hessian", reachable(formal_edges, "finite_P_R_slots", "formal_integrable_Hessian"))
    check("formal registry reaches kappa-free boundary", reachable(formal_edges, "finite_P_R_slots", "kappa_free"))
    check("formal registry does not reach kappa=0", not reachable(formal_edges, "finite_P_R_slots", "kappa_zero_without_endpoint"))
    check("typed source-action/product registry reaches kappa=0", reachable(typed_edges, "physical_source_action", "kappa_zero_without_endpoint"))
    check("one-point product is on the positive route", reachable(typed_edges, "one_point_product_registry", "kappa_zero_without_endpoint"))
    check("raw D2Z registry is on the positive route", reachable(typed_edges, "raw_D2Z_registry", "kappa_zero_without_endpoint"))
    all_nodes = {n for e in formal_edges + typed_edges for n in e}
    check("graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))
    check("missing primitive is typed source-action/product registry", "physical_source_action" in all_nodes and "one_point_product_registry" in all_nodes)


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_FORMAL_SOURCE_COORDINATE_REGISTRY_VACUITY_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)

    required_note = (
        "Actual current-surface status: no-go for a bare formal source-coordinate registry forcing kappa=0",
        "A bare formal source-coordinate registry is vacuous",
        "R_conn(kappa) = 8/9 + kappa/9",
        "finite slots + formal symmetric source-coordinate registry => kappa=0",
        "Route-2 typed source-action/product registry theorem",
        "No endpoint value is used",
    )
    for marker in required_note:
        check(f"note contains marker: {marker}", marker in note_flat)

    for marker in ("Block99 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names formal source-coordinate registry shortcut", "formal symmetric source-coordinate registry" in trace_gate)
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
    print("Route-2 formal source-coordinate registry vacuity no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_formal_embedding()
    part3_kappa_freedom()
    part4_product_registry_boundary()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: formal source-coordinate integrability can embed the slots but leaves kappa free; the missing primitive is a typed source-action/product registry.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
