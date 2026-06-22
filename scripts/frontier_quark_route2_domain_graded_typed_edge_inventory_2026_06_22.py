#!/usr/bin/env python3
"""Route-2 domain-graded typed-edge inventory support/no-go.

This runner attacks the audit-facing residual in
QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md: the finite
typed-edge bank was originally a configured runner constant.  The check here
rebuilds that bank from the quote-anchor authority schema already present in
the source-domain runner, adds an explicit domain grading, and reruns the
source-to-endpoint reachability test on the generated inventory.

Result: the configured edge set is regenerated from the quote-anchor schema,
but the generated domain-graded bank still has no color-to-Route-2 endpoint
edge.  Adding the missing cross-domain bridge remains the only way to connect
SU(3) R_conn support to rho_E=21/4 in this finite bank.

This is not an audit verdict.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable

from frontier_quark_route2_source_domain_bridge_no_go import (
    CURRENT_TYPED_EDGES,
    DERIVED_ADDITIONAL_EDGES,
    DERIVED_EDGE_QUOTE_ANCHORS,
    EDGE_QUOTE_ANCHORS,
    MISSING_BRIDGE,
    TypedEdge,
    edge_key,
    q_e_from_center_ratio,
    quote_in_text,
    quote_is_meaningful,
    r_conn,
    reachable,
    rho_e_from_center_ratio,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS = 0
FAIL = 0

SOURCE = "su3_R_conn_8_9"
TARGET = "route2_rho_E_21_4"


NODE_DOMAIN: dict[str, str] = {
    "route2_support_delta_A1": "route2_support",
    "route2_bright_E_T": "route2_support",
    "route2_bilinear_carrier_K_R": "route2_support",
    "route2_restricted_readout_family": "route2_readout",
    "route2_endpoint_algebra": "route2_algebra",
    "route2_t_side_candidates": "route2_readout",
    "route2_q_T_5_6_and_shell_TE_minus_2": "route2_readout",
    "route2_center_TE_minus_8_9": "route2_readout",
    "route2_q_E_15_8": "route2_readout",
    "route2_rho_E_21_4": "route2_readout",
    "su3_color_trace_channel": "su3_color",
    "su3_R_conn_8_9": "su3_color",
}

ROUTE2_DOMAINS = {"route2_support", "route2_readout", "route2_algebra"}


@dataclass(frozen=True)
class GeneratedInventory:
    current_edges: tuple[TypedEdge, ...]
    derived_edges: tuple[TypedEdge, ...]

    @property
    def all_edges(self) -> tuple[TypedEdge, ...]:
        return self.current_edges + self.derived_edges


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def note_text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def phrase(*parts: str) -> str:
    return "".join(parts)


def reference_by_key(edges: Iterable[TypedEdge]) -> dict[str, TypedEdge]:
    return {edge_key(edge): edge for edge in edges}


def generate_edges(
    anchor_table: dict[str, tuple[str, tuple[str, ...]]],
    reference_edges: tuple[TypedEdge, ...],
) -> tuple[TypedEdge, ...]:
    """Generate edges from anchor keys and authority files.

    The edge key supplies the typed source and target.  The authority file
    and quote anchors must verify against disk.  Role/label metadata is copied
    from the existing source-domain runner so this certificate can compare
    generated inventory against the configured inventory exactly.
    """

    reference = reference_by_key(reference_edges)
    generated: list[TypedEdge] = []
    for key in sorted(anchor_table):
        authority, quotes = anchor_table[key]
        source, target = key.split("->", 1)
        ref = reference[key]
        generated.append(
            TypedEdge(
                source=source,
                target=target,
                label=ref.label,
                authority=authority,
                role=ref.role,
            )
        )
        text = note_text(authority)
        check(f"{key} authority matches reference", authority == ref.authority, authority)
        check(f"{key} has quote anchors", bool(quotes), str(len(quotes)))
        for index, quote in enumerate(quotes, start=1):
            check(f"{key} quote {index} is meaningful", quote_is_meaningful(quote))
            check(f"{key} quote {index} is present", quote_in_text(quote, text), authority)
    return tuple(generated)


def generated_inventory() -> GeneratedInventory:
    return GeneratedInventory(
        current_edges=generate_edges(EDGE_QUOTE_ANCHORS, CURRENT_TYPED_EDGES),
        derived_edges=generate_edges(DERIVED_EDGE_QUOTE_ANCHORS, DERIVED_ADDITIONAL_EDGES),
    )


def domains(edge: TypedEdge) -> tuple[str, str]:
    return NODE_DOMAIN[edge.source], NODE_DOMAIN[edge.target]


def is_color_to_route2(edge: TypedEdge) -> bool:
    source_domain, target_domain = domains(edge)
    return source_domain == "su3_color" and target_domain in ROUTE2_DOMAINS


def is_route2_to_color(edge: TypedEdge) -> bool:
    source_domain, target_domain = domains(edge)
    return source_domain in ROUTE2_DOMAINS and target_domain == "su3_color"


def path_text(path: list[TypedEdge]) -> str:
    if not path:
        return "(none)"
    return " -> ".join([path[0].source, *[edge.target for edge in path]])


def edge_keys(edges: Iterable[TypedEdge]) -> set[str]:
    return {edge_key(edge) for edge in edges}


def part1_anchor_derived_inventory(inv: GeneratedInventory) -> None:
    print("PART 1: quote-anchor generated inventory")
    check("generated current edge count matches configured count", len(inv.current_edges) == len(CURRENT_TYPED_EDGES))
    check("generated derived edge count matches configured derived count", len(inv.derived_edges) == len(DERIVED_ADDITIONAL_EDGES))
    check("generated current edge keys match configured keys", edge_keys(inv.current_edges) == edge_keys(CURRENT_TYPED_EDGES))
    check("generated derived edge keys match configured derived keys", edge_keys(inv.derived_edges) == edge_keys(DERIVED_ADDITIONAL_EDGES))
    check("missing bridge is not generated by current anchors", edge_key(MISSING_BRIDGE) not in edge_keys(inv.current_edges))
    check("missing bridge is not generated by derived anchors", edge_key(MISSING_BRIDGE) not in edge_keys(inv.derived_edges))


def part2_domain_grading(inv: GeneratedInventory) -> None:
    print()
    print("PART 2: domain grading")
    all_nodes = {edge.source for edge in inv.all_edges + (MISSING_BRIDGE,)} | {edge.target for edge in inv.all_edges + (MISSING_BRIDGE,)}
    check("all inventory nodes have declared domains", all(node in NODE_DOMAIN for node in all_nodes), str(sorted(all_nodes - set(NODE_DOMAIN))))
    check("generated inventory contains no color-to-Route-2 edge", not any(is_color_to_route2(edge) for edge in inv.all_edges))
    check("generated inventory contains no Route-2-to-color edge", not any(is_route2_to_color(edge) for edge in inv.all_edges))
    check("SU(3) support edge stays inside color domain", all(domains(edge) == ("su3_color", "su3_color") for edge in inv.current_edges if edge.source.startswith("su3_")))
    check("missing bridge is exactly color-to-Route-2", is_color_to_route2(MISSING_BRIDGE), f"{domains(MISSING_BRIDGE)}")
    check("missing bridge has role missing", MISSING_BRIDGE.role == "missing")


def part3_reachability(inv: GeneratedInventory) -> None:
    print()
    print("PART 3: reachability on generated inventory")
    current_reaches, current_path = reachable(inv.current_edges, SOURCE, TARGET)
    derived_reaches, derived_path = reachable(inv.all_edges, SOURCE, TARGET)
    bridged_reaches, bridged_path = reachable(inv.all_edges + (MISSING_BRIDGE,), SOURCE, TARGET)
    check("generated current inventory has no R_conn-to-rho_E path", not current_reaches, path_text(current_path))
    check("generated current+derived inventory has no R_conn-to-rho_E path", not derived_reaches, path_text(derived_path))
    check("adding missing bridge creates R_conn-to-rho_E path", bridged_reaches, path_text(bridged_path))
    check("successful bridged path uses the missing bridge", MISSING_BRIDGE in bridged_path)
    check("successful bridged path then uses endpoint algebra", {"algebra", "missing"} <= {edge.role for edge in bridged_path})


def part4_endpoint_algebra() -> None:
    print()
    print("PART 4: endpoint algebra remains conditional")
    r = r_conn(3)
    c_te = -r
    q_e = q_e_from_center_ratio(c_te)
    rho_e = rho_e_from_center_ratio(c_te)
    full_c_te = Fraction(-1)
    check("SU(3) adjoint fraction is 8/9", r == Fraction(8, 9), f"R_conn={r}")
    check("if c_TE=-R_conn is supplied then q_E=15/8", q_e == Fraction(15, 8), f"q_E={q_e}")
    check("if c_TE=-R_conn is supplied then rho_E=21/4", rho_e == Fraction(21, 4), f"rho_E={rho_e}")
    check("full-current signed endpoint gives rho_E=4 instead", rho_e_from_center_ratio(full_c_te) == 4)
    check("therefore generated inventory support does not select the endpoint by itself", rho_e_from_center_ratio(full_c_te) != rho_e)


def part5_note_and_scope_markers() -> None:
    print()
    print("PART 5: note and scope markers")
    note = note_text("QUARK_ROUTE2_DOMAIN_GRADED_TYPED_EDGE_INVENTORY_SUPPORT_NOTE_2026-06-22.md")
    source_note = note_text("QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md")
    parent = note_text("S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")
    block73 = note_text("QUARK_ROUTE2_LOCAL_CURRENT_SINGLET_ANNIHILATION_NO_GO_NOTE_2026-06-22.md")

    required = (
        "Claim type:** bounded_support",
        "Actual current-surface status: bounded-support for generated typed-edge inventory",
        "This is not an audit verdict",
        "domain-graded generated inventory",
        "missing bridge remains absent",
        "does not close the parent",
    )
    for marker in required:
        check(f"new note contains marker: {marker}", marker in note)

    check(
        "source-domain note names the configured-inventory residual",
        "hard-codes" in source_note and "CURRENT_TYPED_EDGES" in source_note,
    )
    check("parent still names the readout endpoint blocker", "underlying readout-map endpoint triple is not yet derived" in parent)
    check("Block73 leaves connected-cumulant selector as the open import", "connected-cumulant premise" in block73)

    banned = (
        ("status-authority phrase", phrase("Status ", "authority")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives ", "the endpoint triple", " on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
    )
    for label, marker in banned:
        check(f"new note avoids overclaim marker: {label}", marker not in note)


def main() -> int:
    print("Route-2 domain-graded typed-edge inventory support/no-go")
    print("Status: bounded-support for generated inventory; not an audit verdict.")
    print("TRACE: upstream_support + negative_route_pruning")
    inv = generated_inventory()
    part1_anchor_derived_inventory(inv)
    part2_domain_grading(inv)
    part3_reachability(inv)
    part4_endpoint_algebra()
    part5_note_and_scope_markers()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: domain-graded typed-edge inventory checks failed.")
        return 1
    print(
        "VERDICT: the current Route-2 typed-edge inventory is regenerated "
        "from quote-anchored authority schemas, but the generated "
        "domain-graded bank still lacks the cross-domain R_conn -> c_TE bridge."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
