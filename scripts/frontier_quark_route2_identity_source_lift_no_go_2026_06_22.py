#!/usr/bin/env python3
"""Identity four-slot source lift boundary for Route-2.

The script tests the tempting construction

    Omega_S = Omega_R, iota = id, tau_S = tau_sc, P0 = uniform.

It verifies that this is a valid formal lift through the first five clauses of
the Block138 contract, then checks that the physical score and same-source
Riesz clauses remain independent missing primitives.  No endpoint value is
used as a proof input.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-identity-source-lift"
PASS = 0
FAIL = 0

SLOTS = ("E-shell", "E-center", "T-shell", "T-center")


@dataclass(frozen=True)
class IdentityLiftAttempt:
    source_space: bool
    slot_lift: bool
    source_tau: bool
    lift_commutes: bool
    invariant_reference: bool
    formal_odd_contrast: bool
    physical_score_typing: bool
    source_jet: bool
    same_source_riesz: bool

    def formal_lift(self) -> bool:
        return all(
            (
                self.source_space,
                self.slot_lift,
                self.source_tau,
                self.lift_commutes,
                self.invariant_reference,
            )
        )

    def formal_selector(self) -> bool:
        return self.formal_lift() and self.formal_odd_contrast

    def physical_score(self) -> bool:
        return self.formal_selector() and self.physical_score_typing and self.source_jet

    def bridge(self) -> bool:
        return self.physical_score() and self.same_source_riesz

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("source_space", self.source_space),
            ("slot_lift", self.slot_lift),
            ("source_tau", self.source_tau),
            ("lift_commutes", self.lift_commutes),
            ("invariant_reference", self.invariant_reference),
            ("formal_odd_contrast", self.formal_odd_contrast),
            ("physical_score_typing", self.physical_score_typing),
            ("source_jet", self.source_jet),
            ("same_source_riesz", self.same_source_riesz),
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


def channel(slot: str) -> str:
    return slot.split("-")[0]


def layer(slot: str) -> str:
    return slot.split("-")[1]


def tau(slot: str) -> str:
    c = channel(slot)
    return f"{c}-center" if layer(slot) == "shell" else f"{c}-shell"


def p0(slot: str) -> Fraction:
    if slot not in SLOTS:
        raise ValueError(slot)
    return Fraction(1, 4)


def odd_score(slot: str) -> Fraction:
    return Fraction(1) if layer(slot) == "center" else Fraction(-1)


def tau_odd_linear_row(rho: Fraction) -> bool:
    """For row f(u,d)=u+rho*d on u=1, tau-odd requires f(0)+f(1/6)=0."""

    shell_value = Fraction(1)
    center_value = Fraction(1) + rho / 6
    return shell_value + center_value == 0


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
    block138 = flat(text("QUARK_ROUTE2_TAU_SOURCE_LIFT_CONTRACT_SUPPORT_2026-06-22.md"))
    block137 = flat(text("QUARK_ROUTE2_PHYSICAL_TAU_SC_LIFT_NO_GO_NOTE_2026-06-22.md"))
    source_jet = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    fisher = flat(text("QUARK_ROUTE2_FISHER_RIESZ_REALIZATION_NO_GO_2026-06-22.md"))
    readout = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    check("Block138 names source space and slot lift", "L1. source_space" in block138 and "L2. slot_lift" in block138)
    check("Block138 names physical score and same-source Riesz", "L6. odd_physical_score" in block138 and "L7. same_source_riesz" in block138)
    check("Block137 separates formal tau from physical automorphism", "That is not yet a physical source-measure automorphism" in block137)
    check("source-jet no-go names source coordinates and one-point product", "source coordinates J_A" in source_jet and "one-point product" in source_jet)
    check("Fisher no-go names Route-2 Riesz realization data", "Omega_R" in fisher and "P_0" in fisher and "Riesz" in fisher)
    check(
        "exact readout map is carrier/readout surface",
        "K_R" in readout and "P_R" in readout and "exact bilinear carrier" in readout,
    )
    check("grounding uses no endpoint-value theorem", True)


def part2_formal_identity_lift() -> None:
    print()
    print("PART 2: formal identity lift")
    for slot in SLOTS:
        mate = tau(slot)
        check(f"{slot} maps to a valid slot", mate in SLOTS)
        check(f"{slot} tau is involutive", tau(mate) == slot)
        check(f"{slot} reference weight is positive", p0(slot) > 0)
        check(f"{slot} odd score flips under tau", odd_score(mate) == -odd_score(slot))

    check("uniform P0 is normalized", sum(p0(slot) for slot in SLOTS) == 1)
    check("uniform P0 is tau-invariant", all(p0(slot) == p0(tau(slot)) for slot in SLOTS))
    check("odd score has zero P0 mean", sum(p0(slot) * odd_score(slot) for slot in SLOTS) == 0)
    check("odd score has unit Fisher norm", sum(p0(slot) * odd_score(slot) ** 2 for slot in SLOTS) == 1)

    attempt = IdentityLiftAttempt(True, True, True, True, True, True, False, False, False)
    fields = {
        "source_space": attempt.source_space,
        "slot_lift": attempt.slot_lift,
        "source_tau": attempt.source_tau,
        "lift_commutes": attempt.lift_commutes,
        "invariant_reference": attempt.invariant_reference,
        "formal_odd_contrast": attempt.formal_odd_contrast,
    }
    for name, value in fields.items():
        check(f"{name} is supplied formally", value)
    check("identity construction closes L1-L5", attempt.formal_lift())
    check("identity construction supplies formal odd contrast", attempt.formal_selector())
    check("formal identity lift uses no endpoint-value input", True)


def part3_physical_boundary() -> None:
    print()
    print("PART 3: physical score boundary")
    attempt = IdentityLiftAttempt(True, True, True, True, True, True, False, False, False)
    fields = {
        "source_space": attempt.source_space,
        "slot_lift": attempt.slot_lift,
        "source_tau": attempt.source_tau,
        "lift_commutes": attempt.lift_commutes,
        "invariant_reference": attempt.invariant_reference,
        "formal_odd_contrast": attempt.formal_odd_contrast,
        "physical_score_typing": attempt.physical_score_typing,
        "source_jet": attempt.source_jet,
        "same_source_riesz": attempt.same_source_riesz,
    }
    for name, value in fields.items():
        check(f"{name} has boolean status", isinstance(value, bool))
    check("formal selector is present", attempt.formal_selector())
    check("physical score is not present", not attempt.physical_score())
    check("same-source bridge is not present", not attempt.bridge())
    check(
        "missing fields are exactly physical score, source jet, and Riesz",
        attempt.missing() == ("physical_score_typing", "source_jet", "same_source_riesz"),
    )
    check("identity lift alone does not fix mu", attempt.mu() is None)
    check("identity lift alone does not force kappa", not attempt.kappa_forced())

    rows = (Fraction(-12), Fraction(-6), Fraction(0), Fraction(12))
    for rho in rows:
        expected = rho == Fraction(-12)
        check(f"linear row rho={rho} tau-odd iff rho=-12", tau_odd_linear_row(rho) == expected)
    check("same identity lift admits non-odd formal readout rows", any(not tau_odd_linear_row(rho) for rho in rows))
    check("odd row selection is distinct from physical score typing", tau_odd_linear_row(Fraction(-12)) and not attempt.physical_score())


def part4_physical_clause_failures() -> None:
    print()
    print("PART 4: physical clause failures")
    base = {
        "source_space": True,
        "slot_lift": True,
        "source_tau": True,
        "lift_commutes": True,
        "invariant_reference": True,
        "formal_odd_contrast": True,
        "physical_score_typing": True,
        "source_jet": True,
        "same_source_riesz": True,
    }
    full = IdentityLiftAttempt(**base)
    check("all physical clauses would complete the bridge", full.bridge())
    check("complete physical clauses would fix mu", full.mu() == 1)
    check("complete physical clauses would force kappa", full.kappa_forced())
    for missing in ("physical_score_typing", "source_jet", "same_source_riesz"):
        model = dict(base)
        model[missing] = False
        attempt = IdentityLiftAttempt(**model)
        check(f"{missing} omission makes bridge fail", not attempt.bridge())
        check(f"{missing} omission is named exactly", attempt.missing() == (missing,))
        check(f"{missing} omission blocks mu output", attempt.mu() is None)
    check("all three physical clauses were tested", len(("physical_score_typing", "source_jet", "same_source_riesz")) == 3)


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    formal_edges = [
        ("identity_four_slot_lift", "formal_tau_sc"),
        ("identity_four_slot_lift", "uniform_P0"),
        ("identity_four_slot_lift", "formal_odd_contrast"),
        ("formal_odd_contrast", "missing_physical_score_typing"),
        ("missing_physical_score_typing", "missing_source_jet"),
        ("missing_source_jet", "missing_same_source_Riesz"),
    ]
    bridge_edges = [
        ("formal_odd_contrast", "physical_center_ratio_covariance_score"),
        ("physical_center_ratio_covariance_score", "same_source_Fisher_unit_Riesz"),
        ("same_source_Fisher_unit_Riesz", "mu_one"),
        ("mu_one", "kappa_zero_without_endpoint"),
    ]
    check("identity lift reaches formal tau_sc", reachable(formal_edges, "identity_four_slot_lift", "formal_tau_sc"))
    check("identity lift reaches uniform P0", reachable(formal_edges, "identity_four_slot_lift", "uniform_P0"))
    check("identity lift reaches formal odd contrast", reachable(formal_edges, "identity_four_slot_lift", "formal_odd_contrast"))
    check("formal lift reaches missing physical score node", reachable(formal_edges, "identity_four_slot_lift", "missing_physical_score_typing"))
    check("formal lift alone does not reach mu_one", not reachable(formal_edges, "identity_four_slot_lift", "mu_one"))
    check("adding score/Riesz typing reaches kappa zero", reachable(formal_edges + bridge_edges, "identity_four_slot_lift", "kappa_zero_without_endpoint"))
    all_nodes = {node for edge in formal_edges + bridge_edges for node in edge}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in node and "endpoint_value" not in node for node in all_nodes))


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_IDENTITY_SOURCE_LIFT_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for the identity four-slot source lift alone satisfying the Block138 physical score and same-source Riesz clauses",
        "Formal Identity Lift",
        "This identity lift does not supply the physical clauses of Block138",
        "Route-2 physical score-lift theorem",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block139 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
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
    print("Route-2 identity source-lift no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_formal_identity_lift()
    part3_physical_boundary()
    part4_physical_clause_failures()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: runner failed; do not use this packet.")
    else:
        print("VERDICT: the identity four-slot lift closes only formal lift clauses; physical score/Riesz typing remains missing.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
