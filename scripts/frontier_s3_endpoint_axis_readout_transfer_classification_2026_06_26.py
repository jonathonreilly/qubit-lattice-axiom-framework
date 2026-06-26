#!/usr/bin/env python3
"""Classify finite endpoint transfers into the S3 signed-axis source."""

from __future__ import annotations

import itertools
from collections import Counter, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-endpoint-axis-readout-transfer"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class Slot:
    name: str
    radial: str
    channel: str


@dataclass(frozen=True)
class TransferWitness:
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
    def pair_axis(self) -> int:
        counts = Counter(self.quotient)
        paired = [axis for axis, count in counts.items() if count == 2]
        assert len(paired) == 1
        return paired[0]

    @property
    def pair_indices(self) -> tuple[int, int]:
        axis = self.pair_axis
        return tuple(index for index, target in enumerate(self.quotient) if target == axis)  # type: ignore[return-value]

    @property
    def pair_radials(self) -> tuple[str, str]:
        return tuple(SLOTS[index].radial for index in self.pair_indices)  # type: ignore[return-value]

    def chi_values(self, selected_axis: int, sign: int) -> tuple[int, int, int, int]:
        return tuple(sign * (1 if axis == selected_axis else -1) for axis in self.quotient)

    def mean(self, selected_axis: int, sign: int) -> Fraction:
        return sum(w * x for w, x in zip(self.weights, self.chi_values(selected_axis, sign)))

    def raw_same_source(self, selected_axis: int, sign: int) -> Fraction:
        values = self.chi_values(selected_axis, sign)
        return sum(w * x * x for w, x in zip(self.weights, values))

    def connected(self, selected_axis: int, sign: int) -> Fraction:
        mean = self.mean(selected_axis, sign)
        return self.raw_same_source(selected_axis, sign) - mean * mean

    def kappa(self, selected_axis: int, sign: int) -> Fraction:
        return 9 * (self.connected(selected_axis, sign) - Fraction(8, 9))


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
    for axis in range(3):
        shell_count, center_count = axis_counts(quotient, axis)
        if shell_count * a + center_count * b != Fraction(1, 3):
            return None
    return a, b


def enumerate_witnesses() -> list[TransferWitness]:
    witnesses: list[TransferWitness] = []
    for quotient in itertools.product(range(3), repeat=4):
        if not is_surjective(quotient):
            continue
        solution = solve_uniform_pushforward(quotient)
        if solution is not None:
            witnesses.append(TransferWitness(tuple(quotient), *solution))
    return witnesses


def pair_kind(quotient: tuple[int, int, int, int]) -> str:
    counts = Counter(quotient)
    paired_axes = [axis for axis, count in counts.items() if count == 2]
    if len(paired_axes) != 1:
        return "not-four-to-three"
    indices = [index for index, target in enumerate(quotient) if target == paired_axes[0]]
    radials = {SLOTS[index].radial for index in indices}
    return next(iter(radials)) if len(radials) == 1 else "mixed"


def part1_grounding() -> None:
    print("PART 1: grounding")
    support = flat(prior_text("CUBIC_AXIS_READOUT_SUPPORT_2026-06-26.md"))
    exact_map = flat(prior_text("EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    p0_no_go = flat(prior_text("CANONICAL_P0_SELECTOR_NO_GO_NOTE_2026-06-22.md"))
    multirecord = flat(prior_text("CURRENT_PR_MULTI_RECORD_INSTANTIATION_NO_GO_2026-06-22.md"))
    color_marginal = flat(prior_text("COLOR_MARGINAL_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    queue = flat(prior_text("SOURCE_READOUT_PRIMITIVE_QUEUE_EXHAUSTION_2026-06-22.md"))
    check("Block153 proves the signed three-axis support theorem", "unique normalized S3-invariant law" in support and "E[X]E[Y] = 1/9" in support)
    check("Block153 keeps physical transfer open", "source space Omega_R" in support and "Transfer Boundary" in support)
    check("current endpoint surface has four labels", "E-shell = (1, 0, 0, 0)" in exact_map and "T-center = (0, 1, 0, 1/6)" in exact_map)
    check("current endpoint readout is channelwise", "P_R = [[alpha_E, 0, beta_E, 0], [0, alpha_T, 0, beta_T]]" in exact_map)
    check("source-measure note leaves one-parameter family", "P0(E-shell) = a" in p0_no_go and "2a + 2b = 1" in p0_no_go)
    check("uniform four-slot law is not forced", "uniform reference is only the special case" in p0_no_go)
    check("multi-record shortcut is not present", "carrier/readout reduction, not a same-source covariant multi-record source theorem" in multirecord)
    check("color-marginal shortcut is not present", "not color-axis projectors" in color_marginal)
    check("source/readout queue records open physical realization theorem", "physical same-source selector realization theorem" in queue and "remains open" in queue)


def part2_four_to_three_classification() -> None:
    print()
    print("PART 2: four-slot to three-axis classification")
    witnesses = enumerate_witnesses()
    all_surjections = [tuple(q) for q in itertools.product(range(3), repeat=4) if is_surjective(tuple(q))]
    mixed_pair_surjections = [q for q in all_surjections if pair_kind(q) == "mixed"]
    shell_pair_witnesses = [w for w in witnesses if pair_kind(w.quotient) == "shell"]
    center_pair_witnesses = [w for w in witnesses if pair_kind(w.quotient) == "center"]
    uniform_four_slot = (Fraction(1, 4), Fraction(1, 4), Fraction(1, 4), Fraction(1, 4))
    uniform_pushforwards = [
        tuple(sum(weight for axis, weight in zip(q, uniform_four_slot) if axis == target) for target in range(3))
        for q in all_surjections
    ]

    print(f"  total surjective four-to-three quotients: {len(all_surjections)}")
    print(f"  transfer witnesses with uniform three-axis pushforward: {len(witnesses)}")
    for witness in witnesses:
        print(
            f"  witness quotient={witness.quotient} a={witness.a} b={witness.b} "
            f"pair={pair_kind(witness.quotient)} pushforward={witness.pushforward}"
        )

    check("there are thirty-six total surjective quotients", len(all_surjections) == 36)
    check("there are twelve uniform-axis transfer witnesses", len(witnesses) == 12)
    check("six witnesses pair the shell labels", len(shell_pair_witnesses) == 6)
    check("six witnesses pair the center labels", len(center_pair_witnesses) == 6)
    check("all shell-pair witnesses require a=1/6,b=1/3", all((w.a, w.b) == (Fraction(1, 6), Fraction(1, 3)) for w in shell_pair_witnesses))
    check("all center-pair witnesses require a=1/3,b=1/6", all((w.a, w.b) == (Fraction(1, 3), Fraction(1, 6)) for w in center_pair_witnesses))
    check("all witnesses pair same radial type", all(pair_kind(w.quotient) in {"shell", "center"} for w in witnesses))
    check("mixed shell-center pair quotients exist", len(mixed_pair_surjections) == 24)
    check("mixed shell-center pair quotients have no uniform-axis solution", all(solve_uniform_pushforward(q) is None for q in mixed_pair_surjections))
    check("uniform four-slot law never pushes to uniform three axes", all(pf != (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)) for pf in uniform_pushforwards))
    check("witness pushforwards are exactly uniform", all(w.pushforward == (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)) for w in witnesses))
    check("witness weights are positive and normalized", all(sum(w.weights) == 1 and all(weight > 0 for weight in w.weights) for w in witnesses))


def part3_signed_readout_transfer() -> None:
    print()
    print("PART 3: signed readout moments on classified witnesses")
    witnesses = enumerate_witnesses()
    for index, witness in enumerate(witnesses):
        for selected_axis in range(3):
            for sign in (-1, 1):
                mean = witness.mean(selected_axis, sign)
                raw = witness.raw_same_source(selected_axis, sign)
                connected = witness.connected(selected_axis, sign)
                kappa = witness.kappa(selected_axis, sign)
                print(
                    f"  witness={index:02d} mu={selected_axis} sign={sign} "
                    f"mean={mean} product={mean * mean} raw={raw} connected={connected} kappa={kappa}"
                )
                check("signed values are binary", set(witness.chi_values(selected_axis, sign)) == {-1, 1})
                check("signed mean has magnitude one third", abs(mean) == Fraction(1, 3))
                check("disconnected product is one ninth", mean * mean == Fraction(1, 9))
                check("same-source raw moment is one", raw == 1)
                check("connected value is eight ninths", connected == Fraction(8, 9))
                check("kappa is zero on the classified conditional source", kappa == 0)


def part4_current_surface_firewall() -> None:
    print()
    print("PART 4: current-surface firewall")
    current_edges = [
        ("current_endpoint_surface", "four_endpoint_labels"),
        ("current_endpoint_surface", "channelwise_PR_ET_readout"),
        ("current_endpoint_surface", "ET_symmetric_P0_family"),
        ("ET_symmetric_P0_family", "missing_choice_of_a_b"),
        ("four_endpoint_labels", "missing_total_three_axis_quotient"),
        ("channelwise_PR_ET_readout", "missing_same_source_signed_axis_readout"),
        ("missing_choice_of_a_b", "transfer_blocker"),
        ("missing_total_three_axis_quotient", "transfer_blocker"),
        ("missing_same_source_signed_axis_readout", "transfer_blocker"),
    ]
    classified_edges = [
        ("classified_same_type_pair_quotient", "uniform_three_axis_law"),
        ("uniform_three_axis_law", "signed_axis_readout_support"),
        ("signed_axis_readout_support", "product_one_ninth"),
        ("signed_axis_readout_support", "raw_same_source_one"),
        ("product_one_ninth", "connected_eight_ninths"),
        ("raw_same_source_one", "connected_eight_ninths"),
        ("connected_eight_ninths", "kappa_zero_conditional_endpoint_source"),
    ]
    full_transfer_edges = [
        ("physical_endpoint_axis_readout_transfer_theorem", "classified_same_type_pair_quotient"),
        ("physical_endpoint_axis_readout_transfer_theorem", "same_source_PR_ET_equals_signed_axis_readout"),
        ("same_source_PR_ET_equals_signed_axis_readout", "signed_axis_readout_support"),
        ("classified_same_type_pair_quotient", "uniform_three_axis_law"),
        ("uniform_three_axis_law", "product_one_ninth"),
        ("signed_axis_readout_support", "raw_same_source_one"),
        ("product_one_ninth", "connected_eight_ninths"),
        ("raw_same_source_one", "connected_eight_ninths"),
        ("connected_eight_ninths", "kappa_zero_on_physical_endpoint_source"),
    ]
    check("current surface reaches the transfer blocker", reachable(current_edges, "current_endpoint_surface", "transfer_blocker"))
    check("current surface does not reach physical endpoint kappa zero", not reachable(current_edges, "current_endpoint_surface", "kappa_zero_on_physical_endpoint_source"))
    check("classified conditional quotient reaches conditional kappa zero", reachable(classified_edges, "classified_same_type_pair_quotient", "kappa_zero_conditional_endpoint_source"))
    check("physical transfer theorem would reach physical endpoint kappa zero", reachable(full_transfer_edges, "physical_endpoint_axis_readout_transfer_theorem", "kappa_zero_on_physical_endpoint_source"))
    current_nodes = {node for edge in current_edges for node in edge}
    transfer_nodes = {node for edge in classified_edges + full_transfer_edges for node in edge}
    check("current graph has no endpoint-value input node", all(marker not in node for node in current_nodes for marker in ("endpoint_value", "observed", "fitted")))
    check("transfer graph has no endpoint-value input node", all(marker not in node for node in transfer_nodes for marker in ("endpoint_value", "observed", "fitted")))
    check("unit calibration is not silently inserted", "unit_readout_calibration" not in transfer_nodes)


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("S3_ENDPOINT_AXIS_READOUT_TRANSFER_CLASSIFICATION_2026-06-26.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    pr_body = loop_text("PR_BODY.md")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: exact-support for a four-slot transfer classification; no current endpoint closure",
        "There are twelve labeled witnesses",
        "No quotient that identifies a mixed shell/center pair works",
        "The current endpoint surface does not yet prove the physical quotient",
        "S3 endpoint axis-readout transfer theorem",
        "It proposes no new framework primitive",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block154 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names physical endpoint transfer theorem", "physical endpoint axis-readout transfer theorem" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    check("review history records no review-loop worker", "No review-loop worker was run" in review)
    check("PR body says no framework primitive is proposed", "No framework primitive is proposed" in pr_body)
    banned = (
        ("old shorthand hyphenated upper", phrase("Route", "-", "2")),
        ("old shorthand hyphenated lower", phrase("route", "-", "2")),
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
    print("S3 endpoint axis-readout transfer classification")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_four_to_three_classification()
    part3_signed_readout_transfer()
    part4_current_surface_firewall()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: classified conditional four-slot transfers exist, but the current endpoint surface does not supply the physical quotient, source law, or same-source signed readout theorem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
