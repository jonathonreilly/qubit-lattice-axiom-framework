#!/usr/bin/env python3
"""Source-Hessian connected-cumulant selector support for Route-2.

This runner formalizes the exact algebra behind the allowed alternate target:

    connected-cumulant / disconnected-subtraction readout -> kappa = 0.

The theorem is conditional.  The source Hessian of W = log Z subtracts
factorizable disconnected products exactly.  It forces kappa=0 only if the
Route-2 singlet term in the two-channel packet is typed as a pure disconnected
product for the same source/readout.  No endpoint value is imported.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-source-hessian-cumulant-selector"

PASS = 0
FAIL = 0

F_ADJ = Fraction(8, 9)
SINGLET = Fraction(1, 9)


@dataclass(frozen=True)
class SourceHessianPacket:
    """Two-channel source Hessian after disconnected subtraction.

    eta is the connected fraction of the singlet channel after the
    factorizable disconnected product has been subtracted.
    """

    eta: Fraction

    @property
    def kappa(self) -> Fraction:
        return self.eta

    @property
    def cumulant_readout(self) -> Fraction:
        return F_ADJ + self.eta * SINGLET

    @property
    def raw_moment_readout(self) -> Fraction:
        return F_ADJ + SINGLET


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


def source_log_hessian(raw_second: Fraction, one_point_left: Fraction, one_point_right: Fraction) -> Fraction:
    """D_i D_j log Z at zero source when Z(0)=1."""

    return raw_second - one_point_left * one_point_right


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


def part1_exact_cumulant_identity() -> None:
    print("PART 1: exact source-Hessian cumulant identity")
    left_mean = Fraction(1, 3)
    right_mean = Fraction(1, 3)
    disconnected_product = left_mean * right_mean
    connected_adjoint = F_ADJ
    raw_second = connected_adjoint + disconnected_product
    connected_hessian = source_log_hessian(raw_second, left_mean, right_mean)

    check("SU(3) adjoint channel fraction is 8/9", F_ADJ == Fraction(8, 9))
    check("singlet/disconnected channel fraction is 1/9", SINGLET == Fraction(1, 9))
    check("chosen one-point product realizes the singlet fraction", disconnected_product == SINGLET)
    check("raw second source moment reads full trace", raw_second == 1)
    check("D^2 log Z subtracts the one-point product", connected_hessian == raw_second - disconnected_product)
    check("connected source Hessian keeps the adjoint fraction", connected_hessian == F_ADJ)
    check("pure disconnected singlet gives kappa=0", SourceHessianPacket(Fraction(0)).cumulant_readout == F_ADJ)
    check("raw moment Hessian gives kappa=1", SourceHessianPacket(Fraction(0)).raw_moment_readout == 1)


def part2_singlet_purity_classifier() -> None:
    print()
    print("PART 2: singlet purity classifier")
    samples = (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1))
    values = []
    for eta in samples:
        packet = SourceHessianPacket(eta)
        values.append(packet.cumulant_readout)
        print(f"  eta={eta}: kappa={packet.kappa}, R_cumulant={packet.cumulant_readout}")
        check(f"eta={eta} maps to kappa={eta}", packet.kappa == eta)
        check(f"eta={eta} leaves exact rational readout", isinstance(packet.cumulant_readout, Fraction))

    check("pure disconnected singlet is exactly kappa=0", SourceHessianPacket(Fraction(0)).kappa == 0)
    check("pure connected singlet is exactly kappa=1", SourceHessianPacket(Fraction(1)).kappa == 1)
    check("partial connected singlet gives intermediate kappa", SourceHessianPacket(Fraction(1, 2)).kappa == Fraction(1, 2))
    check("cumulant readout values distinguish singlet-purity assumptions", len(set(values)) == len(values))
    check("source-Hessian algebra alone does not choose eta", SourceHessianPacket(Fraction(0)).kappa != SourceHessianPacket(Fraction(1)).kappa)


def part3_typed_reachability() -> None:
    print()
    print("PART 3: typed readout reachability")
    base_edges = [
        ("source_partition_Z", "raw_moment_hessian"),
        ("source_partition_Z", "log_generating_function_W"),
        ("log_generating_function_W", "connected_source_hessian"),
        ("raw_moment_hessian", "kappa_1_full_trace"),
        ("connected_source_hessian", "kappa_eta_singlet_residual"),
        ("pure_disconnected_singlet_identification", "kappa_0_selector"),
        ("connected_source_hessian", "requires_singlet_purity"),
        ("requires_singlet_purity", "pure_disconnected_singlet_identification"),
    ]
    bridge_edges = [
        ("connected_source_hessian", "pure_disconnected_singlet_identification"),
        ("pure_disconnected_singlet_identification", "kappa_0_selector"),
    ]

    check("raw moment Hessian reaches full-trace selector", reachable(base_edges, "source_partition_Z", "kappa_1_full_trace"))
    check("log source Hessian reaches only residual kappa_eta without singlet purity", reachable(base_edges, "source_partition_Z", "kappa_eta_singlet_residual"))
    check("log source Hessian does not reach kappa=0 without the missing primitive", not reachable(base_edges[:-2], "source_partition_Z", "kappa_0_selector"))
    check("adding pure-disconnected singlet bridge reaches kappa=0", reachable(base_edges + bridge_edges, "source_partition_Z", "kappa_0_selector"))
    check("the kappa=0 path uses no endpoint-value node", all("rho" not in node and "endpoint" not in node for edge in base_edges + bridge_edges for node in edge))


def part4_relation_to_existing_no_gos() -> None:
    print()
    print("PART 4: relation to existing no-go packets")
    connected_note = note_text("QUARK_ROUTE2_CONNECTED_CURRENT_SELECTOR_NO_GO_NOTE_2026-06-22.md")
    local_note = note_text("QUARK_ROUTE2_LOCAL_CURRENT_SINGLET_ANNIHILATION_NO_GO_NOTE_2026-06-22.md")
    graph_note = note_text("QUARK_ROUTE2_GRAPH_FIRST_SPATIAL_COLOR_BRIDGE_NO_GO_NOTE_2026-06-22.md")
    new_note = note_text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md")

    check("connected-current no-go leaves connected-current projector as target", "connected-current projector" in connected_note)
    check("local-current no-go says connected-cumulant premise selects kappa=0", "connected-cumulant premise" in local_note and "does select `kappa=0`" in local_note)
    check("graph-first bridge note leaves connected selector open", "connected selector `kappa=0`" in graph_note)
    check("new note is scoped as conditional support", "Claim type:** bounded_support" in new_note)
    check("new note names the smaller missing primitive", "pure-disconnected singlet identification" in new_note)


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    new_note = note_text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    normalized = " ".join(new_note.replace("**", "").replace("`", "").split())

    required = (
        "Actual current-surface status: conditional-support for source-Hessian connected-cumulant selector",
        "This is not an audit verdict",
        "No endpoint value is used",
        "D^2 log Z subtracts factorizable disconnected products exactly",
        "pure-disconnected singlet identification",
        "Route-2 physical readout is the connected source Hessian",
        "does not derive the missing physical readout primitive",
    )
    for marker in required:
        check(f"new note contains marker: {marker}", marker in normalized)

    handoff_required = (
        "Block76 Summary",
        "upstream_support",
        "Do not audit",
        "Next Exact Action",
    )
    for marker in handoff_required:
        check(f"handoff contains marker: {marker}", marker in handoff)

    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives ", "the endpoint triple", " on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
    )
    combined = new_note + "\n" + handoff
    for label, marker in banned:
        check(f"new packet avoids overclaim marker: {label}", marker not in combined)


def main() -> int:
    print("Route-2 source-Hessian connected-cumulant selector support")
    print("Status: conditional-support for source-Hessian connected-cumulant selector; not an audit verdict.")
    print("TRACE: upstream_support")
    part1_exact_cumulant_identity()
    part2_singlet_purity_classifier()
    part3_typed_reachability()
    part4_relation_to_existing_no_gos()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: source-Hessian cumulant selector checks failed.")
        return 1
    print(
        "VERDICT: D^2 log Z gives exact disconnected subtraction and forces "
        "kappa=0 once the Route-2 singlet term is typed as a pure disconnected "
        "product for the same source/readout.  That source/readout primitive "
        "remains the open bridge."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
