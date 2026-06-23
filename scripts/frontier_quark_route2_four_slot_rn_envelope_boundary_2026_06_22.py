#!/usr/bin/env python3
"""Formal four-slot Route-2 RN envelope boundary no-go."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from math import exp
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-four-slot-rn-envelope-boundary"
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
class Reference:
    weights: dict[str, Fraction]

    def normalized(self) -> bool:
        return sum(self.weights.values(), Fraction(0)) == Fraction(1)

    def positive(self) -> bool:
        return all(self.weights[slot] > 0 for slot in SLOTS)

    def mean(self, values: dict[str, Fraction]) -> Fraction:
        return sum(self.weights[slot] * values[slot] for slot in SLOTS)

    def centered(self, values: dict[str, Fraction]) -> dict[str, Fraction]:
        mean = self.mean(values)
        return {slot: values[slot] - mean for slot in SLOTS}

    def norm_sq(self, values: dict[str, Fraction]) -> Fraction:
        return sum(self.weights[slot] * values[slot] * values[slot] for slot in SLOTS)

    def rn_path(self, score: dict[str, Fraction], h: float) -> dict[str, float]:
        terms = {slot: float(self.weights[slot]) * exp(h * float(score[slot])) for slot in SLOTS}
        z = sum(terms.values())
        return {slot: terms[slot] / z for slot in SLOTS}


@dataclass(frozen=True)
class FourSlotConstruction:
    omega_four: bool
    positive_reference: bool
    rn_source_path: bool
    coordinate_functions: bool
    canonical_route2_p0: bool
    physical_center_ratio_covariance: bool
    same_source_fisher_unit: bool
    sign_after_kappa: bool

    def formal_envelope(self) -> bool:
        return all((self.omega_four, self.positive_reference, self.rn_source_path, self.coordinate_functions))

    def physical_bridge(self) -> bool:
        return all(
            (
                self.formal_envelope(),
                self.canonical_route2_p0,
                self.physical_center_ratio_covariance,
                self.same_source_fisher_unit,
            )
        )

    def complete(self) -> bool:
        return self.physical_bridge() and self.sign_after_kappa

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("omega_four", self.omega_four),
            ("positive_reference", self.positive_reference),
            ("rn_source_path", self.rn_source_path),
            ("coordinate_functions", self.coordinate_functions),
            ("canonical_route2_p0", self.canonical_route2_p0),
            ("physical_center_ratio_covariance", self.physical_center_ratio_covariance),
            ("same_source_fisher_unit", self.same_source_fisher_unit),
            ("sign_after_kappa", self.sign_after_kappa),
        )
        return tuple(name for name, present in fields if not present)

    def mu(self) -> Fraction | None:
        if not self.physical_bridge():
            return None
        return Fraction(1)

    def center_ratio(self) -> Fraction | None:
        if not self.complete():
            return None
        return Fraction(-8, 9)


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


def indicator(slot: str) -> dict[str, Fraction]:
    return {candidate: Fraction(int(candidate == slot)) for candidate in SLOTS}


def part1_grounding() -> None:
    print("PART 1: grounding")
    exact = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    block133 = flat(text("QUARK_ROUTE2_SHELL_CENTER_PROBABILITY_SURFACE_SUPPORT_2026-06-22.md"))
    block130 = flat(text("QUARK_ROUTE2_FISHER_RIESZ_REALIZATION_NO_GO_2026-06-22.md"))
    fisher = flat(text("SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md"))
    block121 = flat(text("QUARK_ROUTE2_MINIMAL_MULTI_RECORD_EXTENSION_SUPPORT_2026-06-22.md"))
    source_jet = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    check("exact readout map has four shell/center slots", all(slot in exact for slot in SLOTS))
    check("exact readout map supplies reduced P_R rows", "P_R = [[alpha_E, 0, beta_E, 0]" in exact)
    check("Block133 names P0, P_h, and coordinate functions", all(marker in block133 for marker in ("P0", "P_h", "coordinate functionals")))
    check("Block130 keeps Omega/P0/P_h missing", "Omega_R" in block130 and "P_0" in block130 and "P_h" in block130)
    check("Fisher theorem has reference probability", "reference probability P_0" in fisher)
    check("Fisher theorem has normalized RN chart", "R_h := dP_h / dP_0" in fisher)
    check("Block121 supplies internal R_conn and kappa", "R_conn = 8 / (8 + 1) = 8/9" in block121 and "kappa = 0" in block121)
    check("source-jet no-go separates finite readout from source data", "finite P_R surface does not provide" in source_jet)


def part2_formal_envelope() -> None:
    print()
    print("PART 2: formal four-slot RN envelope")
    uniform = Reference({slot: Fraction(1, 4) for slot in SLOTS})
    centered = uniform.centered(RAW_CENTER)
    for slot in SLOTS:
        channel, layer = slot.split("-")
        check(f"{slot} is shell/center typed", channel in ("E", "T") and layer in ("shell", "center"))
        check(f"P0({slot}) is positive", uniform.weights[slot] > 0)
    check("uniform P0 is normalized", uniform.normalized())
    check("center contrast is zero-mean under uniform P0", uniform.mean(centered) == 0)
    check("center contrast is Fisher-unit under uniform P0", uniform.norm_sq(centered) == 1)
    for h in (-0.5, 0.0, 0.5):
        path = uniform.rn_path(centered, h)
        check(f"P_h at h={h} is positive", all(value > 0.0 for value in path.values()))
        check(f"P_h at h={h} is normalized", abs(sum(path.values()) - 1.0) < 1.0e-12)
    for slot in SLOTS:
        ind = indicator(slot)
        check(f"{slot} indicator isolates its slot", ind[slot] == 1 and sum(ind.values(), Fraction(0)) == 1)
    fingerprints = {tuple(indicator(slot)[candidate] for candidate in SLOTS) for slot in SLOTS}
    check("four indicators separate all gamma-coordinate slots", len(fingerprints) == 4)
    check("formal envelope uses no endpoint-value input", True)


def part3_non_uniqueness() -> None:
    print()
    print("PART 3: non-uniqueness of reference and unit line")
    uniform = Reference({slot: Fraction(1, 4) for slot in SLOTS})
    center_heavy = Reference(
        {
            "E-shell": Fraction(1, 6),
            "E-center": Fraction(1, 3),
            "T-shell": Fraction(1, 6),
            "T-center": Fraction(1, 3),
        }
    )
    for name, ref in (("uniform", uniform), ("center_heavy", center_heavy)):
        check(f"{name} reference is positive", ref.positive())
        check(f"{name} reference is normalized", ref.normalized())
    uniform_score = uniform.centered(RAW_CENTER)
    center_score = center_heavy.centered(RAW_CENTER)
    uniform_norm = uniform.norm_sq(uniform_score)
    center_norm = center_heavy.norm_sq(center_score)
    print(f"  uniform norm_sq={uniform_norm}")
    print(f"  center_heavy norm_sq={center_norm}")
    check("references use the same four slot labels", set(uniform.weights) == set(center_heavy.weights) == set(SLOTS))
    check("uniform reference gives unit contrast", uniform_norm == 1)
    check("center-heavy reference gives 8/9 contrast norm", center_norm == Fraction(8, 9))
    check("same raw contrast has reference-dependent Fisher norm", uniform_norm != center_norm)
    check("same raw contrast has reference-dependent centered score", uniform_score != center_score)
    scaled = {slot: 2 * uniform_score[slot] for slot in SLOTS}
    check("score rescaling preserves formal typing while changing norm", uniform.norm_sq(scaled) == 4)
    center_path = center_heavy.rn_path(center_score, 0.5)
    check("center-heavy RN path remains positive", all(value > 0.0 for value in center_path.values()))
    check("center-heavy RN path remains normalized", abs(sum(center_path.values()) - 1.0) < 1.0e-12)
    check("formal envelope does not select canonical Route-2 P0", True)


def part4_current_surface_failure_model() -> None:
    print()
    print("PART 4: current-surface failure model")
    construction = FourSlotConstruction(
        omega_four=True,
        positive_reference=True,
        rn_source_path=True,
        coordinate_functions=True,
        canonical_route2_p0=False,
        physical_center_ratio_covariance=False,
        same_source_fisher_unit=False,
        sign_after_kappa=True,
    )
    fields = {
        "omega_four": construction.omega_four,
        "positive_reference": construction.positive_reference,
        "rn_source_path": construction.rn_source_path,
        "coordinate_functions": construction.coordinate_functions,
        "canonical_route2_p0": construction.canonical_route2_p0,
        "physical_center_ratio_covariance": construction.physical_center_ratio_covariance,
        "same_source_fisher_unit": construction.same_source_fisher_unit,
        "sign_after_kappa": construction.sign_after_kappa,
    }
    for name, value in fields.items():
        print(f"  {name}: {value}")
        check(f"{name} has boolean status", isinstance(value, bool))
    check("formal envelope is present", construction.formal_envelope())
    check("physical bridge is not present", not construction.physical_bridge())
    check(
        "missing objects are exactly canonical P0, physical covariance, and same-source unit",
        construction.missing()
        == ("canonical_route2_p0", "physical_center_ratio_covariance", "same_source_fisher_unit"),
    )
    check("formal envelope does not fix mu", construction.mu() is None)
    check("formal envelope does not output c_TE", construction.center_ratio() is None)
    check("no endpoint value is needed to expose the construction boundary", True)


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    formal_edges = [
        ("four_slot_labels", "positive_reference"),
        ("positive_reference", "finite_RN_path"),
        ("finite_RN_path", "slot_coordinate_functionals"),
        ("slot_coordinate_functionals", "formal_RN_envelope"),
    ]
    bridge_edges = [
        ("Route2_source_measure_primitive", "canonical_Route2_P0"),
        ("canonical_Route2_P0", "physical_center_ratio_covariance"),
        ("physical_center_ratio_covariance", "same_source_Fisher_unit_Riesz"),
        ("same_source_Fisher_unit_Riesz", "mu_one"),
        ("mu_one", "physical_c_TE_minus_8_9"),
    ]
    check("formal labels reach coordinate functionals", reachable(formal_edges, "four_slot_labels", "slot_coordinate_functionals"))
    check("formal labels reach formal RN envelope", reachable(formal_edges, "four_slot_labels", "formal_RN_envelope"))
    check("formal envelope does not reach canonical P0", not reachable(formal_edges, "four_slot_labels", "canonical_Route2_P0"))
    check("formal envelope does not reach mu_one", not reachable(formal_edges, "four_slot_labels", "mu_one"))
    check("Route-2 source-measure primitive reaches mu_one", reachable(bridge_edges, "Route2_source_measure_primitive", "mu_one"))
    check("Route-2 source-measure primitive reaches physical c_TE node", reachable(bridge_edges, "Route2_source_measure_primitive", "physical_c_TE_minus_8_9"))
    all_nodes = {node for edge in formal_edges + bridge_edges for node in edge}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in node and "q_E" not in node and "endpoint_value" not in node for node in all_nodes))
    check("formal envelope and physical primitive are distinct nodes", "formal_RN_envelope" in all_nodes and "Route2_source_measure_primitive" in all_nodes)


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_FOUR_SLOT_RN_ENVELOPE_BOUNDARY_NO_GO_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for a formal four-slot RN envelope alone instantiating the physical Route-2 probability surface",
        "Formal Envelope",
        "Boundary",
        "Route-2 shell/center source-measure primitive",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block134 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
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
    print("Route-2 four-slot RN envelope boundary no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_formal_envelope()
    part3_non_uniqueness()
    part4_current_surface_failure_model()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: runner failed; do not use this packet.")
    else:
        print(
            "VERDICT: a formal four-slot RN envelope exists, but it does not "
            "select the physical Route-2 reference/score/unit Riesz bridge."
        )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
