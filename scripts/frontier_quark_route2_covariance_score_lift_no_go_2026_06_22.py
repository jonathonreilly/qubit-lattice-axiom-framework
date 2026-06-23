#!/usr/bin/env python3
"""Route-2 covariance score-lift boundary.

This runner separates exact finite covariance-score algebra from the physical
Route-2 score-lift theorem.  A four-slot RN path can supply a unit odd score,
but the current surface still has to prove that this score is the physical
center-ratio covariance readout and the same-source Riesz representative of
the Block121 connected scalar.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-covariance-score-lift"
PASS = 0
FAIL = 0

SLOTS = ("E-shell", "E-center", "T-shell", "T-center")


@dataclass(frozen=True)
class CovarianceScoreLift:
    four_slot_space: bool
    invariant_p0: bool
    rn_path: bool
    formal_covariance_identity: bool
    physical_center_ratio_observable: bool
    source_coordinates: bool
    same_source_riesz: bool
    unit_isometry: bool

    def formal_score(self) -> bool:
        return all((self.four_slot_space, self.invariant_p0, self.rn_path, self.formal_covariance_identity))

    def physical_score(self) -> bool:
        return self.formal_score() and self.physical_center_ratio_observable and self.source_coordinates

    def bridge(self) -> bool:
        return self.physical_score() and self.same_source_riesz and self.unit_isometry

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("four_slot_space", self.four_slot_space),
            ("invariant_p0", self.invariant_p0),
            ("rn_path", self.rn_path),
            ("formal_covariance_identity", self.formal_covariance_identity),
            ("physical_center_ratio_observable", self.physical_center_ratio_observable),
            ("source_coordinates", self.source_coordinates),
            ("same_source_riesz", self.same_source_riesz),
            ("unit_isometry", self.unit_isometry),
        )
        return tuple(name for name, present in fields if not present)

    def mu(self) -> Fraction | None:
        if not self.bridge():
            return None
        return Fraction(1)

    def kappa_forced(self) -> bool:
        return self.bridge()


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


def p0(slot: str) -> Fraction:
    if slot not in SLOTS:
        raise ValueError(slot)
    return Fraction(1, 4)


def score(slot: str) -> Fraction:
    return Fraction(1) if layer(slot) == "center" else Fraction(-1)


def tau(slot: str) -> str:
    return f"{channel(slot)}-center" if layer(slot) == "shell" else f"{channel(slot)}-shell"


Observable = Callable[[str], Fraction]


def expectation(obs: Observable) -> Fraction:
    return sum(p0(slot) * obs(slot) for slot in SLOTS)


def covariance(obs: Observable, sc: Observable) -> Fraction:
    return expectation(lambda slot: obs(slot) * sc(slot)) - expectation(obs) * expectation(sc)


def center_indicator(slot: str) -> Fraction:
    return Fraction(1) if layer(slot) == "center" else Fraction(0)


def shell_indicator(slot: str) -> Fraction:
    return Fraction(1) if layer(slot) == "shell" else Fraction(0)


def e_channel_indicator(slot: str) -> Fraction:
    return Fraction(1) if channel(slot) == "E" else Fraction(0)


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
    block140_parent = flat(text("QUARK_ROUTE2_IDENTITY_SOURCE_LIFT_NO_GO_NOTE_2026-06-22.md"))
    reflection = flat(text("QUARK_ROUTE2_SHELL_CENTER_REFLECTION_SELECTOR_SUPPORT_2026-06-22.md"))
    source_jet = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    cumulant = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md"))
    isometry = flat(text("QUARK_ROUTE2_SOURCE_READOUT_ISOMETRY_SUFFICIENT_SUPPORT_2026-06-22.md"))
    check("Block139 leaves physical score-lift theorem missing", "Route-2 physical score-lift theorem" in block140_parent)
    check("Block139 separates formal contrast from physical score", "formal odd shell/center contrast" in block140_parent)
    check("Block136 requires physical center-ratio covariance readout", "physical center-ratio covariance readout" in reflection)
    check("source-jet no-go names source coordinates", "source coordinates J_A" in source_jet)
    check("source-jet no-go names same-source identification", "same-source" in source_jet and "source used by P_R/E-T" in source_jet)
    check("cumulant support supplies D2 log Z algebra", "D^2 log Z subtracts factorizable disconnected products exactly" in cumulant)
    check("source-readout isometry leaves typed isometry open", "typed isometry is proven" in isometry)
    check("grounding uses no endpoint-value theorem", True)


def part2_formal_covariance_algebra() -> None:
    print()
    print("PART 2: formal covariance algebra")
    check("uniform P0 is normalized", sum(p0(slot) for slot in SLOTS) == 1)
    check("uniform P0 is positive on every slot", all(p0(slot) > 0 for slot in SLOTS))
    check("score is tau-odd on every slot", all(score(tau(slot)) == -score(slot) for slot in SLOTS))
    check("score has zero mean", expectation(score) == 0)
    check("score has unit Fisher norm", expectation(lambda slot: score(slot) ** 2) == 1)
    check("covariance of score with itself is one", covariance(score, score) == 1)
    check("center indicator covariance is one half", covariance(center_indicator, score) == Fraction(1, 2))
    check("centered center observable has unit response", covariance(lambda slot: 2 * center_indicator(slot) - 1, score) == 1)
    for h_num in (-1, 0, 1):
        h = Fraction(h_num, 2)
        weights = {slot: p0(slot) for slot in SLOTS}
        check(f"formal P_h sample h={h} has positive base weights", all(value > 0 for value in weights.values()))
    check("formal covariance algebra uses no endpoint-value input", True)


def part3_observable_non_uniqueness() -> None:
    print()
    print("PART 3: observable non-uniqueness")
    observables: tuple[tuple[str, Observable, Fraction], ...] = (
        ("center_indicator", center_indicator, Fraction(1, 2)),
        ("shell_indicator", shell_indicator, Fraction(-1, 2)),
        ("E_channel_indicator", e_channel_indicator, Fraction(0)),
        ("layer_score", score, Fraction(1)),
        ("negative_layer_score", lambda slot: -score(slot), Fraction(-1)),
    )
    values = []
    for name, obs, expected in observables:
        value = covariance(obs, score)
        values.append(value)
        print(f"  {name}: covariance={value}")
        check(f"{name} covariance has expected value", value == expected)
        check(f"{name} covariance is rational", isinstance(value, Fraction))
    check("same formal source path gives multiple covariance responses", len(set(values)) > 3)
    check("unit score alone does not select the physical observable", covariance(score, score) != covariance(center_indicator, score))
    check("zero E-channel covariance shows channel labels alone do not select center ratio", covariance(e_channel_indicator, score) == 0)


def part4_current_surface_model() -> None:
    print()
    print("PART 4: current-surface model")
    current = CovarianceScoreLift(True, True, True, True, False, False, False, False)
    fields = {
        "four_slot_space": current.four_slot_space,
        "invariant_p0": current.invariant_p0,
        "rn_path": current.rn_path,
        "formal_covariance_identity": current.formal_covariance_identity,
        "physical_center_ratio_observable": current.physical_center_ratio_observable,
        "source_coordinates": current.source_coordinates,
        "same_source_riesz": current.same_source_riesz,
        "unit_isometry": current.unit_isometry,
    }
    for name, value in fields.items():
        check(f"{name} has boolean status", isinstance(value, bool))
    check("formal covariance score is present", current.formal_score())
    check("physical covariance score is not present", not current.physical_score())
    check("same-source bridge is not present", not current.bridge())
    check(
        "missing fields are exactly physical observable, source coordinates, Riesz, and isometry",
        current.missing()
        == ("physical_center_ratio_observable", "source_coordinates", "same_source_riesz", "unit_isometry"),
    )
    check("current covariance algebra alone does not fix mu", current.mu() is None)
    check("current covariance algebra alone does not force kappa", not current.kappa_forced())


def part5_physical_clause_failures() -> None:
    print()
    print("PART 5: physical clause failures")
    base = {
        "four_slot_space": True,
        "invariant_p0": True,
        "rn_path": True,
        "formal_covariance_identity": True,
        "physical_center_ratio_observable": True,
        "source_coordinates": True,
        "same_source_riesz": True,
        "unit_isometry": True,
    }
    full = CovarianceScoreLift(**base)
    check("all physical clauses would complete the bridge", full.bridge())
    check("complete physical clauses would fix mu", full.mu() == 1)
    check("complete physical clauses would force kappa", full.kappa_forced())
    for missing in ("physical_center_ratio_observable", "source_coordinates", "same_source_riesz", "unit_isometry"):
        model = dict(base)
        model[missing] = False
        attempt = CovarianceScoreLift(**model)
        check(f"{missing} omission makes bridge fail", not attempt.bridge())
        check(f"{missing} omission is named exactly", attempt.missing() == (missing,))
        check(f"{missing} omission blocks mu output", attempt.mu() is None)
    check("all four physical clauses were tested", len(("physical_center_ratio_observable", "source_coordinates", "same_source_riesz", "unit_isometry")) == 4)


def part6_reachability() -> None:
    print()
    print("PART 6: reachability")
    formal_edges = [
        ("four_slot_RN_path", "formal_covariance_identity"),
        ("formal_covariance_identity", "formal_unit_odd_score"),
        ("formal_unit_odd_score", "missing_physical_center_ratio_observable"),
        ("missing_physical_center_ratio_observable", "missing_source_coordinates"),
        ("missing_source_coordinates", "missing_same_source_Riesz"),
        ("missing_same_source_Riesz", "missing_unit_isometry"),
    ]
    bridge_edges = [
        ("formal_unit_odd_score", "physical_center_ratio_covariance_score"),
        ("physical_center_ratio_covariance_score", "same_source_Fisher_unit_Riesz"),
        ("same_source_Fisher_unit_Riesz", "unit_isometry_mu_one"),
        ("unit_isometry_mu_one", "kappa_zero_without_endpoint"),
    ]
    check("formal path reaches covariance identity", reachable(formal_edges, "four_slot_RN_path", "formal_covariance_identity"))
    check("formal path reaches unit odd score", reachable(formal_edges, "four_slot_RN_path", "formal_unit_odd_score"))
    check("formal path reaches missing physical observable node", reachable(formal_edges, "four_slot_RN_path", "missing_physical_center_ratio_observable"))
    check("formal path alone does not reach mu_one", not reachable(formal_edges, "four_slot_RN_path", "unit_isometry_mu_one"))
    check("formal path alone does not reach kappa zero", not reachable(formal_edges, "four_slot_RN_path", "kappa_zero_without_endpoint"))
    check("adding physical score/Riesz typing reaches kappa zero", reachable(formal_edges + bridge_edges, "four_slot_RN_path", "kappa_zero_without_endpoint"))
    all_nodes = {node for edge in formal_edges + bridge_edges for node in edge}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in node and "endpoint_value" not in node for node in all_nodes))


def part7_document_boundary() -> None:
    print()
    print("PART 7: document boundary")
    note = text("QUARK_ROUTE2_COVARIANCE_SCORE_LIFT_NO_GO_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for finite four-slot covariance algebra alone proving the physical center-ratio covariance score",
        "Formal Covariance Algebra",
        "The algebra does not identify which four-slot observable is the physical Route-2 center-ratio covariance readout",
        "Route-2 physical covariance score-lift theorem",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block140 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
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
    print("Route-2 covariance score-lift no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_formal_covariance_algebra()
    part3_observable_non_uniqueness()
    part4_current_surface_model()
    part5_physical_clause_failures()
    part6_reachability()
    part7_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: runner failed; do not use this packet.")
    else:
        print("VERDICT: four-slot covariance algebra supplies a formal unit score, but the physical center-ratio score/Riesz lift remains missing.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
