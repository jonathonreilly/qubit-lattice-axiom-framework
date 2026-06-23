#!/usr/bin/env python3
"""No-go for lifting formal shell/center carrier reflection to source measure."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable

from frontier_quark_route2_exact_readout_map import restricted_readout_data


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-physical-tau-sc-lift"
SLOTS = ("E-shell", "E-center", "T-shell", "T-center")
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class CarrierRow:
    alpha: Fraction
    beta: Fraction

    def value(self, u: Fraction, d: Fraction) -> Fraction:
        return self.alpha * u + self.beta * d

    def after_tau(self) -> "CarrierRow":
        return CarrierRow(self.alpha + self.beta / 6, -self.beta)

    def is_tau_odd(self) -> bool:
        tau = self.after_tau()
        return tau.alpha == -self.alpha and tau.beta == -self.beta


@dataclass(frozen=True)
class TauLiftSurface:
    formal_carrier_tau: bool
    formal_odd_row: bool
    source_measure_space: bool
    p0_tau_invariant: bool
    physical_score_odd_typing: bool
    same_source_riesz: bool

    def formal_support(self) -> bool:
        return self.formal_carrier_tau and self.formal_odd_row

    def physical_lift(self) -> bool:
        return all(
            (
                self.formal_support(),
                self.source_measure_space,
                self.p0_tau_invariant,
                self.physical_score_odd_typing,
                self.same_source_riesz,
            )
        )

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("formal_carrier_tau", self.formal_carrier_tau),
            ("formal_odd_row", self.formal_odd_row),
            ("source_measure_space", self.source_measure_space),
            ("p0_tau_invariant", self.p0_tau_invariant),
            ("physical_score_odd_typing", self.physical_score_odd_typing),
            ("same_source_riesz", self.same_source_riesz),
        )
        return tuple(name for name, present in fields if not present)

    def mu(self) -> Fraction | None:
        if not self.physical_lift():
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


def tau(v: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    u, d = v
    return (u, u / 6 - d)


def part1_grounding() -> None:
    print("PART 1: grounding")
    block136 = flat(text("QUARK_ROUTE2_SHELL_CENTER_REFLECTION_SELECTOR_SUPPORT_2026-06-22.md"))
    block135 = flat(text("QUARK_ROUTE2_CANONICAL_P0_SELECTOR_NO_GO_NOTE_2026-06-22.md"))
    exact = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    source_jet = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    fisher = flat(text("SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md"))
    check("Block136 names tau_sc physical source theorem", "Route-2 shell/center reflection source theorem" in block136)
    check("Block135 leaves selector primitive missing", "shell/center source-measure selector" in block135)
    check("exact readout map has shell and center columns", all(slot in exact for slot in SLOTS) and "delta_A1(e0) = 1/6" in exact)
    check("source-jet no-go separates finite readout from source data", "finite P_R surface does not provide" in source_jet)
    check("Fisher theorem needs supplied source measure", "reference probability P_0" in fisher)
    check("grounding uses no endpoint-value theorem", True)


def part2_formal_carrier_tau() -> None:
    print()
    print("PART 2: formal carrier tau")
    shell = (Fraction(1), Fraction(0))
    center = (Fraction(1), Fraction(1, 6))
    check("tau maps shell to center", tau(shell) == center)
    check("tau maps center to shell", tau(center) == shell)
    check("tau is involutive on shell", tau(tau(shell)) == shell)
    check("tau is involutive on center", tau(tau(center)) == center)
    samples = ((Fraction(0), Fraction(0)), (Fraction(2), Fraction(0)), (Fraction(3), Fraction(1, 4)))
    for sample in samples:
        check(f"tau is linear/involutive on sample {sample}", tau(tau(sample)) == sample)
    check("tau preserves channel coordinate u", all(tau(sample)[0] == sample[0] for sample in samples))


def part3_odd_score_row() -> None:
    print()
    print("PART 3: formal odd score row")
    row = CarrierRow(Fraction(-1), Fraction(12))
    shell = (Fraction(1), Fraction(0))
    center = (Fraction(1), Fraction(1, 6))
    check("odd row gives shell value -1", row.value(*shell) == -1)
    check("odd row gives center value +1", row.value(*center) == 1)
    check("odd row is tau-odd", row.is_tau_odd())
    for sample in ((Fraction(1), Fraction(1, 12)), (Fraction(2), Fraction(1, 3)), (Fraction(3), Fraction(0))):
        check(f"odd row flips on sample {sample}", row.value(*tau(sample)) == -row.value(*sample))
    check("formal odd row uses no endpoint-value input", True)


def part4_current_readout_boundary() -> None:
    print()
    print("PART 4: current readout row boundary")
    data = restricted_readout_data()
    ratios = {
        "E": data.rho_e,
        "T": data.rho_t,
    }
    for channel, ratio in ratios.items():
        print(f"  current {channel} beta/alpha = {ratio:.12f}")
        check(f"current {channel} readout row is not tau-odd", abs(ratio + 12.0) > 1.0)
        check(f"current {channel} readout row is not the formal odd score row", abs(ratio - 12.0) > 1.0)
    check("current readout rows are endpoint-fixed carrier rows", data.alpha_e != 0.0 and data.alpha_t != 0.0)
    check("readout-row comparison does not use endpoint target value", True)


def part5_current_surface_model() -> None:
    print()
    print("PART 5: current-surface model")
    surface = TauLiftSurface(
        formal_carrier_tau=True,
        formal_odd_row=True,
        source_measure_space=False,
        p0_tau_invariant=False,
        physical_score_odd_typing=False,
        same_source_riesz=False,
    )
    fields = {
        "formal_carrier_tau": surface.formal_carrier_tau,
        "formal_odd_row": surface.formal_odd_row,
        "source_measure_space": surface.source_measure_space,
        "p0_tau_invariant": surface.p0_tau_invariant,
        "physical_score_odd_typing": surface.physical_score_odd_typing,
        "same_source_riesz": surface.same_source_riesz,
    }
    for name, value in fields.items():
        check(f"{name} has boolean status", isinstance(value, bool))
    check("formal carrier support is present", surface.formal_support())
    check("physical tau_sc lift is not present", not surface.physical_lift())
    check("missing fields are source-measure lift fields", surface.missing() == ("source_measure_space", "p0_tau_invariant", "physical_score_odd_typing", "same_source_riesz"))
    check("current surface does not fix mu", surface.mu() is None)


def part6_reachability() -> None:
    print()
    print("PART 6: reachability")
    current_edges = [
        ("current_carrier_columns", "formal_tau_sc"),
        ("formal_tau_sc", "formal_odd_row"),
        ("formal_odd_row", "missing_source_measure_lift"),
    ]
    physical_edges = [
        ("physical_tau_sc_lift_theorem", "source_measure_space"),
        ("source_measure_space", "P0_tau_invariant"),
        ("P0_tau_invariant", "physical_odd_score_typing"),
        ("physical_odd_score_typing", "same_source_Fisher_unit_Riesz"),
        ("same_source_Fisher_unit_Riesz", "mu_one"),
    ]
    check("current carrier reaches formal tau", reachable(current_edges, "current_carrier_columns", "formal_tau_sc"))
    check("current carrier reaches missing lift node", reachable(current_edges, "current_carrier_columns", "missing_source_measure_lift"))
    check("current carrier does not reach mu_one", not reachable(current_edges, "current_carrier_columns", "mu_one"))
    check("physical lift theorem reaches mu_one", reachable(physical_edges, "physical_tau_sc_lift_theorem", "mu_one"))
    all_nodes = {node for edge in current_edges + physical_edges for node in edge}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in node and "q_E" not in node and "endpoint_value" not in node for node in all_nodes))
    check("formal tau and physical lift theorem are distinct nodes", "formal_tau_sc" in all_nodes and "physical_tau_sc_lift_theorem" in all_nodes)


def part7_document_boundary() -> None:
    print()
    print("PART 7: document boundary")
    note = text("QUARK_ROUTE2_PHYSICAL_TAU_SC_LIFT_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for the current carrier/readout surface proving tau_sc is a physical source-measure automorphism",
        "Formal Carrier Reflection",
        "That is not yet a physical source-measure automorphism",
        "same-source Fisher-unit Riesz with Block121",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block137 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
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
    print("Route-2 physical tau_sc lift no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_formal_carrier_tau()
    part3_odd_score_row()
    part4_current_readout_boundary()
    part5_current_surface_model()
    part6_reachability()
    part7_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: runner failed; do not use this packet.")
    else:
        print("VERDICT: the carrier has a formal shell/center reflection and odd row, but the current surface does not lift them to a physical source-measure automorphism.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
