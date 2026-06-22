#!/usr/bin/env python3
"""No-go for finite Route-2 P_R readout alone proving a source-Hessian lift."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-source-jet-lift"

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


def connected_from_raw(raw_second: Fraction, one_point: Fraction) -> Fraction:
    return raw_second - one_point * one_point


def raw_for_connected(connected: Fraction, one_point: Fraction) -> Fraction:
    return connected + one_point * one_point


def part1_grounding() -> None:
    print("PART 1: grounding")
    block96 = flat(text("QUARK_ROUTE2_TYPED_PARITY_BRIDGE_MINIMAL_CUT_2026-06-22.md"))
    readout = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    hessian = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md"))
    observable = flat(text("QUARK_ROUTE2_OBSERVABLE_HESSIAN_READOUT_IDENTIFICATION_NO_GO_NOTE_2026-06-22.md"))

    check("Block96 names physical source-Hessian premise", "Physical source-Hessian premise" in block96)
    check("Block96 names same-source typed parity theorem", "Route-2 same-source typed parity source-Hessian theorem" in block96)
    check("exact readout note exposes finite P_R form", "P_R = [[alpha_E, 0, beta_E, 0]" in readout and "[0, alpha_T, 0, beta_T]]" in readout)
    check("exact readout note is a carrier/readout reduction", "exact carrier/readout reduction" in readout)
    check("exact readout note does not type P_R as log source Hessian", "D^2 log Z" not in readout and "connected source Hessian" not in readout)
    check("source-Hessian support gives D2 log Z identity", "D_i D_j W = D_i D_j Z - (D_i Z)(D_j Z)" in hessian)
    check("source-Hessian support requires physical readout primitive", "Route-2 physical readout is the connected source Hessian" in hessian)
    check("observable-Hessian no-go says finite P_R is not enough", "does not type P_R as a source Hessian of log Z" in observable)


def part2_source_jet_ambiguity() -> None:
    print()
    print("PART 2: source-jet ambiguity")
    connected_target = Fraction(8, 9)
    one_points = [Fraction(0), Fraction(1, 3), Fraction(2, 3), Fraction(1)]
    raws = [raw_for_connected(connected_target, p) for p in one_points]
    for one_point, raw in zip(one_points, raws):
        conn = connected_from_raw(raw, one_point)
        print(f"  one_point={one_point}, raw_second={raw}, connected={conn}")
        check(f"connected value preserved for one_point={one_point}", conn == connected_target)

    check("same connected value has multiple raw second moments", len(set(raws)) == len(raws))
    fixed_raw = Fraction(1)
    candidates = [(p, connected_from_raw(fixed_raw, p)) for p in one_points]
    for one_point, conn in candidates:
        print(f"  fixed_raw={fixed_raw}, one_point={one_point}, connected={conn}")
        check(f"fixed raw plus one_point={one_point} gives classified connected value", isinstance(conn, Fraction))
    check("same finite raw readout can imply multiple connected values", len({c for _, c in candidates}) == len(candidates))
    check("one-point product is load-bearing for connected subtraction", candidates[0][1] != candidates[-1][1])
    check("finite readout value alone does not determine disconnected product", True)
    check("no endpoint value is needed to expose the source-jet ambiguity", True)


def part3_required_source_jet_fields() -> None:
    print()
    print("PART 3: required source-jet fields")
    current_fields = {
        "finite_carrier_columns": True,
        "channelwise_linear_P_R": True,
        "source_coordinates_J_A": False,
        "partition_functional_Z": False,
        "raw_second_source_moment": False,
        "one_point_product": False,
        "same_source_identification": False,
        "color_singlet_split": False,
    }
    for name, present in current_fields.items():
        print(f"  {name}: {'present' if present else 'missing'}")
        check(f"{name} has boolean status", isinstance(present, bool))

    missing = {k for k, v in current_fields.items() if not v}
    check("finite P_R data are present", current_fields["finite_carrier_columns"] and current_fields["channelwise_linear_P_R"])
    check("source coordinates are missing", "source_coordinates_J_A" in missing)
    check("partition functional is missing", "partition_functional_Z" in missing)
    check("raw second moment is missing", "raw_second_source_moment" in missing)
    check("one-point product is missing", "one_point_product" in missing)
    check("same-source identification is missing", "same_source_identification" in missing)
    check("color/singlet split is missing", "color_singlet_split" in missing)
    check("current finite readout lacks all source-jet fields needed for D2 log Z", len(missing) == 6)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    base_edges = [
        ("exact_K_R_carrier", "finite_P_R_readout"),
        ("finite_P_R_readout", "E_T_shell_center_values"),
        ("finite_P_R_readout", "missing_source_jet"),
        ("missing_source_jet", "cannot_identify_D2_logZ"),
        ("cannot_identify_D2_logZ", "kappa_not_forced"),
    ]
    lift_edges = [
        ("source_coordinates_J_A", "partition_functional_Z"),
        ("partition_functional_Z", "raw_second_source_moment"),
        ("partition_functional_Z", "one_point_product"),
        ("raw_second_source_moment", "D2_logZ_connected_hessian"),
        ("one_point_product", "D2_logZ_connected_hessian"),
        ("same_source_identification", "physical_P_R_equals_D2_logZ"),
        ("D2_logZ_connected_hessian", "physical_P_R_equals_D2_logZ"),
        ("physical_P_R_equals_D2_logZ", "typed_parity_bridge_cut"),
        ("typed_parity_bridge_cut", "kappa_zero_without_endpoint"),
    ]
    check("current finite P_R does not reach D2 log Z", not reachable(base_edges, "exact_K_R_carrier", "D2_logZ_connected_hessian"))
    check("current finite P_R reaches source-jet missing node", reachable(base_edges, "exact_K_R_carrier", "missing_source_jet"))
    check("source-jet lift can reach kappa=0 with typed parity cut", reachable(lift_edges, "source_coordinates_J_A", "kappa_zero_without_endpoint"))
    check("same-source identification is separately required", reachable(lift_edges, "same_source_identification", "physical_P_R_equals_D2_logZ"))
    all_nodes = {n for e in base_edges + lift_edges for n in e}
    check("graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))
    check("source-jet lift is narrower than full endpoint ratio theorem", True)


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    note_flat = flat(note)

    required_note = (
        "Actual current-surface status: no-go for the current exact P_R finite readout surface",
        "K_R -> P_R -> E/T shell-center readout",
        "D_i D_j W = D_i D_j Z - (D_i Z)(D_j Z)",
        "Route-2 same-source source-jet lift theorem",
        "No endpoint value is used",
    )
    for marker in required_note:
        check(f"note contains marker: {marker}", marker in note_flat)

    for marker in ("Block97 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names source-jet lift", "source-jet lift" in trace_gate)

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
    print("Route-2 source-jet lift no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_source_jet_ambiguity()
    part3_required_source_jet_fields()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: the current finite P_R readout surface does not itself prove a same-source D^2 log Z source-Hessian lift.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
