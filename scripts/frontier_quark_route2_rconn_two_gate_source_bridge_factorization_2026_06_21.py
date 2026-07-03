#!/usr/bin/env python3
"""Route-2/Rconn two-gate source bridge factorization certificate.

Safe claim:
  The algebraic source-domain bridge W1 and the physical connected-trace
  selector W2 are independent. W2-only reaches the color scalar but does not
  type that scalar as the Route-2 signed center ratio. W1-only reaches the
  endpoint target chain from the color scalar but does not supply the physical
  selector.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

from frontier_quark_route2_source_domain_bridge_no_go import (
    CURRENT_TYPED_EDGES,
    DERIVED_ADDITIONAL_EDGES,
    MISSING_BRIDGE,
    TypedEdge,
    reachable,
    rho_e_from_center_ratio,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0

F_ADJ = Fraction(8, 9)
TARGET_Q_E = Fraction(15, 8)
TARGET_RHO_E = Fraction(21, 4)
TARGET_C_TE = Fraction(-8, 9)

PHYSICAL_SELECTOR_EDGE = TypedEdge(
    "rconn_kappa_EW_zero_selector",
    "su3_R_conn_8_9",
    "physical connected-trace selector kappa_EW=0 specializes R_phys to F_adj",
    "RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md",
    "physical_selector",
)


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


def norm(text: str) -> str:
    return " ".join(text.split())


def r_phys(kappa_ew: Fraction) -> Fraction:
    return F_ADJ + kappa_ew * (1 - F_ADJ)


def q_e_from_center_ratio(center_te: Fraction) -> Fraction:
    return Fraction(-2, 1) * Fraction(5, 6) / center_te


def rho_if_typed_from_kappa(kappa_ew: Fraction) -> Fraction:
    return rho_e_from_center_ratio(-r_phys(kappa_ew))


def path_exists(edges: tuple[TypedEdge, ...], source: str, target: str) -> bool:
    ok, _path = reachable(edges, source, target)
    return ok


def part_a_authorities() -> None:
    print("A. Authority surface")
    note_path = DOCS / "QUARK_ROUTE2_RCONN_TWO_GATE_SOURCE_BRIDGE_FACTORIZATION_NOTE_2026-06-21.md"
    source_path = DOCS / "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md"
    typed_path = DOCS / "QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md"
    kappa_path = DOCS / "RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md"
    rconn_path = DOCS / "RCONN_DERIVED_NOTE.md"
    readout_path = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"

    paths = (note_path, source_path, typed_path, kappa_path, rconn_path, readout_path)
    for path in paths:
        check(f"{path.name} exists", path.exists(), str(path.relative_to(ROOT)))

    note = read(note_path)
    source = read(source_path)
    typed = read(typed_path)
    kappa = read(kappa_path)
    rconn = read(rconn_path)
    readout = read(readout_path)

    check(
        "new note names W1 and W2",
        "W1: algebraic source-domain bridge" in note
        and "W2: physical connected-trace selector" in note,
    )
    check(
        "new note declares no repo-wide status change",
        "not a repo-wide status change" in note and "does not apply an audit verdict" in note,
    )
    check(
        "source-domain note names missing typed bridge",
        "There is no current typed edge" in source
        and "R_conn = 8/9 -> c_TE = gamma_T(center)/gamma_E(center) = -8/9" in source,
    )
    compact_typed = norm(typed)
    compact_kappa = norm(kappa)
    check(
        "typed bridge note already separates W1 and W2",
        "W1 does not automatically close W2" in compact_typed
        and "W2 does not automatically close W1" in compact_typed,
    )
    check(
        "kappa note keeps physical selector open",
        "does not close the `kappa_EW = 0` selector" in compact_kappa
        or "does not close the `κ_EW = 0` selector" in compact_kappa,
    )
    check(
        "kappa note requires separate physical bridge for positive downstream use",
        "Any downstream positive use must supply a separate" in kappa,
    )
    check(
        "Rconn note keeps exact support as F_adj",
        "exact `8/9` support remains available as `F_adj`" in rconn,
    )
    check(
        "readout note defines endpoint ratios without Rconn",
        "q_E   := gamma_E(center) / gamma_E(shell)" in readout
        and "R_conn" not in readout,
    )


def part_b_gate_reachability() -> None:
    print("\nB. Four-case reachability")
    base_edges = CURRENT_TYPED_EDGES + DERIVED_ADDITIONAL_EDGES
    w2_only = base_edges + (PHYSICAL_SELECTOR_EDGE,)
    w1_only = base_edges + (MISSING_BRIDGE,)
    both = base_edges + (PHYSICAL_SELECTOR_EDGE, MISSING_BRIDGE)

    physical = PHYSICAL_SELECTOR_EDGE.source
    color = "su3_R_conn_8_9"
    center = "route2_center_TE_minus_8_9"
    rho = "route2_rho_E_21_4"

    check("current inventory lacks color-to-center path", not path_exists(base_edges, color, center))
    check("current inventory lacks color-to-rho path", not path_exists(base_edges, color, rho))
    check("W2-only reaches the color scalar from physical selector", path_exists(w2_only, physical, color))
    check("W2-only does not reach Route-2 center ratio", not path_exists(w2_only, physical, center))
    check("W2-only does not reach endpoint target chain", not path_exists(w2_only, physical, rho))
    check("W1-only reaches Route-2 center ratio from color scalar", path_exists(w1_only, color, center))
    check("W1-only reaches endpoint target chain from color scalar", path_exists(w1_only, color, rho))
    check("W1-only has no physical-selector source path", not path_exists(w1_only, physical, rho))
    check("W1 and W2 together reach endpoint target chain from physical selector", path_exists(both, physical, rho))
    check("the physical selector edge is not already in W9 inventory", PHYSICAL_SELECTOR_EDGE not in base_edges)
    check("the W1 bridge edge is not already in W9 inventory", MISSING_BRIDGE not in base_edges)


def part_c_exact_arithmetic() -> None:
    print("\nC. Exact arithmetic")
    q_e = q_e_from_center_ratio(TARGET_C_TE)
    rho_e = rho_e_from_center_ratio(TARGET_C_TE)

    check("F_adj at N_c=3 is 8/9", F_ADJ == Fraction(8, 9), str(F_ADJ))
    check("W1 center ratio is -F_adj", TARGET_C_TE == -F_ADJ, str(TARGET_C_TE))
    check("W1 center ratio gives q_E=15/8", q_e == TARGET_Q_E, str(q_e))
    check("W1 center ratio gives rho_E=21/4", rho_e == TARGET_RHO_E, str(rho_e))
    check("missing bridge has W1 endpoints", MISSING_BRIDGE.source == "su3_R_conn_8_9" and MISSING_BRIDGE.target == "route2_center_TE_minus_8_9")

    samples = {
        Fraction(0, 1): (Fraction(8, 9), Fraction(15, 8), Fraction(21, 4)),
        Fraction(1, 2): (Fraction(17, 18), Fraction(30, 17), Fraction(78, 17)),
        Fraction(1, 1): (Fraction(1, 1), Fraction(5, 3), Fraction(4, 1)),
    }
    hits = 0
    for kappa, (expected_r, expected_q, expected_rho) in samples.items():
        r_value = r_phys(kappa)
        q_value = q_e_from_center_ratio(-r_value)
        rho_value = rho_if_typed_from_kappa(kappa)
        if rho_value == TARGET_RHO_E:
            hits += 1
        label = f"kappa_EW={kappa}"
        check(f"{label} gives expected R_phys", r_value == expected_r, str(r_value))
        check(f"{label} gives expected q_E if typed as c_TE", q_value == expected_q, str(q_value))
        check(f"{label} gives expected rho_E if typed as c_TE", rho_value == expected_rho, str(rho_value))
    check("only kappa_EW=0 sample lands the target after the extra typing rule", hits == 1, f"hits={hits}")


def part_d_gate_independence_text() -> None:
    print("\nD. Gate-independence discipline")
    note = read(DOCS / "QUARK_ROUTE2_RCONN_TWO_GATE_SOURCE_BRIDGE_FACTORIZATION_NOTE_2026-06-21.md")
    compact = norm(note)

    check(
        "note states W2-only limitation",
        "W2 by itself reaches the color scalar but does not type that scalar as the Route-2 signed center ratio" in compact,
    )
    check(
        "note states W1-only limitation",
        "W1 by itself gives the Route-2 endpoint chain from the color scalar but does not prove the physical connected-trace selector" in compact,
    )
    check(
        "note includes four case table",
        "| W2 only |" in note and "| W1 only |" in note and "| W1 and W2 |" in note,
    )
    check(
        "note keeps forbidden inputs visible",
        "observed quark masses" in note
        and "nearest-rational selection from live data" in note
        and "treating a color scalar as a Route-2 endpoint ratio without W1" in note,
    )
    check(
        "note identifies remaining positive work",
        "either prove W1" in note and "or prove W2 and W1 as separate theorems" in note,
    )
    check(
        "note does not claim selected P_R",
        "does not prove a selected `P_R`" in note,
    )
    check(
        "runner avoids applying verdicts",
        "does not apply an audit verdict" in note,
    )
    check(
        "unsafe endpoint shortcut is explicitly pruned",
        "kappa_EW = 0\n  -> endpoint target" in note,
    )
    check(
        "expected PASS total is recorded",
        "TOTAL: PASS=49, FAIL=0" in note,
    )


def main() -> int:
    part_a_authorities()
    part_b_gate_reachability()
    part_c_exact_arithmetic()
    part_d_gate_independence_text()
    print(f"\nTOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("Status: exact negative boundary for W1/W2 gate conflation.")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
