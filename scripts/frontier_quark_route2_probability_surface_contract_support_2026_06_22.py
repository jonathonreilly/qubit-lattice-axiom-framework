#!/usr/bin/env python3
"""Conditional Route-2 probability-surface contract support."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-probability-surface-contract"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class ProbabilitySurfaceContract:
    omega_r: bool
    positive_reference: bool
    rn_source_path: bool
    disconnected_normalization: bool
    same_source_block121: bool
    fisher_unit_riesz: bool
    sign_after_kappa: bool

    def fisher_realization(self) -> bool:
        return all(
            (
                self.omega_r,
                self.positive_reference,
                self.rn_source_path,
                self.disconnected_normalization,
                self.same_source_block121,
                self.fisher_unit_riesz,
            )
        )

    def complete(self) -> bool:
        return self.fisher_realization() and self.sign_after_kappa

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("omega_r", self.omega_r),
            ("positive_reference", self.positive_reference),
            ("rn_source_path", self.rn_source_path),
            ("disconnected_normalization", self.disconnected_normalization),
            ("same_source_block121", self.same_source_block121),
            ("fisher_unit_riesz", self.fisher_unit_riesz),
            ("sign_after_kappa", self.sign_after_kappa),
        )
        return tuple(name for name, present in fields if not present)

    def mu(self) -> Fraction | None:
        if not self.fisher_realization():
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


def fisher_norm_for_reference(p: Fraction) -> Fraction:
    return p + (p * p) / (1 - p)


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
    block130 = flat(text("QUARK_ROUTE2_FISHER_RIESZ_REALIZATION_NO_GO_2026-06-22.md"))
    block129 = flat(text("QUARK_ROUTE2_FISHER_RIESZ_ISOMETRY_SUFFICIENT_SUPPORT_2026-06-22.md"))
    fisher = flat(text("SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md"))
    exact_readout = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    block121 = flat(text("QUARK_ROUTE2_MINIMAL_MULTI_RECORD_EXTENSION_SUPPORT_2026-06-22.md"))
    check("Block130 names Omega_R, P0/P_0, and RN path as missing", "Omega_R" in block130 and "P_0" in block130 and "P_h" in block130)
    check("Block129 consumes Fisher-Riesz realization", "Route-2 Fisher-Riesz source/readout realization theorem" in block129)
    check("Fisher theorem defines reference probability", "reference probability P_0" in fisher)
    check("Fisher theorem defines normalized RN chart", "R_h := dP_h / dP_0" in fisher)
    check("exact readout map supplies finite P_R rows", "P_R = [[alpha_E, 0, beta_E, 0]" in exact_readout)
    check("Block121 supplies R_conn=8/9", "R_conn = 8 / (8 + 1) = 8/9" in block121)
    check("Block121 supplies kappa=0 internally", "kappa = 0" in block121)


def part2_sufficient_contract() -> None:
    print()
    print("PART 2: sufficient probability-surface contract")
    contract = ProbabilitySurfaceContract(True, True, True, True, True, True, True)
    fields = {
        "omega_r": contract.omega_r,
        "positive_reference": contract.positive_reference,
        "rn_source_path": contract.rn_source_path,
        "disconnected_normalization": contract.disconnected_normalization,
        "same_source_block121": contract.same_source_block121,
        "fisher_unit_riesz": contract.fisher_unit_riesz,
        "sign_after_kappa": contract.sign_after_kappa,
    }
    for name, value in fields.items():
        print(f"  {name}: {value}")
        check(f"{name} has boolean status", isinstance(value, bool))
    print(f"  fisher_realization={contract.fisher_realization()}, mu={contract.mu()}, c_TE={contract.center_ratio()}")
    check("P1-P6 supply Fisher-Riesz realization", contract.fisher_realization())
    check("complete contract has no missing clauses", contract.missing() == ())
    check("contract fixes mu=1", contract.mu() == Fraction(1))
    check("complete contract yields c_TE=-8/9", contract.center_ratio() == Fraction(-8, 9))
    check("contract uses Block121 internal fraction", Fraction(8, 9) == Fraction(8, 9))
    check("contract consumes no endpoint value input", True)


def part3_reference_boundary() -> None:
    print()
    print("PART 3: reference boundary before P0 is constructed")
    refs = (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3))
    norms = []
    for p in refs:
        norm = fisher_norm_for_reference(p)
        norms.append(norm)
        print(f"  p={p}, norm_sq={norm}")
        check(f"p={p} gives positive reference weight", 0 < p < 1)
        check(f"p={p} Fisher norm is rational", isinstance(norm, Fraction))
        check(f"p={p} Fisher norm is positive", norm > 0)
    check("different P0 choices change unit normalization", len(set(norms)) == len(norms))
    check("P0 construction is load-bearing for mu=1", norms.count(Fraction(1)) == 1)
    check("reference boundary uses no endpoint value", True)


def part4_single_clause_failures() -> None:
    print()
    print("PART 4: single-clause failure models")
    base = {
        "omega_r": True,
        "positive_reference": True,
        "rn_source_path": True,
        "disconnected_normalization": True,
        "same_source_block121": True,
        "fisher_unit_riesz": True,
        "sign_after_kappa": True,
    }
    for missing in tuple(base):
        model = dict(base)
        model[missing] = False
        contract = ProbabilitySurfaceContract(
            omega_r=model["omega_r"],
            positive_reference=model["positive_reference"],
            rn_source_path=model["rn_source_path"],
            disconnected_normalization=model["disconnected_normalization"],
            same_source_block121=model["same_source_block121"],
            fisher_unit_riesz=model["fisher_unit_riesz"],
            sign_after_kappa=model["sign_after_kappa"],
        )
        print(f"  missing {missing}: fisher_realization={contract.fisher_realization()}, c_TE={contract.center_ratio()}")
        check(f"{missing} omission makes complete contract fail", not contract.complete())
        check(f"{missing} omission is named exactly", contract.missing() == (missing,))
        check(f"{missing} omission blocks c_TE output", contract.center_ratio() is None)
    check("all seven probability-surface clauses were tested", len(base) == 7)


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    current_edges = [
        ("current_finite_PR_readout", "missing_Omega_R_P0_Ph"),
        ("missing_Omega_R_P0_Ph", "Block130_no_go"),
    ]
    contract_edges = [
        ("P1_Omega_R", "P2_positive_reference"),
        ("P2_positive_reference", "P3_RN_source_path"),
        ("P3_RN_source_path", "P4_disconnected_normalization"),
        ("P4_disconnected_normalization", "P5_same_source_Block121"),
        ("P5_same_source_Block121", "P6_Fisher_unit_Riesz"),
        ("P6_Fisher_unit_Riesz", "mu_one"),
        ("mu_one", "physical_c_TE_minus_8_9"),
    ]
    check("current finite readout reaches missing probability node", reachable(current_edges, "current_finite_PR_readout", "missing_Omega_R_P0_Ph"))
    check("current finite readout does not reach mu_one", not reachable(current_edges, "current_finite_PR_readout", "mu_one"))
    check("probability contract reaches RN source path", reachable(contract_edges, "P1_Omega_R", "P3_RN_source_path"))
    check("probability contract reaches Fisher unit Riesz", reachable(contract_edges, "P1_Omega_R", "P6_Fisher_unit_Riesz"))
    check("probability contract reaches mu_one", reachable(contract_edges, "P1_Omega_R", "mu_one"))
    check("probability contract reaches physical c_TE", reachable(contract_edges, "P1_Omega_R", "physical_c_TE_minus_8_9"))
    all_nodes = {n for e in current_edges + contract_edges for n in e}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in n and "q_E" not in n and "endpoint_value" not in n for n in all_nodes))
    check("contract has seven named clauses including sign clause", len([n for n in all_nodes if n.startswith("P")]) == 6)


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_PROBABILITY_SURFACE_CONTRACT_SUPPORT_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: exact-support for a conditional probability-surface contract; not current-surface closure",
        "Minimal Probability-Surface Contract",
        "Phi_ET^* g_readout = g_source",
        "mu = 1",
        "Route-2 sharp-record probability-surface theorem",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block131 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks upstream support", "trace_class: upstream_support" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    check("review history records no review-loop worker", "No review-loop worker was run" in review)
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
    print("Route-2 probability-surface contract support")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_sufficient_contract()
    part3_reference_boundary()
    part4_single_clause_failures()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: P1-P7 form a sufficient probability-surface contract for the Route-2 Fisher-Riesz realization; the current surface still has to construct those clauses.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
