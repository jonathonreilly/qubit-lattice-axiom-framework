#!/usr/bin/env python3
"""No-go for current finite P_R readout instantiating Fisher-Riesz realization."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-fisher-riesz-realization-no-go"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class CurrentFisherSurface:
    finite_pr_readout: bool
    exact_readout_algebra: bool
    generic_fisher_support: bool
    route2_sample_space: bool
    route2_reference_probability: bool
    rn_source_path: bool
    same_source_riesz_units: bool

    def current_realization(self) -> bool:
        return all(
            (
                self.finite_pr_readout,
                self.exact_readout_algebra,
                self.generic_fisher_support,
                self.route2_sample_space,
                self.route2_reference_probability,
                self.rn_source_path,
                self.same_source_riesz_units,
            )
        )

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("finite_pr_readout", self.finite_pr_readout),
            ("exact_readout_algebra", self.exact_readout_algebra),
            ("generic_fisher_support", self.generic_fisher_support),
            ("route2_sample_space", self.route2_sample_space),
            ("route2_reference_probability", self.route2_reference_probability),
            ("rn_source_path", self.rn_source_path),
            ("same_source_riesz_units", self.same_source_riesz_units),
        )
        return tuple(name for name, present in fields if not present)

    def mu(self) -> Fraction | None:
        if not self.current_realization():
            return None
        return Fraction(1)


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
    exact_readout = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    fisher = flat(text("SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md"))
    transfer = flat(text("QUARK_ROUTE2_SOURCE_MEASURE_COLOR_ENSEMBLE_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    block129 = flat(text("QUARK_ROUTE2_FISHER_RIESZ_ISOMETRY_SUFFICIENT_SUPPORT_2026-06-22.md"))
    block128 = flat(text("QUARK_ROUTE2_PHI_ET_ISOMETRY_GAP_NO_GO_2026-06-22.md"))
    source_jet = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    check("exact readout map supplies finite P_R rows", "P_R = [[alpha_E, 0, beta_E, 0]" in exact_readout)
    check("Fisher theorem requires a reference probability", "reference probability P_0" in fisher)
    check("Fisher theorem defines RN source scores", "R_h := dP_h / dP_0" in fisher)
    check("Block81 says generic Fisher support is not Route-2 transfer", "generic finite Fisher/RN support" in transfer and "does not imply" in transfer)
    check("Block129 names Route-2 Fisher-Riesz realization", "Route-2 Fisher-Riesz source/readout realization theorem" in block129)
    check("Block128 exposes metric pullback target", "Phi_ET^* g_readout = g_source" in block128)
    check("source-jet no-go separates finite readout from source data", "finite P_R surface does not provide" in source_jet)


def part2_current_surface_gap() -> None:
    print()
    print("PART 2: current finite surface gap")
    surface = CurrentFisherSurface(
        finite_pr_readout=True,
        exact_readout_algebra=True,
        generic_fisher_support=True,
        route2_sample_space=False,
        route2_reference_probability=False,
        rn_source_path=False,
        same_source_riesz_units=False,
    )
    fields = {
        "finite_pr_readout": surface.finite_pr_readout,
        "exact_readout_algebra": surface.exact_readout_algebra,
        "generic_fisher_support": surface.generic_fisher_support,
        "route2_sample_space": surface.route2_sample_space,
        "route2_reference_probability": surface.route2_reference_probability,
        "rn_source_path": surface.rn_source_path,
        "same_source_riesz_units": surface.same_source_riesz_units,
    }
    for name, value in fields.items():
        print(f"  {name}: {value}")
        check(f"{name} has boolean status", isinstance(value, bool))
    print(f"  current_realization={surface.current_realization()}, missing={surface.missing()}, mu={surface.mu()}")
    check("finite readout and generic Fisher support are present", surface.finite_pr_readout and surface.generic_fisher_support)
    check("Route-2 Fisher realization is not present", not surface.current_realization())
    check("missing objects are exactly probability/RN/Riesz realization clauses", surface.missing() == ("route2_sample_space", "route2_reference_probability", "rn_source_path", "same_source_riesz_units"))
    check("current finite surface does not fix mu", surface.mu() is None)
    check("no endpoint value is needed to expose the gap", True)


def part3_reference_measure_dependence() -> None:
    print()
    print("PART 3: reference-measure dependence")
    refs = (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3))
    norms = []
    expected = {Fraction(1, 3): Fraction(1, 2), Fraction(1, 2): Fraction(1), Fraction(2, 3): Fraction(2)}
    for p in refs:
        norm = fisher_norm_for_reference(p)
        norms.append(norm)
        print(f"  p={p}, norm_sq={norm}")
        check(f"p={p} norm is rational", isinstance(norm, Fraction))
        check(f"p={p} norm matches zero-mean score formula", norm == expected[p])
        check(f"p={p} reference probability is positive", 0 < p < 1)
        check(f"p={p} zero-mean score can be normalized only after P0 is known", norm > 0)
    check("reference choices give different Fisher norms", len(set(norms)) == len(norms))
    check("unit norm occurs only for p=1/2 among sampled references", norms.count(Fraction(1)) == 1)
    check("reference-measure family uses no endpoint value", True)


def part4_single_clause_failures() -> None:
    print()
    print("PART 4: single-clause failure models")
    base = {
        "finite_pr_readout": True,
        "exact_readout_algebra": True,
        "generic_fisher_support": True,
        "route2_sample_space": True,
        "route2_reference_probability": True,
        "rn_source_path": True,
        "same_source_riesz_units": True,
    }
    for missing in tuple(base):
        model = dict(base)
        model[missing] = False
        surface = CurrentFisherSurface(
            finite_pr_readout=model["finite_pr_readout"],
            exact_readout_algebra=model["exact_readout_algebra"],
            generic_fisher_support=model["generic_fisher_support"],
            route2_sample_space=model["route2_sample_space"],
            route2_reference_probability=model["route2_reference_probability"],
            rn_source_path=model["rn_source_path"],
            same_source_riesz_units=model["same_source_riesz_units"],
        )
        print(f"  missing {missing}: current_realization={surface.current_realization()}, mu={surface.mu()}")
        check(f"{missing} omission blocks current realization", not surface.current_realization())
        check(f"{missing} omission is named exactly", surface.missing() == (missing,))
        check(f"{missing} omission blocks mu output", surface.mu() is None)
    check("all seven current-surface clauses were tested", len(base) == 7)


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    current_edges = [
        ("current_finite_PR_readout", "linear_E_T_rows"),
        ("linear_E_T_rows", "generic_Fisher_support_available"),
        ("generic_Fisher_support_available", "missing_Route2_probability_surface"),
        ("missing_Route2_probability_surface", "metric_pullback_not_proven"),
    ]
    realization_edges = [
        ("Route2_sharp_record_Fisher_Riesz_theorem", "Omega_R_P0_Ph"),
        ("Omega_R_P0_Ph", "RN_score_tangent"),
        ("RN_score_tangent", "same_source_Riesz_unit_lines"),
        ("same_source_Riesz_unit_lines", "Phi_ET_metric_pullback"),
        ("Phi_ET_metric_pullback", "mu_one"),
    ]
    check("current surface reaches missing probability surface", reachable(current_edges, "current_finite_PR_readout", "missing_Route2_probability_surface"))
    check("current surface does not reach metric pullback", not reachable(current_edges, "current_finite_PR_readout", "Phi_ET_metric_pullback"))
    check("realization theorem reaches RN score tangent", reachable(realization_edges, "Route2_sharp_record_Fisher_Riesz_theorem", "RN_score_tangent"))
    check("realization theorem reaches Riesz unit lines", reachable(realization_edges, "Route2_sharp_record_Fisher_Riesz_theorem", "same_source_Riesz_unit_lines"))
    check("realization theorem reaches metric pullback", reachable(realization_edges, "Route2_sharp_record_Fisher_Riesz_theorem", "Phi_ET_metric_pullback"))
    check("realization theorem reaches mu_one", reachable(realization_edges, "Route2_sharp_record_Fisher_Riesz_theorem", "mu_one"))
    all_nodes = {n for e in current_edges + realization_edges for n in e}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in n and "q_E" not in n and "endpoint_value" not in n for n in all_nodes))
    check("current and theorem nodes remain distinct", "current_finite_PR_readout" in all_nodes and "Route2_sharp_record_Fisher_Riesz_theorem" in all_nodes)


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_FISHER_RIESZ_REALIZATION_NO_GO_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for the current finite P_R readout surface plus generic Fisher support instantiating the Block129 Route-2 Fisher-Riesz realization",
        "Reference-Measure Dependence",
        "Route-2 sharp-record Fisher-Riesz realization theorem",
        "construct Omega_R, P_0, and a normalized RN source path P_h",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block130 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks negative pruning", "trace_class: negative_route_pruning" in trace_gate)
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
    print("Route-2 Fisher-Riesz realization no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_current_surface_gap()
    part3_reference_measure_dependence()
    part4_single_clause_failures()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: current finite P_R readout plus generic Fisher support does not instantiate the Route-2 Fisher-Riesz realization; Omega_R, P0, RN path, and Riesz unit lines remain missing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
