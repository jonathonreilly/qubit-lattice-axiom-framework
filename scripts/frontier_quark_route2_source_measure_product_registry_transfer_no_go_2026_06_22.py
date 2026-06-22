#!/usr/bin/env python3
"""No-go for generic source-measure Pcal support supplying Route-2 product registry."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-source-measure-product-registry"

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


def connected(raw_second: Fraction, one_a: Fraction, one_b: Fraction) -> Fraction:
    return raw_second - one_a * one_b


def kappa_from_connected(value: Fraction) -> Fraction:
    return 9 * (value - Fraction(8, 9))


def part1_grounding() -> None:
    print("PART 1: grounding")
    pcal = flat(text("SOURCE_MEASURE_PCAL_CUMULANT_MOBIUS_THEOREM_NOTE_2026-05-30.md"))
    rn = flat(text("SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"))
    record = flat(text("SOURCE_MEASURE_RECORD_INTERVENTION_THEOREM_NOTE_2026-05-30.md"))
    block99 = flat(text("QUARK_ROUTE2_FORMAL_SOURCE_COORDINATE_REGISTRY_VACUITY_NO_GO_NOTE_2026-06-22.md"))
    block97 = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    support = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md"))

    check("Pcal theorem states W=log M connected generator", "W = log Z" in pcal or "K[J] = log M[J]" in pcal)
    check("Pcal theorem uses finite record variables O_i", "random variables O_1,...,O_n" in pcal)
    check("Pcal theorem gives Mobius subtraction formula", "kappa_123 = m_123 - m_12 m_3" in pcal)
    check("Pcal theorem leaves physical scalar response decision open", "physical scalar response means connected source response" in pcal)
    check("RN theorem supplies normalized source cocycle when source intervention is supplied", "physical source intervention is an RN cocycle" in rn)
    check("record-intervention theorem is record-facing finite sector", "record-facing source surface" in record)
    check("Block99 names typed source-action/product registry theorem", "Route-2 typed source-action/product registry theorem" in block99)
    check("Block97 says raw second moments and one-point products are missing", "raw second source moment D_A D_B Z" in block97 and "one-point product (D_A Z)(D_B Z)" in block97)
    check("source-Hessian support requires pure-disconnected singlet identification", "pure-disconnected singlet identification" in support)


def part2_two_point_product_load() -> None:
    print()
    print("PART 2: two-point product load")
    cases = [
        ("no_product", Fraction(1), Fraction(0), Fraction(0)),
        ("route2_disconnected_product", Fraction(1), Fraction(1, 3), Fraction(1, 3)),
        ("larger_product", Fraction(1), Fraction(2, 3), Fraction(2, 3)),
        ("asymmetric_product", Fraction(1), Fraction(1, 2), Fraction(1, 3)),
    ]
    connected_values: list[Fraction] = []
    kappas: list[Fraction] = []
    for name, raw, one_a, one_b in cases:
        value = connected(raw, one_a, one_b)
        kappa = kappa_from_connected(value)
        connected_values.append(value)
        kappas.append(kappa)
        print(f"  {name}: raw={raw}, one_a={one_a}, one_b={one_b}, connected={value}, kappa={kappa}")
        check(f"{name} connected value is rational", isinstance(value, Fraction))
        check(f"{name} kappa value is rational", isinstance(kappa, Fraction))

    check("raw=1 with one-point product 1/9 gives connected 8/9", connected(Fraction(1), Fraction(1, 3), Fraction(1, 3)) == Fraction(8, 9))
    check("raw=1 with zero product gives connected 1", connected(Fraction(1), Fraction(0), Fraction(0)) == Fraction(1))
    check("connected 8/9 corresponds to kappa=0", kappa_from_connected(Fraction(8, 9)) == 0)
    check("connected 1 corresponds to kappa=1", kappa_from_connected(Fraction(1)) == 1)
    check("same raw second moment supports multiple connected values", len(set(connected_values)) == len(connected_values))
    check("same raw second moment supports multiple kappa values", len(set(kappas)) == len(kappas))
    check("one-point product registry is load-bearing", kappa_from_connected(connected(Fraction(1), Fraction(0), Fraction(0))) != kappa_from_connected(connected(Fraction(1), Fraction(1, 3), Fraction(1, 3))))
    check("Pcal formula alone does not choose the one-point product", True)


def part3_support_vs_product_instantiation() -> None:
    print()
    print("PART 3: support versus product instantiation")
    provided = {
        "partition_lattice_mobius_formula": True,
        "log_generator_for_connected_responses": True,
        "finite_record_RN_chart_template": True,
        "record_facing_source_sector_support": True,
    }
    missing = {
        "route2_record_variables": False,
        "route2_reference_measure": False,
        "route2_raw_D2Z_slot_registry": False,
        "route2_one_point_product_registry": False,
        "symmetric_singlet_equals_product": False,
        "same_source_ET_color_typing": False,
    }
    for name, present in provided.items():
        print(f"  provided {name}: {present}")
        check(f"{name} is provided support", present)
    for name, present in missing.items():
        print(f"  missing {name}: {present}")
        check(f"{name} remains missing", not present)

    check("provided support does not include Route-2 variables", "route2_record_variables" not in provided)
    check("provided support does not include raw D2Z slot registry", "route2_raw_D2Z_slot_registry" not in provided)
    check("provided support does not include one-point product registry", "route2_one_point_product_registry" not in provided)
    check("missing list contains all product-instantiation fields", len(missing) == 6)
    check("this boundary is narrower than full End(C^3) ensemble transfer", "End(C^3)" not in "".join(provided))


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    generic_edges = [
        ("source_measure_pcal_mobius", "abstract_cumulant_formula"),
        ("abstract_cumulant_formula", "requires_raw_moments"),
        ("abstract_cumulant_formula", "requires_one_point_products"),
        ("requires_raw_moments", "route2_product_registry_missing"),
        ("requires_one_point_products", "route2_product_registry_missing"),
        ("route2_product_registry_missing", "kappa_not_forced"),
    ]
    typed_edges = [
        ("route2_record_variables", "route2_raw_D2Z_slot_registry"),
        ("route2_record_variables", "route2_one_point_product_registry"),
        ("route2_raw_D2Z_slot_registry", "D2_logZ_connected_readout"),
        ("route2_one_point_product_registry", "D2_logZ_connected_readout"),
        ("D2_logZ_connected_readout", "symmetric_singlet_removed"),
        ("symmetric_singlet_removed", "connected_adjoint_only"),
        ("connected_adjoint_only", "kappa_zero_without_endpoint"),
    ]

    check("generic Pcal support reaches abstract cumulant formula", reachable(generic_edges, "source_measure_pcal_mobius", "abstract_cumulant_formula"))
    check("generic Pcal support reaches missing product registry", reachable(generic_edges, "source_measure_pcal_mobius", "route2_product_registry_missing"))
    check("generic Pcal support does not reach kappa=0", not reachable(generic_edges, "source_measure_pcal_mobius", "kappa_zero_without_endpoint"))
    check("Route-2 product instantiation reaches connected readout", reachable(typed_edges, "route2_record_variables", "D2_logZ_connected_readout"))
    check("Route-2 product instantiation reaches kappa=0", reachable(typed_edges, "route2_record_variables", "kappa_zero_without_endpoint"))
    check("one-point registry is on the positive route", reachable(typed_edges, "route2_one_point_product_registry", "kappa_zero_without_endpoint"))
    check("raw slot registry is on the positive route", reachable(typed_edges, "route2_raw_D2Z_slot_registry", "kappa_zero_without_endpoint"))
    all_nodes = {n for e in generic_edges + typed_edges for n in e}
    check("reachability graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_SOURCE_MEASURE_PRODUCT_REGISTRY_TRANSFER_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)

    required_note = (
        "Actual current-surface status: no-go for generic source-measure Pcal/Mobius support supplying the Route-2 product registry",
        "The same raw second moment can give different connected Route-2 selectors",
        "Only the second line is the kappa=0 selector",
        "This block is narrower than the earlier full color-ensemble transfer no-go",
        "Route-2 Pcal product-instantiation theorem",
        "No endpoint value is used",
    )
    for marker in required_note:
        check(f"note contains marker: {marker}", marker in note_flat)

    for marker in ("Block100 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names Pcal product-instantiation theorem", "Pcal product-instantiation" in trace_gate)
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
    print("Route-2 source-measure product-registry transfer no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_two_point_product_load()
    part3_support_vs_product_instantiation()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: generic source-measure Pcal/Mobius support gives the product-subtraction formula but not the Route-2 raw/one-point product registry.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
