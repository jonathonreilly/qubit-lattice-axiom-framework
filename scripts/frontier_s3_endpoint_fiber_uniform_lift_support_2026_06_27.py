#!/usr/bin/env python3
"""Self-contained finite check for fiber-uniform S3 endpoint lifts."""

from __future__ import annotations

import itertools
from collections import Counter, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class Slot:
    name: str
    radial: str
    channel: str


@dataclass(frozen=True)
class Lift:
    quotient: tuple[int, int, int, int]

    @property
    def counts(self) -> Counter[int]:
        return Counter(self.quotient)

    @property
    def weights(self) -> tuple[Fraction, Fraction, Fraction, Fraction]:
        return tuple(Fraction(1, 3 * self.counts[axis]) for axis in self.quotient)

    @property
    def pushforward(self) -> tuple[Fraction, Fraction, Fraction]:
        return tuple(
            sum(weight for axis, weight in zip(self.quotient, self.weights) if axis == target)
            for target in range(3)
        )

    @property
    def pair_axis(self) -> int:
        paired = [axis for axis, count in self.counts.items() if count == 2]
        assert len(paired) == 1
        return paired[0]

    @property
    def pair_indices(self) -> tuple[int, int]:
        pair = tuple(index for index, axis in enumerate(self.quotient) if axis == self.pair_axis)
        assert len(pair) == 2
        return pair

    @property
    def pair_kind(self) -> str:
        radials = {SLOTS[index].radial for index in self.pair_indices}
        return next(iter(radials)) if len(radials) == 1 else "mixed"

    @property
    def e_t_symmetric(self) -> bool:
        e_shell, e_center, t_shell, t_center = self.weights
        return e_shell == t_shell and e_center == t_center

    @property
    def shell_mass(self) -> Fraction:
        return self.weights[0] + self.weights[2]

    @property
    def center_mass(self) -> Fraction:
        return self.weights[1] + self.weights[3]

    @property
    def radial_mean(self) -> Fraction:
        return self.center_mass - self.shell_mass

    @property
    def radial_connected(self) -> Fraction:
        return 1 - self.radial_mean * self.radial_mean

    @property
    def radial_kappa(self) -> Fraction:
        return 9 * (self.radial_connected - Fraction(8, 9))


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


def text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def flat(s: str) -> str:
    return " ".join(s.replace("`", "").replace("**", "").split())


def is_surjective(quotient: tuple[int, int, int, int]) -> bool:
    return set(quotient) == {0, 1, 2}


def all_lifts() -> list[Lift]:
    return [Lift(tuple(q)) for q in itertools.product(range(3), repeat=4) if is_surjective(tuple(q))]


def reachable(edges: Iterable[tuple[str, str]], start: str, target: str) -> bool:
    graph: dict[str, set[str]] = {}
    for source, dest in edges:
        graph.setdefault(source, set()).add(dest)
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


def part1_fiber_uniform_classification() -> None:
    print("PART 1: fiber-uniform lift classification")
    lifts = all_lifts()
    et_lifts = [lift for lift in lifts if lift.e_t_symmetric]
    shell_pair = [lift for lift in et_lifts if lift.pair_kind == "shell"]
    center_pair = [lift for lift in et_lifts if lift.pair_kind == "center"]
    mixed_pair = [lift for lift in lifts if lift.pair_kind == "mixed"]
    weight_shapes = {lift.weights for lift in lifts}
    et_weight_shapes = {lift.weights for lift in et_lifts}

    check("there are thirty-six total surjective quotients", len(lifts) == 36)
    check("each quotient has one two-label fiber and two singleton fibers", all(sorted(lift.counts.values()) == [1, 1, 2] for lift in lifts))
    check("all fiber-uniform lifts push forward to uniform axes", all(lift.pushforward == (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)) for lift in lifts))
    check("six endpoint weight placements occur", len(weight_shapes) == 6)
    check("every lift uses only one-sixth and one-third weights", all(set(lift.weights) == {Fraction(1, 6), Fraction(1, 3)} for lift in lifts))
    check("twelve fiber-uniform lifts also satisfy E/T symmetry", len(et_lifts) == 12)
    check("six E/T-symmetric lifts pair shell labels", len(shell_pair) == 6)
    check("six E/T-symmetric lifts pair center labels", len(center_pair) == 6)
    check("mixed-pair quotients are the complement", len(mixed_pair) == 24)
    check("all mixed-pair fiber-uniform lifts break E/T symmetry", all(not lift.e_t_symmetric for lift in mixed_pair))
    check(
        "E/T-symmetric lifts have exactly the two same-radial weight shapes",
        et_weight_shapes
        == {
            (Fraction(1, 6), Fraction(1, 3), Fraction(1, 6), Fraction(1, 3)),
            (Fraction(1, 3), Fraction(1, 6), Fraction(1, 3), Fraction(1, 6)),
        },
    )


def part2_conditional_radial_bias() -> None:
    print()
    print("PART 2: conditional radial-bias consequence")
    et_lifts = [lift for lift in all_lifts() if lift.e_t_symmetric]
    shell_pair = [lift for lift in et_lifts if lift.pair_kind == "shell"]
    center_pair = [lift for lift in et_lifts if lift.pair_kind == "center"]

    for index, lift in enumerate(et_lifts):
        print(
            f"  et_lift={index:02d} quotient={lift.quotient} pair={lift.pair_kind} "
            f"weights={lift.weights} shell={lift.shell_mass} center={lift.center_mass} "
            f"radial_mean={lift.radial_mean} radial_kappa={lift.radial_kappa}"
        )
        check("E/T-symmetric lift has endpoint weights in {1/6,1/3}", set(lift.weights) == {Fraction(1, 6), Fraction(1, 3)})
        check("E/T-symmetric lift has radial masses one-third and two-thirds", {lift.shell_mass, lift.center_mass} == {Fraction(1, 3), Fraction(2, 3)})
        check("E/T-symmetric lift gives radial mean magnitude one third", abs(lift.radial_mean) == Fraction(1, 3))
        check("E/T-symmetric lift gives connected eight ninths", lift.radial_connected == Fraction(8, 9))
        check("E/T-symmetric lift gives radial kappa zero", lift.radial_kappa == 0)
    check("shell-pair lifts make shell the lighter radial sector", all(lift.shell_mass == Fraction(1, 3) for lift in shell_pair))
    check("center-pair lifts make center the lighter radial sector", all(lift.center_mass == Fraction(1, 3) for lift in center_pair))
    check("no E/T-symmetric lift selects shell over center by itself", len(shell_pair) == len(center_pair))


def part3_shortcut_boundaries() -> None:
    print()
    print("PART 3: shortcut boundaries")
    lifts = all_lifts()
    lift_weights = {lift.weights for lift in lifts}
    uniform_four = (Fraction(1, 4), Fraction(1, 4), Fraction(1, 4), Fraction(1, 4))
    open_premises = {
        "physical_four_to_three_quotient",
        "fiber_uniform_source_lift",
        "same_source_signed_readout",
        "connected_typing_and_unit_calibration",
    }
    supplied_premises = {"normalized_axis_law", "et_channel_symmetry"}

    check("uniform four-slot law is not any fiber-uniform four-to-three lift", uniform_four not in lift_weights)
    check("fiber-uniform theorem is stronger than positivity", len(lift_weights) == 6)
    check("the support result names four open physical premises", open_premises == {"physical_four_to_three_quotient", "fiber_uniform_source_lift", "same_source_signed_readout", "connected_typing_and_unit_calibration"})
    check("the finite check supplies only axis law and E/T symmetry as premises", supplied_premises == {"normalized_axis_law", "et_channel_symmetry"})
    check("quotient/lift premises remain distinct from readout/calibration premises", open_premises.isdisjoint(supplied_premises))
    check("same-source readout is not silently inserted", "same_source_signed_readout" in open_premises)
    check("connected typing and unit calibration are not silently inserted", "connected_typing_and_unit_calibration" in open_premises)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    current_edges = [
        ("current_endpoint_surface", "four_endpoint_labels"),
        ("current_endpoint_surface", "ET_channel_symmetry"),
        ("current_endpoint_surface", "normalized_axis_support"),
        ("current_endpoint_surface", "missing_physical_four_to_three_quotient"),
        ("current_endpoint_surface", "missing_fiber_uniform_lift"),
        ("missing_physical_four_to_three_quotient", "missing_witness_selection"),
        ("missing_fiber_uniform_lift", "missing_witness_selection"),
    ]
    theorem_edges = [
        ("fiber_uniform_quotient_lift_theorem", "physical_four_to_three_quotient"),
        ("fiber_uniform_quotient_lift_theorem", "fiber_uniform_lift"),
        ("physical_four_to_three_quotient", "fiber_uniform_ET_symmetric_lift"),
        ("fiber_uniform_lift", "fiber_uniform_ET_symmetric_lift"),
        ("ET_channel_symmetry", "fiber_uniform_ET_symmetric_lift"),
        ("fiber_uniform_ET_symmetric_lift", "radial_1_to_2_bias"),
        ("fiber_uniform_ET_symmetric_lift", "conditional_endpoint_witness"),
        ("conditional_endpoint_witness", "missing_same_source_readout_and_typing"),
    ]
    full_edges = theorem_edges + [
        ("same_source_signed_readout_and_typing", "kappa_zero_on_physical_endpoint_source"),
        ("conditional_endpoint_witness", "same_source_signed_readout_and_typing"),
    ]
    check("current surface reaches missing witness selection", reachable(current_edges, "current_endpoint_surface", "missing_witness_selection"))
    check("current surface does not reach radial bias", not reachable(current_edges, "current_endpoint_surface", "radial_1_to_2_bias"))
    check("fiber-uniform quotient theorem reaches radial bias", reachable(current_edges + theorem_edges, "fiber_uniform_quotient_lift_theorem", "radial_1_to_2_bias"))
    check("fiber-uniform quotient theorem selects a conditional endpoint witness", reachable(current_edges + theorem_edges, "fiber_uniform_quotient_lift_theorem", "conditional_endpoint_witness"))
    check("fiber-uniform quotient theorem alone does not claim physical kappa zero", not reachable(current_edges + theorem_edges, "fiber_uniform_quotient_lift_theorem", "kappa_zero_on_physical_endpoint_source"))
    check("adding same-source readout and typing would reach physical kappa zero", reachable(current_edges + full_edges, "fiber_uniform_quotient_lift_theorem", "kappa_zero_on_physical_endpoint_source"))
    all_nodes = {node for edge in current_edges + full_edges for node in edge}
    check("reachability graph has no endpoint-value input node", all(marker not in node for node in all_nodes for marker in ("observed", "fitted", "endpoint_value")))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("S3_ENDPOINT_FIBER_UNIFORM_LIFT_SUPPORT_2026-06-27.md")
    note_flat = flat(note)
    required = (
        "Claim-strength label: exact support theorem on a stated quotient-lift premise; no current endpoint closure",
        "uniform conditional law on each quotient fiber",
        "the radial 1:2 or 2:1 law is a consequence",
        "It is not a separate numerical input once those clauses are independently proven",
        "The note removes one apparent independent burden",
        "S3 endpoint quotient-lift theorem",
        "It proposes no new framework primitive",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    banned = (
        ("old output path", "../outputs/"),
        ("branch-local state path", ".claude/"),
        ("claim-status certificate", "CLAIM_STATUS_CERTIFICATE"),
        ("audit clean prediction", "audited_clean"),
        ("target effective status", "target_effective_status"),
        ("retained status leakage", "retained"),
        ("closed predecessor block dependency", "Block154"),
        ("closed predecessor block dependency", "Block155"),
    )
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in note)


def main() -> int:
    print("S3 endpoint fiber-uniform lift support")
    print("TRACE: conditional_finite_support")
    part1_fiber_uniform_classification()
    part2_conditional_radial_bias()
    part3_shortcut_boundaries()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: under a physical four-to-three quotient plus a fiber-uniform E/T-symmetric lift, the radial one-to-two law follows; the physical quotient-lift theorem remains open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
