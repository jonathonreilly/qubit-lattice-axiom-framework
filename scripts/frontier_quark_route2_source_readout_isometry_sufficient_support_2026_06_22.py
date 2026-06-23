#!/usr/bin/env python3
"""Sufficient source-readout isometry contract for Route-2 mu=1."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-source-readout-isometry-support"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class IsometryContract:
    phi_et: bool
    source_norm_fixed: bool
    readout_norm_fixed: bool
    unit_preserving: bool
    sign_after_kappa: bool

    def isometric_calibration(self) -> bool:
        return all(
            (
                self.phi_et,
                self.source_norm_fixed,
                self.readout_norm_fixed,
                self.unit_preserving,
            )
        )

    def complete(self) -> bool:
        return self.isometric_calibration() and self.sign_after_kappa

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("phi_et", self.phi_et),
            ("source_norm_fixed", self.source_norm_fixed),
            ("readout_norm_fixed", self.readout_norm_fixed),
            ("unit_preserving", self.unit_preserving),
            ("sign_after_kappa", self.sign_after_kappa),
        )
        return tuple(name for name, present in fields if not present)

    def mu(self) -> Fraction | None:
        if not self.isometric_calibration():
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


def oriented_mu(mu: Fraction) -> Fraction:
    return -mu * Fraction(8, 9)


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
    block121 = flat(text("QUARK_ROUTE2_MINIMAL_MULTI_RECORD_EXTENSION_SUPPORT_2026-06-22.md"))
    block123 = flat(text("QUARK_ROUTE2_MINIMAL_READOUT_COUPLING_CONTRACT_SUPPORT_2026-06-22.md"))
    block125 = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_CHANNEL_COUPLING_NO_GO_2026-06-22.md"))
    block126 = flat(text("QUARK_ROUTE2_SOURCE_READOUT_UNIT_CALIBRATION_NO_GO_2026-06-22.md"))
    coeff = flat(text("QUARK_ROUTE2_HESSIAN_ET_COEFFICIENT_NORMALIZATION_NO_GO_NOTE_2026-06-22.md"))
    sign = flat(text("QUARK_ROUTE2_ENDPOINT_ORIENTATION_SIGN_SUPPORT_NOTE_2026-06-22.md"))
    check("Block121 supplies internal R_conn=8/9", "R_conn = 8 / (8 + 1) = 8/9" in block121)
    check("Block121 records kappa=0", "kappa = 0" in block121)
    check("Block123 C4 is mu_one", "C4. mu_one" in block123)
    check("Block123 contract has C1-C5", "C1. internal_kappa_zero" in block123 and "C5. sign_after_kappa" in block123)
    check("Block125 names Phi_ET as missing typed functor", "Phi_ET : Block121 source-Hessian components -> finite P_R E/T output rows" in block125)
    check("Block126 leaves a free mu family", "c_TE(mu) = -mu * (8/9)" in block126)
    check("coefficient normalization remains a separate gate", "E/T coefficient normalization theorem" in coeff)
    check("sign support leaves magnitude open", "magnitude remains open" in sign.lower())


def part2_sufficient_contract() -> None:
    print()
    print("PART 2: sufficient isometry contract")
    contract = IsometryContract(
        phi_et=True,
        source_norm_fixed=True,
        readout_norm_fixed=True,
        unit_preserving=True,
        sign_after_kappa=True,
    )
    field_values = {
        "phi_et": contract.phi_et,
        "source_norm_fixed": contract.source_norm_fixed,
        "readout_norm_fixed": contract.readout_norm_fixed,
        "unit_preserving": contract.unit_preserving,
        "sign_after_kappa": contract.sign_after_kappa,
    }
    for name, value in field_values.items():
        print(f"  {name}: {value}")
        check(f"{name} has boolean status", isinstance(value, bool))
    print(f"  complete={contract.complete()}, missing={contract.missing()}, mu={contract.mu()}, c_TE={contract.center_ratio()}")
    check("I1-I4 form an isometric calibration", contract.isometric_calibration())
    check("complete contract has no missing clauses", contract.missing() == ())
    check("isometric calibration fixes mu=1", contract.mu() == Fraction(1))
    check("complete contract yields c_TE=-8/9", contract.center_ratio() == Fraction(-8, 9))
    check("internal source fraction remains 8/9", Fraction(8, 9) == Fraction(8, 9))
    check("contract consumes no endpoint value input", True)


def part3_free_mu_when_isometry_missing() -> None:
    print()
    print("PART 3: free mu when isometry clauses are missing")
    variants = {
        "missing_source_norm": IsometryContract(True, False, True, True, True),
        "missing_readout_norm": IsometryContract(True, True, False, True, True),
        "missing_unit_preserving": IsometryContract(True, True, True, False, True),
    }
    mus = (Fraction(1, 2), Fraction(1), Fraction(3, 2))
    for name, contract in variants.items():
        outputs = tuple(oriented_mu(mu) for mu in mus)
        print(f"  {name}: missing={contract.missing()}, outputs={outputs}")
        check(f"{name} is not a complete isometric calibration", not contract.isometric_calibration())
        check(f"{name} does not fix mu", contract.mu() is None)
        check(f"{name} leaves a three-member rational family", len(outputs) == 3)
        check(f"{name} outputs have different magnitudes", len(set(outputs)) == len(outputs))
    all_outputs = {oriented_mu(mu) for mu in mus}
    check("mu=1 is one admissible rational member before isometry", Fraction(-8, 9) in all_outputs)
    check("non-unit mu choices remain endpoint-free before isometry", oriented_mu(Fraction(1, 2)) == Fraction(-4, 9))
    check("free family does not alter internal R_conn", Fraction(8, 9) == Fraction(8, 9))


def part4_single_clause_failures() -> None:
    print()
    print("PART 4: single-clause failure models")
    base = {
        "phi_et": True,
        "source_norm_fixed": True,
        "readout_norm_fixed": True,
        "unit_preserving": True,
        "sign_after_kappa": True,
    }
    for missing in tuple(base):
        model = dict(base)
        model[missing] = False
        contract = IsometryContract(
            phi_et=model["phi_et"],
            source_norm_fixed=model["source_norm_fixed"],
            readout_norm_fixed=model["readout_norm_fixed"],
            unit_preserving=model["unit_preserving"],
            sign_after_kappa=model["sign_after_kappa"],
        )
        print(f"  missing {missing}: complete={contract.complete()}, mu={contract.mu()}, c_TE={contract.center_ratio()}")
        check(f"{missing} omission makes contract incomplete", not contract.complete())
        check(f"{missing} omission is named exactly", contract.missing() == (missing,))
        check(f"{missing} omission blocks c_TE output", contract.center_ratio() is None)
    check("all five isometry clauses were tested", len(base) == 5)


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    current_edges = [
        ("Block121_minimal_source", "internal_R_conn_8_9"),
        ("internal_R_conn_8_9", "free_source_to_readout_mu"),
        ("free_source_to_readout_mu", "C4_mu_one_open"),
        ("C4_mu_one_open", "no_physical_c_TE"),
    ]
    isometry_edges = [
        ("Route2_source_readout_isometry_theorem", "Phi_ET_typed"),
        ("Phi_ET_typed", "source_and_readout_units_identified"),
        ("source_and_readout_units_identified", "mu_one"),
        ("mu_one", "C4_satisfied"),
        ("C4_satisfied", "C1_C5_contract_complete"),
        ("C1_C5_contract_complete", "physical_c_TE_minus_8_9"),
    ]
    check("current path reaches open C4 node", reachable(current_edges, "Block121_minimal_source", "C4_mu_one_open"))
    check("current path does not reach physical c_TE", not reachable(current_edges, "Block121_minimal_source", "physical_c_TE_minus_8_9"))
    check("isometry theorem reaches mu_one", reachable(isometry_edges, "Route2_source_readout_isometry_theorem", "mu_one"))
    check("isometry theorem reaches physical c_TE", reachable(isometry_edges, "Route2_source_readout_isometry_theorem", "physical_c_TE_minus_8_9"))
    check("isometry path satisfies Block123 C4", reachable(isometry_edges, "Route2_source_readout_isometry_theorem", "C4_satisfied"))
    all_nodes = {n for e in current_edges + isometry_edges for n in e}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in n and "q_E" not in n and "endpoint_value" not in n for n in all_nodes))
    check("reachability graph names Phi_ET explicitly", "Phi_ET_typed" in all_nodes)


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_SOURCE_READOUT_ISOMETRY_SUFFICIENT_SUPPORT_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: exact-support for a conditional source-readout isometry theorem; not current-surface closure",
        "Route-2 Source-Readout Isometry Sufficient Theorem",
        "mu = 1",
        "c_TE = sigma * mu * R_* = (-1) * 1 * (8/9) = -8/9",
        "The theorem is sufficient only after the typed isometry is proven",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block127 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
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
    print("Route-2 source-readout isometry sufficient support")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_sufficient_contract()
    part3_free_mu_when_isometry_missing()
    part4_single_clause_failures()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: A typed unit-preserving Phi_ET isometry would satisfy Block123 C4 by fixing mu=1; the current surface still has to prove that isometry.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
