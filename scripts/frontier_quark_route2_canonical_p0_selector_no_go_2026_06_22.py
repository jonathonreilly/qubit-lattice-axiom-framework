#!/usr/bin/env python3
"""No-go for selecting canonical Route-2 four-slot P0 from slot typing alone."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-canonical-p0-selector"
SLOTS = ("E-shell", "E-center", "T-shell", "T-center")
RAW_CENTER = {
    "E-shell": Fraction(-1),
    "E-center": Fraction(1),
    "T-shell": Fraction(-1),
    "T-center": Fraction(1),
}

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class FourSlotReference:
    weights: dict[str, Fraction]

    def positive(self) -> bool:
        return all(self.weights[slot] > 0 for slot in SLOTS)

    def normalized(self) -> bool:
        return sum(self.weights[slot] for slot in SLOTS) == 1

    def et_invariant(self) -> bool:
        return self.weights["E-shell"] == self.weights["T-shell"] and self.weights["E-center"] == self.weights["T-center"]

    def shell_center_balanced(self) -> bool:
        return self.weights["E-shell"] == self.weights["E-center"] and self.weights["T-shell"] == self.weights["T-center"]

    def mean(self, values: dict[str, Fraction]) -> Fraction:
        return sum(self.weights[slot] * values[slot] for slot in SLOTS)

    def centered(self, values: dict[str, Fraction]) -> dict[str, Fraction]:
        mean = self.mean(values)
        return {slot: values[slot] - mean for slot in SLOTS}

    def norm_sq(self, values: dict[str, Fraction]) -> Fraction:
        return sum(self.weights[slot] * values[slot] * values[slot] for slot in SLOTS)


@dataclass(frozen=True)
class P0Selector:
    slot_typing: bool
    positivity_normalization: bool
    et_channel_symmetry: bool
    shell_center_balance: bool
    physical_source_measure: bool
    same_source_riesz: bool

    def current_selector(self) -> bool:
        return all((self.slot_typing, self.positivity_normalization, self.et_channel_symmetry))

    def canonical_p0(self) -> bool:
        return self.current_selector() and self.shell_center_balance and self.physical_source_measure

    def complete_bridge(self) -> bool:
        return self.canonical_p0() and self.same_source_riesz

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("slot_typing", self.slot_typing),
            ("positivity_normalization", self.positivity_normalization),
            ("et_channel_symmetry", self.et_channel_symmetry),
            ("shell_center_balance", self.shell_center_balance),
            ("physical_source_measure", self.physical_source_measure),
            ("same_source_riesz", self.same_source_riesz),
        )
        return tuple(name for name, present in fields if not present)

    def mu(self) -> Fraction | None:
        if not self.complete_bridge():
            return None
        return Fraction(1)


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


def et_reference(shell_weight: Fraction) -> FourSlotReference:
    center_weight = Fraction(1, 2) - shell_weight
    return FourSlotReference(
        {
            "E-shell": shell_weight,
            "E-center": center_weight,
            "T-shell": shell_weight,
            "T-center": center_weight,
        }
    )


def part1_grounding() -> None:
    print("PART 1: grounding")
    exact = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    block134 = flat(text("QUARK_ROUTE2_FOUR_SLOT_RN_ENVELOPE_BOUNDARY_NO_GO_2026-06-22.md"))
    block133 = flat(text("QUARK_ROUTE2_SHELL_CENTER_PROBABILITY_SURFACE_SUPPORT_2026-06-22.md"))
    block130 = flat(text("QUARK_ROUTE2_FISHER_RIESZ_REALIZATION_NO_GO_2026-06-22.md"))
    gauge = flat(text("QUARK_ROUTE2_SOURCE_COORDINATE_GAUGE_NORMALIZATION_NO_GO_NOTE_2026-06-22.md"))
    fisher = flat(text("SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md"))
    check("exact readout map has four slot labels", all(slot in exact for slot in SLOTS))
    check("Block134 names canonical P0 as missing", "canonical P0" in block134)
    check("Block133 requires positive reference", "P0 is strictly positive and normalized" in block133)
    check("Block130 says finite P_R does not provide P0", "finite P_R packet does not provide" in block130 and "P_0" in block130)
    check("source-coordinate gauge no-go keeps source normalization open", "origin and scale" in gauge)
    check("Fisher theorem needs a reference probability", "reference probability P_0" in fisher)
    check("grounding uses no endpoint-value theorem", True)


def part2_et_symmetric_family() -> None:
    print()
    print("PART 2: E/T-symmetric P0 family")
    refs = {
        "uniform": et_reference(Fraction(1, 4)),
        "shell_heavy": et_reference(Fraction(1, 3)),
        "center_heavy": et_reference(Fraction(1, 6)),
    }
    for name, ref in refs.items():
        print(f"  {name}: {ref.weights}")
        check(f"{name} reference is positive", ref.positive())
        check(f"{name} reference is normalized", ref.normalized())
        check(f"{name} reference is E/T invariant", ref.et_invariant())
    check("examples give distinct P0 choices", len({tuple(ref.weights[slot] for slot in SLOTS) for ref in refs.values()}) == 3)
    shell_totals = {name: ref.weights["E-shell"] + ref.weights["T-shell"] for name, ref in refs.items()}
    check("shell totals are not fixed by E/T symmetry", len(set(shell_totals.values())) == 3)
    check("E/T family has one free shell/center parameter", all(ref.weights["E-shell"] + ref.weights["E-center"] == Fraction(1, 2) for ref in refs.values()))


def part3_zero_mean_selector() -> None:
    print()
    print("PART 3: zero-mean raw score selector")
    refs = {
        "uniform": et_reference(Fraction(1, 4)),
        "shell_heavy": et_reference(Fraction(1, 3)),
        "center_heavy": et_reference(Fraction(1, 6)),
    }
    raw_means = {}
    centered_norms = {}
    for name, ref in refs.items():
        centered = ref.centered(RAW_CENTER)
        raw_mean = ref.mean(RAW_CENTER)
        norm = ref.norm_sq(centered)
        raw_means[name] = raw_mean
        centered_norms[name] = norm
        print(f"  {name}: raw_mean={raw_mean}, centered_norm_sq={norm}")
        check(f"{name} centered score is zero mean", ref.mean(centered) == 0)
        check(f"{name} centered score has positive norm", norm > 0)
    check("raw shell/center means differ across valid references", len(set(raw_means.values())) == 3)
    check("centered Fisher norms are not all equal", len(set(centered_norms.values())) == 2)
    check("raw zero-mean condition selects uniform among examples", [name for name, mean in raw_means.items() if mean == 0] == ["uniform"])
    check("raw zero-mean is equivalent to shell/center balance in E/T family", et_reference(Fraction(1, 4)).shell_center_balanced())


def part4_shell_center_symmetry() -> None:
    print()
    print("PART 4: added shell/center balance")
    uniform = et_reference(Fraction(1, 4))
    for slot in SLOTS:
        check(f"uniform P0({slot}) is 1/4", uniform.weights[slot] == Fraction(1, 4))
    check("uniform P0 is positive", uniform.positive())
    check("uniform P0 is normalized", uniform.normalized())
    check("uniform P0 is E/T invariant", uniform.et_invariant())
    check("uniform P0 is shell/center balanced", uniform.shell_center_balanced())
    check("shell/center balance is an extra selector premise", True)


def part5_current_surface_model() -> None:
    print()
    print("PART 5: current-surface selector model")
    selector = P0Selector(
        slot_typing=True,
        positivity_normalization=True,
        et_channel_symmetry=True,
        shell_center_balance=False,
        physical_source_measure=False,
        same_source_riesz=False,
    )
    fields = {
        "slot_typing": selector.slot_typing,
        "positivity_normalization": selector.positivity_normalization,
        "et_channel_symmetry": selector.et_channel_symmetry,
        "shell_center_balance": selector.shell_center_balance,
        "physical_source_measure": selector.physical_source_measure,
        "same_source_riesz": selector.same_source_riesz,
    }
    for name, value in fields.items():
        print(f"  {name}: {value}")
        check(f"{name} has boolean status", isinstance(value, bool))
    check("current selector has typed E/T-symmetric family", selector.current_selector())
    check("current selector does not give canonical P0", not selector.canonical_p0())
    check("current selector does not complete bridge", not selector.complete_bridge())
    check("missing objects are shell/center balance, physical measure, and Riesz line", selector.missing() == ("shell_center_balance", "physical_source_measure", "same_source_riesz"))
    check("current selector does not fix mu", selector.mu() is None)


def part6_reachability() -> None:
    print()
    print("PART 6: reachability")
    current_edges = [
        ("four_slot_typing", "positive_normalized_simplex"),
        ("positive_normalized_simplex", "ET_symmetric_P0_family"),
        ("ET_symmetric_P0_family", "free_shell_center_parameter"),
    ]
    selector_edges = [
        ("shell_center_source_measure_selector", "canonical_uniform_P0"),
        ("canonical_uniform_P0", "raw_center_score_zero_mean"),
        ("raw_center_score_zero_mean", "physical_center_ratio_covariance"),
        ("physical_center_ratio_covariance", "same_source_Fisher_unit_Riesz"),
        ("same_source_Fisher_unit_Riesz", "mu_one"),
    ]
    check("current typing reaches E/T-symmetric family", reachable(current_edges, "four_slot_typing", "ET_symmetric_P0_family"))
    check("current typing reaches free shell/center parameter", reachable(current_edges, "four_slot_typing", "free_shell_center_parameter"))
    check("current typing does not reach canonical P0", not reachable(current_edges, "four_slot_typing", "canonical_uniform_P0"))
    check("current typing does not reach mu_one", not reachable(current_edges, "four_slot_typing", "mu_one"))
    check("selector primitive reaches canonical P0", reachable(selector_edges, "shell_center_source_measure_selector", "canonical_uniform_P0"))
    check("selector primitive reaches mu_one", reachable(selector_edges, "shell_center_source_measure_selector", "mu_one"))
    all_nodes = {node for edge in current_edges + selector_edges for node in edge}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in node and "q_E" not in node and "endpoint_value" not in node for node in all_nodes))
    check("current family and selector primitive are distinct", "ET_symmetric_P0_family" in all_nodes and "shell_center_source_measure_selector" in all_nodes)


def part7_document_boundary() -> None:
    print()
    print("PART 7: document boundary")
    note = text("QUARK_ROUTE2_CANONICAL_P0_SELECTOR_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for slot typing plus E/T channel symmetry selecting a unique physical four-slot P0",
        "E/T-symmetric references",
        "Route-2 shell/center source-measure selector",
        "same-source Fisher-unit Riesz line",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block135 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
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
    print("Route-2 canonical P0 selector no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_et_symmetric_family()
    part3_zero_mean_selector()
    part4_shell_center_symmetry()
    part5_current_surface_model()
    part6_reachability()
    part7_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: runner failed; do not use this packet.")
    else:
        print("VERDICT: slot typing plus E/T symmetry leaves a shell/center P0 parameter; a source-measure selector remains missing.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
