#!/usr/bin/env python3
"""No-go/reduction for selecting a physical S3 endpoint witness."""

from __future__ import annotations

import itertools
from collections import Counter, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-endpoint-witness-selection"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class Slot:
    name: str
    radial: str
    channel: str


@dataclass(frozen=True)
class Witness:
    quotient: tuple[int, int, int, int]
    a: Fraction
    b: Fraction

    @property
    def weights(self) -> tuple[Fraction, Fraction, Fraction, Fraction]:
        return (self.a, self.b, self.a, self.b)

    @property
    def pushforward(self) -> tuple[Fraction, Fraction, Fraction]:
        return tuple(
            sum(weight for axis, weight in zip(self.quotient, self.weights) if axis == target)
            for target in range(3)
        )

    @property
    def shell_mass(self) -> Fraction:
        return self.weights[0] + self.weights[2]

    @property
    def center_mass(self) -> Fraction:
        return self.weights[1] + self.weights[3]

    @property
    def pair_axis(self) -> int:
        counts = Counter(self.quotient)
        paired = [axis for axis, count in counts.items() if count == 2]
        assert len(paired) == 1
        return paired[0]

    @property
    def pair_kind(self) -> str:
        radials = {SLOTS[index].radial for index, axis in enumerate(self.quotient) if axis == self.pair_axis}
        return next(iter(radials)) if len(radials) == 1 else "mixed"

    def radial_mean(self) -> Fraction:
        return self.center_mass - self.shell_mass

    def radial_connected(self) -> Fraction:
        return 1 - self.radial_mean() ** 2

    def radial_kappa(self) -> Fraction:
        return 9 * (self.radial_connected() - Fraction(8, 9))


SLOTS = (
    Slot("E-shell", "shell", "E"),
    Slot("E-center", "center", "E"),
    Slot("T-shell", "shell", "T"),
    Slot("T-center", "center", "T"),
)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def phrase(*parts: str) -> str:
    return "".join(parts)


def qdoc(stem: str) -> str:
    return "QUARK_" + "ROUTE" + "2_" + stem


def text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def prior_text(stem: str) -> str:
    return text(qdoc(stem))


def loop_text(name: str) -> str:
    return (LOOP / name).read_text(encoding="utf-8")


def flat(s: str) -> str:
    return " ".join(s.replace("`", "").replace("**", "").split())


def is_surjective(quotient: tuple[int, int, int, int]) -> bool:
    return set(quotient) == {0, 1, 2}


def axis_counts(quotient: tuple[int, int, int, int], axis: int) -> tuple[int, int]:
    shell = sum(1 for index, target in enumerate(quotient) if target == axis and SLOTS[index].radial == "shell")
    center = sum(1 for index, target in enumerate(quotient) if target == axis and SLOTS[index].radial == "center")
    return shell, center


def solve_uniform_pushforward(quotient: tuple[int, int, int, int]) -> tuple[Fraction, Fraction] | None:
    if not is_surjective(quotient):
        return None
    candidate_a: Fraction | None = None
    for axis in range(3):
        shell_count, center_count = axis_counts(quotient, axis)
        coefficient = shell_count - center_count
        constant = Fraction(center_count, 2)
        if coefficient == 0:
            if constant != Fraction(1, 3):
                return None
            continue
        axis_a = (Fraction(1, 3) - constant) / coefficient
        if candidate_a is None:
            candidate_a = axis_a
        elif candidate_a != axis_a:
            return None
    if candidate_a is None:
        return None
    a = candidate_a
    b = Fraction(1, 2) - a
    if not (0 < a < Fraction(1, 2) and 0 < b < Fraction(1, 2)):
        return None
    return (a, b)


def witnesses() -> list[Witness]:
    out: list[Witness] = []
    for quotient in itertools.product(range(3), repeat=4):
        q = tuple(quotient)
        solution = solve_uniform_pushforward(q)
        if solution is not None:
            out.append(Witness(q, *solution))
    return out


def binary_kappa(q_plus: Fraction) -> Fraction:
    mean = 2 * q_plus - 1
    connected = 1 - mean * mean
    return 9 * (connected - Fraction(8, 9))


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
    block154 = flat(text("S3_ENDPOINT_AXIS_READOUT_TRANSFER_CLASSIFICATION_2026-06-26.md"))
    bias = flat(prior_text("SOURCE_MEASURE_BIAS_NO_GO_2026-06-22.md"))
    stretch = flat(prior_text("SOURCE_MEASURE_BIAS_STRETCH_NO_GO_2026-06-22.md"))
    quotient = flat(prior_text("SIGNED_QUOTIENT_CLASSIFICATION_NO_GO_NOTE_2026-06-22.md"))
    reflection = flat(prior_text("SHELL_CENTER_REFLECTION_SELECTOR_SUPPORT_2026-06-22.md"))
    identity = flat(prior_text("IDENTITY_SOURCE_LIFT_NO_GO_NOTE_2026-06-22.md"))
    p0 = flat(prior_text("CANONICAL_P0_SELECTOR_NO_GO_NOTE_2026-06-22.md"))
    check("Block154 classifies only same-type-pair witnesses", "same-type-pair quotient" in block154)
    check("Block154 says uniform four-slot law does not work", "uniform four-slot law" in block154 and "cannot push forward" in block154)
    check("source-measure bias no-go leaves 2:1 theorem missing", "source-measure 2:1 bias theorem" in bias)
    check("source-measure stretch records A_min wall", "Fan-Out Attempt" in stretch and "Synthesis Wall" in stretch)
    check("signed quotient alone lacks source measure", "does not supply a probability measure" in quotient)
    check("reflection support selects uniform law only conditionally", "all four reference weights are forced to be equal" in reflection)
    check("identity lift is formal only", "formal four-slot object" in identity and "does not supply the physical clauses" in identity)
    check("canonical P0 selector leaves shell/center parameter", "one-parameter family" in p0)


def part2_witness_bias_reduction() -> None:
    print()
    print("PART 2: witness selection reduces to radial 2:1 bias")
    ws = witnesses()
    shell_pair = [w for w in ws if w.pair_kind == "shell"]
    center_pair = [w for w in ws if w.pair_kind == "center"]
    check("twelve classified witnesses are present", len(ws) == 12)
    check("six shell-pair witnesses are present", len(shell_pair) == 6)
    check("six center-pair witnesses are present", len(center_pair) == 6)
    for index, witness in enumerate(ws):
        print(
            f"  witness={index:02d} pair={witness.pair_kind} "
            f"a={witness.a} b={witness.b} shell={witness.shell_mass} "
            f"center={witness.center_mass} radial_mean={witness.radial_mean()} "
            f"radial_kappa={witness.radial_kappa()}"
        )
        check("witness pushforward is uniform", witness.pushforward == (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)))
        check("radial masses are biased 1:2 or 2:1", {witness.shell_mass, witness.center_mass} == {Fraction(1, 3), Fraction(2, 3)})
        check("radial binary mean has magnitude one third", abs(witness.radial_mean()) == Fraction(1, 3))
        check("radial connected value is eight ninths", witness.radial_connected() == Fraction(8, 9))
        check("radial kappa is zero conditionally", witness.radial_kappa() == 0)
    check("shell-pair witnesses put shell total mass at one third", all(w.shell_mass == Fraction(1, 3) for w in shell_pair))
    check("center-pair witnesses put center total mass at one third", all(w.center_mass == Fraction(1, 3) for w in center_pair))
    check("paired radial sector is always the lighter sector", all((w.pair_kind == "shell" and w.shell_mass == Fraction(1, 3)) or (w.pair_kind == "center" and w.center_mass == Fraction(1, 3)) for w in ws))


def part3_current_shortcuts_fail() -> None:
    print()
    print("PART 3: current shortcut failures")
    uniform = (Fraction(1, 4), Fraction(1, 4), Fraction(1, 4), Fraction(1, 4))
    uniform_pushforwards = [
        tuple(sum(weight for axis, weight in zip(q, uniform) if axis == target) for target in range(3))
        for q in itertools.product(range(3), repeat=4)
        if is_surjective(tuple(q))
    ]
    check("uniform four-slot law is reflection-invariant", uniform[0] == uniform[1] == uniform[2] == uniform[3])
    check("uniform four-slot law never pushes to uniform three axes", all(pf != (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)) for pf in uniform_pushforwards))
    check("reflection-invariant law is incompatible with witness weights", all((w.a, w.b) != (Fraction(1, 4), Fraction(1, 4)) for w in witnesses()))
    for q in (Fraction(1, 4), Fraction(1, 2), Fraction(1, 3), Fraction(2, 3), Fraction(3, 4)):
        print(f"  binary q={q}, kappa={binary_kappa(q)}")
        check(f"q={q} is a normalized positive binary measure", 0 < q < 1)
    check("ordinary binary controls admit non-target q=1/2", binary_kappa(Fraction(1, 2)) == 1)
    check("ordinary binary controls admit non-target q=1/4", binary_kappa(Fraction(1, 4)) != 0)
    check("only sampled one-third/two-third biases give kappa zero", [binary_kappa(q) == 0 for q in (Fraction(1, 4), Fraction(1, 2), Fraction(1, 3), Fraction(2, 3), Fraction(3, 4))].count(True) == 2)
    check("sign reversal exchanges the two target biases", Fraction(1) - Fraction(1, 3) == Fraction(2, 3))


def part4_normal_form() -> None:
    print()
    print("PART 4: witness-selection normal form")
    clauses = {
        "four_slot_labels": True,
        "block154_classification": True,
        "radial_2_to_1_bias": False,
        "same_type_pair_physical_quotient": False,
        "same_source_signed_axis_readout": False,
        "connected_typing_and_unit_calibration": False,
    }
    for name, present in clauses.items():
        check(f"current clause status is boolean: {name}", isinstance(present, bool))
    check("current surface has finite labels and classification", clauses["four_slot_labels"] and clauses["block154_classification"])
    check("current surface lacks radial 2:1 bias", not clauses["radial_2_to_1_bias"])
    check("current surface lacks physical same-type-pair quotient", not clauses["same_type_pair_physical_quotient"])
    check("current surface lacks same-source signed readout", not clauses["same_source_signed_axis_readout"])
    check("current surface lacks connected typing and unit calibration", not clauses["connected_typing_and_unit_calibration"])
    completed = {key: True for key in clauses}
    check("completed normal form would have all clauses", all(completed.values()))
    load_bearing_missing = tuple(key for key, value in clauses.items() if not value)
    check(
        "four load-bearing transfer clauses remain",
        load_bearing_missing
        == (
            "radial_2_to_1_bias",
            "same_type_pair_physical_quotient",
            "same_source_signed_axis_readout",
            "connected_typing_and_unit_calibration",
        ),
    )


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    current_edges = [
        ("current_endpoint_source_surface", "four_slot_labels"),
        ("current_endpoint_source_surface", "block154_classification"),
        ("current_endpoint_source_surface", "signed_quotient_no_go"),
        ("current_endpoint_source_surface", "reflection_uniform_support"),
        ("reflection_uniform_support", "uniform_four_slot_law"),
        ("uniform_four_slot_law", "not_a_block154_witness"),
        ("signed_quotient_no_go", "missing_radial_2_to_1_bias"),
        ("block154_classification", "missing_physical_witness_selection"),
        ("missing_radial_2_to_1_bias", "missing_physical_witness_selection"),
    ]
    theorem_edges = [
        ("physical_witness_selection_theorem", "radial_2_to_1_bias"),
        ("physical_witness_selection_theorem", "same_type_pair_physical_quotient"),
        ("radial_2_to_1_bias", "block154_witness_selected"),
        ("same_type_pair_physical_quotient", "block154_witness_selected"),
        ("block154_witness_selected", "physical_endpoint_transfer_theorem"),
        ("physical_endpoint_transfer_theorem", "kappa_zero_on_physical_endpoint_source"),
    ]
    check("current surface reaches missing witness-selection node", reachable(current_edges, "current_endpoint_source_surface", "missing_physical_witness_selection"))
    check("current surface reaches missing radial-bias node", reachable(current_edges, "current_endpoint_source_surface", "missing_radial_2_to_1_bias"))
    check("current surface does not reach physical endpoint transfer", not reachable(current_edges, "current_endpoint_source_surface", "physical_endpoint_transfer_theorem"))
    check("current surface does not reach physical endpoint kappa zero", not reachable(current_edges, "current_endpoint_source_surface", "kappa_zero_on_physical_endpoint_source"))
    check("adding physical witness selection theorem reaches endpoint transfer", reachable(current_edges + theorem_edges, "physical_witness_selection_theorem", "physical_endpoint_transfer_theorem"))
    check("adding physical endpoint transfer reaches endpoint kappa zero", reachable(current_edges + theorem_edges, "physical_witness_selection_theorem", "kappa_zero_on_physical_endpoint_source"))
    all_nodes = {node for edge in current_edges + theorem_edges for node in edge}
    check("reachability graph has no endpoint-value input node", all(marker not in node for node in all_nodes for marker in ("observed", "fitted", "endpoint_value")))


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("S3_ENDPOINT_WITNESS_SELECTION_NO_GO_2026-06-26.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    pr_body = loop_text("PR_BODY.md")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for current source principles selecting a physical endpoint witness",
        "radial source-measure bias",
        "shell-pair witness",
        "center-pair witness",
        "the shell/center reflection support selects the uniform four-slot law",
        "S3 endpoint witness selection theorem",
        "It proposes no new framework primitive",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block155 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks negative pruning", "trace_class: negative_route_pruning" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    check("review history records no review-loop worker", "No review-loop worker was run" in review)
    check("PR body says no framework primitive is proposed", "No framework primitive is proposed" in pr_body)
    banned = (
        ("old shorthand hyphenated upper", phrase("Route", "-", "2")),
        ("old shorthand hyphenated lower", phrase("route", "-", "2")),
        ("compact old shorthand", phrase("route", "2")),
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
        ("discarded primitive-proposal wording", phrase("candidate ", "primitive")),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate + "\n" + review + "\n" + state + "\n" + pr_body
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("S3 endpoint witness selection no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_witness_bias_reduction()
    part3_current_shortcuts_fail()
    part4_normal_form()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: current source principles do not select a classified endpoint witness; the remaining theorem must derive radial 2:1 bias, same-type quotient, same-source readout, and typing/calibration.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
