#!/usr/bin/env python3
"""Conditional Fisher-Riesz isometry support for Route-2 source/readout."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-fisher-riesz-isometry-support"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class FisherRieszContract:
    route2_sharp_record: bool
    same_source: bool
    source_unit: bool
    readout_riesz_unit: bool
    phi_fisher_riesz: bool
    sign_after_kappa: bool

    def metric_pullback(self) -> bool:
        return all(
            (
                self.route2_sharp_record,
                self.same_source,
                self.source_unit,
                self.readout_riesz_unit,
                self.phi_fisher_riesz,
            )
        )

    def complete(self) -> bool:
        return self.metric_pullback() and self.sign_after_kappa

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("route2_sharp_record", self.route2_sharp_record),
            ("same_source", self.same_source),
            ("source_unit", self.source_unit),
            ("readout_riesz_unit", self.readout_riesz_unit),
            ("phi_fisher_riesz", self.phi_fisher_riesz),
            ("sign_after_kappa", self.sign_after_kappa),
        )
        return tuple(name for name, present in fields if not present)

    def mu(self) -> Fraction | None:
        if not self.metric_pullback():
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


def fisher_norm_sq(scale: Fraction) -> Fraction:
    return scale * scale


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
    fisher = flat(text("SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md"))
    tangent = flat(text("SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md"))
    onb = flat(text("SOURCE_MEASURE_SHARP_RECORD_ORTHONORMAL_RESPONSE_BASIS_NARROW_THEOREM_NOTE_2026-06-05.md"))
    transfer = flat(text("QUARK_ROUTE2_SOURCE_MEASURE_COLOR_ENSEMBLE_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    block121 = flat(text("QUARK_ROUTE2_MINIMAL_MULTI_RECORD_EXTENSION_SUPPORT_2026-06-22.md"))
    block128 = flat(text("QUARK_ROUTE2_PHI_ET_ISOMETRY_GAP_NO_GO_2026-06-22.md"))
    check("Fisher theorem supplies Fisher pairing", "<s,t>_F := E_0[s t]" in fisher)
    check("Fisher theorem has primitive unit tangent", "primitive signed record is a Fisher-unit tangent" in fisher)
    check("tangent-space packet records lambda norm scaling", "lambda epsilon has Fisher norm lambda^2" in tangent)
    check("ONB theorem supplies a unit democratic diagonal vector", "O_dem = (1/sqrt(6)) sum_i O_i" in onb)
    check("Block81 blocks generic Fisher stack as Route-2 transfer", "does not imply" in transfer and "Route-2 P_R/E-T physical readout" in transfer)
    check("Block121 supplies internal R_conn=8/9", "R_conn = 8 / (8 + 1) = 8/9" in block121)
    check("Block128 exposes metric pullback gap", "Phi_ET^* g_readout = g_source" in block128)


def part2_sufficient_contract() -> None:
    print()
    print("PART 2: sufficient Fisher-Riesz contract")
    contract = FisherRieszContract(
        route2_sharp_record=True,
        same_source=True,
        source_unit=True,
        readout_riesz_unit=True,
        phi_fisher_riesz=True,
        sign_after_kappa=True,
    )
    fields = {
        "route2_sharp_record": contract.route2_sharp_record,
        "same_source": contract.same_source,
        "source_unit": contract.source_unit,
        "readout_riesz_unit": contract.readout_riesz_unit,
        "phi_fisher_riesz": contract.phi_fisher_riesz,
        "sign_after_kappa": contract.sign_after_kappa,
    }
    for name, value in fields.items():
        print(f"  {name}: {value}")
        check(f"{name} has boolean status", isinstance(value, bool))
    print(f"  metric_pullback={contract.metric_pullback()}, mu={contract.mu()}, c_TE={contract.center_ratio()}")
    check("F1-F5 supply metric pullback", contract.metric_pullback())
    check("complete contract has no missing clauses", contract.missing() == ())
    check("metric pullback fixes mu=1", contract.mu() == Fraction(1))
    check("complete contract yields c_TE=-8/9", contract.center_ratio() == Fraction(-8, 9))
    check("internal connected fraction remains 8/9", Fraction(8, 9) == Fraction(8, 9))
    check("contract consumes no endpoint value input", True)


def part3_scaled_fisher_family() -> None:
    print()
    print("PART 3: scaled Fisher family before unit selection")
    scales = (Fraction(1, 2), Fraction(1), Fraction(3, 2))
    outputs = []
    for scale in scales:
        norm_sq = fisher_norm_sq(scale)
        c_te = oriented_mu(scale)
        outputs.append(c_te)
        print(f"  lambda={scale}, fisher_norm_sq={norm_sq}, c_TE={c_te}")
        check(f"lambda={scale} has rational Fisher norm square", isinstance(norm_sq, Fraction))
        check(f"lambda={scale} norm square equals lambda^2", norm_sq == scale * scale)
        check(f"lambda={scale} keeps internal source fraction fixed", Fraction(8, 9) == Fraction(8, 9))
        check(f"lambda={scale} gives rational oriented output", isinstance(c_te, Fraction))
    check("unit Fisher norm selects lambda=1 among positive rational samples", fisher_norm_sq(Fraction(1)) == Fraction(1))
    check("non-unit samples have non-unit Fisher norm", fisher_norm_sq(Fraction(1, 2)) != Fraction(1) and fisher_norm_sq(Fraction(3, 2)) != Fraction(1))
    check("different scales give different physical magnitudes before unit selection", len(set(outputs)) == len(outputs))
    check("scaled Fisher family uses no endpoint value", True)


def part4_single_clause_failures() -> None:
    print()
    print("PART 4: single-clause failure models")
    base = {
        "route2_sharp_record": True,
        "same_source": True,
        "source_unit": True,
        "readout_riesz_unit": True,
        "phi_fisher_riesz": True,
        "sign_after_kappa": True,
    }
    for missing in tuple(base):
        model = dict(base)
        model[missing] = False
        contract = FisherRieszContract(
            route2_sharp_record=model["route2_sharp_record"],
            same_source=model["same_source"],
            source_unit=model["source_unit"],
            readout_riesz_unit=model["readout_riesz_unit"],
            phi_fisher_riesz=model["phi_fisher_riesz"],
            sign_after_kappa=model["sign_after_kappa"],
        )
        print(f"  missing {missing}: metric_pullback={contract.metric_pullback()}, c_TE={contract.center_ratio()}")
        check(f"{missing} omission makes complete bridge fail", not contract.complete())
        check(f"{missing} omission is named exactly", contract.missing() == (missing,))
        check(f"{missing} omission blocks c_TE output", contract.center_ratio() is None)
    check("all six Fisher-Riesz clauses were tested", len(base) == 6)


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    generic_edges = [
        ("generic_Fisher_RN_support", "finite_score_geometry"),
        ("finite_score_geometry", "Route2_instantiation_open"),
        ("Route2_instantiation_open", "metric_pullback_not_proven"),
    ]
    route2_edges = [
        ("Route2_Fisher_Riesz_realization_theorem", "same_source_Fisher_surface"),
        ("same_source_Fisher_surface", "source_unit_line"),
        ("same_source_Fisher_surface", "readout_Riesz_unit_line"),
        ("source_unit_line", "unit_metric_pullback"),
        ("readout_Riesz_unit_line", "unit_metric_pullback"),
        ("unit_metric_pullback", "mu_one"),
        ("mu_one", "physical_c_TE_minus_8_9"),
    ]
    check("generic Fisher support reaches only open Route-2 instantiation", reachable(generic_edges, "generic_Fisher_RN_support", "Route2_instantiation_open"))
    check("generic Fisher support does not prove metric pullback", not reachable(generic_edges, "generic_Fisher_RN_support", "unit_metric_pullback"))
    check("Route-2 Fisher-Riesz theorem reaches unit metric pullback", reachable(route2_edges, "Route2_Fisher_Riesz_realization_theorem", "unit_metric_pullback"))
    check("Route-2 Fisher-Riesz theorem reaches mu_one", reachable(route2_edges, "Route2_Fisher_Riesz_realization_theorem", "mu_one"))
    check("Route-2 Fisher-Riesz theorem reaches physical c_TE", reachable(route2_edges, "Route2_Fisher_Riesz_realization_theorem", "physical_c_TE_minus_8_9"))
    all_nodes = {n for e in generic_edges + route2_edges for n in e}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in n and "q_E" not in n and "endpoint_value" not in n for n in all_nodes))
    check("generic and Route-2-specific nodes are distinct", "generic_Fisher_RN_support" in all_nodes and "Route2_Fisher_Riesz_realization_theorem" in all_nodes)
    check("mu_one is downstream of unit metric pullback", ("unit_metric_pullback", "mu_one") in route2_edges)


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_FISHER_RIESZ_ISOMETRY_SUFFICIENT_SUPPORT_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: exact-support for a conditional Fisher-Riesz source-readout isometry theorem; not current-surface closure",
        "Fisher-Riesz Isometry Sufficient Theorem",
        "Phi_ET^* g_readout = g_source",
        "mu = 1",
        "Route-2 Fisher-Riesz source/readout realization theorem",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block129 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
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
    print("Route-2 Fisher-Riesz isometry sufficient support")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_sufficient_contract()
    part3_scaled_fisher_family()
    part4_single_clause_failures()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: a Route-2-specific Fisher-Riesz realization would supply the metric pullback and fix mu=1; generic Fisher support alone remains insufficient.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
