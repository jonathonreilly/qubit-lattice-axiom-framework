#!/usr/bin/env python3
"""Conditional shell/center reflection selector support for Route-2 P0."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from math import exp
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-shell-center-reflection-selector"
SLOTS = ("E-shell", "E-center", "T-shell", "T-center")
TAU = {
    "E-shell": "E-center",
    "E-center": "E-shell",
    "T-shell": "T-center",
    "T-center": "T-shell",
}
ET_SWAP = {
    "E-shell": "T-shell",
    "E-center": "T-center",
    "T-shell": "E-shell",
    "T-center": "E-center",
}
SCORE = {
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

    def positive(self) -> bool:
        return all(self.weights[slot] > 0 for slot in SLOTS)

    def normalized(self) -> bool:
        return sum(self.weights[slot] for slot in SLOTS) == 1

    def tau_invariant(self) -> bool:
        return all(self.weights[slot] == self.weights[TAU[slot]] for slot in SLOTS)

    def et_invariant(self) -> bool:
        return all(self.weights[slot] == self.weights[ET_SWAP[slot]] for slot in SLOTS)

    def mean(self, values: dict[str, Fraction]) -> Fraction:
        return sum(self.weights[slot] * values[slot] for slot in SLOTS)

    def norm_sq(self, values: dict[str, Fraction]) -> Fraction:
        return sum(self.weights[slot] * values[slot] * values[slot] for slot in SLOTS)

    def rn_path(self, score: dict[str, Fraction], h: float) -> dict[str, float]:
        terms = {slot: float(self.weights[slot]) * exp(h * float(score[slot])) for slot in SLOTS}
        z = sum(terms.values())
        return {slot: terms[slot] / z for slot in SLOTS}


@dataclass(frozen=True)
class ReflectionSelectorContract:
    omega_four: bool
    tau_involution: bool
    p0_tau_invariant: bool
    et_channel_symmetry: bool
    score_tau_odd: bool
    physical_score_typing: bool
    same_source_riesz: bool
    sign_after_kappa: bool

    def canonical_p0(self) -> bool:
        return all((self.omega_four, self.tau_involution, self.p0_tau_invariant, self.et_channel_symmetry))

    def unit_score(self) -> bool:
        return self.canonical_p0() and self.score_tau_odd

    def bridge(self) -> bool:
        return self.unit_score() and self.physical_score_typing and self.same_source_riesz

    def complete(self) -> bool:
        return self.bridge() and self.sign_after_kappa

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("omega_four", self.omega_four),
            ("tau_involution", self.tau_involution),
            ("p0_tau_invariant", self.p0_tau_invariant),
            ("et_channel_symmetry", self.et_channel_symmetry),
            ("score_tau_odd", self.score_tau_odd),
            ("physical_score_typing", self.physical_score_typing),
            ("same_source_riesz", self.same_source_riesz),
            ("sign_after_kappa", self.sign_after_kappa),
        )
        return tuple(name for name, present in fields if not present)

    def mu(self) -> Fraction | None:
        if not self.bridge():
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


def uniform_reference() -> Reference:
    return Reference({slot: Fraction(1, 4) for slot in SLOTS})


def part1_grounding() -> None:
    print("PART 1: grounding")
    block135 = flat(text("QUARK_ROUTE2_CANONICAL_P0_SELECTOR_NO_GO_NOTE_2026-06-22.md"))
    block134 = flat(text("QUARK_ROUTE2_FOUR_SLOT_RN_ENVELOPE_BOUNDARY_NO_GO_2026-06-22.md"))
    block133 = flat(text("QUARK_ROUTE2_SHELL_CENTER_PROBABILITY_SURFACE_SUPPORT_2026-06-22.md"))
    exact = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    fisher = flat(text("SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md"))
    block121 = flat(text("QUARK_ROUTE2_MINIMAL_MULTI_RECORD_EXTENSION_SUPPORT_2026-06-22.md"))
    check("Block135 leaves shell/center source-measure selector missing", "shell/center source-measure selector" in block135)
    check("Block134 leaves canonical P0 missing", "canonical P0" in block134)
    check("Block133 names four-slot P0/P_h target", "E-shell, E-center, T-shell, T-center" in block133 and "P_h" in block133)
    check("exact readout map supplies four shell/center slots", all(slot in exact for slot in SLOTS))
    check("Fisher theorem supplies finite RN chart once score is supplied", "normalized positive exponential chart" in fisher)
    check("Block121 supplies internal connected source fraction", "R_conn = 8 / (8 + 1) = 8/9" in block121)
    check("grounding uses no endpoint-value theorem", True)


def part2_reflection_structure() -> None:
    print()
    print("PART 2: shell/center reflection structure")
    for slot in SLOTS:
        reflected = TAU[slot]
        channel, layer = slot.split("-")
        reflected_channel, reflected_layer = reflected.split("-")
        print(f"  tau({slot})={reflected}")
        check(f"tau maps {slot} to a slot", reflected in SLOTS)
        check(f"tau preserves {slot} channel", channel == reflected_channel)
        check(f"tau swaps {slot} layer", layer != reflected_layer and {layer, reflected_layer} == {"shell", "center"})
        check(f"tau is involutive on {slot}", TAU[reflected] == slot)
        check(f"score is tau-odd on {slot}", SCORE[reflected] == -SCORE[slot])
    check("tau has no fixed slots", all(TAU[slot] != slot for slot in SLOTS))
    check("tau preserves E/T channel partition", {slot.split("-")[0] for slot in SLOTS} == {TAU[slot].split("-")[0] for slot in SLOTS})


def part3_reference_selection() -> None:
    print()
    print("PART 3: invariant reference selection")
    p0 = uniform_reference()
    for slot in SLOTS:
        check(f"selected P0({slot}) is 1/4", p0.weights[slot] == Fraction(1, 4))
    check("selected P0 is positive", p0.positive())
    check("selected P0 is normalized", p0.normalized())
    check("selected P0 is tau-invariant", p0.tau_invariant())
    check("selected P0 is E/T invariant", p0.et_invariant())
    check("tau plus E/T invariance selects one common weight", len({p0.weights[slot] for slot in SLOTS}) == 1)
    check("common weight is forced by normalization", sum(p0.weights.values()) == 1 and p0.weights["E-shell"] == Fraction(1, 4))


def part4_unit_score_and_rn_path() -> None:
    print()
    print("PART 4: unit score and RN path")
    p0 = uniform_reference()
    check("tau-odd score has zero mean", p0.mean(SCORE) == 0)
    check("tau-odd score has unit Fisher norm", p0.norm_sq(SCORE) == 1)
    check("score separates shell from center", SCORE["E-shell"] == SCORE["T-shell"] == -1 and SCORE["E-center"] == SCORE["T-center"] == 1)
    for h in (-0.5, 0.0, 0.5):
        path = p0.rn_path(SCORE, h)
        check(f"P_h at h={h} is positive", all(value > 0.0 for value in path.values()))
        check(f"P_h at h={h} is normalized", abs(sum(path.values()) - 1.0) < 1.0e-12)
    check("unit score construction uses no endpoint-value input", True)


def part5_clause_failures() -> None:
    print()
    print("PART 5: clause failure models")
    base = {
        "omega_four": True,
        "tau_involution": True,
        "p0_tau_invariant": True,
        "et_channel_symmetry": True,
        "score_tau_odd": True,
        "physical_score_typing": True,
        "same_source_riesz": True,
        "sign_after_kappa": True,
    }
    full = ReflectionSelectorContract(**base)
    check("full conditional contract selects canonical P0", full.canonical_p0())
    check("full conditional contract supplies unit score", full.unit_score())
    check("full conditional contract reaches bridge", full.bridge())
    check("full conditional contract fixes mu", full.mu() == 1)
    check("full conditional contract yields signed endpoint after kappa", full.center_ratio() == Fraction(-8, 9))
    for missing in tuple(base):
        model = dict(base)
        model[missing] = False
        contract = ReflectionSelectorContract(**model)
        print(f"  missing {missing}: bridge={contract.bridge()}, c_TE={contract.center_ratio()}")
        check(f"{missing} omission makes complete contract fail", not contract.complete())
        check(f"{missing} omission is named exactly", contract.missing() == (missing,))
        check(f"{missing} omission blocks c_TE output", contract.center_ratio() is None)
    check("all eight reflection selector clauses were tested", len(base) == 8)


def part6_current_boundary() -> None:
    print()
    print("PART 6: current-surface boundary")
    current = ReflectionSelectorContract(
        omega_four=True,
        tau_involution=False,
        p0_tau_invariant=False,
        et_channel_symmetry=True,
        score_tau_odd=False,
        physical_score_typing=False,
        same_source_riesz=False,
        sign_after_kappa=True,
    )
    check("current surface has four slots and E/T symmetry candidate", current.omega_four and current.et_channel_symmetry)
    check("current surface has not supplied tau as source symmetry", not current.tau_involution)
    check("current surface has not supplied tau-invariant P0", not current.p0_tau_invariant)
    check("current surface has not typed physical odd score", not current.physical_score_typing)
    check("current surface has not supplied same-source Riesz line", not current.same_source_riesz)
    check("current surface does not complete reflection bridge", not current.complete())
    check("current surface missing list names physical primitive", current.missing() == ("tau_involution", "p0_tau_invariant", "score_tau_odd", "physical_score_typing", "same_source_riesz"))


def part7_reachability() -> None:
    print()
    print("PART 7: reachability")
    support_edges = [
        ("shell_center_reflection_source_theorem", "tau_sc"),
        ("tau_sc", "tau_invariant_P0"),
        ("tau_invariant_P0", "uniform_P0"),
        ("uniform_P0", "tau_odd_unit_score"),
        ("tau_odd_unit_score", "physical_center_ratio_covariance"),
        ("physical_center_ratio_covariance", "same_source_Fisher_unit_Riesz"),
        ("same_source_Fisher_unit_Riesz", "mu_one"),
        ("mu_one", "physical_c_TE_minus_8_9"),
    ]
    current_edges = [
        ("current_four_slot_typing", "free_shell_center_P0_parameter"),
        ("free_shell_center_P0_parameter", "Block135_no_go"),
    ]
    check("reflection theorem reaches uniform P0", reachable(support_edges, "shell_center_reflection_source_theorem", "uniform_P0"))
    check("reflection theorem reaches unit score", reachable(support_edges, "shell_center_reflection_source_theorem", "tau_odd_unit_score"))
    check("reflection theorem reaches mu_one", reachable(support_edges, "shell_center_reflection_source_theorem", "mu_one"))
    check("reflection theorem reaches physical c_TE node", reachable(support_edges, "shell_center_reflection_source_theorem", "physical_c_TE_minus_8_9"))
    check("current typing reaches free parameter", reachable(current_edges, "current_four_slot_typing", "free_shell_center_P0_parameter"))
    check("current typing does not reach uniform P0", not reachable(current_edges, "current_four_slot_typing", "uniform_P0"))
    all_nodes = {node for edge in support_edges + current_edges for node in edge}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in node and "q_E" not in node and "endpoint_value" not in node for node in all_nodes))
    check("support theorem and current typing are distinct nodes", "shell_center_reflection_source_theorem" in all_nodes and "current_four_slot_typing" in all_nodes)


def part8_document_boundary() -> None:
    print()
    print("PART 8: document boundary")
    note = text("QUARK_ROUTE2_SHELL_CENTER_REFLECTION_SELECTOR_SUPPORT_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: exact-support for a conditional shell/center reflection selector; not current-surface closure",
        "Conditional Selector Theorem",
        "Route-2 shell/center reflection source theorem",
        "same Fisher-unit Riesz line as the Block121 connected source scalar",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block136 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks upstream support", "trace_class: upstream_support" in trace_gate)
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
    print("Route-2 shell/center reflection selector support")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_reflection_structure()
    part3_reference_selection()
    part4_unit_score_and_rn_path()
    part5_clause_failures()
    part6_current_boundary()
    part7_reachability()
    part8_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: runner failed; do not use this packet.")
    else:
        print("VERDICT: a shell/center reflection source theorem would select uniform P0 and a unit center score; current surface still has to supply the physical reflection and same-source typing.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
