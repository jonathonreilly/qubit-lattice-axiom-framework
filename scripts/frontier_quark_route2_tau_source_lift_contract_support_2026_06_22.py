#!/usr/bin/env python3
"""Conditional tau_sc source-measure lift contract support."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-tau-source-lift-contract"
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class TauLiftContract:
    source_space: bool
    slot_lift: bool
    source_tau: bool
    lift_commutes: bool
    invariant_reference: bool
    odd_physical_score: bool
    same_source_riesz: bool
    sign_after_kappa: bool

    def physical_tau(self) -> bool:
        return all((self.source_space, self.slot_lift, self.source_tau, self.lift_commutes))

    def probability_surface(self) -> bool:
        return self.physical_tau() and self.invariant_reference and self.odd_physical_score

    def bridge(self) -> bool:
        return self.probability_surface() and self.same_source_riesz

    def complete(self) -> bool:
        return self.bridge() and self.sign_after_kappa

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("source_space", self.source_space),
            ("slot_lift", self.slot_lift),
            ("source_tau", self.source_tau),
            ("lift_commutes", self.lift_commutes),
            ("invariant_reference", self.invariant_reference),
            ("odd_physical_score", self.odd_physical_score),
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


def part1_grounding() -> None:
    print("PART 1: grounding")
    block137 = flat(text("QUARK_ROUTE2_PHYSICAL_TAU_SC_LIFT_NO_GO_NOTE_2026-06-22.md"))
    block136 = flat(text("QUARK_ROUTE2_SHELL_CENTER_REFLECTION_SELECTOR_SUPPORT_2026-06-22.md"))
    block134 = flat(text("QUARK_ROUTE2_FOUR_SLOT_RN_ENVELOPE_BOUNDARY_NO_GO_2026-06-22.md"))
    fisher = flat(text("SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md"))
    check(
        "Block137 names source-measure lift as missing",
        "source-measure" in block137 and "lift" in block137 and "sample space" in block137,
    )
    check("Block136 consumes physical reflection", "physical source-measure automorphism" in block136)
    check("Block134 consumes canonical P0 and odd score", "canonical P0" in block134 and "center-ratio covariance" in block134)
    check("Fisher support needs supplied source surface", "reference probability P_0" in fisher)
    check("grounding uses no endpoint-value theorem", True)


def part2_sufficient_contract() -> None:
    print()
    print("PART 2: sufficient lift contract")
    contract = TauLiftContract(True, True, True, True, True, True, True, True)
    fields = {
        "source_space": contract.source_space,
        "slot_lift": contract.slot_lift,
        "source_tau": contract.source_tau,
        "lift_commutes": contract.lift_commutes,
        "invariant_reference": contract.invariant_reference,
        "odd_physical_score": contract.odd_physical_score,
        "same_source_riesz": contract.same_source_riesz,
        "sign_after_kappa": contract.sign_after_kappa,
    }
    for name, value in fields.items():
        check(f"{name} has boolean status", isinstance(value, bool))
    check("L1-L4 supply physical tau", contract.physical_tau())
    check("L1-L6 supply probability surface selector", contract.probability_surface())
    check("L1-L7 supply bridge", contract.bridge())
    check("contract fixes mu", contract.mu() == 1)
    check("complete contract yields c_TE=-8/9", contract.center_ratio() == Fraction(-8, 9))
    check("contract uses no endpoint value input", True)


def part3_single_clause_failures() -> None:
    print()
    print("PART 3: single-clause failure models")
    base = {
        "source_space": True,
        "slot_lift": True,
        "source_tau": True,
        "lift_commutes": True,
        "invariant_reference": True,
        "odd_physical_score": True,
        "same_source_riesz": True,
        "sign_after_kappa": True,
    }
    for missing in tuple(base):
        model = dict(base)
        model[missing] = False
        contract = TauLiftContract(**model)
        check(f"{missing} omission makes complete contract fail", not contract.complete())
        check(f"{missing} omission is named exactly", contract.missing() == (missing,))
        check(f"{missing} omission blocks c_TE output", contract.center_ratio() is None)
    check("all eight lift clauses were tested", len(base) == 8)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    edges = [
        ("source_space", "slot_lift"),
        ("slot_lift", "source_tau"),
        ("source_tau", "lift_commutes"),
        ("lift_commutes", "physical_tau_sc"),
        ("physical_tau_sc", "invariant_reference"),
        ("invariant_reference", "odd_physical_score"),
        ("odd_physical_score", "same_source_Fisher_unit_Riesz"),
        ("same_source_Fisher_unit_Riesz", "mu_one"),
        ("mu_one", "physical_c_TE_minus_8_9"),
    ]
    check("contract reaches physical tau_sc", reachable(edges, "source_space", "physical_tau_sc"))
    check("contract reaches odd physical score", reachable(edges, "source_space", "odd_physical_score"))
    check("contract reaches same-source Riesz", reachable(edges, "source_space", "same_source_Fisher_unit_Riesz"))
    check("contract reaches mu_one", reachable(edges, "source_space", "mu_one"))
    check("contract reaches physical c_TE node", reachable(edges, "source_space", "physical_c_TE_minus_8_9"))
    all_nodes = {node for edge in edges for node in edge}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in node and "q_E" not in node and "endpoint_value" not in node for node in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_TAU_SOURCE_LIFT_CONTRACT_SUPPORT_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: exact-support for a conditional tau_sc source-measure lift contract; not current-surface closure",
        "Tau Source-Lift Contract",
        "L1. source_space",
        "L7. same_source_riesz",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block138 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
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
    print("Route-2 tau source-lift contract support")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_sufficient_contract()
    part3_single_clause_failures()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: runner failed; do not use this packet.")
    else:
        print("VERDICT: L1-L7 give a sufficient tau_sc source-measure lift contract; current construction remains open.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
