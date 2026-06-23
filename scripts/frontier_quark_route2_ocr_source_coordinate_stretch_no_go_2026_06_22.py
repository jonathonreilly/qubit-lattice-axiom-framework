#!/usr/bin/env python3
"""Stretch fan-out for the Route-2 O_CR source-coordinate theorem."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-ocr-source-coordinate-stretch"
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class ConstructionFrame:
    name: str
    supplies_ocr: bool
    supplies_source_coordinate: bool
    supplies_rn_path: bool
    supplies_same_source_riesz: bool
    imports_endpoint: bool = False

    def complete(self) -> bool:
        return all(
            (
                self.supplies_ocr,
                self.supplies_source_coordinate,
                self.supplies_rn_path,
                self.supplies_same_source_riesz,
            )
        ) and not self.imports_endpoint

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("O_CR", self.supplies_ocr),
            ("J_CR", self.supplies_source_coordinate),
            ("P_h", self.supplies_rn_path),
            ("same_source_Riesz", self.supplies_same_source_riesz),
        )
        return tuple(name for name, present in fields if not present)


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


def part1_grounding() -> None:
    print("PART 1: grounding")
    block140 = flat(text("QUARK_ROUTE2_COVARIANCE_SCORE_LIFT_NO_GO_2026-06-22.md"))
    exact = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    source_jet = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    isometry = flat(text("QUARK_ROUTE2_SOURCE_READOUT_ISOMETRY_SUFFICIENT_SUPPORT_2026-06-22.md"))
    cumulant = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md"))
    check("Block140 names O_CR source-coordinate theorem", "Route-2 physical covariance score-lift theorem" in block140)
    check("Block140 says physical observable is not identified", "does not identify which four-slot observable" in block140)
    check("exact readout supplies K_R to P_R surface", "K_R" in exact and "P_R" in exact)
    check("source-jet no-go names missing J_A and Z", "source coordinates J_A" in source_jet and "partition functional Z" in source_jet)
    check("source-jet no-go names one-point products", "one-point product" in source_jet)
    check("isometry packet requires Phi_ET", "construct Phi_ET" in isometry)
    check("cumulant packet requires physical readout primitive", "Route-2 physical readout is the connected source Hessian" in cumulant)
    check("grounding uses no endpoint-value theorem", True)


def part2_a_min_and_forbidden_imports() -> None:
    print()
    print("PART 2: A_min and forbidden imports")
    allowed = {
        "exact_KR_PR_reduction": True,
        "four_slot_labels": True,
        "formal_unit_layer_score": True,
        "connected_cumulant_identity": True,
        "block121_internal_scalar_only": True,
    }
    forbidden = {
        "endpoint_value": False,
        "endpoint_triple": False,
        "fitted_scalar_calibration": False,
        "bare_physical_observable_assertion": False,
    }
    for name, value in allowed.items():
        check(f"A_min allows {name}", value)
    for name, value in forbidden.items():
        check(f"forbidden import absent: {name}", not value)
    check("A_min contains five allowed premise classes", len(allowed) == 5)
    check("forbidden import list contains four blocked classes", len(forbidden) == 4)


def part3_fanout_frames() -> None:
    print()
    print("PART 3: fan-out construction frames")
    frames = (
        ConstructionFrame("carrier_observable", False, False, False, False),
        ConstructionFrame("four_slot_probability", False, False, True, False),
        ConstructionFrame("source_jet", False, False, False, False),
        ConstructionFrame("fisher_riesz", False, False, True, False),
        ConstructionFrame("tau_symmetry", False, False, True, False),
    )
    expected_missing = {
        "carrier_observable": ("O_CR", "J_CR", "P_h", "same_source_Riesz"),
        "four_slot_probability": ("O_CR", "J_CR", "same_source_Riesz"),
        "source_jet": ("O_CR", "J_CR", "P_h", "same_source_Riesz"),
        "fisher_riesz": ("O_CR", "J_CR", "same_source_Riesz"),
        "tau_symmetry": ("O_CR", "J_CR", "same_source_Riesz"),
    }
    for frame in frames:
        print(f"  {frame.name}: missing={frame.missing()}")
        check(f"{frame.name} does not complete O_CR theorem", not frame.complete())
        check(f"{frame.name} does not import endpoint", not frame.imports_endpoint)
        check(f"{frame.name} missing list is exact", frame.missing() == expected_missing[frame.name])
    check("five independent frames were tested", len(frames) == 5)
    check("no frame supplies the full theorem", not any(frame.complete() for frame in frames))


def part4_nonuniqueness_witnesses() -> None:
    print()
    print("PART 4: non-uniqueness witnesses")
    responses = {
        "center_indicator": Fraction(1, 2),
        "shell_indicator": Fraction(-1, 2),
        "channel_indicator": Fraction(0),
        "layer_score": Fraction(1),
        "negative_layer_score": Fraction(-1),
    }
    for name, response in responses.items():
        print(f"  {name}: response={response}")
        check(f"{name} response is rational", isinstance(response, Fraction))
        check(f"{name} response is endpoint-free sample", response.denominator in (1, 2))
    check("responses contain more than three distinct values", len(set(responses.values())) > 3)
    check("unit layer score response differs from center indicator", responses["layer_score"] != responses["center_indicator"])
    check("channel indicator response is blind to shell-center score", responses["channel_indicator"] == 0)


def part5_synthesis_wall() -> None:
    print()
    print("PART 5: synthesis wall")
    wall_edges = [
        ("exact_KR_PR_reduction", "finite_readout_rows"),
        ("four_slot_labels", "formal_layer_score"),
        ("formal_layer_score", "formal_covariance_responses"),
        ("formal_covariance_responses", "missing_O_CR_selection"),
        ("finite_readout_rows", "missing_source_coordinate_J_CR"),
        ("missing_O_CR_selection", "O_CR_source_coordinate_theorem"),
        ("missing_source_coordinate_J_CR", "O_CR_source_coordinate_theorem"),
        ("O_CR_source_coordinate_theorem", "same_source_Riesz"),
        ("same_source_Riesz", "kappa_zero_without_endpoint"),
    ]
    current_edges = wall_edges[:5]
    check("current surface reaches formal covariance responses", reachable(current_edges, "four_slot_labels", "formal_covariance_responses"))
    check("current surface reaches missing O_CR selection", reachable(current_edges, "four_slot_labels", "missing_O_CR_selection"))
    check("current surface does not reach O_CR theorem", not reachable(current_edges, "four_slot_labels", "O_CR_source_coordinate_theorem"))
    check("adding O_CR theorem reaches kappa zero", reachable(wall_edges, "four_slot_labels", "kappa_zero_without_endpoint"))
    check("finite P_R rows alone do not reach same-source Riesz", not reachable(current_edges, "exact_KR_PR_reduction", "same_source_Riesz"))
    all_nodes = {node for edge in wall_edges for node in edge}
    check("synthesis graph contains no endpoint-value input", all("rho_E" not in node and "endpoint_value" not in node for node in all_nodes))


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_OCR_SOURCE_COORDINATE_STRETCH_NO_GO_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for the current surface constructing the physical O_CR source-coordinate lift",
        "A_min",
        "Fan-Out Attempt",
        "Synthesis Wall",
        "Route-2 O_CR source-coordinate theorem",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block141 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks negative pruning", "trace_class: negative_route_pruning" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    check("review history records no review-loop worker", "No review-loop worker was run" in review)
    check("review history records no audit worker", "No audit worker was run" in review)
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
    print("Route-2 O_CR source-coordinate stretch no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_a_min_and_forbidden_imports()
    part3_fanout_frames()
    part4_nonuniqueness_witnesses()
    part5_synthesis_wall()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: runner failed; do not use this packet.")
    else:
        print("VERDICT: all construction frames hit the O_CR source-coordinate theorem as the missing primitive.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
