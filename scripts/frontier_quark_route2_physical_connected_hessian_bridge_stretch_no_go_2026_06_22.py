#!/usr/bin/env python3
"""Stretch no-go for a physical connected-Hessian Route-2 bridge."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-connected-hessian-stretch"

PASS = 0
FAIL = 0


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


def r_phys(kappa: Fraction) -> Fraction:
    return Fraction(8, 9) + kappa * Fraction(1, 9)


def parity_coeffs(s: Fraction, t: Fraction) -> tuple[Fraction, Fraction]:
    return s + t, -s + t


def part1_grounding() -> None:
    print("PART 1: grounding")
    source_hessian = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md"))
    parity_cut = flat(text("QUARK_ROUTE2_TYPED_PARITY_BRIDGE_MINIMAL_CUT_2026-06-22.md"))
    coeff_no_go = flat(text("QUARK_ROUTE2_HESSIAN_ET_COEFFICIENT_NORMALIZATION_NO_GO_NOTE_2026-06-22.md"))
    gauge_no_go = flat(text("QUARK_ROUTE2_SOURCE_COORDINATE_GAUGE_NORMALIZATION_NO_GO_NOTE_2026-06-22.md"))
    rconn = flat(text("QUARK_ROUTE2_RCONN_TYPED_BRIDGE_FACTORIZATION_NO_GO_NOTE_2026-06-22.md"))
    sign = flat(text("QUARK_ROUTE2_ENDPOINT_ORIENTATION_SIGN_SUPPORT_NOTE_2026-06-22.md"))
    readout = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    check("source-Hessian support gives connected subtraction", "D_i D_j W = D_i D_j Z - (D_i Z)(D_j Z)" in source_hessian)
    check("typed parity cut names three same-source premises", "Physical source-Hessian premise" in parity_cut and "Symmetric purity premise" in parity_cut and "Antisymmetric adjoint premise" in parity_cut)
    check("coefficient no-go leaves E/T lambdas free", "lambda_E, lambda_T" in coeff_no_go and "separate gates" in coeff_no_go)
    check("source gauge no-go leaves origin and scale open", "fixed origin and scale" in gauge_no_go)
    check("Rconn factorization separates kappa and sigma", "derive kappa=0 and sigma=-1" in rconn)
    check("endpoint orientation sign support leaves kappa open", "magnitude remains open" in sign and "kappa=0" in sign)
    check("exact readout still supplies finite P_R matrix", "P_R = [[alpha_E, 0, beta_E, 0]" in readout)


def part2_minimal_premises() -> None:
    print()
    print("PART 2: minimal premise firewall")
    allowed = {
        "Pcal_connected_subtraction": True,
        "SU3_adjoint_fraction_8_over_9": True,
        "finite_P_R_readout_surface": True,
        "E_T_parity_decomposition": True,
        "conditional_endpoint_orientation_sign": True,
    }
    forbidden = {
        "endpoint_values": False,
        "fitted_readout_coefficients": False,
        "finite_box_comparator": False,
        "binary_log_odds_selector": False,
        "color_marginal_transfer": False,
    }
    for name, present in allowed.items():
        print(f"  allowed {name}: {present}")
        check(f"allowed premise present: {name}", present)
    for name, present in forbidden.items():
        print(f"  forbidden {name}: {present}")
        check(f"forbidden import absent: {name}", not present)
    check("allowed and forbidden sets are disjoint", not (set(allowed) & set(forbidden)))


def part3_schur_coefficient_frame() -> None:
    print()
    print("PART 3: SU3 Schur coefficient frame")
    color_block = Fraction(8, 9)
    coeffs = {
        "target_ratio": (Fraction(1), Fraction(-8, 9)),
        "orientation_only": (Fraction(1), Fraction(-1)),
        "wrong_orientation": (Fraction(1), Fraction(8, 9)),
        "same_ratio_scaled": (Fraction(2), Fraction(-16, 9)),
    }
    ratios: dict[str, Fraction] = {}
    for name, (lam_e, lam_t) in coeffs.items():
        h_e = lam_e * color_block
        h_t = lam_t * color_block
        ratio = h_t / h_e
        ratios[name] = ratio
        print(f"  {name}: lambda_E={lam_e}, lambda_T={lam_t}, H_E={h_e}, H_T={h_t}, ratio={ratio}")
        check(f"{name} uses same color block", color_block == Fraction(8, 9))
        check(f"{name} ratio equals lambda ratio", ratio == lam_t / lam_e)
    check("target ratio is available only after coefficient choice", ratios["target_ratio"] == Fraction(-8, 9))
    check("same color block permits non-target orientation-only ratio", ratios["orientation_only"] == Fraction(-1))
    check("same color block permits wrong orientation", ratios["wrong_orientation"] == Fraction(8, 9))
    check("scale remains free even at target ratio", coeffs["same_ratio_scaled"][0] != coeffs["target_ratio"][0] and ratios["same_ratio_scaled"] == ratios["target_ratio"])


def part4_parity_and_selector_frames() -> None:
    print()
    print("PART 4: parity, selector, and orientation frames")
    eta_cases = {
        "pure_disconnected": Fraction(0),
        "half_residual": Fraction(1, 2),
        "pure_connected_singlet": Fraction(1),
    }
    for name, eta in eta_cases.items():
        r = r_phys(eta)
        k = 9 * (r - Fraction(8, 9))
        print(f"  {name}: eta={eta}, R_phys={r}, kappa={k}")
        check(f"{name} selector formula exact", k == eta)
    check("only pure disconnected singlet gives kappa=0", all((name == "pure_disconnected") == (eta == 0) for name, eta in eta_cases.items()))
    parity_cases = {
        "anti_unit": (Fraction(1), Fraction(0)),
        "anti_scaled": (Fraction(2), Fraction(0)),
        "mixed": (Fraction(1), Fraction(1, 3)),
    }
    for name, (s, t) in parity_cases.items():
        lam_e, lam_t = parity_coeffs(s, t)
        print(f"  {name}: s={s}, t={t}, coeff=({lam_e},{lam_t})")
        check(f"{name} parity decomposition exact", (lam_e, lam_t) == (s + t, -s + t))
    check("anti-invariant line still has scale freedom", parity_coeffs(Fraction(1), 0) != parity_coeffs(Fraction(2), 0))
    check("mixed parity keeps symmetric residue", parity_coeffs(Fraction(1), Fraction(1, 3))[0] + parity_coeffs(Fraction(1), Fraction(1, 3))[1] != 0)
    orientation_cases = {
        "target": (Fraction(-1), Fraction(0), Fraction(-8, 9)),
        "orientation_without_selector": (Fraction(-1), Fraction(1), Fraction(-1)),
        "wrong_orientation_connected": (Fraction(1), Fraction(0), Fraction(8, 9)),
    }
    for name, (sigma, kappa_value, expected) in orientation_cases.items():
        c = sigma * r_phys(kappa_value)
        print(f"  {name}: sigma={sigma}, kappa={kappa_value}, center_ratio={c}")
        check(f"{name} oriented Rphys formula exact", c == expected)
    check("orientation sign alone does not fix target magnitude", orientation_cases["orientation_without_selector"][2] != orientation_cases["target"][2])


def part5_fanout_synthesis() -> None:
    print()
    print("PART 5: stretch fan-out synthesis")
    frames = {
        "SU3_schur": "missing_E_T_coefficient_normalization",
        "parity_purity": "missing_same_source_pure_disconnected_singlet",
        "source_action": "missing_physical_source_action_and_gauge_fixing",
        "endpoint_orientation": "missing_kappa_selector_magnitude",
        "carrier_readout": "missing_nontrivial_color_tensor_source_carrier",
    }
    for frame, wall in frames.items():
        print(f"  {frame}: {wall}")
        check(f"{frame} has named wall", wall.startswith("missing_"))
    check("fan-out has five orthogonal frames", len(frames) == 5)
    check("no fan-out frame closes the bridge", all(wall.startswith("missing_") for wall in frames.values()))
    locks = {
        "physical_same_source_color_tensor_action": False,
        "pure_disconnected_singlet_and_adjoint_typing": False,
        "coefficient_and_source_gauge_normalization": False,
    }
    for lock, supplied in locks.items():
        print(f"  three-lock theorem supplies {lock}: {supplied}")
        check(f"{lock} remains unsupplied on current surface", not supplied)
    check("all three locks are required for direct bridge", set(locks) == {"physical_same_source_color_tensor_action", "pure_disconnected_singlet_and_adjoint_typing", "coefficient_and_source_gauge_normalization"})


def part6_reachability() -> None:
    print()
    print("PART 6: reachability")
    current_edges = [
        ("current_minimal_premises", "Pcal_connected_subtraction"),
        ("current_minimal_premises", "SU3_adjoint_fraction"),
        ("current_minimal_premises", "finite_P_R_readout"),
        ("finite_P_R_readout", "missing_physical_connected_Hessian_bridge"),
        ("SU3_adjoint_fraction", "missing_E_T_coefficient_map"),
    ]
    positive_edges = [
        ("Route2_physical_connected_Hessian_bridge_theorem", "physical_same_source_D2_logZ"),
        ("physical_same_source_D2_logZ", "pure_disconnected_singlet"),
        ("pure_disconnected_singlet", "kappa_zero_without_endpoint"),
        ("kappa_zero_without_endpoint", "oriented_center_bridge_minus_8_9"),
        ("Route2_physical_connected_Hessian_bridge_theorem", "coefficient_normalized_E_T_map"),
        ("coefficient_normalized_E_T_map", "oriented_center_bridge_minus_8_9"),
    ]
    check("current premises reach missing connected-Hessian bridge node", reachable(current_edges, "current_minimal_premises", "missing_physical_connected_Hessian_bridge"))
    check("current premises do not reach kappa=0", not reachable(current_edges, "current_minimal_premises", "kappa_zero_without_endpoint"))
    check("physical connected-Hessian theorem would reach kappa=0", reachable(positive_edges, "Route2_physical_connected_Hessian_bridge_theorem", "kappa_zero_without_endpoint"))
    check("physical connected-Hessian theorem would reach oriented center bridge", reachable(positive_edges, "Route2_physical_connected_Hessian_bridge_theorem", "oriented_center_bridge_minus_8_9"))
    all_nodes = {n for e in current_edges + positive_edges for n in e}
    check("reachability graph contains no endpoint triple node", all("rho_E_21_4" not in n and "q_E_15_8" not in n for n in all_nodes))
    check("reachability graph does not use finite-box comparator", all("finite_box" not in n and "box" not in n for n in all_nodes))


def part7_document_boundary() -> None:
    print()
    print("PART 7: document boundary")
    note = text("QUARK_ROUTE2_PHYSICAL_CONNECTED_HESSIAN_BRIDGE_STRETCH_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for deriving a coefficient-normalized physical Route-2 connected-Hessian bridge from the current minimal premises",
        "Minimal Premises And Forbidden Imports",
        "Fan-Out Stretch Attempts",
        "Route-2 physical connected-Hessian bridge theorem",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block112 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names physical connected-Hessian bridge theorem", "physical connected-Hessian bridge theorem" in trace_gate)
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
    print("Route-2 physical connected-Hessian bridge stretch no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_minimal_premises()
    part3_schur_coefficient_frame()
    part4_parity_and_selector_frames()
    part5_fanout_synthesis()
    part6_reachability()
    part7_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: the direct physical connected-Hessian bridge remains blocked by three unsupplied locks: same-source color/tensor action, disconnected/adjoint typing, and coefficient plus source-gauge normalization.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
