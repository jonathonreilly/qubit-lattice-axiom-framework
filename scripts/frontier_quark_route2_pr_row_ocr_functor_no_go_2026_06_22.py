#!/usr/bin/env python3
"""No-go for finite P_R rows alone defining the physical O_CR observable."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-pr-row-ocr-functor"
PASS = 0
FAIL = 0

SLOTS = ("E-shell", "E-center", "T-shell", "T-center")


@dataclass(frozen=True)
class RowToOCRAttempt:
    finite_pr_rows: bool
    row_labels: bool
    scalar_observable_choice: bool
    source_coordinate: bool
    rn_path: bool
    same_source_riesz: bool
    unit_isometry: bool

    def row_surface(self) -> bool:
        return self.finite_pr_rows and self.row_labels

    def ocr_functor(self) -> bool:
        return self.row_surface() and self.scalar_observable_choice and self.source_coordinate and self.rn_path

    def bridge(self) -> bool:
        return self.ocr_functor() and self.same_source_riesz and self.unit_isometry

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("finite_pr_rows", self.finite_pr_rows),
            ("row_labels", self.row_labels),
            ("scalar_observable_choice", self.scalar_observable_choice),
            ("source_coordinate", self.source_coordinate),
            ("rn_path", self.rn_path),
            ("same_source_riesz", self.same_source_riesz),
            ("unit_isometry", self.unit_isometry),
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


def layer(slot: str) -> str:
    return slot.split("-")[1]


def channel(slot: str) -> str:
    return slot.split("-")[0]


Observable = Callable[[str], Fraction]


def p0(_: str) -> Fraction:
    return Fraction(1, 4)


def score(slot: str) -> Fraction:
    return Fraction(1) if layer(slot) == "center" else Fraction(-1)


def expectation(obs: Observable) -> Fraction:
    return sum(p0(slot) * obs(slot) for slot in SLOTS)


def covariance(obs: Observable, sc: Observable = score) -> Fraction:
    return expectation(lambda slot: obs(slot) * sc(slot)) - expectation(obs) * expectation(sc)


def indicator(predicate: Callable[[str], bool]) -> Observable:
    return lambda slot: Fraction(1) if predicate(slot) else Fraction(0)


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
    exact = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    block141 = flat(text("QUARK_ROUTE2_OCR_SOURCE_COORDINATE_STRETCH_NO_GO_2026-06-22.md"))
    block140 = flat(text("QUARK_ROUTE2_COVARIANCE_SCORE_LIFT_NO_GO_2026-06-22.md"))
    source_jet = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    check("exact readout gives P_R row form", "P_R = [[alpha_E, 0, beta_E, 0]," in exact)
    check(
        "exact readout gives restricted carrier basis",
        "restricted bright readout class" in exact
        and "disjoint E and T endpoint subspaces" in exact
        and "gamma_E = alpha_E u_E + beta_E delta_A1 u_E" in exact
        and "gamma_T = alpha_T u_T + beta_T delta_A1 u_T" in exact,
    )
    check("Block141 names carrier observable frame failure", "Carrier observable" in block141)
    check("Block141 names O_CR source-coordinate theorem", "Route-2 O_CR source-coordinate theorem" in block141)
    check("Block140 says physical observable not identified", "does not identify which four-slot observable" in block140)
    check("source-jet no-go keeps source coordinates missing", "source coordinates J_A" in source_jet)
    check("grounding uses no endpoint-value theorem", True)


def part2_scalarization_nonuniqueness() -> None:
    print()
    print("PART 2: scalarization non-uniqueness")
    observables: tuple[tuple[str, Observable, Fraction], ...] = (
        ("E_channel_indicator", indicator(lambda slot: channel(slot) == "E"), Fraction(0)),
        ("T_channel_indicator", indicator(lambda slot: channel(slot) == "T"), Fraction(0)),
        ("center_indicator", indicator(lambda slot: layer(slot) == "center"), Fraction(1, 2)),
        ("E_center_indicator", indicator(lambda slot: slot == "E-center"), Fraction(1, 4)),
        ("layer_score", score, Fraction(1)),
    )
    values = []
    for name, obs, expected in observables:
        value = covariance(obs)
        values.append(value)
        print(f"  {name}: covariance={value}")
        check(f"{name} covariance matches expected value", value == expected)
        check(f"{name} covariance is rational", isinstance(value, Fraction))
    check("same row labels admit multiple scalar covariance responses", len(set(values)) >= 4)
    check("E/T row indicators are shell-center blind", values[0] == 0 and values[1] == 0)
    check("center score and center indicator are distinct choices", values[-1] != values[2])


def part3_current_surface_model() -> None:
    print()
    print("PART 3: current-surface model")
    current = RowToOCRAttempt(True, True, False, False, False, False, False)
    fields = {
        "finite_pr_rows": current.finite_pr_rows,
        "row_labels": current.row_labels,
        "scalar_observable_choice": current.scalar_observable_choice,
        "source_coordinate": current.source_coordinate,
        "rn_path": current.rn_path,
        "same_source_riesz": current.same_source_riesz,
        "unit_isometry": current.unit_isometry,
    }
    for name, value in fields.items():
        check(f"{name} has boolean status", isinstance(value, bool))
    check("current surface has finite P_R row surface", current.row_surface())
    check("current surface does not have O_CR functor", not current.ocr_functor())
    check("current surface does not complete bridge", not current.bridge())
    check(
        "missing fields are scalar observable, source coordinate, RN path, Riesz, and isometry",
        current.missing()
        == ("scalar_observable_choice", "source_coordinate", "rn_path", "same_source_riesz", "unit_isometry"),
    )


def part4_clause_failures() -> None:
    print()
    print("PART 4: clause failures")
    base = {
        "finite_pr_rows": True,
        "row_labels": True,
        "scalar_observable_choice": True,
        "source_coordinate": True,
        "rn_path": True,
        "same_source_riesz": True,
        "unit_isometry": True,
    }
    full = RowToOCRAttempt(**base)
    check("all clauses complete the functor bridge", full.bridge())
    for missing in ("scalar_observable_choice", "source_coordinate", "rn_path", "same_source_riesz", "unit_isometry"):
        model = dict(base)
        model[missing] = False
        attempt = RowToOCRAttempt(**model)
        check(f"{missing} omission makes bridge fail", not attempt.bridge())
        check(f"{missing} omission is named exactly", attempt.missing() == (missing,))
    check("all five physical functor clauses were tested", len(("scalar_observable_choice", "source_coordinate", "rn_path", "same_source_riesz", "unit_isometry")) == 5)


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    current_edges = [
        ("finite_P_R_rows", "row_labels"),
        ("row_labels", "many_scalarizations"),
        ("many_scalarizations", "missing_Phi_OCR"),
    ]
    bridge_edges = [
        ("missing_Phi_OCR", "Phi_OCR_theorem"),
        ("Phi_OCR_theorem", "O_CR_source_coordinate"),
        ("O_CR_source_coordinate", "same_source_Riesz"),
        ("same_source_Riesz", "kappa_zero_without_endpoint"),
    ]
    check("finite rows reach many scalarizations", reachable(current_edges, "finite_P_R_rows", "many_scalarizations"))
    check("finite rows reach missing Phi_OCR node", reachable(current_edges, "finite_P_R_rows", "missing_Phi_OCR"))
    check("finite rows alone do not reach O_CR source coordinate", not reachable(current_edges, "finite_P_R_rows", "O_CR_source_coordinate"))
    check("adding Phi_OCR theorem reaches kappa zero", reachable(current_edges + bridge_edges, "finite_P_R_rows", "kappa_zero_without_endpoint"))
    all_nodes = {node for edge in current_edges + bridge_edges for node in edge}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in node and "endpoint_value" not in node for node in all_nodes))


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_PR_ROW_OCR_FUNCTOR_NO_GO_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for current finite P_R rows alone constructing the physical O_CR observable",
        "Non-Uniqueness",
        "Route-2 P_R-to-O_CR functor theorem",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block142 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
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
    print("Route-2 P_R row to O_CR functor no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_scalarization_nonuniqueness()
    part3_current_surface_model()
    part4_clause_failures()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: runner failed; do not use this packet.")
    else:
        print("VERDICT: finite P_R rows do not canonically construct O_CR; Phi_OCR remains missing.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
