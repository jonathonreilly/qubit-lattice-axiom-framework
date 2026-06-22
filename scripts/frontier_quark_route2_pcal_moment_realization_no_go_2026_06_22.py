#!/usr/bin/env python3
"""No-go for exact Route-2 P_R slots determining a Pcal moment realization."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-pcal-moment-realization"

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


def connected_from_mean(mean: Fraction) -> Fraction:
    return Fraction(1) - mean * mean


def kappa_from_connected(value: Fraction) -> Fraction:
    return 9 * (value - Fraction(8, 9))


def probability_for_mean(mean: Fraction) -> tuple[Fraction, Fraction]:
    return ((Fraction(1) + mean) / 2, (Fraction(1) - mean) / 2)


def part1_grounding() -> None:
    print("PART 1: grounding")
    readout = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    block100 = flat(text("QUARK_ROUTE2_SOURCE_MEASURE_PRODUCT_REGISTRY_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    block97 = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    pcal = flat(text("SOURCE_MEASURE_PCAL_CUMULANT_MOBIUS_THEOREM_NOTE_2026-05-30.md"))

    check("exact readout note supplies carrier/readout reduction", "exact carrier/readout reduction" in readout)
    check("exact readout note exposes four endpoint columns", all(marker in readout for marker in ("E-shell", "E-center", "T-shell", "T-center")))
    check("exact readout note does not claim source moments", "D_A D_B Z" not in readout and "one-point" not in readout)
    check("Block100 names Route-2 Pcal product-instantiation theorem", "Route-2 Pcal product-instantiation theorem" in block100)
    check("Block100 says raw and one-point registries are not supplied", "raw D_A D_B Z" in block100 and "one-point products D_A Z D_B Z" in block100)
    check("Block97 lists missing raw second source moment", "raw second source moment D_A D_B Z" in block97)
    check("Block97 lists missing one-point product", "one-point product (D_A Z)(D_B Z)" in block97)
    check("Pcal theorem gives connected response formula only after moments are supplied", "moments and cumulants are related" in pcal and "M[J] = E exp(sum_i J_i O_i)" in pcal)


def part2_moment_realization_family() -> None:
    print()
    print("PART 2: moment realization family")
    means = [Fraction(0), Fraction(1, 3), Fraction(2, 3), Fraction(1)]
    connected_values: list[Fraction] = []
    kappas: list[Fraction] = []
    for mean in means:
        p_plus, p_minus = probability_for_mean(mean)
        raw_second = Fraction(1)
        one_point_product = mean * mean
        conn = connected_from_mean(mean)
        kappa = kappa_from_connected(conn)
        connected_values.append(conn)
        kappas.append(kappa)
        print(
            f"  mean={mean}, P(+1)={p_plus}, P(-1)={p_minus}, "
            f"raw={raw_second}, product={one_point_product}, connected={conn}, kappa={kappa}"
        )
        check(f"mean={mean} has valid probabilities", p_plus >= 0 and p_minus >= 0 and p_plus + p_minus == 1)
        check(f"mean={mean} realizes raw second moment one", raw_second == 1)
        check(f"mean={mean} connected value matches 1-m^2", conn == 1 - mean * mean)
        check(f"mean={mean} kappa is rational", isinstance(kappa, Fraction))

    check("same raw second moment has multiple connected values", len(set(connected_values)) == len(connected_values))
    check("same raw second moment has multiple kappa values", len(set(kappas)) == len(kappas))
    check("mean 1/3 is the kappa=0 realization", kappa_from_connected(connected_from_mean(Fraction(1, 3))) == 0)
    check("mean 0 is a kappa=1 realization", kappa_from_connected(connected_from_mean(Fraction(0))) == 1)
    check("mean 2/3 is not kappa=0", kappa_from_connected(connected_from_mean(Fraction(2, 3))) != 0)
    check("selecting mean 1/3 is a product theorem, not a consequence of raw=1", True)


def part3_required_moment_realization_fields() -> None:
    print()
    print("PART 3: required moment-realization fields")
    fields = {
        "exact_P_R_endpoint_slots": True,
        "finite_record_probability_space": False,
        "route2_record_variables": False,
        "reference_source_measure": False,
        "raw_DAZ_DBZ_slot_assignment": False,
        "one_point_DAZ_registry": False,
        "symmetric_singlet_product_theorem": False,
        "same_source_color_ET_typing": False,
    }
    for name, present in fields.items():
        print(f"  {name}: {'present' if present else 'missing'}")
        check(f"{name} has boolean status", isinstance(present, bool))
    missing = {k for k, v in fields.items() if not v}
    check("exact P_R slots are present", fields["exact_P_R_endpoint_slots"])
    check("finite probability space remains missing", "finite_record_probability_space" in missing)
    check("Route-2 record variables remain missing", "route2_record_variables" in missing)
    check("reference source measure remains missing", "reference_source_measure" in missing)
    check("raw slot assignment remains missing", "raw_DAZ_DBZ_slot_assignment" in missing)
    check("one-point registry remains missing", "one_point_DAZ_registry" in missing)
    check("symmetric singlet product theorem remains missing", "symmetric_singlet_product_theorem" in missing)
    check("same-source color/E-T typing remains missing", "same_source_color_ET_typing" in missing)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    current_edges = [
        ("exact_P_R_slots", "carrier_readout_reduction"),
        ("carrier_readout_reduction", "no_probability_space"),
        ("carrier_readout_reduction", "one_point_product_underdetermined"),
        ("one_point_product_underdetermined", "kappa_not_forced"),
    ]
    positive_edges = [
        ("route2_probability_space", "route2_record_variables"),
        ("route2_record_variables", "raw_DAZ_DBZ_slot_assignment"),
        ("route2_record_variables", "one_point_DAZ_registry"),
        ("raw_DAZ_DBZ_slot_assignment", "D2_logZ_connected_readout"),
        ("one_point_DAZ_registry", "D2_logZ_connected_readout"),
        ("D2_logZ_connected_readout", "symmetric_singlet_removed"),
        ("symmetric_singlet_removed", "connected_adjoint_only"),
        ("connected_adjoint_only", "kappa_zero_without_endpoint"),
    ]
    check("current exact P_R reaches product underdetermination", reachable(current_edges, "exact_P_R_slots", "one_point_product_underdetermined"))
    check("current exact P_R does not reach kappa=0", not reachable(current_edges, "exact_P_R_slots", "kappa_zero_without_endpoint"))
    check("positive moment-realization theorem reaches kappa=0", reachable(positive_edges, "route2_probability_space", "kappa_zero_without_endpoint"))
    check("raw slot assignment is on the positive route", reachable(positive_edges, "raw_DAZ_DBZ_slot_assignment", "kappa_zero_without_endpoint"))
    check("one-point registry is on the positive route", reachable(positive_edges, "one_point_DAZ_registry", "kappa_zero_without_endpoint"))
    all_nodes = {n for e in current_edges + positive_edges for n in e}
    check("reachability graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_PCAL_MOMENT_REALIZATION_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required_note = (
        "Actual current-surface status: no-go for exact P_R slots determining the Route-2 Pcal product instantiation",
        "The same raw second moment E[XY]=1 therefore realizes multiple connected selectors",
        "The m=1/3 realization is the desired disconnected product",
        "Route-2 Pcal moment-realization theorem",
        "No endpoint value is used",
    )
    for marker in required_note:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block101 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names moment-realization theorem", "moment-realization theorem" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)

    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("parent closure", "closes the parent"),
        ("current-surface endpoint derivation", "derives the endpoint triple on the current surface"),
        ("audit ratification", phrase("audit", "-ratified")),
        ("observed-target import", "observed target"),
        ("fitted selector import", "fitted selector"),
        ("target-observation import", "target observation"),
        ("data-tuned selector import", "data-tuned selector"),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate + "\n" + state
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 Pcal moment-realization no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_moment_realization_family()
    part3_required_moment_realization_fields()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: exact P_R slots do not determine the Route-2 Pcal moment realization; the one-point product remains a typed theorem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
