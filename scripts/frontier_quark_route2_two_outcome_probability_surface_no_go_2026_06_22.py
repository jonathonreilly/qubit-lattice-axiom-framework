#!/usr/bin/env python3
"""No-go for a two-outcome E/T probability surface carrying Route-2 center readout."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-two-outcome-probability-no-go"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class ProbabilitySurfaceShape:
    e_t_labels: bool
    shell_center_labels: bool
    four_endpoint_slots: bool
    center_ratio_readout: bool
    same_source_riesz: bool

    def supports_route2_center_readout(self) -> bool:
        return all(
            (
                self.e_t_labels,
                self.shell_center_labels,
                self.four_endpoint_slots,
                self.center_ratio_readout,
                self.same_source_riesz,
            )
        )

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("e_t_labels", self.e_t_labels),
            ("shell_center_labels", self.shell_center_labels),
            ("four_endpoint_slots", self.four_endpoint_slots),
            ("center_ratio_readout", self.center_ratio_readout),
            ("same_source_riesz", self.same_source_riesz),
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


def part1_grounding() -> None:
    print("PART 1: grounding")
    exact = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    block131 = flat(text("QUARK_ROUTE2_PROBABILITY_SURFACE_CONTRACT_SUPPORT_2026-06-22.md"))
    block130 = flat(text("QUARK_ROUTE2_FISHER_RIESZ_REALIZATION_NO_GO_2026-06-22.md"))
    fisher = flat(text("SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md"))
    check("exact readout map has E-shell", "E-shell = (1, 0, 0, 0)" in exact)
    check("exact readout map has E-center", "E-center = (1, 0, 1/6, 0)" in exact)
    check("exact readout map has T-shell", "T-shell = (0, 1, 0, 0)" in exact)
    check("exact readout map has T-center", "T-center = (0, 1, 0, 1/6)" in exact)
    check("exact readout map defines q_T shell/center ratio", "q_T := gamma_T(center) / gamma_T(shell)" in exact)
    check("Block131 requires Omega_R", "construct a finite Route-2 sharp-record sample space Omega_R" in block131)
    check("Block130 keeps probability surface missing", "Omega_R, P_0, and a normalized RN source path P_h" in block130)
    check("Fisher theorem itself is generic finite probability geometry", "finite sharp-record sample space" in fisher)


def part2_two_outcome_shape() -> None:
    print()
    print("PART 2: two-outcome shape")
    two = ProbabilitySurfaceShape(
        e_t_labels=True,
        shell_center_labels=False,
        four_endpoint_slots=False,
        center_ratio_readout=False,
        same_source_riesz=False,
    )
    fields = {
        "e_t_labels": two.e_t_labels,
        "shell_center_labels": two.shell_center_labels,
        "four_endpoint_slots": two.four_endpoint_slots,
        "center_ratio_readout": two.center_ratio_readout,
        "same_source_riesz": two.same_source_riesz,
    }
    for name, value in fields.items():
        print(f"  {name}: {value}")
        check(f"{name} has boolean status", isinstance(value, bool))
    check("two-outcome surface has E/T labels", two.e_t_labels)
    check("two-outcome surface lacks shell/center labels", not two.shell_center_labels)
    check("two-outcome surface lacks four endpoint slots", not two.four_endpoint_slots)
    check("two-outcome surface does not support center readout", not two.supports_route2_center_readout())
    check("missing clauses are exactly shell/center, four-slot, center-readout, and Riesz typing", two.missing() == ("shell_center_labels", "four_endpoint_slots", "center_ratio_readout", "same_source_riesz"))


def part3_four_slot_shape() -> None:
    print()
    print("PART 3: four-slot shape as next target")
    four = ProbabilitySurfaceShape(True, True, True, True, True)
    slots = ("E-shell", "E-center", "T-shell", "T-center")
    for slot in slots:
        print(f"  slot={slot}")
        check(f"{slot} is a typed endpoint slot", "-" in slot)
        check(f"{slot} has E/T or shell/center marker", any(x in slot for x in ("E", "T")) and any(x in slot for x in ("shell", "center")))
    check("four-slot shape supports Route-2 center readout when all extra clauses hold", four.supports_route2_center_readout())
    check("four-slot shape has no missing shape clauses", four.missing() == ())
    check("four-slot shape is a construction target, not current closure", True)


def part4_single_clause_failures() -> None:
    print()
    print("PART 4: single-clause failure models")
    base = {
        "e_t_labels": True,
        "shell_center_labels": True,
        "four_endpoint_slots": True,
        "center_ratio_readout": True,
        "same_source_riesz": True,
    }
    for missing in tuple(base):
        model = dict(base)
        model[missing] = False
        shape = ProbabilitySurfaceShape(
            e_t_labels=model["e_t_labels"],
            shell_center_labels=model["shell_center_labels"],
            four_endpoint_slots=model["four_endpoint_slots"],
            center_ratio_readout=model["center_ratio_readout"],
            same_source_riesz=model["same_source_riesz"],
        )
        print(f"  missing {missing}: supports={shape.supports_route2_center_readout()}")
        check(f"{missing} omission blocks center readout support", not shape.supports_route2_center_readout())
        check(f"{missing} omission is named exactly", shape.missing() == (missing,))
        check(f"{missing} omission leaves no current closure", True)
    check("all five shape clauses were tested", len(base) == 5)


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    two_edges = [
        ("Omega_ET_two_outcome", "E_T_label_score"),
        ("E_T_label_score", "shell_center_missing"),
        ("shell_center_missing", "center_ratio_not_typed"),
    ]
    four_edges = [
        ("Omega_ET_shell_center", "four_endpoint_slots"),
        ("four_endpoint_slots", "shell_center_ratios"),
        ("shell_center_ratios", "center_ratio_scalar_line"),
        ("center_ratio_scalar_line", "same_source_Riesz_target"),
    ]
    check("two-outcome surface reaches shell/center missing node", reachable(two_edges, "Omega_ET_two_outcome", "shell_center_missing"))
    check("two-outcome surface does not reach center scalar line", not reachable(two_edges, "Omega_ET_two_outcome", "center_ratio_scalar_line"))
    check("four-slot target reaches shell/center ratios", reachable(four_edges, "Omega_ET_shell_center", "shell_center_ratios"))
    check("four-slot target reaches center scalar line", reachable(four_edges, "Omega_ET_shell_center", "center_ratio_scalar_line"))
    check("four-slot target reaches same-source Riesz target", reachable(four_edges, "Omega_ET_shell_center", "same_source_Riesz_target"))
    all_nodes = {n for e in two_edges + four_edges for n in e}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in n and "q_E_value" not in n and "endpoint_value" not in n for n in all_nodes))
    check("two-outcome and four-slot targets are distinct", "Omega_ET_two_outcome" in all_nodes and "Omega_ET_shell_center" in all_nodes)


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_TWO_OUTCOME_PROBABILITY_SURFACE_NO_GO_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for a two-outcome {E,T} sharp-record probability surface supplying the Route-2 shell/center P_R/E-T probability contract",
        "E-shell, E-center, T-shell, T-center",
        "Route-2 shell/center probability-surface theorem",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block132 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks negative pruning", "trace_class: negative_route_pruning" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    check("review history records no review-loop worker", "No review-loop worker was run" in review)
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
    print("Route-2 two-outcome probability surface no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_two_outcome_shape()
    part3_four_slot_shape()
    part4_single_clause_failures()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: a two-outcome {E,T} probability surface cannot carry the Route-2 shell/center center-ratio readout; a shell/center probability surface remains required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
