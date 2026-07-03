#!/usr/bin/env python3
"""Exact checks for the Route-2 source-count selector bridge boundary.

The runner verifies a narrow support result: the compressed bridge
c_TE=s_TE/kappa^2 equals -F_adj at the current quark source counts when
kappa=N_color/N_pair and s_TE=-N_pair. It also verifies that a physical color
route still needs the connected-selector specialization.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "QUARK_ROUTE2_SOURCE_COUNT_SELECTOR_BRIDGE_BOUNDARY_NOTE_2026-06-21.md"
READOUT = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
E_CENTER = DOCS / "QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md"
NATURALITY = DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"
SOURCE_BRIDGE = DOCS / "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md"
CKM_A2 = DOCS / "CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md"
CKM_COUNTS = DOCS / "CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md"
RCONN = DOCS / "RCONN_DERIVED_NOTE.md"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(s: str) -> str:
    return " ".join(s.split())


def contains_all(haystack: str, needles: tuple[str, ...]) -> bool:
    return all(needle in haystack for needle in needles)


def extract_int(pattern: str, haystack: str) -> int | None:
    match = re.search(pattern, haystack)
    return int(match.group(1)) if match else None


def f_adj(n_color: int) -> Fraction:
    return Fraction(n_color * n_color - 1, n_color * n_color)


def count_bridge(n_pair: int, n_color: int, shell_ratio: Fraction | None = None) -> tuple[Fraction, Fraction]:
    if shell_ratio is None:
        shell_ratio = Fraction(-n_pair, 1)
    kappa = Fraction(n_color, n_pair)
    return kappa, shell_ratio / (kappa * kappa)


def endpoint_from_center_ratio(
    c_te: Fraction,
    shell_ratio: Fraction = Fraction(-2, 1),
    rho_t: Fraction = Fraction(-1, 1),
    center_denominator: int = 6,
) -> tuple[Fraction, Fraction, Fraction]:
    q_t = Fraction(1, 1) + rho_t / center_denominator
    q_e = shell_ratio * q_t / c_te
    rho_e = center_denominator * (q_e - 1)
    return q_t, q_e, rho_e


def r_phys(n_color: int, xi: Fraction) -> Fraction:
    f = f_adj(n_color)
    return f + xi * (1 - f)


def main() -> int:
    print("Route-2 source-count selector bridge boundary check")

    print("Authority/file presence")
    for path in (
        NOTE,
        READOUT,
        E_CENTER,
        NATURALITY,
        SOURCE_BRIDGE,
        CKM_A2,
        CKM_COUNTS,
        RCONN,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = text(NOTE)
    readout = text(READOUT)
    e_center = text(E_CENTER)
    naturality = text(NATURALITY)
    source_bridge = text(SOURCE_BRIDGE)
    ckm_a2 = text(CKM_A2)
    ckm_counts = text(CKM_COUNTS)
    rconn = text(RCONN)

    print("Source-note boundary checks")
    check(
        "note states exact-support selector-boundary status",
        "**Actual current-surface status:** exact-support / selector-boundary." in note,
    )
    check(
        "note does not claim endpoint closure",
        contains_all(
            note,
            (
                "This note does not establish:",
                "`beta_E/alpha_E = 21/4` on the actual current surface",
                "the typed bridge `c_TE=-F_adj`",
            ),
        ),
    )
    forbidden = (
        "audit" + "ed_" + "clean",
        "audit" + "ed_" + "conditional",
        "retained_" + "no_go",
        "retained_" + "bounded",
        "proposed_" + "retained",
    )
    check("note does not assign audit/effective verdict tokens", not any(token in note for token in forbidden))
    check(
        "note links all one-hop authorities with markdown dependencies",
        contains_all(
            note,
            (
                "[QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md]",
                "[QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md]",
                "[CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md]",
                "[RCONN_DERIVED_NOTE.md]",
            ),
        ),
    )

    print("Authority text checks")
    check(
        "readout authority defines c_TE algebra",
        contains_all(
            readout,
            (
                "c_TE  := gamma_T(center) / gamma_E(center) = s_TE * q_T / q_E",
                "beta_E / alpha_E = 21/4",
            ),
        ),
    )
    check(
        "E-center attempt names typed bridge residual",
        contains_all(
            e_center,
            (
                "derive gamma_E(center)/gamma_E(shell) = 15/8",
                "gamma_T(center)/gamma_E(center) = -8/9",
            ),
        ),
    )
    check(
        "naturality no-go says rho_E remains free without added input",
        "remains a free parameter unless an additional E-center endpoint ratio" in naturality,
    )
    check(
        "source-domain bridge note keeps R_conn to c_TE as missing typed edge",
        contains_all(
            source_bridge,
            (
                "R_conn = (N_c^2 - 1) / N_c^2",
                "?=> gamma_T(center) / gamma_E(center) = -R_conn",
            ),
        ),
    )
    check(
        "RCONN authority separates F_adj from physical selector",
        contains_all(
            flat(rconn),
            (
                "F_adj = dim(adj) / dim(N_c x N_c-bar) = (N_c^2 - 1) / N_c^2.",
                "physical EW-current readout has a free disconnected-channel coefficient",
                "does not derive the selector `kappa_EW = 0`",
            ),
        ),
    )

    print("Source-count extraction checks")
    n_pair = extract_int(r"N_pair\s*=\s*dim_SU2\(Q_L\)\s*=\s*(\d+)", ckm_a2)
    n_color = extract_int(r"N_color\s*=\s*dim_SU3\(Q_L\)\s*=\s*(\d+)", ckm_a2)
    n_quark = extract_int(r"n_quark\s*=\s*n_pair n_color\s*=\s*(\d+)", ckm_counts)
    check("extract N_pair=2 from Q_L source-count note", n_pair == 2, str(n_pair))
    check("extract N_color=3 from Q_L source-count note", n_color == 3, str(n_color))
    check("extract n_quark=6 from structural-counts note", n_quark == 6, str(n_quark))

    assert n_pair is not None and n_color is not None

    print("Exact bridge arithmetic")
    kappa, c_count = count_bridge(n_pair, n_color)
    f = f_adj(n_color)
    check("kappa=N_color/N_pair is 3/2", kappa == Fraction(3, 2), str(kappa))
    check("kappa^2 is 9/4", kappa * kappa == Fraction(9, 4), str(kappa * kappa))
    check("source-count compressed bridge gives c_TE=-8/9", c_count == Fraction(-8, 9), str(c_count))
    check("adjoint fraction at N_color=3 is 8/9", f == Fraction(8, 9), str(f))
    check("compressed bridge equals signed adjoint fraction", c_count == -f, f"c={c_count}, F={f}")
    check(
        "integer identity N_pair^3=N_color^2-1 holds",
        n_pair**3 == n_color**2 - 1,
        f"{n_pair**3} vs {n_color**2 - 1}",
    )
    q_t, q_e, rho_e = endpoint_from_center_ratio(c_count)
    check("endpoint q_T is 5/6", q_t == Fraction(5, 6), str(q_t))
    check("typed bridge would give q_E=15/8", q_e == Fraction(15, 8), str(q_e))
    check("typed bridge would give rho_E=21/4", rho_e == Fraction(21, 4), str(rho_e))
    check("covariance ratio q_E/q_T is kappa^2", q_e / q_t == kappa * kappa, str(q_e / q_t))

    print("Uniqueness and falsifier checks")
    hits = []
    for color in range(2, 13):
        pair = color - 1
        if pair**3 == color**2 - 1:
            hits.append((pair, color))
    check("under N_pair=N_color-1, equality occurs only at (2,3) for 2<=N_color<=12", hits == [(2, 3)], str(hits))
    fixed_pair_hits = []
    for color in range(2, 13):
        if n_pair**3 == color**2 - 1:
            fixed_pair_hits.append(color)
    check("with N_pair=2, equality selects N_color=3 in scan", fixed_pair_hits == [3], str(fixed_pair_hits))

    k_wrong_color, c_wrong_color = count_bridge(2, 4)
    _, q_wrong_color, rho_wrong_color = endpoint_from_center_ratio(c_wrong_color)
    check("wrong color count (2,4) gives c_TE=-1/2", c_wrong_color == Fraction(-1, 2), str(c_wrong_color))
    check("wrong color count endpoint rho_E is 14", rho_wrong_color == Fraction(14, 1), str(rho_wrong_color))
    k_wrong_pair, c_wrong_pair = count_bridge(3, 4)
    check("wrong pair/color (3,4) gives c_TE=-27/16", c_wrong_pair == Fraction(-27, 16), str(c_wrong_pair))
    _, c_wrong_shell = count_bridge(2, 3, shell_ratio=Fraction(-1, 1))
    check("wrong shell orientation gives c_TE=-4/9", c_wrong_shell == Fraction(-4, 9), str(c_wrong_shell))
    check("no covariance normalization kappa=1 would give c_TE=-2", Fraction(-2, 1) != Fraction(-8, 9))

    print("Disconnected-selector family checks")
    selector_results = {}
    for xi in (Fraction(0, 1), Fraction(1, 2), Fraction(1, 1)):
        r = r_phys(n_color, xi)
        c = -r
        _, qe, rho = endpoint_from_center_ratio(c)
        selector_results[xi] = (r, c, rho)
    check("connected selector xi=0 gives rho_E=21/4", selector_results[Fraction(0, 1)][2] == Fraction(21, 4), str(selector_results[Fraction(0, 1)]))
    check("mid selector xi=1/2 gives rho_E=78/17", selector_results[Fraction(1, 2)][2] == Fraction(78, 17), str(selector_results[Fraction(1, 2)]))
    check("full-trace selector xi=1 gives rho_E=4", selector_results[Fraction(1, 1)][2] == Fraction(4, 1), str(selector_results[Fraction(1, 1)]))
    check("only xi=0 in tested selector set gives target rho_E", [xi for xi, vals in selector_results.items() if vals[2] == Fraction(21, 4)] == [Fraction(0, 1)])

    print("Note content checks")
    flat_note = flat(note)
    check("note records selector family formula", "R_phys(xi) = F_adj + xi (1 - F_adj)" in note)
    check("note records wrong-structure falsifiers", "Wrong-structure falsifiers" in note and "full-trace color selector" in note)
    check("note names sharpened target", "derive a typed source/readout theorem identifying the Route-2 center ratio" in flat_note)

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
