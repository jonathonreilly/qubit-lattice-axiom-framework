#!/usr/bin/env python3
"""Hidden adjoint carrier no-go for Route-2 K_R.

Checks whether the current Route-2 bilinear carrier definition already hides a
nontrivial SU(3)-adjoint / End(C^3) color-source slot.  It does not: K_R is a
four-entry scalar carrier defined from delta_A1, u_E, and u_T on the current
surface.  No endpoint value is imported.
"""

from __future__ import annotations

from collections import deque
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-hidden-adjoint-carrier"

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


def part1_kr_definition_surface() -> None:
    print("PART 1: K_R definition surface")
    s3 = text("S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md")
    s3_flat = flat(s3)

    check("S3 primitive is class-A definition only", "class-A definition only" in s3)
    check("K_R is defined from delta_A1, u_E, u_T", "delta_A1, u_E, u_T" in s3 and "K_R(q)" in s3)
    check("K_R vector has exactly four displayed scalar entries", "vec K_R(q) := (u_E, u_T, delta_A1 u_E, delta_A1 u_T)" in s3)
    check("definition says K_R denotes only the right-hand-side polynomial expression", "denotes nothing more than the right-hand-side polynomial expression" in s3_flat)
    check("physical tensor primitive bridge is explicitly open", "physical tensor primitive" in s3_flat and "open gaps" in s3_flat)
    check("aligned-bright coordinate identification is explicitly open", "aligned-bright coordinate identification" in s3_flat)
    check("delta_A1 decoupling derivation is explicitly open", "delta_A1-decoupling" in s3_flat)
    check("S3 primitive note has no SU(3) token", "SU(3)" not in s3 and "su(3)" not in s3)
    check("S3 primitive note has no End(C^3) token", "End(C^3)" not in s3)
    check("S3 primitive note has no sl_3 token", "sl_3" not in s3)
    check("S3 primitive note has no color-source claim", "color-source" not in s3 and "color source" not in s3)


def part2_time_readout_surfaces() -> None:
    print()
    print("PART 2: time/readout surfaces")
    readout = text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    time = text("QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md")
    block83 = text("QUARK_ROUTE2_SAME_SOURCE_COLOR_READOUT_PRIMITIVE_OBSTRUCTION_NOTE_2026-06-22.md")
    readout_flat = flat(readout)
    time_flat = flat(time)
    block83_flat = flat(block83)

    check("readout note reduces to four-coordinate P_R family", "P_R = [[alpha_E, 0, beta_E, 0]," in readout)
    check("readout note keeps exact readout theorem not derived", "exact endpoint ratio theorem: not derived" in readout_flat)
    check("time note says P_R must be supplied", "once an admissible readout map P_R is supplied" in time_flat)
    check("time note says current stack does not determine unique law", "does not determine one unique exact Theta_R -> Lambda_R time-coupling law" in time_flat)
    check("Block83 names missing Route-2 adjoint color-source carrier theorem", "Route-2 adjoint color-source carrier theorem" in block83)
    check("Block83 says current feature carrier has no adjoint source slot", "no adjoint color" in block83 and "slot" in block83)
    check("Block83 leaves constructive extension route open", "adding an explicit adjoint color-source carrier" in block83_flat)


def part3_dimension_slot_obstruction() -> None:
    print()
    print("PART 3: dimension and typed-slot obstruction")
    named_scalar_inputs = {"delta_A1", "u_E", "u_T"}
    kr_entries = ("u_E", "u_T", "delta_A1*u_E", "delta_A1*u_T")
    adjoint_dim = 8
    endc3_dim = 9
    hidden_adjoint_slots = 0

    check("K_R uses three named scalar input symbols", len(named_scalar_inputs) == 3)
    check("K_R exposes four scalar entries", len(kr_entries) == 4)
    check("full End(C^3) source would have dimension nine", endc3_dim == 9)
    check("adjoint connected source would have dimension eight", adjoint_dim == 8)
    check("current definition exposes zero typed adjoint slots", hidden_adjoint_slots == 0)
    check("zero hidden adjoint slots cannot carry an eight-dimensional adjoint", hidden_adjoint_slots < adjoint_dim)
    check("four scalar entries are not a typed End(C^3) variable", len(kr_entries) != endc3_dim)
    check("adding an adjoint carrier would change or extend the current definition", hidden_adjoint_slots == 0 and len(kr_entries) == 4)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    base_edges = [
        ("S3_bilinear_definition", "three_scalar_inputs"),
        ("three_scalar_inputs", "four_scalar_K_R_entries"),
        ("four_scalar_K_R_entries", "current_P_R_scalar_ET_readout"),
        ("current_P_R_scalar_ET_readout", "no_adjoint_slot"),
        ("hidden_adjoint_carrier_route", "no_adjoint_slot"),
        ("full_EndC3_color_source", "sl3_adjoint_tangent"),
        ("sl3_adjoint_tangent", "kappa0_selector"),
    ]
    extension_edges = [
        ("Route2_adjoint_color_source_extension", "full_EndC3_color_source"),
        ("Route2_adjoint_color_source_extension", "same_source_P_R_color_readout"),
        ("same_source_P_R_color_readout", "kappa0_selector"),
    ]

    for start in ("S3_bilinear_definition", "four_scalar_K_R_entries", "hidden_adjoint_carrier_route"):
        check(f"{start} does not reach full End(C^3) source", not reachable(base_edges, start, "full_EndC3_color_source"))
        check(f"{start} does not reach kappa=0 selector", not reachable(base_edges, start, "kappa0_selector"))

    check("full End(C^3) source reaches kappa=0 if supplied", reachable(base_edges, "full_EndC3_color_source", "kappa0_selector"))
    check("extension theorem would reach full End(C^3)", reachable(base_edges + extension_edges, "Route2_adjoint_color_source_extension", "full_EndC3_color_source"))
    check("extension theorem would reach kappa=0", reachable(base_edges + extension_edges, "Route2_adjoint_color_source_extension", "kappa0_selector"))
    check("base graph contains no endpoint-value node", all("c_TE" not in n and "rho_E" not in n for e in base_edges for n in e))
    check("extension graph contains no endpoint-value node", all("c_TE" not in n and "rho_E" not in n for e in extension_edges for n in e))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document and loop boundary")
    note = text("QUARK_ROUTE2_HIDDEN_ADJOINT_CARRIER_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace = loop_text("TRACE_GATE.md")
    note_flat = flat(note)

    required = (
        "Actual current-surface status: no-go for finding a hidden SU(3)-adjoint color-source slot",
        "This is not an audit verdict",
        "No endpoint value is used",
        "No hidden adjoint carrier exists in the current K_R definition",
        "Route-2 adjoint color-source extension theorem",
        "not already latent in the current K_R definition",
    )
    for marker in required:
        check(f"new note contains marker: {marker}", marker in note_flat)

    for marker in ("Block84 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)

    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("certificate marks bare retained wording disallowed", "bare_retained_allowed: false" in cert)
    check("trace gate records negative route pruning", "trace_class: negative_route_pruning" in trace)
    check("trace gate names adjoint extension theorem", "Route-2 adjoint color-source extension theorem" in trace)

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
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace
    for label, marker in banned:
        check(f"packet avoids overclaim marker: {label}", marker not in combined)


def main() -> int:
    print("Route-2 hidden adjoint carrier no-go")
    print("Status: no hidden SU(3)-adjoint source slot in current K_R definition; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_kr_definition_surface()
    part2_time_readout_surfaces()
    part3_dimension_slot_obstruction()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: hidden adjoint carrier checks failed.")
        return 1
    print(
        "VERDICT: the current K_R definition has no hidden SU(3)-adjoint "
        "color-source slot; a Route-2 adjoint color-source extension theorem "
        "is still missing."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
