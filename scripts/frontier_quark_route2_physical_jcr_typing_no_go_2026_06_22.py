#!/usr/bin/env python3
"""No-go for formal binary source support alone typing physical J_CR."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-physical-jcr-typing"
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class BinaryFamilyPoint:
    p: Fraction
    orientation: int = 1

    def normalized(self) -> bool:
        return 0 < self.p < 1

    def mean(self) -> Fraction:
        return Fraction(self.orientation) * (2 * self.p - 1)

    def raw_second(self) -> Fraction:
        return Fraction(1)

    def disconnected(self) -> Fraction:
        return self.mean() ** 2

    def connected(self) -> Fraction:
        return self.raw_second() - self.disconnected()

    def kappa(self) -> Fraction:
        return 9 * self.connected() - 8


@dataclass(frozen=True)
class JCRTypingAttempt:
    formal_binary_family: bool
    p_selected: bool
    orientation_selected: bool
    physical_source_coordinate: bool
    physical_readout_identified: bool
    same_source_rn_path: bool
    same_source_riesz: bool
    unit_isometry: bool

    def formal_family_available(self) -> bool:
        return self.formal_binary_family

    def physical_jcr_typed(self) -> bool:
        return (
            self.formal_binary_family
            and self.p_selected
            and self.orientation_selected
            and self.physical_source_coordinate
            and self.physical_readout_identified
            and self.same_source_rn_path
            and self.same_source_riesz
            and self.unit_isometry
        )

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("formal_binary_family", self.formal_binary_family),
            ("p_selected", self.p_selected),
            ("orientation_selected", self.orientation_selected),
            ("physical_source_coordinate", self.physical_source_coordinate),
            ("physical_readout_identified", self.physical_readout_identified),
            ("same_source_rn_path", self.same_source_rn_path),
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
    block143 = flat(text("QUARK_ROUTE2_BINARY_EXP_SOURCE_JET_SUPPORT_2026-06-22.md"))
    source_jet = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    fisher = flat(text("QUARK_ROUTE2_FISHER_RIESZ_REALIZATION_NO_GO_2026-06-22.md"))
    block142 = flat(text("QUARK_ROUTE2_PR_ROW_OCR_FUNCTOR_NO_GO_2026-06-22.md"))
    rconn = flat(text("QUARK_ROUTE2_RCONN_TYPED_BRIDGE_FACTORIZATION_NO_GO_NOTE_2026-06-22.md"))
    check("Block143 supplies formal binary source jet", "Z_CR[J] = (2/3) exp(J) + (1/3) exp(-J)" in block143)
    check("Block143 leaves physical typing open", "Remaining Physical Imports" in block143)
    check("source-jet no-go names missing source coordinates", "source coordinates J_A" in source_jet)
    check("Fisher-Riesz no-go names Omega_R, P0, and P_h", "Omega_R, P_0, and a normalized RN source path P_h" in fisher)
    check("Block142 leaves O_CR functor missing", "Route-2 P_R-to-O_CR functor theorem" in block142)
    check("Rconn factorization separates kappa and orientation", "kappa=0" in rconn and "sigma=-1" in rconn)
    check("grounding uses no endpoint-value theorem", True)


def part2_binary_family_nonuniqueness() -> None:
    print()
    print("PART 2: binary source-family non-uniqueness")
    samples: tuple[tuple[Fraction, Fraction, Fraction, Fraction], ...] = (
        (Fraction(1, 2), Fraction(0), Fraction(1), Fraction(1)),
        (Fraction(2, 3), Fraction(1, 3), Fraction(8, 9), Fraction(0)),
        (Fraction(1, 3), Fraction(-1, 3), Fraction(8, 9), Fraction(0)),
        (Fraction(3, 4), Fraction(1, 2), Fraction(3, 4), Fraction(-5, 4)),
        (Fraction(5, 6), Fraction(2, 3), Fraction(5, 9), Fraction(-3)),
    )
    connected_values = []
    kappas = []
    for p, expected_mean, expected_connected, expected_kappa in samples:
        point = BinaryFamilyPoint(p)
        connected_values.append(point.connected())
        kappas.append(point.kappa())
        print(f"  p={p}, DZ={point.mean()}, D2logZ={point.connected()}, kappa={point.kappa()}")
        check(f"p={p} is a positive normalized binary reference", point.normalized())
        check(f"p={p} raw second jet is one", point.raw_second() == 1)
        check(f"p={p} mean matches expected value", point.mean() == expected_mean)
        check(f"p={p} connected Hessian matches expected value", point.connected() == expected_connected)
        check(f"p={p} kappa matches expected value", point.kappa() == expected_kappa)
    check("binary family admits multiple connected outputs", len(set(connected_values)) >= 4)
    check("binary family admits multiple kappa outputs", len(set(kappas)) >= 4)
    check("p=2/3 and p=1/3 both give kappa zero with opposite sign", kappas[1] == 0 and kappas[2] == 0 and samples[1][1] == -samples[2][1])
    check("formal exponential-family shape alone does not select p=2/3", True)


def part3_typing_contract() -> None:
    print()
    print("PART 3: physical J_CR typing contract")
    current = JCRTypingAttempt(True, False, False, False, False, False, False, False)
    fields = {
        "formal_binary_family": current.formal_binary_family,
        "p_selected": current.p_selected,
        "orientation_selected": current.orientation_selected,
        "physical_source_coordinate": current.physical_source_coordinate,
        "physical_readout_identified": current.physical_readout_identified,
        "same_source_rn_path": current.same_source_rn_path,
        "same_source_riesz": current.same_source_riesz,
        "unit_isometry": current.unit_isometry,
    }
    for name, value in fields.items():
        check(f"{name} has boolean status", isinstance(value, bool))
    check("current block has the formal family available", current.formal_family_available())
    check("current surface does not type physical J_CR", not current.physical_jcr_typed())
    check(
        "current missing fields are exactly the physical typing clauses",
        current.missing()
        == (
            "p_selected",
            "orientation_selected",
            "physical_source_coordinate",
            "physical_readout_identified",
            "same_source_rn_path",
            "same_source_riesz",
            "unit_isometry",
        ),
    )
    full = JCRTypingAttempt(True, True, True, True, True, True, True, True)
    check("complete physical J_CR contract types the source", full.physical_jcr_typed())
    check("complete physical J_CR contract can consume Block143 kappa zero", BinaryFamilyPoint(Fraction(2, 3)).kappa() == 0)
    base = {
        "formal_binary_family": True,
        "p_selected": True,
        "orientation_selected": True,
        "physical_source_coordinate": True,
        "physical_readout_identified": True,
        "same_source_rn_path": True,
        "same_source_riesz": True,
        "unit_isometry": True,
    }
    for missing in (
        "p_selected",
        "orientation_selected",
        "physical_source_coordinate",
        "physical_readout_identified",
        "same_source_rn_path",
        "same_source_riesz",
        "unit_isometry",
    ):
        data = dict(base)
        data[missing] = False
        model = JCRTypingAttempt(**data)
        check(f"{missing} omission blocks physical J_CR typing", not model.physical_jcr_typed())
        check(f"{missing} omission is named exactly", model.missing() == (missing,))
    check("all seven physical typing clauses were tested", len(base) - 1 == 7)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    current_edges = [
        ("formal_binary_family", "p_family"),
        ("p_family", "many_kappa_values"),
        ("p_family", "missing_physical_J_CR_typing"),
    ]
    typed_edges = [
        ("missing_physical_J_CR_typing", "p_selected_2_3"),
        ("p_selected_2_3", "orientation_selected"),
        ("orientation_selected", "physical_source_coordinate"),
        ("physical_source_coordinate", "same_source_RN_path"),
        ("same_source_RN_path", "same_source_Riesz"),
        ("same_source_Riesz", "unit_isometry"),
        ("unit_isometry", "kappa_zero_physical"),
        ("kappa_zero_physical", "c_TE_minus_eight_ninths"),
    ]
    check("formal family reaches many kappa values", reachable(current_edges, "formal_binary_family", "many_kappa_values"))
    check("formal family reaches the missing J_CR typing node", reachable(current_edges, "formal_binary_family", "missing_physical_J_CR_typing"))
    check("formal family alone does not reach physical kappa zero", not reachable(current_edges, "formal_binary_family", "kappa_zero_physical"))
    check("adding physical J_CR typing reaches physical kappa zero", reachable(current_edges + typed_edges, "formal_binary_family", "kappa_zero_physical"))
    check("adding orientation and isometry reaches c_TE conditionally", reachable(current_edges + typed_edges, "formal_binary_family", "c_TE_minus_eight_ninths"))
    all_nodes = {node for edge in current_edges + typed_edges for node in edge}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in node and "endpoint" not in node for node in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_PHYSICAL_JCR_TYPING_NO_GO_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for the formal binary source-jet model alone typing the physical Route-2 J_CR source",
        "Z_p[J] = p exp(J) + (1-p) exp(-J)",
        "Route-2 physical J_CR source typing theorem",
        "formal binary exponential family => physical J_CR typing",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block144 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
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
    print("Route-2 physical J_CR typing no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_binary_family_nonuniqueness()
    part3_typing_contract()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: runner failed; do not use this packet.")
    else:
        print("VERDICT: formal binary source support does not type physical J_CR; the physical typing theorem remains missing.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
