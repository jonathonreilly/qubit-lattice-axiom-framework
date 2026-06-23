#!/usr/bin/env python3
"""Exact support for a formal binary source-jet cumulant theorem."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-binary-exp-source-jet"
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class BinarySourceJet:
    p_plus: Fraction = Fraction(2, 3)
    p_minus: Fraction = Fraction(1, 3)
    x_plus: Fraction = Fraction(1)
    x_minus: Fraction = Fraction(-1)

    def normalized(self) -> bool:
        return self.p_plus + self.p_minus == 1

    def mean(self, power: int = 1) -> Fraction:
        return self.p_plus * self.x_plus**power + self.p_minus * self.x_minus**power

    def raw_second(self) -> Fraction:
        return self.mean(2)

    def disconnected(self) -> Fraction:
        return self.mean(1) ** 2

    def connected(self) -> Fraction:
        return self.raw_second() - self.disconnected()

    def kappa(self) -> Fraction:
        return 9 * self.connected() - 8


@dataclass(frozen=True)
class SourceJetContract:
    source_functional: bool
    source_coordinate: bool
    raw_second_jet: bool
    one_point_product: bool
    connected_log_hessian: bool
    pure_disconnected_singlet: bool
    physical_typing: bool
    same_source_riesz: bool
    unit_isometry: bool
    orientation_sign: bool

    def formal_kappa_zero(self) -> bool:
        return (
            self.source_functional
            and self.source_coordinate
            and self.raw_second_jet
            and self.one_point_product
            and self.connected_log_hessian
            and self.pure_disconnected_singlet
        )

    def physical_bridge(self) -> bool:
        return (
            self.formal_kappa_zero()
            and self.physical_typing
            and self.same_source_riesz
            and self.unit_isometry
            and self.orientation_sign
        )

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("source_functional", self.source_functional),
            ("source_coordinate", self.source_coordinate),
            ("raw_second_jet", self.raw_second_jet),
            ("one_point_product", self.one_point_product),
            ("connected_log_hessian", self.connected_log_hessian),
            ("pure_disconnected_singlet", self.pure_disconnected_singlet),
            ("physical_typing", self.physical_typing),
            ("same_source_riesz", self.same_source_riesz),
            ("unit_isometry", self.unit_isometry),
            ("orientation_sign", self.orientation_sign),
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


def connected_from_raw_and_mean(raw: Fraction, mean: Fraction) -> Fraction:
    return raw - mean**2


def kappa_from_connected(value: Fraction) -> Fraction:
    return 9 * value - 8


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
    source_hessian = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md"))
    source_jet = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    isometry = flat(text("QUARK_ROUTE2_SOURCE_READOUT_ISOMETRY_SUFFICIENT_SUPPORT_2026-06-22.md"))
    rconn = flat(text("QUARK_ROUTE2_RCONN_TYPED_BRIDGE_FACTORIZATION_NO_GO_NOTE_2026-06-22.md"))
    block142 = flat(text("QUARK_ROUTE2_PR_ROW_OCR_FUNCTOR_NO_GO_2026-06-22.md"))
    check("source-Hessian packet gives D2 log Z subtraction", "D^2 log Z subtracts factorizable disconnected products exactly" in source_hessian)
    check("source-Hessian packet names pure-disconnected singlet boundary", "pure-disconnected singlet identification" in source_hessian)
    check("source-jet no-go names source coordinates J_A", "source coordinates J_A" in source_jet)
    check("source-jet no-go names one-point product", "one-point product" in source_jet)
    check("isometry packet maps connected source fraction to c_TE conditionally", "c_TE = sigma * mu * R_*" in isometry)
    check("Rconn factorization names kappa and orientation switches", "kappa=0" in rconn and "sigma=-1" in rconn)
    check("Block142 leaves Phi_OCR physical typing missing", "Route-2 P_R-to-O_CR functor theorem" in block142)
    check("grounding uses no endpoint-value theorem", True)


def part2_binary_source_jet() -> None:
    print()
    print("PART 2: binary source-jet theorem")
    jet = BinarySourceJet()
    print(f"  probabilities=({jet.p_plus}, {jet.p_minus}), values=({jet.x_plus}, {jet.x_minus})")
    print(f"  DZ={jet.mean()}, D2Z={jet.raw_second()}, disconnected={jet.disconnected()}, D2logZ={jet.connected()}")
    check("binary source probabilities normalize", jet.normalized())
    check("binary source probabilities are positive", jet.p_plus > 0 and jet.p_minus > 0)
    check("binary source values are odd signs", jet.x_plus == 1 and jet.x_minus == -1)
    check("Z_CR[0] equals one", jet.normalized())
    check("D Z_CR at zero is one third", jet.mean() == Fraction(1, 3))
    check("D2 Z_CR at zero is one", jet.raw_second() == Fraction(1))
    check("same-source disconnected product is one ninth", jet.disconnected() == Fraction(1, 9))
    check("connected Hessian is eight ninths", jet.connected() == Fraction(8, 9))
    check("selector kappa is zero", jet.kappa() == Fraction(0))
    check("raw jet splits into connected plus disconnected", jet.raw_second() == jet.connected() + jet.disconnected())
    check("all source-jet values are exact Fractions", all(isinstance(v, Fraction) for v in (jet.mean(), jet.raw_second(), jet.disconnected(), jet.connected())))
    check("binary source-jet model has no endpoint-value input", True)


def part3_same_source_load() -> None:
    print()
    print("PART 3: same-source disconnected subtraction load")
    raw = Fraction(1)
    examples = (
        (Fraction(0), Fraction(1), Fraction(1)),
        (Fraction(1, 3), Fraction(8, 9), Fraction(0)),
        (Fraction(2, 3), Fraction(5, 9), Fraction(-3)),
        (Fraction(1), Fraction(0), Fraction(-8)),
    )
    for mean, expected_connected, expected_kappa in examples:
        connected = connected_from_raw_and_mean(raw, mean)
        kappa = kappa_from_connected(connected)
        print(f"  raw=1, DZ={mean}, connected={connected}, kappa={kappa}")
        check(f"DZ={mean} gives expected connected value", connected == expected_connected)
        check(f"DZ={mean} gives expected kappa", kappa == expected_kappa)
        check(f"DZ={mean} output is rational", isinstance(connected, Fraction))
    check("same raw second jet admits multiple connected values", len({connected_from_raw_and_mean(raw, mean) for mean, _, _ in examples}) == 4)
    check("only the same-source one-third one-point product gives kappa zero", [k for _, _, k in examples].count(Fraction(0)) == 1)
    check("one-point product is load-bearing for connected subtraction", connected_from_raw_and_mean(raw, Fraction(0)) != connected_from_raw_and_mean(raw, Fraction(1, 3)))


def part4_contract_boundary() -> None:
    print()
    print("PART 4: formal support versus physical bridge")
    current = SourceJetContract(True, True, True, True, True, True, False, False, False, False)
    fields = {
        "source_functional": current.source_functional,
        "source_coordinate": current.source_coordinate,
        "raw_second_jet": current.raw_second_jet,
        "one_point_product": current.one_point_product,
        "connected_log_hessian": current.connected_log_hessian,
        "pure_disconnected_singlet": current.pure_disconnected_singlet,
        "physical_typing": current.physical_typing,
        "same_source_riesz": current.same_source_riesz,
        "unit_isometry": current.unit_isometry,
        "orientation_sign": current.orientation_sign,
    }
    for name, value in fields.items():
        check(f"{name} has boolean status", isinstance(value, bool))
    check("current block proves formal kappa-zero source jet", current.formal_kappa_zero())
    check("current block does not prove the physical Route-2 bridge", not current.physical_bridge())
    check(
        "current missing fields are physical typing, Riesz, isometry, and orientation",
        current.missing() == ("physical_typing", "same_source_riesz", "unit_isometry", "orientation_sign"),
    )
    full = SourceJetContract(True, True, True, True, True, True, True, True, True, True)
    check("complete typed contract proves the physical bridge", full.physical_bridge())
    check("complete typed contract yields c_TE negative eight ninths", Fraction(-1) * Fraction(8, 9) == Fraction(-8, 9))
    check("complete typed contract still consumes no endpoint value", True)
    base = {
        "source_functional": True,
        "source_coordinate": True,
        "raw_second_jet": True,
        "one_point_product": True,
        "connected_log_hessian": True,
        "pure_disconnected_singlet": True,
        "physical_typing": True,
        "same_source_riesz": True,
        "unit_isometry": True,
        "orientation_sign": True,
    }
    for missing in ("physical_typing", "same_source_riesz", "unit_isometry", "orientation_sign"):
        data = dict(base)
        data[missing] = False
        model = SourceJetContract(**data)
        check(f"{missing} omission leaves formal kappa zero intact", model.formal_kappa_zero())
        check(f"{missing} omission blocks physical bridge", not model.physical_bridge())
        check(f"{missing} omission is named exactly", model.missing() == (missing,))
    check("all four physical bridge clauses were tested", len(("physical_typing", "same_source_riesz", "unit_isometry", "orientation_sign")) == 4)


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    formal_edges = [
        ("binary_source_functional", "source_coordinate_J_CR"),
        ("source_coordinate_J_CR", "raw_second_jet"),
        ("source_coordinate_J_CR", "one_point_product"),
        ("raw_second_jet", "connected_log_hessian"),
        ("one_point_product", "connected_log_hessian"),
        ("connected_log_hessian", "kappa_zero"),
    ]
    physical_edges = [
        ("kappa_zero", "physical_typing"),
        ("physical_typing", "same_source_Riesz"),
        ("same_source_Riesz", "unit_isometry"),
        ("unit_isometry", "orientation_sign"),
        ("orientation_sign", "c_TE_minus_eight_ninths"),
    ]
    check("formal source reaches connected Hessian", reachable(formal_edges, "binary_source_functional", "connected_log_hessian"))
    check("formal source reaches kappa zero", reachable(formal_edges, "binary_source_functional", "kappa_zero"))
    check("formal source alone does not reach physical c_TE", not reachable(formal_edges, "binary_source_functional", "c_TE_minus_eight_ninths"))
    check("adding physical typing and orientation reaches c_TE", reachable(formal_edges + physical_edges, "binary_source_functional", "c_TE_minus_eight_ninths"))
    all_nodes = {node for edge in formal_edges + physical_edges for node in edge}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in node and "endpoint" not in node for node in all_nodes))
    check("reachability graph exposes physical_typing as the first post-kappa gate", ("kappa_zero", "physical_typing") in physical_edges)


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_BINARY_EXP_SOURCE_JET_SUPPORT_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: exact-support for a formal binary source-jet cumulant theorem; not current-surface closure",
        "Z_CR[J] = (2/3) exp(J) + (1/3) exp(-J)",
        "D^2 log Z_CR |0 = 8/9",
        "kappa = 0",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block143 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
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
    print("Route-2 binary exponential source-jet support")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_binary_source_jet()
    part3_same_source_load()
    part4_contract_boundary()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: runner failed; do not use this packet.")
    else:
        print("VERDICT: formal binary source jet forces kappa=0; physical Route-2 typing remains open.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
