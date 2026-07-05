#!/usr/bin/env python3
"""W67 bounded derivation attempt for the Route-2 R_conn typed bridge."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

from frontier_quark_route2_source_domain_bridge_no_go import (
    CURRENT_TYPED_EDGES,
    DERIVED_ADDITIONAL_EDGES,
    MISSING_BRIDGE,
    reachable,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalize(text: str) -> str:
    return " ".join(text.split())


def f_adj(n_c: int = 3) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def route2_values(rho_e: Fraction) -> dict[str, Fraction]:
    alpha_e = Fraction(1, 1)
    alpha_t = Fraction(-2, 1)
    beta_t = Fraction(2, 1)
    delta_center = Fraction(1, 6)
    gamma_e_shell = alpha_e
    gamma_e_center = alpha_e + rho_e * delta_center
    gamma_t_shell = alpha_t
    gamma_t_center = alpha_t + beta_t * delta_center
    return {
        "q_e": gamma_e_center / gamma_e_shell,
        "q_t": gamma_t_center / gamma_t_shell,
        "s_te": gamma_t_shell / gamma_e_shell,
        "c_te": gamma_t_center / gamma_e_center,
    }


def rho_e_for_center_ratio(c_te: Fraction) -> Fraction:
    q_t = Fraction(5, 6)
    s_te = Fraction(-2, 1)
    q_e = s_te * q_t / c_te
    return 6 * (q_e - 1)


def main() -> int:
    note_path = DOCS / "QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md"
    source_note_path = DOCS / "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md"
    rconn_note_path = DOCS / "RCONN_DERIVED_NOTE.md"
    kappa_note_path = DOCS / "RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md"
    fierz_note_path = DOCS / "EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md"
    readout_note_path = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
    time_note_path = DOCS / "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md"
    bilinear_note_path = DOCS / "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md"
    naturality_note_path = DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"
    axiom_note_path = DOCS / "MINIMAL_AXIOMS_2026-06-05.md"
    primitive_registry_path = DOCS / "audit" / "data" / "axiom_premise_nodes.json"

    paths = (
        note_path,
        source_note_path,
        rconn_note_path,
        kappa_note_path,
        fierz_note_path,
        readout_note_path,
        time_note_path,
        bilinear_note_path,
        naturality_note_path,
        axiom_note_path,
        primitive_registry_path,
    )
    for path in paths:
        check(f"{path.name} exists", path.exists(), str(path.relative_to(ROOT)))

    note = read(note_path)
    source_note = read(source_note_path)
    rconn_note = read(rconn_note_path)
    kappa_note = read(kappa_note_path)
    fierz_note = read(fierz_note_path)
    readout_note = read(readout_note_path)
    time_note = read(time_note_path)
    bilinear_note = read(bilinear_note_path)
    naturality_note = read(naturality_note_path)
    axiom_note = read(axiom_note_path)
    primitive_registry = read(primitive_registry_path)

    print("A. Source-note hygiene")
    check(
        "note declares canonical bounded_theorem metadata",
        "**Type:** bounded_theorem" in note and "**Claim type:** bounded_theorem" in note,
    )
    check(
        "note carries standard status-authority block",
        "Status authority:** independent audit lane only" in note,
    )
    check(
        "note uses portable markdown runner and cache links",
        "[scripts/frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.py]"
        "(../scripts/frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.py)"
        in note
        and "[logs/runner-cache/frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.txt]"
        "(../logs/runner-cache/frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.txt)"
        in note,
    )
    check(
        "note avoids overreach phrases",
        all(
            phrase not in note.lower()
            for phrase in (
                "only route",
                "last route",
                "exhausted",
                "closes the program",
            )
        ),
    )
    check(
        "note declares no new scientific imports",
        "No literature values, new axioms" in note
        and "external citations" in note
        and "new physical weighting rules" in note,
    )
    check(
        "note quotes the W9 bridge target",
        "R_conn = (N_c^2 - 1) / N_c^2\n    ?=> gamma_T(center) / gamma_E(center) = -R_conn" in note,
    )
    check(
        "source-domain note names the same missing bridge",
        "R_conn = (N_c^2 - 1) / N_c^2\n    ?=> gamma_T(center) / gamma_E(center) = -R_conn" in source_note,
    )
    check(
        "source-domain runner exports the same missing bridge endpoints",
        MISSING_BRIDGE.source == "su3_R_conn_8_9"
        and MISSING_BRIDGE.target == "route2_center_TE_minus_8_9",
    )

    print("B. Exact algebraic counter-witness")
    f = f_adj(3)
    values_zero = route2_values(Fraction(0, 1))
    values_target = route2_values(Fraction(21, 4))
    check("F_adj at N_c=3 is exact 8/9", f == Fraction(8, 9), str(f))
    check(
        "rho_E=0 keeps granted T-side values",
        values_zero["q_t"] == Fraction(5, 6) and values_zero["s_te"] == Fraction(-2, 1),
        f"q_T={values_zero['q_t']}, s_TE={values_zero['s_te']}",
    )
    check(
        "rho_E=21/4 keeps granted T-side values",
        values_target["q_t"] == Fraction(5, 6) and values_target["s_te"] == Fraction(-2, 1),
        f"q_T={values_target['q_t']}, s_TE={values_target['s_te']}",
    )
    check("rho_E=0 gives c_TE=-5/3 exactly", values_zero["c_te"] == Fraction(-5, 3), str(values_zero["c_te"]))
    check("rho_E=21/4 gives q_E=15/8 exactly", values_target["q_e"] == Fraction(15, 8), str(values_target["q_e"]))
    check("rho_E=21/4 gives c_TE=-8/9 exactly", values_target["c_te"] == Fraction(-8, 9), str(values_target["c_te"]))
    check(
        "same F_adj does not determine a unique c_TE",
        f == Fraction(8, 9) and values_zero["c_te"] != values_target["c_te"],
        f"{values_zero['c_te']} vs {values_target['c_te']}",
    )
    check(
        "solving c_TE=-F_adj returns rho_E=21/4",
        rho_e_for_center_ratio(-f) == Fraction(21, 4),
        str(rho_e_for_center_ratio(-f)),
    )
    check(
        "positive F_adj alone has wrong signed Route-2 lift",
        rho_e_for_center_ratio(f) == Fraction(-69, 4),
        str(rho_e_for_center_ratio(f)),
    )

    print("C. Authority surface separation")
    check("Rconn note keeps exact support as F_adj", "exact `8/9` support remains available as `F_adj`" in rconn_note)
    check("Rconn note does not define Route-2 gamma objects", "gamma_T(center)" not in rconn_note and "gamma_E(center)" not in rconn_note)
    check("Fierz note supplies Fierz channel algebra", "Tr[M^† M]" in fierz_note and "(N_c^2 − 1) / N_c^2" in fierz_note)
    check("Fierz note does not define Route-2 gamma objects", "gamma_T(center)" not in fierz_note and "gamma_E(center)" not in fierz_note)
    check("readout note defines gamma_E and gamma_T", "gamma_E = alpha_E u_E + beta_E delta_A1 u_E" in readout_note and "gamma_T = alpha_T u_T + beta_T delta_A1 u_T" in readout_note)
    check("readout note does not import R_conn", "R_conn" not in readout_note and "F_adj" not in readout_note)
    check("time-coupling note leaves P_R selection open", "What it\nlacks is a theorem that selects one unique `P_R`" in time_note)
    check("bilinear note defines K_R without R_conn", "`K_R(q) := [[u_E(q), u_T(q)], [delta_A1(q) u_E(q), delta_A1(q) u_T(q)]]`" in bilinear_note and "R_conn" not in bilinear_note)
    check("naturality note names c_TE equivalence", "c_TE = gamma_T(center)/gamma_E(center) = -8/9" in naturality_note)

    print("D. Physical selector boundary kept separate")
    normalized_kappa = normalize(kappa_note)
    normalized_axiom = normalize(axiom_note)
    check(
        "kappa note separates exact algebra from physical selector",
        "the exact Fierz trace/traceless algebra is still valid support" in normalized_kappa
        and "does not close the `κ_EW = 0` selector" in normalized_kappa,
    )
    check(
        "kappa note names missing readout-weighting rule",
        "physical weighting or\nobservable-bridge rule" in kappa_note
        or "physical weighting or observable-bridge rule" in normalize(kappa_note),
    )
    check(
        "minimal axioms withhold readout and weighting",
        "A record supplies no readout context" in normalized_axiom
        and "weighting" in normalized_axiom
        and "physical observable bridge" in normalized_axiom,
    )
    check(
        "primitive registry does not grant readout bridge",
        "selector, readout bridge" in primitive_registry
        and "weighting, normalization" in primitive_registry,
    )
    check(
        "new note keeps algebraic W1 separate from kappa_EW W2",
        "W1 does not automatically close W2" in note
        and "the headline obstruction uses W1" in note,
    )

    print("E. Reachability re-run")
    source = "su3_R_conn_8_9"
    center_target = "route2_center_TE_minus_8_9"
    rho_target = "route2_rho_E_21_4"
    derived_edges = CURRENT_TYPED_EDGES + DERIVED_ADDITIONAL_EDGES
    without_center, without_center_path = reachable(derived_edges, source, center_target)
    without_rho, without_rho_path = reachable(derived_edges, source, rho_target)
    with_bridge_center, with_bridge_center_path = reachable(derived_edges + (MISSING_BRIDGE,), source, center_target)
    with_bridge_rho, with_bridge_rho_path = reachable(derived_edges + (MISSING_BRIDGE,), source, rho_target)
    check("W9 derived inventory has no R_conn-to-center path", not without_center, f"path={len(without_center_path)}")
    check("W9 derived inventory has no Rconn-to-rho path", not without_rho, f"path={len(without_rho_path)}")
    check("hypothetical missing bridge reaches center", with_bridge_center, f"path={len(with_bridge_center_path)}")
    check("hypothetical missing bridge reaches rho_E", with_bridge_rho, f"path={len(with_bridge_rho_path)}")
    check("new note does not add missing bridge to derived inventory", MISSING_BRIDGE not in derived_edges)
    check(
        "source-domain note names the typed bridge gap",
        "R_conn -> gamma_T(center)/gamma_E(center) = -R_conn" in source_note,
    )
    check(
        "new note states s3-time discharge surface unchanged",
        "the discharge surface is unchanged" in note
        and "not a discharge of the full gate" in note,
    )

    print("F. No-go discipline visibility")
    for label in ("N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"):
        check(f"{label} checklist item is present", f"**{label}" in note)
    check("N1 lists at least five alternative routes", note.count("| Direct Fierz count |") == 1 and note.count("ATTEMPTED") >= 4)
    check("N6 records primitive registry scan", "The primitive registry lists" in note)
    check("N7 steelman is present", "A hostile reviewer could argue" in note)
    check("N8 cross-cycle echo is present", "Similar walls appear in the Lane 3 no-go ledger" in note)
    check("gate result is narrow PASS", "Gate result: PASS for this narrow obstruction" in note)

    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
