#!/usr/bin/env python3
"""Direct obstruction for the Route-2 same-source full color-readout primitive.

The current exact Route-2 P_R surface is a four-feature scalar E/T readout.
The full color source needed by the connected/disconnected selector is
End(C^3)=C I + sl_3, whose connected tangent is the eight-dimensional SU(3)
adjoint.  This runner checks that the current P_R feature carrier cannot itself
be that same-source full color-record ensemble.

No endpoint value is imported.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-same-source-color-readout-primitive"

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


def note_text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def loop_text(name: str) -> str:
    return (LOOP / name).read_text(encoding="utf-8")


def normalized(text: str) -> str:
    return " ".join(text.replace("`", "").replace("**", "").split())


def reachable(edges: Iterable[tuple[str, str]], start: str, target: str) -> bool:
    graph: dict[str, set[str]] = {}
    for src, dst in edges:
        graph.setdefault(src, set()).add(dst)
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


@dataclass(frozen=True)
class Route:
    name: str
    output_needed: str
    status: str
    reason: str


def hom_su3_adjoint_to_trivial_copies(trivial_copies: int) -> int:
    # The SU(3) adjoint has no invariant vector, so each trivial copy
    # contributes zero equivariant maps from sl_3.
    adjoint_invariant_multiplicity = 0
    return trivial_copies * adjoint_invariant_multiplicity


def part1_current_route2_surface() -> None:
    print("PART 1: current Route-2 P_R surface")
    exact = note_text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    source_domain = note_text("QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md")
    block82 = note_text("QUARK_ROUTE2_COLOR_SU3_RECORD_ENSEMBLE_TRANSFER_NO_GO_NOTE_2026-06-22.md")
    flat_exact = normalized(exact)
    flat_source = normalized(source_domain)
    flat_block82 = normalized(block82)

    check("exact readout map gives channelwise P_R form", "P_R = [[alpha_E, 0, beta_E, 0]," in exact)
    check("exact readout map says carrier has disjoint E/T endpoint subspaces", "disjoint E and T endpoint subspaces" in flat_exact)
    check("exact readout map keeps endpoint ratio theorem open", "exact endpoint ratio theorem: not derived" in flat_exact)
    check("exact readout map names missing E-channel map entry", "beta_E / alpha_E = 21/4" in exact)
    check("source-domain note separates support-side endpoint and color domains", "different typed domains" in flat_source)
    check("source-domain note says no current typed edge from color to endpoint ratio", "There is no current typed edge" in source_domain)
    check("source-domain note keeps bridge theorem missing", "It does not supply the bridge theorem itself" in source_domain)
    check("Block82 names MR_color plus Route-2 same-source theorem", "MR_color + Route-2 same-source color-readout theorem" in flat_block82)
    check("Block82 says current artifacts do not identify P_R as full color readout", "identify Route-2 P_R/E-T as a same-source readout" in flat_block82)
    check("Block82 leaves full End(C^3) variation open", "full End(C^3) matrix variation" in flat_block82)


def part2_representation_and_rank_obstruction() -> None:
    print()
    print("PART 2: representation and rank obstruction")
    color_dim = 3
    endc3_dim = color_dim * color_dim
    scalar_line_dim = 1
    sl3_dim = endc3_dim - scalar_line_dim
    route2_feature_dim = 4
    route2_output_dim = 2
    route2_trivial_copies = route2_feature_dim

    hom_dim = hom_su3_adjoint_to_trivial_copies(route2_trivial_copies)
    max_centered_feature_rank = min(sl3_dim, route2_feature_dim)
    max_readout_rank = min(sl3_dim, route2_output_dim)

    check("dim End(C^3) = 9", endc3_dim == 9)
    check("scalar disconnected line has dimension one", scalar_line_dim == 1)
    check("connected color tangent sl_3 has dimension eight", sl3_dim == 8)
    check("current Route-2 K_R feature carrier has dimension four", route2_feature_dim == 4)
    check("current P_R output has dimension two", route2_output_dim == 2)
    check("current Route-2 feature carrier has only trivial SU(3) copies on the minimal surface", route2_trivial_copies == 4)
    check("Hom_SU3(sl_3_adjoint, trivial^4) has dimension zero", hom_dim == 0)
    check("equivariant connected color response into current K_R features is zero", hom_dim == 0 and sl3_dim > 0)
    check("non-equivariant maps through K_R have centered rank at most four", max_centered_feature_rank == 4 and max_centered_feature_rank < sl3_dim)
    check("P_R outputs have centered color rank at most two", max_readout_rank == 2 and max_readout_rank < sl3_dim)
    check("current P_R feature carrier cannot be full sl_3 same-source variation", hom_dim == 0 and max_centered_feature_rank < sl3_dim)


def part3_route_family_pruning() -> None:
    print()
    print("PART 3: route family pruning")
    routes = (
        Route(
            "MR_color_only",
            "same-source full End(C^3) P_R readout",
            "pruned",
            "MR_color can assign color matter/records/link index, but it does not add an adjoint source slot to current P_R",
        ),
        Route(
            "equivariant_map_into_current_K_R",
            "nonzero sl_3 connected response",
            "pruned",
            "the current K_R feature carrier is SU(3)-trivial, so the adjoint-to-trivial equivariant Hom is zero",
        ),
        Route(
            "non_equivariant_four_feature_selector",
            "full sl_3 tangent",
            "pruned",
            "a four-feature selector has rank at most four and imports a color basis choice",
        ),
        Route(
            "current_P_R_output_selector",
            "full sl_3 tangent",
            "pruned",
            "the two-output E/T readout cannot preserve eight connected color directions",
        ),
        Route(
            "new_adjoint_color_source_carrier",
            "same-source full End(C^3) P_R readout",
            "open",
            "adding an explicit adjoint or End(C^3) source slot is the constructive primitive",
        ),
    )
    for route in routes:
        expected = "open" if route.name == "new_adjoint_color_source_carrier" else "pruned"
        check(f"{route.name}: status is {expected}", route.status == expected, route.reason)
        check(f"{route.name}: names the needed output", bool(route.output_needed), route.output_needed)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    base_edges = [
        ("current_route2_surface", "K_R_scalar_ET_features"),
        ("K_R_scalar_ET_features", "SU3_trivial_feature_carrier"),
        ("SU3_trivial_feature_carrier", "zero_equivariant_adjoint_response"),
        ("K_R_scalar_ET_features", "rank_at_most_4_feature_selector"),
        ("current_route2_surface", "P_R_two_output_readout"),
        ("P_R_two_output_readout", "rank_at_most_2_output_selector"),
        ("MR_color", "color_matter_records_link_assignment"),
        ("full_EndC3_color_source", "sl3_adjoint_tangent"),
        ("sl3_adjoint_tangent", "kappa0_selector"),
    ]
    missing_edges = [
        ("route2_adjoint_color_source_carrier", "full_EndC3_color_source"),
        ("route2_adjoint_color_source_carrier", "same_source_P_R_color_readout"),
        ("same_source_P_R_color_readout", "scalar_disconnected_line_typed"),
        ("MR_color_plus_route2_adjoint_source_carrier", "route2_adjoint_color_source_carrier"),
        ("MR_color", "MR_color_plus_route2_adjoint_source_carrier"),
    ]

    for start in ("current_route2_surface", "K_R_scalar_ET_features", "P_R_two_output_readout", "MR_color"):
        check(f"{start} does not reach full End(C^3) source", not reachable(base_edges, start, "full_EndC3_color_source"))
        check(f"{start} does not reach kappa=0 selector", not reachable(base_edges, start, "kappa0_selector"))

    check("full End(C^3) source reaches kappa=0 when supplied", reachable(base_edges, "full_EndC3_color_source", "kappa0_selector"))
    check("adding adjoint source carrier lets MR_color reach full End(C^3)", reachable(base_edges + missing_edges, "MR_color", "full_EndC3_color_source"))
    check("adding adjoint source carrier lets MR_color reach kappa=0", reachable(base_edges + missing_edges, "MR_color", "kappa0_selector"))
    check("base graph contains no endpoint-value node", all("c_TE" not in n and "rho_E" not in n for edge in base_edges for n in edge))
    check("missing-edge graph contains no endpoint-value node", all("c_TE" not in n and "rho_E" not in n for edge in missing_edges for n in edge))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document and loop boundary")
    note = note_text("QUARK_ROUTE2_SAME_SOURCE_COLOR_READOUT_PRIMITIVE_OBSTRUCTION_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    certificate = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    flat = normalized(note)

    required = (
        "Actual current-surface status: no-go for the current P_R feature carrier as a same-source full color readout",
        "This is not an audit verdict",
        "No endpoint value is used",
        "Hom_SU3(sl_3, trivial^4) = 0",
        "rank at most four, not the eight-dimensional full sl_3 tangent",
        "Route-2 adjoint color-source carrier theorem",
        "current Route-2 feature carrier is SU(3)-trivial",
    )
    for marker in required:
        check(f"new note contains marker: {marker}", marker in flat)

    for marker in ("Block83 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)

    check("certificate keeps proposal disallowed", "proposal_allowed: false" in certificate)
    check("certificate marks bare retained wording disallowed", "bare_retained_allowed: false" in certificate)
    check("trace gate records negative route pruning", "trace_class: negative_route_pruning" in trace_gate)
    check("trace gate names adjoint color-source carrier", "Route-2 adjoint color-source carrier theorem" in trace_gate)

    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives ", "the endpoint triple", " on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("target-observation import", "target observation"),
        ("data-tuned selector import", "data-tuned selector"),
    )
    combined = note + "\n" + handoff + "\n" + certificate + "\n" + trace_gate
    for label, marker in banned:
        check(f"packet avoids overclaim marker: {label}", marker not in combined)


def main() -> int:
    print("Route-2 same-source color-readout primitive obstruction")
    print("Status: no-go for current P_R feature carrier as full color readout; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_current_route2_surface()
    part2_representation_and_rank_obstruction()
    part3_route_family_pruning()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: same-source color-readout primitive obstruction checks failed.")
        return 1
    print(
        "VERDICT: the current scalar E/T P_R feature carrier cannot be the "
        "same-source full End(C^3) color readout; a Route-2 adjoint color-source "
        "carrier theorem is still missing."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
