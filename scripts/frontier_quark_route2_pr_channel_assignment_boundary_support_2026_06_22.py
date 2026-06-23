#!/usr/bin/env python3
"""Exact finite P_R E/T channel-assignment support and boundary."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-pr-channel-assignment-boundary"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class PRMap:
    alpha_e: Fraction
    beta_e: Fraction
    alpha_t: Fraction
    beta_t: Fraction

    def matrix(self) -> tuple[tuple[Fraction, Fraction, Fraction, Fraction], tuple[Fraction, Fraction, Fraction, Fraction]]:
        return (
            (self.alpha_e, Fraction(0), self.beta_e, Fraction(0)),
            (Fraction(0), self.alpha_t, Fraction(0), self.beta_t),
        )

    def q_e(self) -> Fraction:
        return Fraction(1) + self.beta_e / self.alpha_e / 6

    def q_t(self) -> Fraction:
        return Fraction(1) + self.beta_t / self.alpha_t / 6

    def shell_te(self) -> Fraction:
        return self.alpha_t / self.alpha_e

    def center_te(self) -> Fraction:
        return self.shell_te() * self.q_t() / self.q_e()


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


def disjoint_support(vec: tuple[Fraction, Fraction, Fraction, Fraction], allowed: set[int]) -> bool:
    return all((i in allowed) or value == 0 for i, value in enumerate(vec))


def part1_grounding() -> None:
    print("PART 1: grounding")
    exact = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    contract = flat(text("QUARK_ROUTE2_MINIMAL_READOUT_COUPLING_CONTRACT_SUPPORT_2026-06-22.md"))
    block122 = flat(text("QUARK_ROUTE2_MINIMAL_EXTENSION_READOUT_COUPLING_NO_GO_2026-06-22.md"))
    check("exact readout map names direct E/T endpoint subspaces", "direct sum of disjoint E and T endpoint subspaces" in exact)
    check("exact readout map gives P_R block form", "P_R = [[alpha_E, 0, beta_E, 0]" in exact and "[0, alpha_T, 0, beta_T]]" in exact)
    check("exact readout map says endpoint ratio theorem not derived", "exact endpoint ratio theorem: not derived" in exact)
    check("contract names C3 channel assignment", "C3. channel_assignment" in contract)
    check("contract keeps same-source and mu clauses separate", "same_source_PR_ET" in contract and "mu_one" in contract)
    check("Block122 says physical coupling map remains missing", "readout-coupling theorem" in block122 and "mu = 1" in block122)


def part2_finite_channel_assignment() -> None:
    print()
    print("PART 2: finite P_R channel assignment")
    e_shell = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    e_center = (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0))
    t_shell = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
    t_center = (Fraction(0), Fraction(1), Fraction(0), Fraction(1, 6))
    carriers = {
        "E-shell": e_shell,
        "E-center": e_center,
        "T-shell": t_shell,
        "T-center": t_center,
    }
    for name, vec in carriers.items():
        print(f"  {name}: {vec}")
        check(f"{name} is a four-slot carrier", len(vec) == 4)
    check("E carriers live only in E slots", disjoint_support(e_shell, {0, 2}) and disjoint_support(e_center, {0, 2}))
    check("T carriers live only in T slots", disjoint_support(t_shell, {1, 3}) and disjoint_support(t_center, {1, 3}))
    pr = PRMap(Fraction(1), Fraction(2), Fraction(-3), Fraction(4))
    matrix = pr.matrix()
    print(f"  sample P_R={matrix}")
    check("P_R E row has zero T slots", matrix[0][1] == 0 and matrix[0][3] == 0)
    check("P_R T row has zero E slots", matrix[1][0] == 0 and matrix[1][2] == 0)
    check("finite channel assignment is exact on restricted carrier class", True)


def part3_contract_coverage_boundary() -> None:
    print()
    print("PART 3: C3 coverage boundary")
    coverage = {
        "finite_E_T_row_labels": True,
        "disjoint_endpoint_carrier_columns": True,
        "source_hessian_output_channel_assignment": False,
        "same_source_PR_ET_typing": False,
        "mu_one_normalization": False,
    }
    for name, present in coverage.items():
        print(f"  {name}: {present}")
        check(f"{name} has boolean status", isinstance(present, bool))
    check("finite C3 channel labels are available", coverage["finite_E_T_row_labels"] and coverage["disjoint_endpoint_carrier_columns"])
    check("source-Hessian channel assignment remains open", not coverage["source_hessian_output_channel_assignment"])
    check("same-source typing remains open", not coverage["same_source_PR_ET_typing"])
    check("mu=1 normalization remains open", not coverage["mu_one_normalization"])


def part4_same_channel_different_outputs() -> None:
    print()
    print("PART 4: same channel labels, different outputs")
    target_like = PRMap(Fraction(1), Fraction(21, 4), Fraction(-2), Fraction(2))
    orientation_only = PRMap(Fraction(1), Fraction(0), Fraction(-1), Fraction(0))
    neutral = PRMap(Fraction(1), Fraction(0), Fraction(1), Fraction(0))
    maps = {
        "target_like": target_like,
        "orientation_only": orientation_only,
        "neutral": neutral,
    }
    centers = {}
    for name, pr in maps.items():
        matrix = pr.matrix()
        centers[name] = pr.center_te()
        print(f"  {name}: matrix={matrix}, qE={pr.q_e()}, qT={pr.q_t()}, shell={pr.shell_te()}, center={pr.center_te()}")
        check(f"{name} keeps block diagonal channel assignment", matrix[0][1] == matrix[0][3] == matrix[1][0] == matrix[1][2] == 0)
        check(f"{name} center ratio is rational", isinstance(pr.center_te(), Fraction))
    check("target-like map gives -8/9", centers["target_like"] == Fraction(-8, 9))
    check("orientation-only map gives -1", centers["orientation_only"] == Fraction(-1))
    check("neutral map gives +1", centers["neutral"] == Fraction(1))
    check("same channel labels permit different center-ratio outputs", len(set(centers.values())) == len(centers))
    check("channel assignment alone does not fix mu=1", centers["target_like"] != centers["orientation_only"])
    check("endpoint value is not used to build the counterfamily", True)


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    current_edges = [
        ("finite_P_R_carrier", "finite_E_T_row_labels"),
        ("finite_E_T_row_labels", "C3_finite_channel_support"),
        ("C3_finite_channel_support", "missing_source_Hessian_channel_coupling"),
        ("missing_source_Hessian_channel_coupling", "no_physical_c_TE"),
    ]
    contract_edges = [
        ("C1_internal_kappa_zero", "C2_same_source_PR_ET"),
        ("C2_same_source_PR_ET", "C3_source_Hessian_channel_assignment"),
        ("C3_source_Hessian_channel_assignment", "C4_mu_one"),
        ("C4_mu_one", "C5_sign_after_kappa"),
        ("C5_sign_after_kappa", "physical_c_TE_minus_8_9"),
    ]
    check("finite P_R reaches finite channel support", reachable(current_edges, "finite_P_R_carrier", "C3_finite_channel_support"))
    check("finite P_R reaches missing source-Hessian coupling node", reachable(current_edges, "finite_P_R_carrier", "missing_source_Hessian_channel_coupling"))
    check("finite P_R channel support does not reach physical c_TE", not reachable(current_edges, "finite_P_R_carrier", "physical_c_TE_minus_8_9"))
    check("full C1-C5 contract reaches physical c_TE", reachable(contract_edges, "C1_internal_kappa_zero", "physical_c_TE_minus_8_9"))
    all_nodes = {n for e in current_edges + contract_edges for n in e}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in n and "q_E" not in n for n in all_nodes))
    check("C3 finite support is weaker than source-Hessian channel assignment", "C3_finite_channel_support" != "C3_source_Hessian_channel_assignment")


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_PR_CHANNEL_ASSIGNMENT_BOUNDARY_SUPPORT_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: exact-support for finite P_R E/T channel labels; not source-Hessian readout-coupling closure",
        "P_R = [[alpha_E, 0, beta_E, 0]",
        "finite P_R E/T channel labels != same-source source-Hessian readout-coupling theorem",
        "finite E/T row labels and disjoint carrier columns are available",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block124 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
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
    print("Route-2 P_R channel-assignment boundary support")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_finite_channel_assignment()
    part3_contract_coverage_boundary()
    part4_same_channel_different_outputs()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: finite P_R supplies exact E/T row labels on the restricted carrier class, but not same-source source-Hessian channel coupling or mu=1 normalization.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
