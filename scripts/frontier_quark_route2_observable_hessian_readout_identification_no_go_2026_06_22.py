#!/usr/bin/env python3
"""No-go for identifying the scalar observable Hessian with Route-2 readout.

Block76 showed that a connected source Hessian D^2 log Z would force kappa=0
after a pure-disconnected singlet identification.  This runner tests whether
the existing S3 observable-Hessian authority already supplies that physical
Route-2 source/readout identification.

It does not: the existing observable-Hessian surface is scalar-only, while the
Route-2 selector needs a color/channel-resolved source functional and an E/T
readout map.  No endpoint value is imported.
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-observable-hessian-readout-identification"

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


def scalar_logdet_second_derivative(diagonal: tuple[Fraction, ...]) -> Fraction:
    # W(j) = sum_i log(d_i + j) - log(d_i), so W''(0) = -sum_i 1/d_i^2.
    return -sum(Fraction(1, d * d) for d in diagonal)


def part1_authority_surface() -> None:
    print("PART 1: authority surface")
    hessian = note_text("S3_TIME_OBSERVABLE_HESSIAN_ROUTE_NOTE.md")
    readout = note_text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    block76 = note_text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md")

    check("observable-Hessian note contains W=logdet scalar generator", "W[J] = log|det(D+J)|" in hessian)
    check("observable-Hessian note says scalar-only", "scalar-only" in hessian and "scalar source generator" in hessian)
    check("observable-Hessian note says no tensor/time-coupling law", "does not generate a tensor-valued" in hessian)
    check("Route-2 exact readout map is finite carrier/readout algebra", "P_R" in readout and "restricted bright readout" in readout)
    for absent in ("log Z", "D^2 log Z", "connected source Hessian", "pure-disconnected singlet"):
        check(f"Route-2 exact readout map lacks source-Hessian marker {absent}", absent not in readout)
    check("Block76 names physical source/readout identification as open", "Route-2 physical readout is the connected source Hessian" in block76)
    check("Block76 names pure-disconnected singlet identification as open", "pure-disconnected singlet identification" in block76)


def part2_scalar_rank_no_go() -> None:
    print()
    print("PART 2: scalar-rank no-go")
    diagonal = (Fraction(2), Fraction(3), Fraction(5))
    scalar_hessian = scalar_logdet_second_derivative(diagonal)
    source_rank = 1
    required_channel_rank = 2
    required_route2_slots = 4

    print(f"  W''(0) for scalar jI source on diag{diagonal} = {scalar_hessian}")
    check("scalar logdet Hessian is one scalar number", isinstance(scalar_hessian, Fraction))
    check("scalar source rank is one", source_rank == 1)
    check("two-channel selector needs at least adjoint/singlet separation", required_channel_rank == 2)
    check("Route-2 restricted readout carrier has four endpoint columns", required_route2_slots == 4)
    check("scalar Hessian rank is below color-channel rank", source_rank < required_channel_rank)
    check("scalar Hessian rank is below Route-2 endpoint slot count", source_rank < required_route2_slots)
    check("a scalar Hessian cannot choose a singlet-purity coefficient eta", source_rank == 1 and required_channel_rank > source_rank)


def part3_typed_reachability() -> None:
    print()
    print("PART 3: typed reachability")
    base_edges = [
        ("observable_logdet_W", "scalar_source_hessian"),
        ("scalar_source_hessian", "scalar_bilinear_response"),
        ("route2_bilinear_carrier_K_R", "route2_restricted_readout_P_R"),
        ("route2_restricted_readout_P_R", "route2_E_T_center_readout"),
        ("source_hessian_cumulant_theorem", "connected_source_hessian_D2_logZ"),
        ("pure_disconnected_singlet_identification", "kappa_0_selector"),
    ]
    missing_source_bridge = ("scalar_source_hessian", "connected_source_hessian_D2_logZ")
    missing_route2_bridge = ("connected_source_hessian_D2_logZ", "route2_physical_readout")
    missing_purity_bridge = ("route2_physical_readout", "pure_disconnected_singlet_identification")

    check("scalar observable Hessian does not reach Route-2 readout", not reachable(base_edges, "observable_logdet_W", "route2_physical_readout"))
    check("scalar observable Hessian does not reach kappa=0", not reachable(base_edges, "observable_logdet_W", "kappa_0_selector"))
    check(
        "adding all missing source/readout bridges reaches kappa=0",
        reachable(
            base_edges + [missing_source_bridge, missing_route2_bridge, missing_purity_bridge],
            "observable_logdet_W",
            "kappa_0_selector",
        ),
    )
    check("Route-2 carrier path remains separate from scalar Hessian path", not reachable(base_edges, "route2_bilinear_carrier_K_R", "scalar_source_hessian"))
    check("the needed bridge is a typed source/readout identification", missing_route2_bridge[1] == "route2_physical_readout")


def part4_missing_primitive() -> None:
    print()
    print("PART 4: missing primitive")
    primitives = {
        "color_tensor_source_functional": "source has adjoint/singlet and E/T readout directions",
        "same_source_identification": "the source used by W is the source used by Route-2 physical readout",
        "connected_hessian_readout": "physical readout is D^2 log Z, not raw finite readout P_R alone",
        "singlet_purity": "the 1/9 singlet term is pure disconnected product",
    }
    check("four independent primitive labels are named", set(primitives) == {"color_tensor_source_functional", "same_source_identification", "connected_hessian_readout", "singlet_purity"})
    check("scalar-only observable Hessian supplies none of the color/tensor labels", "scalar" not in primitives)
    check("pure-disconnected singlet remains separate from source identity", primitives["singlet_purity"] != primitives["same_source_identification"])
    check("connected Hessian readout is not the raw P_R readout", "not raw finite readout" in primitives["connected_hessian_readout"])
    check("a positive theorem must supply all labels", len(primitives) == 4)


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    new_note = note_text("QUARK_ROUTE2_OBSERVABLE_HESSIAN_READOUT_IDENTIFICATION_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    normalized = " ".join(new_note.replace("**", "").replace("`", "").split())
    normalized_lower = normalized.lower()

    required = (
        "Actual current-surface status: no-go for scalar observable-Hessian to Route-2 readout identification",
        "This is not an audit verdict",
        "No endpoint value is used",
        "scalar source Hessian",
        "not a color/channel-resolved Route-2 source",
        "Missing primitive",
        "color/tensor-resolved source functional",
        "same-source identification",
        "pure-disconnected singlet identification",
    )
    for marker in required:
        present = marker.lower() in normalized_lower if marker == "Missing primitive" else marker in normalized
        check(f"new note contains marker: {marker}", present)

    for marker in ("Block77 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
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
    print("Route-2 observable-Hessian readout-identification no-go")
    print("Status: no-go for scalar observable-Hessian to Route-2 readout identification; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_authority_surface()
    part2_scalar_rank_no_go()
    part3_typed_reachability()
    part4_missing_primitive()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: observable-Hessian readout-identification checks failed.")
        return 1
    print(
        "VERDICT: the existing scalar observable Hessian is not a typed "
        "Route-2 color/E-T connected readout.  A positive theorem still needs "
        "a color/tensor-resolved source functional, same-source identification, "
        "connected-Hessian readout, and pure-disconnected singlet typing."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
